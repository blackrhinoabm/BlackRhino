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
        self.accrue_interests(environment, time)
        # Then agents get their labour endowment for the step (work hours to spend)
        self.endow_labour(environment, time)
        # Households sell labour
        self.sell_labour(environment, time)  # CHECK CAREFULLY
        # Firms produce
        self.produce(environment, time)
        # Households buy goods
        self.consume(environment, time)  # CHECK CAREFULLY
        # Households make deposits
        self.make_deposits(environment, time)
        # Labour and goods are perishable, so must be removed before next step
        self.remove_labour(environment, time)
        # Labour and goods are perishable, so must be removed before next step
        self.remove_goods(environment, time)
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
            amount = production_factors * firm.productivity
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
                                amount_proxy = min(tranx.amount, tranx_h.amount, to_consume)
                                # And remove the appropriate amount of cash
                                tranx_h.amount = tranx_h.amount - amount_proxy
                                # Lower the amount household wants to consume
                                to_consume = to_consume - amount_proxy
                                # And remove the goods from firm's account
                                tranx.amount = tranx.amount - amount_proxy
                                # And we note the cash to be added to the firm
                                firm_cash = firm_cash + amount_proxy
                        for tranx_h in household.accounts:
                            # And look for deposits
                            if tranx_h.type_ == "deposits":
                                # We can buy for minimum of the deposits and goods
                                # in question
                                amount_proxy = min(tranx.amount, tranx_h.amount, to_consume)
                                # And remove the appropriate amount of deposits
                                tranx_h.amount = tranx_h.amount - amount_proxy
                                # Lower the amount household wants to consume
                                to_consume = to_consume - amount_proxy
                                # And remove the goods from firm's account
                                tranx.amount = tranx.amount - amount_proxy
                                # And we note the cash to be added to the firm
                                firm_cash = firm_cash + amount_proxy
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