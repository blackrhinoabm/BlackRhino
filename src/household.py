#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
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
    identifier = ""
    parameters = {}
    state_variables = {}
    accounts = []  # all accounts of a bank

    parameters["labour"] = 0.0  # labour to sell every step
    parameters["propensity_to_save"] = 0.40  # propensity to save, percentage of income household wants to save as deposits
    parameters["active"] = 0

#
#
# CODE
#
#

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        super(Household, self).set_identifier(_value)

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, _value):
        """
        Class variables: parameters
        Local variables: _params
        """
        super(Household, self).set_parameters(_value)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _value):
        """
        Class variables: state_variables
        Local variables: _variables
        """
        super(Household, self).set_state_variables(_value)

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
    # -------------------------------------------------------------------------
    def __str__(self):
        text = "<household identifier='" + self.identifier + "'>\n"
        text += "    <value name='active' value='" + str(self.parameters["active"]) + "'></value>\n"
        text += "    <parameter name='labour' value='" + str(self.parameters["labour"]) + "'></parameter>\n"
        text += "    <parameter name='propensity_to_save' value='" + str(self.parameters["propensity_to_save"]) + "'></parameter>\n"
        text += "    <transactions>\n"
        for transaction in self.accounts:
            text += transaction.write_transaction()
        text += "    </transactions>\n"
        text += "</household>\n"

        return text
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_parameters_from_file
    # -------------------------------------------------------------------------
    def get_parameters_from_file(self,  householdFilename, environment):
        from xml.etree import ElementTree

        try:
            xmlText = open(householdFilename).read()
            element = ElementTree.XML(xmlText)
            self.identifier = element.attrib['identifier']

            # loop over all entries in the xml file
            for subelement in element:
                name = subelement.attrib['name']
                value = subelement.attrib['value']
                if (name == 'labour'):
                    self.parameters["labour"] = float(value)
                if (name == 'propensity_to_save'):
                    self.parameters["propensity_to_save"] = float(value)

            # self.initialize_transactions(environment)
        except:
            logging.error("    ERROR: %s could not be parsed",  householdFilename)
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_new_savings
    # -------------------------------------------------------------------------
    def get_new_savings(self, low, high):
        volume = 0.0

        from random import uniform
        volume = uniform(low, high)

        return volume
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account
    # -------------------------------------------------------------------------
    def get_account(self,  type):
        volume = 0.0

        for transaction in self.accounts:
            if (transaction.transactionType == type):
                volume = volume + float(transaction.transactionValue)

        return volume
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account_num_transactions
    # -------------------------------------------------------------------------
    def get_account_num_transactions(self,  type):  # returns the number of transactions in a given account
        num_transactions = 0.0

        for transaction in self.accounts:
            if (transaction.transactionType == type):
                num_transactions += 1

        return num_transactions
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # add_transaction
    # -------------------------------------------------------------------------
    def add_transaction(self,  type,  fromID,  toID,  value,  interest,  maturity, timeOfDefault):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction(type,  fromID,  toID,  value,  interest,  maturity,  timeOfDefault)
        self.accounts.append(transaction)
        del transaction
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # clear_accounts
    # -------------------------------------------------------------------------
    def clear_accounts(self):
        self.accounts = []
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # purge_accounts
    # -------------------------------------------------------------------------
    def purge_accounts(self):
        new_accounts = []

        for transaction in self.accounts:
            if transaction.transactionValue > 0.0:
                new_accounts.append(transaction)

        self.accounts = new_accounts
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_standard_household
    #
    # this routine initializes a household with a standard balance sheet,
    # which can be used to make the tests more handy
    # -------------------------------------------------------------------------
    def initialize_standard_household(self, environment):
        from src.transaction import Transaction

        self.identifier = "standard_household_id"  # identifier
        self.parameters["labour"] = 24.00  # labour to sell per step
        self.parameters["propensity_to_save"] = 0.40  # propensity to save, percentage of income household wants to save as deposits

        # deposits - we get the first bank from the list of banks
        # if there are no banks it will be a blank which is fine for testing
        value = 200.0
        transaction = Transaction()
        transaction.this_transaction("DEPOSIT",  self.identifier, environment.banks[0:1][0], value, environment.static_parameters["interest_rate_deposits"],  0, -1)
        self.accounts.append(transaction)
        del transaction

        # money - cash and equivalents
        value = 50.0
        transaction = Transaction()
        transaction.this_transaction("MONEY", self.identifier, self.identifier, value, 0,  0, -1)
        self.accounts.append(transaction)
        del transaction

        # manhours - labour to sell
        value = 250.0
        transaction = Transaction()
        transaction.this_transaction("MANHOURS", self.identifier, self.identifier, value, 0,  0, -1)
        self.accounts.append(transaction)
        del transaction

    # -------------------------------------------------------------------------
