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

# ============================================================================
#
# class Helper
#
# ============================================================================


class Helper(object):
    #
    #
    # VARIABLES
    #
    #

    #
    #
    # CODE
    #
    #

    # -------------------------------------------------------------------------
    # initialize_standard_bank
    #
    # this routine initializes a bank with a standard balance sheet,
    # which can be used to make the tests more handy
    # -------------------------------------------------------------------------
    def initialize_standard_bank(self, bank, environment):
        from src.transaction import Transaction

        bank.identifier = "standard_bank_id"

        # deposits - we get the first household from the list of households
        # if there are no households it will be a blank which is fine for testing
        amount = 250.0
        transaction = Transaction()
        transaction.this_transaction("deposits", "", environment.households[0].identifier, bank.identifier,
                                     amount,  bank.interest_rate_deposits,  0, -1)
        # environment.households[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(environment)

        # money - cash and equivalents
        amount = 100.0
        transaction = Transaction()
        transaction.this_transaction("cash", "", bank.identifier, bank.identifier,
                                     amount,  0,  0, -1)
        transaction.add_transaction(environment)

        # loans - we get the first firm from the list of firms
        # if there are no firms it will be a blank which is fine for testing
        amount = 150.0
        transaction = Transaction()
        transaction.this_transaction("loans", "", bank.identifier, environment.firms[0].identifier,
                                     amount,  bank.interest_rate_loans,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_standard_firm
    #
    # this routine initializes a firm with a standard balance sheet,
    # which can be used to make the tests more handy
    # -------------------------------------------------------------------------
    def initialize_standard_firm(self, firm, environment):
        from src.transaction import Transaction

        firm.identifier = "standard_firm_id"  # identifier
        firm.parameters["productivity"] = 1.20  # how much goods do we get from 1 unit of labour

        # loans - we get the first bank from the list of banks
        # if there are no banks it will be a blank which is fine for testing
        amount = 250.0
        transaction = Transaction()
        transaction.this_transaction("loans", "", environment.banks[0].identifier, firm.identifier,
                                     amount,  environment.banks[0].interest_rate_loans,  0, -1)
        # environment.banks[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(environment)

        # money - cash and equivalents
        amount = 200.0
        transaction = Transaction()
        transaction.this_transaction("cash", "", firm.identifier, firm.identifier, amount,  0,  0, -1)
        transaction.add_transaction(environment)

        # goods - unique production
        amount = 50.0
        transaction = Transaction()
        transaction.this_transaction("goods", "", firm.identifier, firm.identifier, amount,  0,  0, -1)
        transaction.add_transaction(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_standard_household
    #
    # this routine initializes a household with a standard balance sheet,
    # which can be used to make the tests more handy
    # -------------------------------------------------------------------------
    def initialize_standard_household(self, household, environment):
        from src.transaction import Transaction

        household.identifier = "standard_household_id"  # identifier
        household.parameters["labour"] = 24.00  # labour to sell per step
        household.parameters["propensity_to_save"] = 0.40  # propensity to save
        # percentage of income household wants to save as deposits

        # deposits - we get the first bank from the list of banks
        # if there are no banks it will be a blank which is fine for testing
        amount = 200.0
        transaction = Transaction()
        transaction.this_transaction("deposits", "",  household.identifier, environment.banks[0].identifier,
                                     amount, environment.banks[0].interest_rate_deposits,  0, -1)
        # environment.banks[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(environment)

        # money - cash and equivalents
        amount = 50.0
        transaction = Transaction()
        transaction.this_transaction("cash", "", household.identifier, household.identifier, amount, 0,  0, -1)
        transaction.add_transaction(environment)

        # manhours - labour to sell
        amount = 250.0
        transaction = Transaction()
        transaction.this_transaction("manhours", "", household.identifier, household.identifier, amount, 0,  0, -1)
        transaction.add_transaction(environment)
    # -------------------------------------------------------------------------
