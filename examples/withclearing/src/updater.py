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
    agents = []
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

    def get_agents(self):
        return self.agents

    def set_agents(self, _value):
        super(Updater, self).set_agents(_value)

    def get_interactions(self):
        return self.interactions

    def set_interactions(self, _value):
        super(Updater, self).set_interactions(_value)

    def get_agent_by_id(self, _id):
        super(Updater, self).get_agent_by_id(_id)

    def check_agent_homogeneity(self):
        super(Updater, self).check_agent_homogeneity()

    def initialize_agents(self):
        super(Updater, self).initialize_agents()

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

        print "Accounts:" , environment.banks[0].identifier, environment.banks[0].accounts

        self.accrue_interests(environment, time)
        # Then agents get their labour endowment for the step (work hours to spend)
        self.endow_labour(environment, time)
        # Households sell labour
        #self.sell_labour(environment, time)
        self.sell_labour_priced(environment, time)
        # Firms produce
        self.produce(environment, time)
        # Households buy goods
        self.consume_rationed(environment, time)
        # Households make deposits
        self.make_deposits(environment, time)
        # Labour and goods are perishable, so must be removed before next step
        self.remove_labour(environment, time)
        # Labour and goods are perishable, so must be removed before next step
        self.remove_goods(environment, time)
        # Collapse cash transactions, just in case
        self.collapse_one_sided(environment, time, "cash")
        # Purge accounts at the end of the routine
        transaction = Transaction()
        transaction.purge_accounts(environment)
        # //Need to work loans to the above, presumably around selling labour
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # accrue_interests(environment, time)
    # This method accrues interest on all transaction
    # making sure we don't double count the transactions that are
    # on the books of multiple agents, interest is specified within the
    # transaction itself
    # -------------------------------------------------------------------------
    def accrue_interests(self,  environment, time):
        done_list = []  # This keeps the IDs of updated transactions
        # The above is important as the same transactions may be on the books
        # of different agents, we don't want to double count the interest
        for agent in environment.agents_generator():  # Iterate over all agents

            for tranx in agent.accounts:  # Iterate over all transactions
                if tranx.identifier not in done_list:  # If not amended previously
                    # The below adds the interest on the principal amount

                    tranx.amount = tranx.amount + tranx.amount * tranx.interest
                    # The below makes sure that we don't double count
                    done_list.append(tranx.identifier)
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
        for household in environment.households:
            # First, we set a control variable that makes sure we have exactly
            # one transaction with "manhours", though this should in general
            # be the case, this should always run through the second if
            check = 0
            for tranx in household.accounts:
                if tranx.type_ == "manhours":
                    check = check + 1  # We check how many transactions with manhours are there for the household
            # If there are no "manhours" transactions then we create one and add it to the household's accounts
            if check == 0:
                # The amount is equal to the parameter read from the config of the household
                amount = household.labour
                # We create the transaction
                transaction = Transaction()
                # We add the appropriate values to the transaction
                transaction.this_transaction("manhours", "", household.identifier, household.identifier, amount, 0,  0, -1)
                # It's important to add the transaction using the method
                # from Transaction class and not manually
                transaction.add_transaction(environment)
            else:
                # If we have more than one "mahhours" transaction we raise an error
                raise LookupError("Labour transactions for a household haven't been properly removed.")
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
        # We want the sell to be done in random pairs
        # So we need to randomise the households and the firms
        # We start with the firms and create a list of order integers
        # the size of the number of firms
        itrange = list(range(0, int(environment.num_firms)))
        # Then we shuffle the list
        random.shuffle(itrange)
        # And use it to loop over the firms randomly
        for i in itrange:
            # Since we don't loop directly over firms
            # We assign the correct firm in this run over the loop
            firm = environment.firms[i]
            # We calculate the amount of cash firm has to buy labour
            to_buy = 0.0
            # We go through the firm's transactions
            for tranx in firm.accounts:
                # If we find cash transaction
                if tranx.type_ == "cash":
                    # We add the cash to the amount of labour the firm
                    # wants to buy, we assume 1 unit of labour costs 1 unit of cash
                    to_buy = to_buy + tranx.amount
            # Now we randomise households and create a list of order integers
            # the size of the number of households
            itrange_hh = list(range(0, int(environment.num_households)))
            # Then we shuffle the list
            random.shuffle(itrange_hh)
            # For each household in random order
            for h in itrange_hh:
                # Since we don't loop directly over households
                # We assign the correct household in this run over the loop
                household = environment.households[h]
                household_cash = 0.0
                # We go through household's accounts
                for tranx in household.accounts:
                    # And find transactions with labour
                    if tranx.type_ == "manhours":
                        # We will sell them for cash
                        # So we look through firm's accounts
                        for tranx_f in firm.accounts:
                            # And find cash transactions
                            if tranx_f.type_ == "cash":
                                # We can only buy the lowest amount from the cash the firm
                                # has, the labour the household has, and however many units
                                # they want to buy
                                amount_proxy = min(tranx.amount, tranx_f.amount, to_buy)
                                # Then we remove the appropriate amount of cash from the firm
                                tranx_f.amount = tranx_f.amount - amount_proxy
                                # Lower the amount firm wants to buy
                                to_buy = to_buy - amount_proxy
                                # And remove the goods from household's account
                                tranx.amount = tranx.amount - amount_proxy
                                # And we note the cash to be added to the household
                                household_cash = household_cash + amount_proxy
                                # Create a transaction
                                transaction = Transaction()
                                # Add the appropriate values to the transaction
                                transaction.this_transaction("manhours", "",  firm.identifier, firm.identifier,
                                                             amount_proxy, 0,  0, -1)
                                # And add the transaction to the books (do it through function/not manually)
                                transaction.add_transaction(environment)
                # Add cash for sold items to the household
                cash_number = 0
                # We calculate how many cash account the household has
                for tranx in household.accounts:
                    if tranx.type_ == "cash":
                        cash_number = cash_number + 1
                # If there are no cash transactions on the household's books
                # We create a new one and put the proceeds there
                if cash_number == 0:
                    # Create a transaction
                    transaction = Transaction()
                    # Add the appropriate values to the transaction
                    transaction.this_transaction("cash", "",  household.identifier, household.identifier,
                                                 household_cash, 0,  0, -1)
                    # And add the transaction to the books (do it through function/not manually)
                    transaction.add_transaction(environment)
                # If the household has previous cash transactions we add the cash from sales proportionately
                else:
                    # We find all cash transactions
                    for tranx in household.accounts:
                        if tranx.type_ == "cash":
                            # And add the sales proceeds proportionately
                            tranx.amount = tranx.amount + (household_cash / cash_number)
        # The sales above may have rendered some transactions worthless
        # So we need to purge all accounts to make sure everything is in order
        transaction = Transaction()
        transaction.purge_accounts(environment)
        logging.info("  labour sold to firms on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # sell_labour_priced(environment, time)
    # This function allows the households to sell their labour to firms
    # For now we assume that firms want to buy all the labour they can get
    # And that they need to use cash for this purpose, they can't take loans
    # And firms keep cash, they do not keep deposits, these will be updated
    # in later time
    # -------------------------------------------------------------------------
    def sell_labour_priced(self,  environment, time):
        # First we find the market equilibrium price
        # Important to note that this currently does
        # not depend on the wealth of the buyers
        # That is their demand may be higher than
        # what they can actually buy, which may be ok
        # We set the values necessary for tatonnement
        # The list of suppliers and their supply functions
        suppliers = []
        for agent in environment.households:
            suppliers.append([agent, agent.supply_of_labour])
        # And the list of buyers and their demand functions
        buyers = []
        for agent in environment.firms:
            buyers.append([agent, agent.demand_for_labour])
        # We may start the search for price at some specific point
        # Here we pass 0, which means it'll start looking at a
        # random point between 0 and 10
        starting_price = 0.0
        # We initialize the price
        price = 0.0
        # Import market clearing class
        from market import Market
        # Put the appropriate settings, i.e.
        # tolerance of error, resolution of search
        # and amplification for exponential search
        market = Market("market", 0.01, 0.01, 1.1)
        # And we find the market price of labour
        # given supply and demand of the agents
        price = market.tatonnement(suppliers, buyers, starting_price)
        ## print(price) # This is for testing, should be commented out
        # We find the amount of supply the households have
        # at market price
        to_sell = list(range(0, int(environment.num_households)))
        for h in range(0, len(to_sell)):
            to_sell[h] = environment.households[h].supply_of_labour(price)
        # We want the sell to be done in random pairs
        # So we need to randomise the households and the firms
        # We start with the firms and create a list of order integers
        # the size of the number of firms
        itrange = list(range(0, int(environment.num_firms)))
        # Then we shuffle the list
        random.shuffle(itrange)
        # And use it to loop over the firms randomly
        for i in itrange:
            # Since we don't loop directly over firms
            # We assign the correct firm in this run over the loop
            firm = environment.firms[i]
            # We calculate the amount of demand firm has at the market price
            to_buy = firm.demand_for_labour(price)
            # Now we randomise households and create a list of order integers
            # the size of the number of households
            itrange_hh = list(range(0, int(environment.num_households)))
            # Then we shuffle the list
            random.shuffle(itrange_hh)
            # For each household in random order
            for h in itrange_hh:
                # Since we don't loop directly over households
                # We assign the correct household in this run over the loop
                household = environment.households[h]
                household_cash = 0.0
                # We go through household's accounts
                for tranx in household.accounts:
                    # And find transactions with labour
                    if tranx.type_ == "manhours":
                        # We will sell them for cash
                        # So we look through firm's accounts
                        for tranx_f in firm.accounts:
                            # And find cash transactions
                            if tranx_f.type_ == "cash":
                                # We can only buy the lowest amount from the cash the firm
                                # has, the labour the household has, and however many units
                                # they want to buy
                                amount_proxy = min(tranx.amount, tranx_f.amount/price, to_buy, to_sell[h])
                                # MOVE TO LOGGING FOR PRODUCTION
                                print("%s sold %d units of labour at a price %f to %s at time %d.") % (household.identifier, amount_proxy, price, firm.identifier, time)
                                # We only sell labour in full amounts
                                # Can think about it as full hours
                                amount_proxy = round(amount_proxy, 0)
                                # And remove the goods from household's account
                                tranx.amount = tranx.amount - amount_proxy
                                to_sell[h] = to_sell[h] - amount_proxy
                                # Lower the amount firm wants to buy
                                to_buy = to_buy - amount_proxy
                                # Then we remove the appropriate amount of cash from the firm
                                tranx_f.amount = tranx_f.amount - amount_proxy * price
                                # And we note the cash to be added to the household
                                household_cash = household_cash + amount_proxy * price
                                # Create a transaction
                                transaction = Transaction()
                                # Add the appropriate values to the transaction
                                transaction.this_transaction("manhours", "",  firm.identifier, firm.identifier,
                                                             amount_proxy, 0,  0, -1)
                                # And add the transaction to the books (do it through function/not manually)
                                transaction.add_transaction(environment)
                # Add cash for sold items to the household
                cash_number = 0
                # We calculate how many cash account the household has
                for tranx in household.accounts:
                    if tranx.type_ == "cash":
                        cash_number = cash_number + 1
                # If there are no cash transactions on the household's books
                # We create a new one and put the proceeds there
                if cash_number == 0:
                    # Create a transaction
                    transaction = Transaction()
                    # Add the appropriate values to the transaction
                    transaction.this_transaction("cash", "",  household.identifier, household.identifier,
                                                 household_cash, 0,  0, -1)
                    # And add the transaction to the books (do it through function/not manually)
                    transaction.add_transaction(environment)
                # If the household has previous cash transactions we add the cash from sales proportionately
                else:
                    # We find all cash transactions
                    for tranx in household.accounts:
                        if tranx.type_ == "cash":
                            # And add the sales proceeds proportionately
                            tranx.amount = tranx.amount + (household_cash / cash_number)
        # The sales above may have rendered some transactions worthless
        # So we need to purge all accounts to make sure everything is in order
        transaction = Transaction()
        transaction.purge_accounts(environment)
        logging.info("  labour sold to firms on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # produce(environment, time)
    # This function lets firms to turn their production factors (labour)
    # into goods, using their know-how (productivity parameter)
    # Thus in principle firms may differ in their production function and their
    # outputs from the same amount of labour may be different
    # -------------------------------------------------------------------------
    def produce(self,  environment, time):
        # We take all the labour and turn it into goods
        for firm in environment.firms:  # We do it for every firm
            production_factors = 0  # Here, we count how much labour the firm has
            for tranx in firm.accounts:
                if tranx.type_ == "manhours":
                    # We move the labour to production as a production factor
                    # First, we move it to production factors used below
                    # Then we will remove it from the books
                    production_factors = production_factors + tranx.amount
            # Amount produced is labour * productivity in this simple model
            amount = round(production_factors * firm.productivity, 0)
            # Create a transaction
            transaction = Transaction()
            # Add the appropriate values to the transaction
            transaction.this_transaction("goods", "",  firm.identifier, firm.identifier,
                                         amount, 0,  0, -1)
            # And add the transaction to the books (do it through function/not manually)
            transaction.add_transaction(environment)
        # Finally, we remove all the labour that was used in production
        # from the books of the firms
        self.remove_labour_firms(environment, time)
        logging.info("  goods produced on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # consume(environment, time)
    # This function lets households buy the goods the firms have produced
    # so they can satisfy their needs through consumption
    # This consumption depends on the propensity to save of the households
    # The matching of buyers and sellers on the market is random
    # -------------------------------------------------------------------------
    def consume(self,  environment, time):
        # We want the consumption to be done in random pairs
        # So we need to randomise the households and the firms
        # We start with the households and create a list of order integers
        # the size of the number of households
        itrange_hh = list(range(0, int(environment.num_households)))
        # Then we shuffle the list
        random.shuffle(itrange_hh)
        # And use it to loop over the households randomly
        for h in itrange_hh:
            # Since we don't loop directly over households
            # We assign the correct household in this run over the loop
            household = environment.households[h]
            wealth = 0.0  # total of deposits and cash available for the household
            cash = 0.0  # total of cash available for the household
            # Price is static for now
            price = 50.0
            # We calculate the above two values
            for tranx in household.accounts:
                # We add all deposits and all cash to the wealth
                if tranx.type_ == "deposits" or tranx.type_ == "cash":
                    wealth = wealth + tranx.amount
                # But only cash to the available cash
                if tranx.type_ == "cash":
                    cash = cash + tranx.amount
            # We consume the percentage of wealth determined by
            # the propensity to save, cash first
            to_consume = wealth * (1 - household.propensity_to_save)
            to_consume = round(to_consume / price, 0)
            # Now we randomise firms and create a list of order integers
            # the size of the number of households
            itrange = list(range(0, int(environment.num_firms)))
            # Then we shuffle the list
            random.shuffle(itrange)
            # For each firm in random order
            for i in itrange:
                # For every transaction on that firm's books
                # We make a proxy for the cash that firm should obtain
                # for whatever good they've sold to the household
                firm = environment.firms[i]
                firm_cash = 0.0
                for tranx in firm.accounts:
                    # If the transaction contains goods
                    if tranx.type_ == "goods":
                        # We go through the household's accounts
                        for tranx_h in household.accounts:
                            # And look for cash
                            if tranx_h.type_ == "cash":
                                # We can buy for minimum of the cash and goods
                                # in question
                                amount_proxy = min(tranx.amount, tranx_h.amount/price, to_consume)
                                amount_proxy = round(amount_proxy, 0)
                                print("%s sold %d units of goods at a price %f to %s at time %d.") % (firm.identifier, amount_proxy, price, household.identifier, time)
                                # And remove the appropriate amount of cash
                                tranx_h.amount = tranx_h.amount - amount_proxy * price
                                # Lower the amount household wants to consume
                                to_consume = to_consume - amount_proxy
                                # And remove the goods from firm's account
                                tranx.amount = tranx.amount - amount_proxy
                                # And we note the cash to be added to the firm
                                firm_cash = firm_cash + amount_proxy * price
                        for tranx_h in household.accounts:
                            # And look for deposits
                            if tranx_h.type_ == "deposits":
                                # We can buy for minimum of the deposits and goods
                                # in question
                                amount_proxy = min(tranx.amount, tranx_h.amount/price, to_consume)
                                amount_proxy = round(amount_proxy, 0)
                                # And remove the appropriate amount of deposits
                                tranx_h.amount = tranx_h.amount - amount_proxy * price
                                # Lower the amount household wants to consume
                                to_consume = to_consume - amount_proxy
                                # And remove the goods from firm's account
                                tranx.amount = tranx.amount - amount_proxy
                                # And we note the cash to be added to the firm
                                firm_cash = firm_cash + amount_proxy * price
                # Add cash for sold items to the firm
                cash_number = 0
                # We calculate how many cash account the firm has
                for tranx in firm.accounts:
                    if tranx.type_ == "cash":
                        cash_number = cash_number + 1
                # If the firm doesn't have any cash accounts we create a new one
                if cash_number == 0:
                    # Create a transaction
                    transaction = Transaction()
                    # Add the appropriate values to the transaction
                    transaction.this_transaction("cash", "",  firm.identifier, firm.identifier,
                                                 firm_cash, 0,  0, -1)
                    # And add the transaction to the books (do it through function/not manually)
                    transaction.add_transaction(environment)
                # If the firm has previous cash transactions we add the cash from sales proportionately
                else:
                    # We find all cash transactions
                    for tranx in firm.accounts:
                        if tranx.type_ == "cash":
                            # And add the sales proceeds proportionately
                            tranx.amount = tranx.amount + (firm_cash / cash_number)
        # The sales above may have rendered some transactions worthless
        # So we need to purge all accounts to make sure everything is in order
        transaction = Transaction()
        transaction.purge_accounts(environment)
        # Finally, we remove the goods which weren't sold from firms' accounts
        # As they are perishable
        self.remove_goods_firms(environment, time)
        logging.info("  goods consumed on step: %s",  time)
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
        price = 50.0
        # We need a list of agents and their demand or supply
        # Supply is denoted with positive float, demand with negative float
        for_rationing = []
        # Firms give us their supply, we assume that since the goods are
        # perishable their supply is all they have in stock
        for firm in environment.firms:
            for_rationing.append([firm, firm.get_account("goods")])
        # Households give use their demand, we assume that they want to
        # consume the part of their wealth (cash and deposits) that they
        # do not want to save (determined through propensity to save)
        # We denote demand in units of the goods, so we divide the cash
        # households want to spend by price to get the demand
        for household in environment.households:
            demand = 0.0
            demand = -round((((household.get_account("cash") + household.get_account("deposits")) * (1 - household.propensity_to_save)) / price), 0)
            for_rationing.append([household, demand])
        # We import the market clearing class
        from market import Market
        # Put the appropriate settings, i.e.
        # tolerance of error, resolution of search
        # and amplification for exponential search
        # This does not matter for rationing
        # But in principle we need to initialize
        # with these values
        market = Market("market", 0.0, 0.0, 0.0)
        # And we find the rationing, ie the amounts
        # of goods sold between pairs of agents
        rationed = market.rationing(for_rationing)
        # Then we go through the rationing
        # and move the goods and cash appropriately
        for ration in rationed:
            # We have the agent selling goods
            # who gets the cash
            agent_from = ration[0]
            # And the agent buying goods
            # who gives the cash
            agent_to = ration[1]
            # And the amount of goods transferred
            ration_amount = ration[2]
            # And it's hard copy for changing
            ration_goods = ration_amount
            # And a copy for the amount of cash as well
            ration_cash = ration_amount * price
            # We print the action of selling to the screen
            print("%s sold %d units of goods at a price %f to %s at time %d.") % (agent_from.identifier, ration_goods, price, agent_to.identifier, time)
            # AGENT_TO GOODS +
            # Add goods for sold items to the agent
            goods_number = 0
            # We calculate how many goods account the agent has
            for tranx in agent_from.accounts:
                if tranx.type_ == "goods":
                    goods_number = goods_number + 1
            # If the agent doesn't have any goods accounts we create a new one
            if goods_number == 0:
                # Create a transaction
                transaction = Transaction()
                # Add the appropriate values to the transaction
                transaction.this_transaction("goods", "",  agent_from.identifier, agent_from.identifier,
                                             ration_goods, 0,  0, -1)
                # And add the transaction to the books (do it through function/not manually)
                transaction.add_transaction(environment)
            # If the agent has previous goods transactions we add the goods from sales proportionately
            else:
                # We find all goods transactions
                for tranx in agent_from.accounts:
                    if tranx.type_ == "goods":
                        # And add the sales proceeds proportionately
                        tranx.amount = tranx.amount + (ration_goods / goods_number)
            # AGENT_FROM GOODS -
            # We go through the agent's accounts
            # and remove the goods that are sold
            for tranx in agent_from.accounts:
                if tranx.type_ == "goods":
                    # We can only remove the minimum of what's in the
                    # transaction and what is left to sell for the agent
                    amount_proxy = min(tranx.amount, ration_goods)
                    # We adjust the amount in the transaction
                    tranx.amount = tranx.amount - amount_proxy
                    # And we diminish the amount that agents should sell
                    # from other transactions
                    ration_goods = ration_goods - amount_proxy
            # AGENT_FROM CASH +
            # Add cash for sold items to the agent
            cash_number = 0
            # We calculate how many cash account the agent has
            for tranx in agent_from.accounts:
                if tranx.type_ == "cash":
                    cash_number = cash_number + 1
            # If the agent doesn't have any cash accounts we create a new one
            if cash_number == 0:
                # Create a transaction
                transaction = Transaction()
                # Add the appropriate values to the transaction
                transaction.this_transaction("cash", "",  agent_from.identifier, agent_from.identifier,
                                             ration_cash, 0,  0, -1)
                # And add the transaction to the books (do it through function/not manually)
                transaction.add_transaction(environment)
            # If the agent has previous cash transactions we add the cash from sales proportionately
            else:
                # We find all cash transactions
                for tranx in agent_from.accounts:
                    if tranx.type_ == "cash":
                        # And add the sales proceeds proportionately
                        tranx.amount = tranx.amount + (ration_cash / cash_number)
            # AGENT_TO CASH -
            for tranx in agent_to.accounts:
                # We first pay for the goods with cash
                if tranx.type_ == "cash":
                    # We can only remove the minimum of what's in the
                    # transaction and what is left to sell for the agent
                    amount_proxy = min(tranx.amount, ration_cash)
                    # We adjust the amount in the transaction
                    tranx.amount = tranx.amount - amount_proxy
                    # And we diminish the amount that agents should sell
                    # from other transactions
                    ration_cash = ration_cash - amount_proxy
            for tranx in agent_to.accounts:
                # And only if cash is not enough we pay with deposits
                if tranx.type_ == "deposits":
                    # We can only remove the minimum of what's in the
                    # transaction and what is left to sell for the agent
                    amount_proxy = min(tranx.amount, ration_cash)
                    # We adjust the amount in the transaction
                    tranx.amount = tranx.amount - amount_proxy
                    # And we diminish the amount that agents should sell
                    # from other transactions
                    ration_cash = ration_cash - amount_proxy
        # So we need to purge all accounts to make sure everything is in order
        transaction = Transaction()
        transaction.purge_accounts(environment)
        # Finally, we remove the goods which weren't sold from firms' accounts
        # As they are perishable
        self.remove_goods_firms(environment, time)
        logging.info("  goods consumed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # make_deposits(environment, time)
    # This function makes deposits of all the remaining cash of the households
    # It is important to notice that this ultimately depends on the propensity
    # to save parameter, but indirectly, since it influences how much in goods
    # the agents buy from firms prior to this step, thus allowing this step
    # to be easier and move all cash to deposits in the banks
    # -------------------------------------------------------------------------
    def make_deposits(self,  environment, time):
        for household in environment.households:
            cash = 0.0  # total of cash available for the household
            control_deposits = 0  # checking if the household already has deposits
            # We calculate the available cash
            for tranx in household.accounts:
                if tranx.type_ == "cash":
                    cash = cash + tranx.amount
                    tranx.amount = 0
            # And the number of existing deposits
                if tranx.type_ == "deposits":
                    control_deposits = control_deposits + 1
            # And move all available cash to deposits at the end of the step
            # If there are no deposits we create one in a bank
            # The bank is chosen randomly
            if control_deposits == 0:
                # We choose a bank randomly
                random_bank = random.choice(environment.banks)
                # Create a transaction
                transaction = Transaction()
                # Add the appropriate values to the transaction
                transaction.this_transaction("deposits", "",  household.identifier, random_bank,
                                             amount, random_bank.interest_rate_deposits,  0, -1)
                # And add the transaction to the books (do it through function/not manually)
                transaction.add_transaction(environment)
            # If there are previous deposits we expand them linearly
            else:
                for tranx in household.accounts:
                    if tranx.type_ == "deposits":
                        # We add the remaining cash to the existing deposits
                        # in equal proportions
                        # Perhaps this can be done proportionate with regards
                        # to the value of these deposits, but it's minor at this point
                        tranx.amount = tranx.amount + (cash/control_deposits)
        logging.info("  deposits made on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # remove_labour(environment, time)
    # This function removes all the labour that hasn't been sold within
    # sell_labour, in economic terms this means that labour doesn't carry
    # over to the next step, just like in the real economy
    # -------------------------------------------------------------------------
    def remove_labour(self,  environment, time):
        # We go through all households
        for household in environment.households:
                # We find the transactions that should be deleted from household's books
                # We don't iterate over the accounts directly since we want to delete
                # them and this could cause the loop to jump around
                to_delete = []  # An empty list to be used to keep the transactions to delete
                # The below creates a SOFT COPY of the transactions that contain labour
                to_delete[:] = [x for x in household.accounts if x.type_ == "manhours"]
                # Once we have the transactions to find in a separate list
                # We remove them from the appropriate books using the
                # method from the Transaction class
                for tranx in to_delete:
                    # This is important, we shouldn't do it manually though del/remove
                    tranx.remove_transaction()
        logging.info("  labour removed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # remove_labour_firms(environment, time)
    # This function removes all the labour that hasn't been sold within
    # sell_labour, in economic terms this means that labour doesn't carry
    # over to the next step, just like in the real economy
    # -------------------------------------------------------------------------
    def remove_labour_firms(self,  environment, time):
        # We go through all households
        for firm in environment.firms:
                # We find the transactions that should be deleted from firm's books
                # We don't iterate over the accounts directly since we want to delete
                # them and this could cause the loop to jump around
                to_delete = []  # An empty list to be used to keep the transactions to delete
                # The below creates a SOFT COPY of the transactions that contain labour
                to_delete[:] = [x for x in firm.accounts if x.type_ == "manhours"]
                # Once we have the transactions to find in a separate list
                # We remove them from the appropriate books using the
                # method from the Transaction class
                for tranx in to_delete:
                    # This is important, we shouldn't do it manually though del/remove
                    tranx.remove_transaction()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # remove_goods(environment, time)
    # This function removes all the goods that hasn't been sold within
    # the step, in economic terms this means that goods doesn't carry
    # over to the next step, i.e. goods are perishable
    # -------------------------------------------------------------------------
    def remove_goods(self,  environment, time):
        # We go through all households
        for household in environment.households:
                # We find the transactions that should be deleted from household's books
                # We don't iterate over the accounts directly since we want to delete
                # them and this could cause the loop to jump around
                to_delete = []  # An empty list to be used to keep the transactions to delete
                # The below creates a SOFT COPY of the transactions that contain goods
                to_delete[:] = [x for x in household.accounts if x.type_ == "goods"]
                # Once we have the transactions to find in a separate list
                # We remove them from the appropriate books using the
                # method from the Transaction class
                for tranx in to_delete:
                    # This is important, we shouldn't do it manually though del/remove
                    tranx.remove_transaction()
        logging.info("  goods removed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # remove_goods_firms(environment, time)
    # This function removes all the goods that hasn't been sold within
    # the step, in economic terms this means that goods doesn't carry
    # over to the next step, i.e. goods are perishable
    # -------------------------------------------------------------------------
    def remove_goods_firms(self,  environment, time):
        # We go through all firms
        for firm in environment.firms:
                # We find the transactions that should be deleted from firm's books
                # We don't iterate over the accounts directly since we want to delete
                # them and this could cause the loop to jump around
                to_delete = []  # An empty list to be used to keep the transactions to delete
                # The below creates a SOFT COPY of the transactions that contain goods
                to_delete[:] = [x for x in firm.accounts if x.type_ == "goods"]
                # Once we have the transactions to find in a separate list
                # We remove them from the appropriate books using the
                # method from the Transaction class
                for tranx in to_delete:
                    # This is important, we shouldn't do it manually though del/remove
                    tranx.remove_transaction()
        # logging.info("  goods removed from firms on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # collapse_one_sided(environment, time)
    # if there are more than one transaction this method will collapse them
    # this works only for single-entity transactions like cash or goods
    # do not use for stuff like deposits where there are two agents involved
    # -------------------------------------------------------------------------
    def collapse_one_sided(self,  environment, time, type_):
        # We go through all agents
        for agent in environment.agents_generator():
            # Initialize a list of items to be deleted
            to_delete = []  # An empty list to be used to keep the transactions to delete
            # The below creates a SOFT COPY of the transactions that contain cash
            to_delete[:] = [x for x in agent.accounts if x.type_ == type_]
            # We do it only
            if len(to_delete) > 1:
                # Initialize a variable for the total cash of an agent
                cash_total = 0.0
                # Find the total cash
                for tranx in to_delete:
                    cash_total = cash_total + tranx.amount
                # Delete the cash transactions
                for tranx in to_delete:
                        # This is important, we shouldn't do it manually though del/remove
                        tranx.remove_transaction()
                # And add the whole cash as a transaction
                # Create a transaction
                transaction = Transaction()
                # Add the appropriate values to the transaction
                transaction.this_transaction(type_, "",  agent.identifier, agent.identifier,
                                             cash_total, 0,  0, -1)
                # And add the transaction to the books (do it through function/not manually)
                transaction.add_transaction(environment)
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # transfer_cash(agent_from, agent_two, amount)
    # transfers cash between two agents
    # -------------------------------------------------------------------------
    def transfer_cash(self,  agent_from, agent_two, amount):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # random_agents(agent_set)
    # returns a generator randomly going through the specified set of agents
    # -------------------------------------------------------------------------
    def random_agents(self,  agent_set):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # remove_amount(agent, type, amount)
    # removes an amount of given type from a given agent from its books
    # -------------------------------------------------------------------------
    def remove_amount(self,  agent, type, amount):
        pass
    # -------------------------------------------------------------------------
