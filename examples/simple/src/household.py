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

import logging
from abm_template.src.baseagent import BaseAgent

# ============================================================================
#
# class Household
#
# ============================================================================


class Household(BaseAgent):
    #
    #
    # VARIABLES
    #
    #
    identifier = ""  # identifier of the specific household
    parameters = {}  # parameters of the specific household
    state_variables = {}  # state variables of the specific household
    accounts = []  # all accounts of a household (filled with transactions)
    # DO NOT EVER ASSIGN PARAMETERS BY HAND AS DONE BELOW IN PRODUCTION CODE
    # ALWAYS READ THE PARAMETERS FROM CONFIG FILES
    # OR USE THE FUNCTIONS FOR SETTING / CHANGING VARIABLES
    # CONVERSELY, IF YOU WANT TO READ THE VALUE, DON'T USE THE FULL NAMES
    # INSTEAD USE __getattr__ POWER TO CHANGE THE COMMAND FROM
    # instance.static_parameters["xyz"] TO instance.xyz - THE LATTER IS PREFERRED
    parameters["labour"] = 0.0  # labour to sell every step (labour endowment)
    parameters["propensity_to_save"] = 0.40  # propensity to save, percentage of income household wants to save as deposits
    parameters["active"] = 0  # this is a control parameter checking whether bank is active

    #
    #
    # CODE
    #
    #

    # -------------------------------------------------------------------------
    # functions for setting/changing id, parameters, and state variables
    # these either return or set specific value to the above variables
    # with the exception of append (2 last ones) which append the dictionaries
    # which contain parameters or state variables
    # -------------------------------------------------------------------------
    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Household, self).set_identifier(value)

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, value):
        super(Household, self).set_parameters(value)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, value):
        super(Household, self).set_state_variables(value)

    def append_parameters(self, value):
        super(Household, self).append_parameters(value)

    def append_state_variables(self, value):
        super(Household, self).append_state_variables(value)

    # -------------------------------------------------------------------------
    # functions needed to make Household() hashable
    # -------------------------------------------------------------------------
    def __key__(self):
        return self.identifier

    def __eq__(self, other):
        return self.__key__() == other.__key__()

    def __hash__(self):
        return hash(self.__key__())
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self):
        self.accounts = []  # clear transactions when household is initialized
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __del__
    # -------------------------------------------------------------------------
    def __del__(self):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __str__
    # returns a string describing the household and its properties
    # based on the implementation in the abstract class BaseAgent
    # but adds the type of agent (household) and lists all transactions
    # -------------------------------------------------------------------------
    def __str__(self):
        household_string = super(Household, self).__str__()
        household_string = household_string.replace("\n", "\n    <type value='household'>\n", 1)
        text = "\n"
        for transaction in self.accounts:
            text += transaction.write_transaction()
        text += "  </agent>"
        return household_string.replace("\n  </agent>", text, 1)
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_parameters_from_file
    # reads the specified config file given the environment
    # and sets parameters to the ones found in the config file
    # the config file should be an xml file that looks like the below:
    # <household identifier='string'>
    #     <parameter name='string' value='string'></parameter>
    # </household>
    # -------------------------------------------------------------------------
    def get_parameters_from_file(self,  household_filename, environment):
        super(Household, self).get_parameters_from_file(household_filename, environment)
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_new_savings
    # placeholder for a function determining savings size of a household
    # -------------------------------------------------------------------------
    def get_new_savings(self, low, high):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # check_consistency
    # checks whether the assets and liabilities have the same total value
    # the types of transactions that make up assets and liabilities is
    # controlled by the lists below
    # NOT IMPLEMENTED FOR HOUSEHOLD YET, NEED TO FILL assets & liabilities
    # -------------------------------------------------------------------------
    def check_consistency(self):
        assets = []
        liabilities = []
        return super(Household, self).check_consistency(assets, liabilities)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account
    # returns the value of all transactions of a given type
    # -------------------------------------------------------------------------
    def get_account(self,  type_):
        return super(Household, self).get_account(type_)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account_num_transactions
    # returns the number of transactions of a given type
    # -------------------------------------------------------------------------
    def get_account_num_transactions(self,  type_):
        return super(Household, self).get_account_num_transactions(type_)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # add_transaction
    # adds a transaction to the accounts
    # the transaction is endowed with the following information:
    #   type_           - type of transactions, e.g. "deposit"
    #   assets          - type of asset, used for investment types
    #   from_id         - agent being the originator of the transaction
    #   to_id           - agent being the recipient of the transaction
    #   amount          - amount of the transaction
    #   interest        - interest rate paid to the originator each time step
    #   maturity        - time (in steps) to maturity
    #   time_of_default - control variable checking for defaulted transactions
    # -------------------------------------------------------------------------
    def add_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction(type_, asset, from_id, to_id, amount, interest, maturity, time_of_default)
        self.accounts.append(transaction)
        del transaction  # append() above does make a copy so we may delete for garbage collection
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # clear_accounts
    # removes all transactions from bank's accounts
    # -------------------------------------------------------------------------
    def clear_accounts(self):
        super(Household, self).clear_accounts()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # purge_accounts
    # removes worthless transactions from bank's accounts
    # -------------------------------------------------------------------------
    def purge_accounts(self):
        super(Household, self).purge_accounts()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_transactions_from_file
    # reads transactions from the config file to the household's accounts
    # -------------------------------------------------------------------------
    def get_transactions_from_file(self, filename, environment):
        super(Household, self).get_transactions_from_file(filename, environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __getattr__
    # if the attribute isn't found by Python we tell Python
    # to look for it first in parameters and then in state variables
    # which allows for directly fetching parameters from the Household
    # i.e. household.active instead of a bit more bulky
    # household.parameters["active"]
    # makes sure we don't have it in both containers, which
    # would be bad practice [provides additional checks]
    # -------------------------------------------------------------------------
    def __getattr__(self, attr):
        if (attr in self.parameters) and (attr in self.state_variables):
            raise AttributeError('The same name exists in both parameters and state variables.')
        else:
            try:
                return self.parameters[attr]
            except:
                try:
                    return self.state_variables[attr]
                except:
                    raise AttributeError('Household has no attribute "%s".' % attr)
    # -------------------------------------------------------------------------
