#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-

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
        # self.find_interbank_liquidity(environment, time)
        self.endow_equity(environment, time)
        self.accrue_interests(environment, time)
        self.maturities(environment, time)
        self.amortisation(environment, time)
        self.get_funding(environment, time)
        # TODO: make sure finding in firms is positive
        # The households sell labour to firms
        self.sell_labour(environment, time)
        # The firms sell goods to households
        self.consume_rationed(environment, time)
        # We net deposits and loans
        # self.net_loans_deposits(environment, time)
        # We remove the perishable transactions
        self.remove_perishable(environment, time)
        # And add capital to balance the books
        self.check_liquidity(environment, time)
        # self.state_variables["capital"]ise(environment, time)
        self.capitalise_new(environment, time)
        # Investing of the banks
        # self.invest(environment, time)
        # self.invest_interbank(environment, time)
        # Purging accounts at every step just in case
        transaction = Transaction()
        transaction.purge_accounts(environment)
        # And finally we check if all the books are balanced
        # TODO here:
        # - simplify the code
        # - careful about acrrue interests - so it doesn't explode, and think about the fluctuations
        # - so banks will have A: loans(investments)+reserves L: deposits+cb_loans
        self.check_consistency(environment, time)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # endow_equity(environment, time)
    # This method adds banking capital at the start of the simulation
    # The specific point at which equity starts off shouldn't matter too much
    # And the results be rather dependent on the target equity set in the
    # Config of each bank, unless the shock would happen strictly at the
    # Beginning of the simulation which is not prudent anyway
    # -------------------------------------------------------------------------
    def endow_equity(self,  environment, time):
        # We only do it at the start of the simulation
        if time == 0:
            # Each bank is endowed with some equity
            starting_capital = 100.0  # to config
            for bank in environment.banks:
                # NOTE: We may want it to be stochastic around the above
                # But since it shouldn't matter it could be a waste of time
                # Each household owns an equal part of the bank's equity
                # This could be done differently but shouldn't change the
                # Results dramatically
                single_capital = starting_capital / len(environment.households)
                for household in environment.households:
                    # We add the equity to the books (we assume highly liquid equity as is common in literature)
                    environment.new_transaction("equity", "",  household.identifier, bank.identifier,
                                                single_capital, 0.0,  0, -1)
        logging.info("  banks' equity endowed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # accrue_interests(environment, time)
    # This method accrues interest on all transaction
    # making sure we don't double count the transactions that are
    # on the books of multiple agents, interest rates are specified within the
    # transaction itself, the interest are accounted for in the retained
    # earnings on the bank's side, and within funding used for consumption
    # and production in firms and households
    # -------------------------------------------------------------------------
    def accrue_interests(self,  environment, time):
        # First, add interests to all the transactions
        already_done = []
        # We keep a list so we don't update interests twice for the same
        # transaction on both ends (from_ and to)
        for agent in environment.agents_generator():
            # Going through all agents
            for tranx in agent.accounts:
                #
                # We have specific logic for each type of transaction (not counting equity which doesn't carry interest in the model)
                #
                # For loans the bank gets the profit converted into equity (retained earnings), and the firm pays interests to lower its funding
                if tranx.type_ == "loans" and tranx not in already_done:
                    for tranx_inner in tranx.from_.accounts:
                        if tranx_inner.type_ == "equity":
                            tranx_inner.amount = tranx_inner.amount + (tranx.amount * tranx.interest / tranx.from_.get_account_num_transactions("equity"))
                    tranx.to.state_variables["funding"] = tranx.to.state_variables["funding"] - tranx.amount * tranx.interest
                    # And append the list of already processed transactions
                    already_done.append(tranx)
                # For deposits the bank gets the loss converted into equity, and the firm/household gets interests to increase its funding
                if tranx.type_ == "deposits" and tranx not in already_done:
                    for tranx_inner in tranx.to.accounts:
                        if tranx_inner.type_ == "equity":
                            tranx_inner.amount = tranx_inner.amount - (tranx.amount * tranx.interest / tranx.to.get_account_num_transactions("equity"))
                    tranx.from_.state_variables["funding"] = tranx.from_.state_variables["funding"] + tranx.amount * tranx.interest
                    # And append the list of already processed transactions
                    already_done.append(tranx)
                # For interbank loans the bank which gives out the loan gets profit retained as earnings, and the other bank lowers its equity by the loss on interest
                if tranx.type_ == "ib_loans" and tranx not in already_done:
                    for tranx_inner in tranx.to.accounts:
                        if tranx_inner.type_ == "equity":
                            tranx_inner.amount = tranx_inner.amount - (tranx.amount * tranx.interest / tranx.to.get_account_num_transactions("equity"))
                    for tranx_inner in tranx.from_.accounts:
                        if tranx_inner.type_ == "equity":
                            tranx_inner.amount = tranx_inner.amount + (tranx.amount * tranx.interest / tranx.from_.get_account_num_transactions("equity"))
                    # And append the list of already processed transactions
                    already_done.append(tranx)
                # For central bank loans the bank lowers its equity by the loss on interests
                if tranx.type_ == "cb_loans" and tranx not in already_done:
                    for tranx_inner in tranx.to.accounts:
                        if tranx_inner.type_ == "equity":
                            tranx_inner.amount = tranx_inner.amount - (tranx.amount * tranx.interest / tranx.to.get_account_num_transactions("equity"))
                    # And append the list of already processed transactions
                    already_done.append(tranx)
                # For central bank reserves the bank increases its equity by the profit on interests
                if tranx.type_ == "cb_reserves" and tranx not in already_done:
                    for tranx_inner in tranx.from_.accounts:
                        if tranx_inner.type_ == "equity":
                            tranx_inner.amount = tranx_inner.amount + (tranx.amount * tranx.interest / tranx.from_.get_account_num_transactions("equity"))
                    # And append the list of already processed transactions
                    already_done.append(tranx)

        # Then we take care of dividends
        # Each bank has a maximum equity above which they will send out dividends
        for bank in environment.banks:
            # We check if the equity excees maximum level
            if bank.get_account("equity") > bank.parameters["max_equity"]:
                # And find the percentage we need to shave into dividends
                dividend_percentage = 1 - bank.parameters["max_equity"] / bank.get_account("equity")
                # We look for the equity transactions
                for tranx in bank.accounts:
                    if tranx.type_ == "equity":
                        # Send out dividends to the owners of equity
                        tranx.from_.funding = tranx.from_.funding + tranx.amount * dividend_percentage
                        # And shave the equity to maximum level
                        tranx.amount = tranx.amount * (1 - dividend_percentage)
        logging.info("  interest accrued on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # maturities(environment, time)
    # -------------------------------------------------------------------------
    def maturities(self,  environment, time):

        # Just in case we reset liquidity check for a bank
        for bank in environment.banks:
            # It's a state variable within the bank class
            bank.state_variables["liquidity"] = 0.0

        # Update maturities
        already_matured = []
        # We keep a list so we don't update maturities twice for the same
        # transaction on both ends (from_ and to)
        for agent in environment.agents_generator():
            # Going through all agents
            for tranx in agent.accounts:
                # And all accounts
                if (int(tranx.maturity) > 0):  # reduce maturity if duration longer than 0
                    # stuff that doesn't mature or mature always is handled separately
                    if tranx not in already_matured:
                        # And check if it's already matured, if not:
                        tranx.maturity = int(tranx.maturity) - 1
                        # Change maturity (decrease by 1)
                        already_matured.append(tranx)
                        # And add to already matured

        # If maturity is zero then we must remove the transaction
        # (remembering the economics properly)

        # It's easier to roll the deposits at each step since we keep track of each household's or firm's funding through the step
        # But it works equivalently to just having the old deposits amended later
        to_delete = []
        for household in environment.banks:
            # THen we mature households' or firms' deposits
            for tranx in bank.accounts:
                # Deposits mature at each step currently
                if tranx.type_ == "deposits":
                    to_delete.append(tranx)
                    tranx.from_.state_variables["funding"] = tranx.from_.state_variables["funding"] + tranx.amount  # household gains funding
                    tranx.to.state_variables["liquidity"] = tranx.to.liquidity - tranx.amount  # banks lose liquidity
        for tranx in to_delete:
            # Deleting the matured transactions
            tranx.remove_transaction()

        # Loans are paid off only at their maturity
        # TODO: defaults (how to implement them on the firm's side?) and returns
        to_delete = []
        # We will delete the matured transactions after
        for bank in environment.banks:
            # THen we mature loans
            for tranx in bank.accounts:
                if ((tranx.type_ == 'loans') and (int(tranx.maturity) == 0)):
                    to_delete.append(tranx)
                    tranx.to.state_variables["funding"] = tranx.to.state_variables["funding"] - tranx.amount  # firm loses funding
                    tranx.from_.state_variables["liquidity"] = tranx.from_.liquidity + tranx.amount  # bank gains liquidity
        for tranx in to_delete:
            # Deleting the matured transactions
            tranx.remove_transaction()

        # Interbank loans are paid back at each step
        # TODO: think of term interbank market
        to_delete = []
        # We will delete the matured transactions after
        for bank in environment.banks:
            for tranx in bank.accounts:
                if tranx.type_ == "ib_loans":
                    to_delete.append(tranx)
                    tranx.from_.state_variables["liquidity"] = tranx.from_.liquidity + tranx.amount  # one bank gains liquidity
                    tranx.to.state_variables["liquidity"] = tranx.to.liquidity - tranx.amount  # while the other loses liquidity
        for tranx in to_delete:
            # Deleting the matured transactions
            tranx.remove_transaction()

        # Central bank reserves are paid off at each step
        to_delete = []
        # We will delete the matured transactions after
        for tranx in environment.central_bank[0].accounts:
            if tranx.type_ == "cb_reserves":
                to_delete.append(tranx)
                tranx.from_.state_variables["liquidity"] = tranx.from_.liquidity + tranx.amount  # bank gains liquidity
        for tranx in to_delete:
            # Deleting the matured transactions
            tranx.remove_transaction()

        # Central bank loans are repaid at each step
        to_delete = []
        # We will delete the matured transactions after
        for tranx in environment.central_bank[0].accounts:
            if tranx.type_ == "cb_loans":
                to_delete.append(tranx)
                tranx.to.state_variables["liquidity"] = tranx.to.liquidity - tranx.amount  # bank loses liquidity
        for tranx in to_delete:
            # Deleting the matured transactions
            tranx.remove_transaction()

        logging.info("  maturities resolved on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # amortisation(environment, time)
    # -------------------------------------------------------------------------
    def amortisation(self,  environment, time):
        # We perform amortisation of capital at each firm
        # the amortisation parameter shows the % of capital
        # that is lost at each time step (due to age, use, etc.)
        for firm in environment.firms:
            # And here it's depreciated
            firm.state_variables["capital"] = firm.state_variables["capital"] * (1 - firm.amortisation)
        logging.info("  capital amortisation performed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_funding(environment, time)
    # -------------------------------------------------------------------------
    def get_funding(self,  environment, time):
        # This part is for kickstarting the simulation
        # We give each firm starting capital of 30
        # And a loan of equal value from a random bank
        if time == 0:
            for firm in environment.firms:
                # The initial value of funding shouldn't really matter to the equilibrium
                firm.state_variables["funding"] = 100.0
                random_bank = random.choice(environment.banks)
                environment.new_transaction("loans", "",  random_bank.identifier, firm.identifier,
                                            firm.state_variables["funding"], random_bank.interest_rate_loans,  2, -1)
                random_bank.state_variables["liquidity"] = random_bank.state_variables["liquidity"] - firm.state_variables["funding"]
        # During the simulation, i.e. after the first time step
        # We find the amount of new loans based on the previous capital stock
        # (we assume firms want to have a specific), and existing loans
        # else:
        # For every firm
            # If we have too much funding already
            # Remember to check funding at the end and sell capital if necessary
        for firm in environment.firms:
            # The assumption is that capital costs 10.0 units of money
            total_funding = firm.state_variables["funding"] + firm.state_variables["capital"] * 10.0
            # The assumption is that capital used in production has a perfect market and is perfectly liquid
            # Thus can be changed into labour at firm's discretion
            # Thus the firm divides its capital + funding into chunks based on their
            # Respective elasticities in the C-D production function, taking into consideration the price of capital
            firm.state_variables["capital"] = firm.capital_elasticity * total_funding / 10.0
            firm.state_variables["funding"] = (1 - firm.capital_elasticity) * total_funding
        logging.info("  funding performed on step: %s",  time)
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
        for firm in environment.firms:
            firm.state_variables["labour"] = 0.0
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
            print(agent.state_variables["capital"])
            buyers.append([agent, agent.demand_for_labour_solow])
        # Import market clearing class
        from market import Market
        # Put the appropriate settings, i.e. desired identifier
        market = Market("market")
        # And we find the market price of labour
        # given supply and demand of the agents
        # and tolerance of error, resolution of search
        # and amplification factor for exponential search
        # We start the search around 0 for simplicity
        # Shouldn't matter as the algorithm is quite efficient
        price = market.tatonnement(sellers, buyers, 0.001, 0.001, 0.01, 1.1)
        environment.variable_parameters["price_of_labour"] = price
        # now we use rationing to find the actual transactions between agents
        for_rationing = []
        for household in environment.households:
            for_rationing.append([household, household.supply_of_labour_solow(price)])
            # TODO: some function of price, maybe the original now, since it's constrained anyway
            # for_rationing.append([household, household.labour])
        for firm in environment.firms:
            for_rationing.append([firm, -firm.state_variables["funding"]/price])
        # And we find the rationing, ie the amounts
        # of goods sold between pairs of agents
        rationed = market.rationing_proportional(for_rationing)
        #
        #             A (from)    L (to)
        # bank        loan        deposit
        # household   deposit     labour
        # firm        labour      loan
        #
        for ration in rationed:
            # The labour is an asset (production factor) for the firm
            # and a liability (promise to work) for the household
            # ration[0]: household
            # ration[1]: firm
            # Firm's labour increases by the bought amount
            ration[1].state_variables["labour"] = ration[1].state_variables["labour"] + ration[2]
            # random_bank = random.choice(environment.banks)
            # Deposit is a liability of the bank
            # and an asset of the household
            # Household's funding increases by the sold amount of labour * price
            ration[0].state_variables["funding"] = ration[0].state_variables["funding"] + ration[2]*price
            # environment.new_transaction("deposits", "",  ration[0].identifier, random_bank.identifier,
            #                             ration[2]*price, random_bank.interest_rate_deposits,  -1, -1)
            # random_bank = random.choice(environment.banks)
            # Loan is an asset of the bank
            # and a liability of the firm
            # Firm's funding increases by the bought amount of labour * price
            ration[1].state_variables["funding"] = ration[1].state_variables["funding"] - ration[2]*price
            # environment.new_transaction("loans", "",  random_bank.identifier, ration[1].identifier,
            #                             ration[2]*price, random_bank.interest_rate_loans,  -1, -1)
            # We print the action of selling to the screen
            print("%s sold %d units of labour at a price %f to %s at time %d.") % (ration[0].identifier,
                                                                                   ration[2], price, ration[1].identifier, time)

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
            # Firms produce based on their capital, for generality
            # we use their net capital, as in their capital stock
            # minus the capital owned of other agents
            # We find the amount produced through the Cobb-Douglas function
            amount = helper.cobb_douglas(firm.state_variables["labour"], firm.state_variables["capital"],
                                         firm.total_factor_productivity, firm.labour_elasticity, firm.capital_elasticity)*price
            # And assume firm wants to sell whole production given the perishable nature of the goods
            for_rationing.append([firm, amount])
        # Here firms sell
        # TODO
        for ration in for_rationing:
            ration[0].state_variables["funding"] = ration[0].state_variables["funding"] + ration[1]*price
        # Households give use their demand, we assume that they want to
        # consume the part of their wealth (cash and deposits) that they
        # do not want to save (determined through propensity to save)
        # We denote demand in units of the goods, so we divide the cash
        # households want to spend by price to get the demand
        for_rationing = []
        for household in environment.households:
            demand = 0.0
            wealth = 0.0
            # For generality we calculate net wealth for this, that is the
            # amount of deposits they carry minus the amount of loans
            for tranx in household.accounts:
                if tranx.type_ == "deposits" and tranx.from_ == household:
                    wealth = wealth + tranx.amount
                if tranx.type_ == "loans" and tranx.to == household:
                    wealth = wealth - tranx.amount
            # Then the demand is determined by the agent's propensity to save
            # and the wealth calculated above
            wealth = wealth + household.state_variables["funding"]
            print("wealth")  # todo: remove
            print(wealth)  # todo: remove
            demand = ((wealth * (1 - household.propensity_to_save)) / price)
            for_rationing.append([household, demand])
        # We import the market clearing class
        for ration in for_rationing:
            ration[0].state_variables["funding"] = ration[0].state_variables["funding"] - ration[1]*price
        logging.info("  goods produced, sold, and consumed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # remove_perishable(environment, time)
    # This function removes the perishable transactions in the system
    # which need to be removed from the books before the end of the step
    # all methods that use these temporary transactions need to be invoked
    # before this method, currently it removes labour and goods
    # -------------------------------------------------------------------------
    def remove_perishable(self,  environment, time):
        for firm in environment.firms:
            firm.parameters["labour"] = 0.0

        # Firms deposit excess funding
        for firm in environment.firms:
            if firm.state_variables["funding"] >= 0.0:
                # add a deposit
                # TODO: add the deposits randomly as to get the fluctuations
                # TODO: if we're worried about too much fluctuations (albeit should be okay for lots of agents)
                # TODOL we may store their exces in a network and then only disturb the percentages
                # for bank in environment.banks:
                #     if bank is not environment.banks[-1]:
                #         current_dep_perc = random.random  # random should be read from 0 to 1 # for the first
                #     else:
                #         current_dep_perc = 1.0
                #     one_deposit = current_dep_perc * firm.state_variables["funding"]
                #     firm.state_variables["funding"] = firm.state_variables["funding"] - one_deposit
                #     environment.new_transaction("deposits", "",  firm.identifier, bank.identifier,
                #                                 one_deposit, bank.interest_rate_deposits,  -1, -1)
                random_bank = random.choice(environment.banks)
                environment.new_transaction("deposits", "",  firm.identifier, random_bank.identifier,
                                            firm.state_variables["funding"], random_bank.interest_rate_deposits,  -1, -1)
                random_bank.state_variables["liquidity"] = random_bank.liquidity + firm.state_variables["funding"]
                firm.state_variables["funding"] = 0.0
            else:
                # This should not happen as the firms would have to have negative capital
                raise LookupError("Firm has negative funding at the end of the step.")

        # Households deposit excess funding
        for household in environment.households:
            if household.state_variables["funding"] >= 0.0:
                # add a deposit
                # for bank in environment.banks:
                #     if bank is not environment.banks[-1]:
                #         current_dep_perc = random.random  # random should be read from 0 to 1 # for the first
                #     else:
                #         current_dep_perc = 1.0
                #     one_deposit = current_dep_perc * household.state_variables["funding"]
                #     household.state_variables["funding"] = household.state_variables["funding"] - one_deposit
                #     environment.new_transaction("deposits", "",  household.identifier, bank.identifier,
                #                                 one_deposit, bank.interest_rate_deposits,  -1, -1)
                random_bank = random.choice(environment.banks)
                environment.new_transaction("deposits", "",  household.identifier, random_bank.identifier,
                                            household.state_variables["funding"], random_bank.interest_rate_deposits,  -1, -1)
                random_bank.state_variables["liquidity"] = random_bank.liquidity + household.state_variables["funding"]
                household.state_variables["funding"] = 0.0
            else:
                # remove old deposits randomly (can do proportional but let's have some fun)
                if abs(household.state_variables["funding"]) <= household.get_account("deposits"):
                    # remove the deposits
                    perc_to_liquidate = abs(household.state_variables["funding"]) / household.get_account("deposits")
                    for tranx in household.accounts:
                        if tranx.type_ == "deposits":
                            household.state_variables["funding"] = household.state_variables["funding"] + tranx.amount * perc_to_liquidate
                            tranx.to.state_variables["liquidity"] = tranx.to.state_variables["liquidity"] - tranx.amount * perc_to_liquidate
                            tranx.amount = tranx.amount * (1 - perc_to_liquidate)
                else:
                    raise LookupError("Household has more shortfall than deposits.")

        logging.info("  perishables removed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # check_liquidity(environment, time)
    # This function checks whether banks are liquid, if they are illiquid they
    # are removed from the system
    # -------------------------------------------------------------------------
    def check_liquidity(self, environment, time):  # TODO: what if it's not liquid

        discount_factor = 0.85  # put this in config file?

        # somewhere below we have to add check for leverage ratio

        for bank in environment.banks:
            if bank.state_variables["liquidity"] < 0.0:
                if abs(bank.state_variables["liquidity"]) <= (bank.get_account("loans") * discount_factor):
                    perc_to_liquidate = (abs(bank.state_variables["liquidity"]) / bank.get_account("loans")) / discount_factor
                    for tranx in bank.accounts:
                        if tranx.type_ == "loans":
                            bank.state_variables["liquidity"] = bank.state_variables["liquidity"] + tranx.amount * perc_to_liquidate * discount_factor
                            tranx.to.state_variables["funding"] = tranx.to.state_variables["funding"] - tranx.amount * perc_to_liquidate * discount_factor
                            tranx.amount = tranx.amount * (1 - perc_to_liquidate)
                            # NOTE: do we sell everything and liquidate bank (deposits repaid with a discount?)
                    # We don't have any excess reserves at this point in time so have to look at loans maturing in next steps
                    # NOTE: when we have more than just loans we'll need to figure out what we can sell
                else:
                    # raise LookupError("The bank will go into default")  # placeholder
                    # TODO: Here we'll dig into equity
                    for tranx in bank.accounts:
                        if tranx.type_ == "loans":
                            bank.state_variables["liquidity"] = bank.state_variables["liquidity"] + tranx.amount * discount_factor
                            tranx.to.state_variables["funding"] = tranx.to.state_variables["funding"] - tranx.amount * discount_factor
                            tranx.amount = 0.0
                            # NOTE: what happens with the negative liquidity here? guess the deposits are defaulted on
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # capitalise_new(environment, time)
    # This function makes capital transactions which represent final
    # ownership of firms by the household which is done through the bank
    # deposits and bank loans, these are in principle not necessary for the
    # model to work, as we can assume the loans are the capital, and produce off
    # that assumption, but this ensures the books are balanced for all agents
    # -------------------------------------------------------------------------
    def capitalise_new(self,  environment, time):
        # TODO: think about this
        import math
        # TODO: proper economics of loans (supply.demand > one can be infinite in principle)
        for_rationing = []
        for bank in environment.banks:
            # supply_of_loans = (((1+bank.interest_rate_loans)**(1-1.8))/bank.interest_rate_loans)**(1/1.8) * bank.get_account("deposits")
            # HERE WE CAN HAVE A RATIO OF LOANS TO DEPOSITS BANK WANTS FIXED
            # If loans are maturing in 2 steps, we get 2.0 from below times 2 steps and then ratio
            # of loans to deposits will be 4, where the number of deposits is exogeneous to the bank

            # <CRRA>
            # NOTES FOR CRRA
            pReal = 0.99
            rhoReal = 0.04
            theta = 1.67
            xi = bank.get_account("deposits")
            rb = 0.02
            # parameters["pReal"] = 0.0  # probability of credit success
            # parameters["rhoReal"] = 0.0  # interest charged on risky investment
            # parameters["theta"] = 0.0  # risk aversion parameter of bank
            # parameters["xi"] = 0.0  # scaling parameter in CRRA
            # parameters["rb"] = 0.0  # refinancing costs of the bank -> tbd in environment
            mu = pReal*rhoReal - (1.0 - pReal)
            sigma2 = pReal*(rhoReal - mu)*(rhoReal - mu) + (1-pReal)*((-1-mu)*(-1-mu))
            lamb = max(0.0,  min((mu/(theta*sigma2)), 1.0))
            # </CRRA>

            # supply_of_loans = 0.6 * bank.get_account("deposits")
            target_leverage = 30.0
            volume = target_leverage * bank.get_account("equity")
            supply_of_loans = volume * lamb
            to_reserves = volume - supply_of_loans
            environment.new_transaction("cb_reserves", "",  bank.identifier, environment.central_bank[0].identifier,
                                        to_reserves, environment.central_bank[0].interest_rate_cb_reserves,  -1, -1)
            for_rationing.append([bank, supply_of_loans])
        for firm in environment.firms:
            # The above doesn't mean that firms will buy all the loans however
            demand_for_loans = 3.0 * firm.state_variables["capital"] * 10.0
            for_rationing.append([firm, -demand_for_loans])

        from market import Market
        # Put the appropriate settings, i.e. desired identifier
        market = Market("market")

        rationed = market.rationing_proportional(for_rationing)

        for ration in rationed:
            ration[1].state_variables["funding"] = ration[1].state_variables["funding"] + ration[2]
            environment.new_transaction("loans", "",  ration[0].identifier, ration[1].identifier,
                                        ration[2], ration[0].interest_rate_loans,  2, -1)

        #
        # add required reserves
        #
        for bank in environment.banks:
            reserves = environment.required_reserves * bank.get_account("deposits")
            environment.new_transaction("cb_reserves", "",  bank.identifier, environment.central_bank[0].identifier,
                                        reserves, environment.central_bank[0].interest_rate_cb_reserves,  -1, -1)
        #
        # add interbank market
        #
        # TODO: network of banks like in old_br (start with full network and we can work off it later)
        # TODO: the network would then be used by the function in market (create new one that works on networks instead of functions)
        # TODO: (or create a function checking if they're connected in the network which may be better)
        for_rationing = []
        from market import Market
        # Put the appropriate settings, i.e. desired identifier
        market = Market("market")
        # to_delete = []
        for bank in environment.banks:
            demand = -bank.get_account("loans")-bank.get_account("cb_reserves")+bank.get_account("deposits")+bank.get_account("equity")  # TODO: rethink
            # for tranx in bank.accounts:
            #     if tranx.type_ == "ib_loans":
            #         to_delete.append(tranx)
            for_rationing.append([bank, demand])
        # for tranx in to_delete:
        #     tranx.remove_transaction()
        rationed = market.rationing_proportional(for_rationing)
        for ration in rationed:
            environment.new_transaction("ib_loans", "",  ration[0].identifier, ration[1].identifier,
                                        ration[2], 0,  -1, -1)
            # And print it to the screen for easy greping
            print("%s lent %f worth of interbank loans to %s at time %d.") % (ration[0].identifier,
                                                                              ration[2], ration[1].identifier, time)
        #
        # central bank loans
        #
        for bank in environment.banks:
            # Then we add or remove central bank loans
            # We assume that since there is only one central bank we can keep those
            # in one transaction for now, if we fiddle with maturities this may change
            # If we don't yet have a central bank loan we create one
            cb_volume = bank.get_account("loans") + bank.get_account("cb_reserves") - bank.get_account("deposits") - bank.get_account("equity")  # TODO: rethink
            for tranx in bank.accounts:
                if tranx.type_ == "ib_loans":
                    if tranx.from_ == bank:
                        cb_volume = cb_volume + tranx.amount
                    elif tranx.to == bank:
                        cb_volume = cb_volume - tranx.amount
            if cb_volume > 0.0:
                # cb loans
                environment.new_transaction("cb_loans", "",  environment.central_bank[0].identifier, bank.identifier,
                                            cb_volume, environment.central_bank[0].interest_rate_cb_loans,  -1, -1)
            elif cb_volume < 0.0:
                # dividends??
                environment.new_transaction("cb_reserves", "",  bank.identifier, environment.central_bank[0].identifier,
                                            -cb_volume, environment.central_bank[0].interest_rate_cb_reserves,  -1, -1)
        #
        # excess reserves ???
        #
        # for bank in environment.banks:
        #     if round(bank.state_variables["funding"], 3) > 0.0:
        #         num_households = len(environment.households)
        #         to_fund = bank.state_variables["funding"] / num_households
        #         for household in environment.households:
        #             household.state_variables["funding"] = household.state_variables["funding"] + to_fund
        #         bank.state_variables["funding"] = 0.0

        logging.info("  capitalised on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # check_consistency(environment, time)
    # This function checks whether the books of agents are balanced
    # Based on the functions defined for agents
    # Note that central bank does not have a balanced book as they can
    # always create money, so to speak
    # -------------------------------------------------------------------------
    def check_consistency(self, environment, time):
        for bank in environment.banks:
            check_status = bank.check_consistency()
            if check_status is False:
                print(bank)
                raise LookupError("Bank's books are not balanced.")
        # for firm in environment.firms:
        #     check_status = firm.check_consistency()
        #     if check_status is False:
        #         print(firm)
        #         raise LookupError("Firm's books are not balanced.")
        # for household in environment.households:
        #     check_status = household.check_consistency()
        #     if check_status is False:
        #         print(household)
        #         raise LookupError("Household's books are not balanced.")
    # -------------------------------------------------------------------------
