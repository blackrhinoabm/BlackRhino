from src.market import Market

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2016 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)
Pawel Fiedor (pawel@fiedor.eu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from abm_template.src.basemodel import BaseModel
import random
import logging
from src.transaction import Transaction

# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------


class Updater(BaseModel):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""
    model_parameters = {}
    interactions = None

    #
    #
    # METHODS
    #
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Updater, self).set_identifier(_value)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, _value):
        super(Updater, self).set_model_parameters(_value)

    def get_interactions(self):
        return self.interactions

    def set_interactions(self, _value):
        super(Updater, self).set_interactions(_value)

    def __str__(self):
        return super(Updater, self).__str__()

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self,  environment):
        self.environment = environment
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self,  environment,  time):
        # As a first step, we accrue all interest over the transactions
        # Thus, important to notice to keep 0 as interest by default
        # Unless transaction should carry interest
        # DON'T DO INTERESTS SO FAR, DO ONCE THE REST WORKS
        self.accrue_interests(environment, time)
        # Then agents get their labour endowment for the step (e.g. work hours to spend)
        # For now we don't need to keep track of labour left as there is no queue
        # self.endow_labour(environment, time)
        # The households sell labour to firms
        self.sell_labour(environment, time)
        # The firms sell goods to households
        self.consume_rationed(environment, time)
        # We net deposits and loans
        self.net_loans_deposits(environment, time)
        # We remove goods and labour (perishable) and are left with capital
        self.net_labour_goods(environment, time)
        # Purging accounts at every step just in case
        transaction = Transaction()
        transaction.purge_accounts(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # accrue_interests(environment, time)
    # This method accrues interest on all transaction
    # making sure we don't double count the transactions that are
    # on the books of multiple agents, interest is specified within the
    # transaction itself
    # -------------------------------------------------------------------------
    def accrue_interests(self,  environment, time):
        environment.accrue_interests()
        logging.info("  interest accrued on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # endow_labour
    # This function makes sure that all households have the appropriate
    # labour endowment for every step, in line with the parameters
    # -------------------------------------------------------------------------
    def endow_labour(self,  environment, time):
        # We make sure household get their labour endowment per step
        # labour is a parameter, doesn't change in the simulation
        # sweep_labour is a state variable and can be depleted within the sweep
        for household in environment.households:
            household.sweep_labour = household.labour
        logging.info("  labour endowed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # sell_labour(environment, time)
    # This function allows the households to sell their labour to firms
    # For now we assume that firms want to buy all the labour they can get
    # And that they need to use cash for this purpose, they can't take loans
    # And firms keep cash, they do not keep deposits, these will be updated
    # in later time
    # -------------------------------------------------------------------------
    def sell_labour(self,  environment, time):
        # First we find the market equilibrium price
        # Important to note that this currently does
        # not depend on the wealth of the buyers
        # That is their demand may be higher than
        # what they can actually buy, which may be ok
        # We set the values necessary for tatonnement
        # The list of sellers and their supply functions
        sellers = []
        for agent in environment.households:
            sellers.append([agent, agent.supply_of_labour_solow])
        # And the list of buyers and their demand functions
        buyers = []
        for agent in environment.firms:
            buyers.append([agent, agent.demand_for_labour_solow])
        # We may start the search for price at some specific point
        # Here we pass 0, which means it'll start looking at a
        # random point between 0 and 10
        starting_price = 0.0
        # We initialize the price
        price = 0.0
        # Put the appropriate settings, i.e. desired identifier
        market = Market("market")
        # And we find the market price of labour
        # given supply and demand of the agents
        # and tolerance of error, resolution of search
        # and amplification factor for exponential search
        price = market.tatonnement(sellers, buyers, starting_price, 0.00000000001, 0.01, 1.1)
        environment.variable_parameters["price_of_labour"] = price
        # now we use rationing to find the actual transactions between agents
        for_rationing = []
        for household in environment.households:
            for_rationing.append([household, household.supply_of_labour_solow(price)])
        for firm in environment.firms:
            for_rationing.append([firm, -firm.demand_for_labour_solow(price)])
        # And we find the rationing, ie the amounts
        # of goods sold between pairs of agents
        rationed = market.rationing(for_rationing)
        #
        #             A (from)    L (to)
        # bank        loan        deposit
        # household   deposit     labour
        # firm        labour      loan
        #
        for ration in rationed:
            # The labour is an asset (production factor) for the firm
            # and a liability (promise to work) for the household
            environment.new_transaction("labour", "",  ration[1].identifier, ration[0].identifier,
                                        ration[2], 0,  0, -1)
            random_bank = random.choice(environment.banks)
            # Deposit is a liability of the bank
            # and an asset of the household
            environment.new_transaction("deposits", "",  ration[0].identifier, random_bank.identifier,
                                        ration[2]*price, random_bank.interest_rate_deposits,  0, -1)
            # Loan is an asset of the bank
            # and a liability of the firm
            environment.new_transaction("loans", "",  random_bank.identifier, ration[1].identifier,
                                        ration[2]*price, random_bank.interest_rate_loans,  0, -1)
            # We print the action of selling to the screen
            print("{}s sold {}d units of labour at a price {}f to {}s at time {}d.".format(ration[0].identifier, ration[2], price, ration[1].identifier, time))
        logging.info("  labour sold to firms on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # consume_rationed(environment, time)
    # This function lets households buy the goods the firms have produced
    # so they can satisfy their needs through consumption
    # This consumption depends on the propensity to save of the households
    # The matching of buyers and sellers on the market is random
    # -------------------------------------------------------------------------
    def consume_rationed(self, environment, time):
        # We want the consumption to be done in random pairs
        # We use rationing from market clearing class to do that
        # Price is static for this example, otherwise we can't use rationing
        # and need some other market clearing
        price = 10.0
        environment.variable_parameters["price_of_goods"] = price
        # We need a list of agents and their demand or supply
        # Supply is denoted with positive float, demand with negative float
        for_rationing = []
        # Firms give us their supply, we assume that since the goods are
        # perishable their supply is all they have in stock
        from src.helper import Helper
        helper = Helper()
        for firm in environment.firms:
            # amount = round(helper.leontief([firm.get_account("labour")], [1/firm.productivity]), 0)
            amount = helper.cobb_douglas(firm.get_account("labour"), firm.get_account("capital"),
                                         firm.total_factor_productivity, firm.labour_elasticity, firm.capital_elasticity)*price
            for_rationing.append([firm, amount])
        # Households give use their demand, we assume that they want to
        # consume the part of their wealth (cash and deposits) that they
        # do not want to save (determined through propensity to save)
        # We denote demand in units of the goods, so we divide the cash
        # households want to spend by price to get the demand
        for household in environment.households:
            demand = 0.0
            # demand = -round(((household.get_account("deposits") * (1 - household.propensity_to_save)) / price), 0)
            demand = -((household.get_account("deposits") * (1 - household.propensity_to_save)) / price)
            # demand = -household.get_account("deposits")/price
            for_rationing.append([household, demand])
        # We import the market clearing class

        # Put the appropriate settings, i.e.
        # tolerance of error, resolution of search
        # and amplification for exponential search
        # This does not matter for rationing
        # But in principle we need to initialize
        # with these values
        market = Market("market")
        # And we find the rationing, ie the amounts
        # of goods sold between pairs of agents
        # TESTING THE ABSTRACT RATIONING
        # The matching function means that all pairs will have the same priority

        def matching_agents_basic(agent_one, agent_two):
            return 1.0

        # The below function means that all pairs are allowed

        def allow_match_basic(agent_one, agent_two):
            return True
        # We find the actual trades
        rationed = market.rationing_abstract(for_rationing, matching_agents_basic, allow_match_basic)
        # Then we go through the rationing
        # and move the goods and cash appropriately
        for ration in rationed:
            #
            #             A (from)    L (to)
            # bank        loan        deposit
            # household   goods       loan
            # firm        deposit     goods
            #
            environment.new_transaction("goods", "",  ration[1].identifier, ration[0].identifier,
                                        ration[2], 0,  0, -1)
            random_bank = random.choice(environment.banks)
            environment.new_transaction("deposits", "",  ration[0].identifier, random_bank.identifier,
                                        ration[2]*price, random_bank.interest_rate_deposits,  0, -1)
            environment.new_transaction("loans", "",  random_bank.identifier, ration[1].identifier,
                                        ration[2]*price, random_bank.interest_rate_loans,  0, -1)
            # We print the action of selling to the screen
            print("{}s sold {}d units of goods at a price {}f to {}s at time {}d.".format(ration[0].identifier,
                                                                                          ration[2], price,
                                                                                          ration[1].identifier, time))
        logging.info("  goods consumed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # net_loans_deposits(environment, time)
    # This function makes deposits of all the remaining cash of the households
    # It is important to notice that this ultimately depends on the propensity
    # to save parameter, but indirectly, since it influences how much in goods
    # the agents buy from firms prior to this step, thus allowing this step
    # to be easier and move all cash to deposits in the banks
    # -------------------------------------------------------------------------
    def net_loans_deposits(self,  environment, time):
        # We do it from the bank's perspective
        for bank in environment.banks:
            # And first go through the firms
            for firm in environment.firms:
                # Finding what their balance of deposits (+) and loans (-) is
                balance = 0.0
                # And mark all the loan and deposits we account for to be deleted
                to_delete = []
                # We go through the firm's accounts
                for tranx in firm.accounts:
                    # And find deposits from the firm to the bank
                    if tranx.type_ == "deposits":
                        if tranx.to == bank:
                            # If we find one we append the balance
                            balance = balance + tranx.amount
                            # And mark the transaction for deletion
                            to_delete.append(tranx)
                    # And find loans from the bank to the firm
                    if tranx.type_ == "loans":
                        if tranx.from_ == bank:
                            # If we find one we append the balance
                            balance = balance - tranx.amount
                            # And mark the transaction for deletio
                            to_delete.append(tranx)
                # Then we delete all market transactions
                for tranx in to_delete:
                    tranx.remove_transaction()
                # And add the netted transaction to the firm's and bank's books
                if balance > 0.0:
                    # If the balance is positive it's a deposit
                    environment.new_transaction("deposits", "",  firm.identifier, bank.identifier,
                                                balance, bank.interest_rate_deposits,  0, -1)
                elif balance < 0.0:
                    # If the balance is negative it's a loan
                    environment.new_transaction("loans", "",  bank.identifier, firm.identifier,
                                                abs(balance), bank.interest_rate_loans,  0, -1)
        # We do it from the bank's perspective
        for bank in environment.banks:
            # And first go through the households
            for household in environment.households:
                # Finding what their balance of deposits (+) and loans (-) is
                balance = 0.0
                # And mark all the loan and deposits we account for to be deleted
                to_delete = []
                # We go through the household's accounts
                for tranx in household.accounts:
                    # And find deposits from the household to the bank
                    if tranx.type_ == "deposits":
                        if tranx.to == bank:
                            # If we find one we append the balance
                            balance = balance + tranx.amount
                            # And mark the transaction for deletion
                            to_delete.append(tranx)
                    # And find loans from the bank to the household
                    if tranx.type_ == "loans":
                        if tranx.from_ == bank:
                            # If we find one we append the balance
                            balance = balance - tranx.amount
                            # And mark the transaction for deletion
                            to_delete.append(tranx)
                # Then we delete all market transactions
                for tranx in to_delete:
                    tranx.remove_transaction()
                # And add the netted transaction to the household's and bank's books
                if balance > 0.0:
                    # If the balance is positive it's a deposit
                    environment.new_transaction("deposits", "",  household.identifier, bank.identifier,
                                                balance, bank.interest_rate_deposits,  0, -1)
                elif balance < 0.0:
                    # If the balance is negative it's a loan
                    environment.new_transaction("loans", "",  bank.identifier, household.identifier,
                                                abs(balance), bank.interest_rate_loans,  0, -1)
        logging.info("  deposits and loans netted on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # net_labour_goods(environment, time)
    # This function makes deposits of all the remaining cash of the households
    # It is important to notice that this ultimately depends on the propensity
    # to save parameter, but indirectly, since it influences how much in goods
    # the agents buy from firms prior to this step, thus allowing this step
    # to be easier and move all cash to deposits in the banks
    # -------------------------------------------------------------------------
    def net_labour_goods(self,  environment, time):
        # We do it from firm's perspective
        for firm in environment.firms:
            # And go through households
            for household in environment.households:
                # We find a balance of labour and goods sold between firm and household
                # This is the saved part of the household's income, which
                # is equivalent to capital accumulated in Solow's model
                balance = 0.0
                # And we mark all the transactions for deletion once they're added
                # to the above balance
                to_delete = []
                # We go through the household's transactions
                for tranx in household.accounts:
                    # And find labour sold from the household to the firm
                    if tranx.type_ == "labour":
                        if tranx.from_ == firm:
                            # and subtract it to the balance
                            balance = balance - tranx.amount * environment.price_of_labour
                            # and mark for deletion
                            to_delete.append(tranx)
                    # We also find goods sold from the firm to the household
                    if tranx.type_ == "goods":
                        if tranx.to == firm:
                            # and add it to the balance
                            balance = balance + tranx.amount * environment.price_of_goods
                            # and mark for deletion
                            to_delete.append(tranx)
                    # We also net previous capital
                    # This is so we have only one capital transaction per firm or household
                    if tranx.type_ == "capital":
                        if tranx.to == firm:
                            # we add this to the balance if it's from the household to the firm
                            balance = balance + tranx.amount
                            # and mark for deletion
                            to_delete.append(tranx)
                    if tranx.type_ == "capital":
                        if tranx.from_ == firm:
                            # we subtract it from the balance if it's from the firm to the household
                            balance = balance - tranx.amount
                            # and mark for deletion
                            to_delete.append(tranx)
                # We delete all the marked transactions
                for tranx in to_delete:
                    tranx.remove_transaction()
                # And if the balance isn't 0, we add the capital to the books
                if balance < 0.0:
                    environment.new_transaction("capital", "",  household.identifier, firm.identifier,
                                                balance, 0,  0, -1)
                elif balance > 0.0:
                    environment.new_transaction("capital", "",  firm.identifier, household.identifier,
                                                balance, 0,  0, -1)
        logging.info("  labour and goods netted on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------
