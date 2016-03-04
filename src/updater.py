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
        self.accrue_interests(environment)
        self.endow_labour(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # accrue_interests
    # -------------------------------------------------------------------------
    def accrue_interests(self,  environment):
        # accruing interest on all transactions for banks
        for bank in environment.banks:
            for tranx in bank.accounts:
                    tranx.amount = tranx.amount + tranx.amount * tranx.interest

        # accruing interest on all transactions for firms
        for firm in environment.firms:
            for tranx in firm.accounts:
                    tranx.amount = tranx.amount + tranx.amount * tranx.interest

        # accruing interest on all transactions for households
        for household in environment.households:
            for tranx in household.accounts:
                    tranx.amount = tranx.amount + tranx.amount * tranx.interest
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # endow_labour
    # -------------------------------------------------------------------------
    def endow_labour(self,  environment):
        # we make sure household get their labour endowment per step
        for household in environment.households:
            # First, we set a control variable that makes sure we have exactly
            # one transaction with "manhours"
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
                household.accounts.append(transaction)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # sell_labour
    # -------------------------------------------------------------------------
    def sell_labour(self,  environment):
        for firm in environment.firms:
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
