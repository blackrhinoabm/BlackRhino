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
        # Firms produce
        # Households buy goods
        # Households make deposits
        self.remove_labour(environment, time)
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
    # labour endowment for every step
    # -------------------------------------------------------------------------
    def endow_labour(self,  environment, time):
        # We make sure household get their labour endowment per step
        for household in environment.households:
            # First, we set a control variable that makes sure we have exactly
            # one transaction with "manhours", though this should in general
            # be the case
            check = 0
            for tranx in household.accounts:
                if tranx.type_ == "manhours":
                    if check == 0:
                        # If this is the first appropriate transaction found we fix the amount to the parameter
                        tranx.amount == household.labour
                        check += 1
                    else:
                        # If we have more than one "mahhours" transaction we raise an error
                        raise LookupError("Too many labour transactions for a household.")
            # If there are no "manhours" transactions then we create one and add it to the household's accounts
            if check == 0:
                amount = household.labour
                transaction = Transaction()
                transaction.this_transaction("manhours", "", household.identifier, household.identifier, amount, 0,  0, -1)
                # It's important to add the transaction using the method
                # from Transaction class and not manually
                transaction.add_transaction()
        logging.info("  labour endowed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # sell_labour
    # -------------------------------------------------------------------------
    def sell_labour(self,  environment):
        # find the cash available through loans in the system
        for firm in environment.firms:  #TODO: make this iterate randomly
            # find the available cash of the firm
            # find the collateral value for loans
            # go through households and buy all the labour firm can afford
            # 
            pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # produce
    # -------------------------------------------------------------------------
    def produce(self,  environment):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # consume
    # -------------------------------------------------------------------------
    def consume(self,  environment):
        for household in environment.households:
            wealth = 0.0  # total of deposits and cash available for the household
            cash = 0.0  # total of cash available for the household
            # We calculate the above
            for tranx in household.accounts:
                if tranx.type_ == "deposits" or tranx.type_ == "cash":
                    wealth += tranx.amount
                if tranx.type_ == "cash":
                    cash += tranx.amount
            # We consume the percentage of wealth of, cash first
            to_consume = wealth * (1 - household.propensity_to_save)
            # Consume here: firms sell goods,
            # We randomise the order of firms
            # TODO: randomise the households selling too above
            itrange = list(range(0, environment.num_firms))
            random.shuffle(itrange)
            # For each firm in random order
            for i in itrange:
                for tranx in environment.firms[i].accounts:
                    if tranx.type_ == "goods":
                        for tranx_h in household.accounts:
                            if tranx_h == "cash":
                                amount_proxy = min(tranx.amount, to_consume)
                                tranx_h.amount += amount_proxy
                        to_consume -= amount_proxy
                        tranx.amount -= amount_proxy
        for household in environment.households:
            household.purge_acconts()
        for firm in environment.firms:
            firm.purge_acconts()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # push_savings
    # -------------------------------------------------------------------------
    def push_savings(self,  environment):
        for household in environment.households:
            cash = 0.0  # total of cash available for the household
            control_deposits = 0  # checking if the household already has a deposit
            # We calculate the available cash
            for tranx in household.accounts:
                if tranx.type_ == "cash":
                    cash += tranx.amount
                    tranx.amount = 0
            # And move all available cash to deposits at the end of the step
            for tranx in household.accounts:
                # If we already have a deposit in one of the banks we add the cash there
                if tranx.type_ == "deposits":
                    tranx.amount += cash
                    control_deposits += 1
                # If there are no prior deposits we choose a random bank and make a deposit there
                if control_deposits == 0:
                    random_bank = random.choice(environment.banks)
                    transaction = Transaction()
                    transaction.this_transaction("deposits", "",  household.identifier, random_bank,
                                     amount, random_bank.interest_rate_deposits,  0, -1)
                    household.accounts.append(transaction)
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
                to_delete = []
                to_delete[:] = [x for x in household.accounts if x.type_ == "manhours"]
                # Once we have the transactions to find in a separate list
                # We remove them from the appropriate books using the
                # method from the Transaction class
                for tranx in to_delete:
                    tranx.remove_transaction()
        logging.info("  labour removed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------
