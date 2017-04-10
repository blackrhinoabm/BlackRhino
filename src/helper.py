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
        # environment.households[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction("deposits", "", environment.households[0].identifier, bank.identifier,
                                     amount,  bank.interest_rate_deposits,  0, -1, environment)

        # money - cash and equivalents
        amount = 100.0
        transaction = Transaction()
        transaction.add_transaction("cash", "", bank.identifier, bank.identifier,
                                     amount,  0,  0, -1, environment)

        # loans - we get the first firm from the list of firms
        # if there are no firms it will be a blank which is fine for testing
        amount = 150.0
        transaction = Transaction()
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction("loans", "", bank.identifier, environment.firms[0].identifier,
                                     amount,  bank.interest_rate_loans,  0, -1, environment)
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
        # environment.banks[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction("loans", "", environment.banks[0].identifier, firm.identifier,
                                     amount,  environment.banks[0].interest_rate_loans,  0, -1, environment)

        # money - cash and equivalents
        amount = 200.0
        transaction = Transaction()
        transaction.add_transaction("cash", "", firm.identifier, firm.identifier, amount,  0,  0, -1, environment)

        # goods - unique production
        amount = 50.0
        transaction = Transaction()
        transaction.add_transaction("goods", "", firm.identifier, firm.identifier, amount,  0,  0, -1, environment)
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
        # environment.banks[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction("deposits", "",  household.identifier, environment.banks[0].identifier,
                                     amount, environment.banks[0].interest_rate_deposits,  0, -1, environment)

        # money - cash and equivalents
        amount = 50.0
        transaction = Transaction()
        transaction.add_transaction("cash", "", household.identifier, household.identifier, amount, 0,  0, -1, environment)

        # manhours - labour to sell
        amount = 250.0
        transaction = Transaction()
        transaction.add_transaction("manhours", "", household.identifier, household.identifier, amount, 0,  0, -1, environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # cobb_douglas
    #
    # this routine calculates production according to
    # Cobb-Douglas production function
    # https://en.wikipedia.org/wiki/Cobb%E2%80%93Douglas_production_function
    # -------------------------------------------------------------------------
    def cobb_douglas(self, labour, capital, total_factor_productivity, labour_elasticity, capital_elasticity):
        production = 0.0
        production = total_factor_productivity * labour ** labour_elasticity * capital ** capital_elasticity
        return production
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # leontief
    #
    # this routine calculates production according to
    # Leontief production function
    # https://en.wikipedia.org/wiki/Leontief_production_function
    # -------------------------------------------------------------------------
    def leontief(self, input_, constants):
        dummy = []
        for i in range(0, len(input_)):
            dummy.append(input_[i]/constants[i])
        production = 0.0
        production = min(dummy)
        return production
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # ces
    #
    # this routine calculates production according to
    # Constant elasticity of substitution production function
    # https://en.wikipedia.org/wiki/Constant_elasticity_of_substitution
    # -------------------------------------------------------------------------
    def ces(self, labour, capital, capital_share, elasticity_of_substitution):
        r = (elasticity_of_substitution - 1) / elasticity_of_substitution
        production = 0.0
        production = (capital_share * capital ** r + (1 - capital_share) * labour ** r) ** (1 / r)
        return production
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # translog
    #
    # this routine calculates production according to
    # translog production function
    # https://en.wikipedia.org/wiki/Cobb%E2%80%93Douglas_production_function
    # -------------------------------------------------------------------------
    def translog(self, labour, capital, a_0, a_l, a_c, a_ll, a_cc, a_lc):
        import math
        production = 0.0
        production = a_0 +\
            a_l * math.log(labour) + \
            a_c * math.log(capital) + \
            a_ll * (math.log(labour)) ** 2 + \
            a_cc * (math.log(capital)) ** 2 + \
            a_lc * math.log(labour) * math.log(capital)
        production = math.exp(production)
        return production
    # -------------------------------------------------------------------------
