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
# class Firm
#
# ============================================================================


class Firm(BaseAgent):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""  # identifier of the specific firm
    parameters = {}  # parameters of the specific firm
    state_variables = {}  # state variables of the specific firm
    accounts = []  # all accounts of a firm (filled with transactions)

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
        super(Firm, self).set_identifier(value)

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, value):
        super(Firm, self).set_parameters(value)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, value):
        super(Firm, self).set_state_variables(value)

    def append_parameters(self, value):
        super(Firm, self).append_parameters(value)

    def append_state_variables(self, value):
        super(Firm, self).append_state_variables(value)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # functions needed to make Firm() hashable
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
        self.identifier = ""  # identifier of the specific firm
        self.parameters = {}  # parameters of the specific firm
        self.state_variables = {}  # state variables of the specific firm
        self.accounts = []  # all accounts of a firm (filled with transactions)
        # DO NOT EVER ASSIGN PARAMETERS BY HAND AS DONE BELOW IN PRODUCTION CODE
        # ALWAYS READ THE PARAMETERS FROM CONFIG FILES
        # OR USE THE FUNCTIONS FOR SETTING / CHANGING VARIABLES
        # CONVERSELY, IF YOU WANT TO READ THE VALUE, DON'T USE THE FULL NAMES
        # INSTEAD USE __getattr__ POWER TO CHANGE THE COMMAND FROM
        # instance.static_parameters["xyz"] TO instance.xyz - THE LATTER IS PREFERRED
        self.parameters["productivity"] = 0.0  # how many units of goods do we get from 1 unit of labour
        self.parameters["active"] = 0  # this is a control parameter checking whether firm is active
        self.parameters["funding"] = 0.0  # intratemporal liquidity
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __del__
    # -------------------------------------------------------------------------
    def __del__(self):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __str__
    # returns a string describing the firm and its properties
    # based on the implementation in the abstract class BaseAgent
    # but adds the type of agent (firm) and lists all transactions
    # -------------------------------------------------------------------------
    def __str__(self):
        firm_string = super(Firm, self).__str__()
        firm_string = firm_string.replace("\n", "\n    <type value='firm''>\n", 1)
        text = "\n"
        text = text + "  </agent>"
        return firm_string.replace("\n  </agent>", text, 1)
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_parameters_from_file
    # reads the specified config file given the environment
    # and sets parameters to the ones found in the config file
    # the config file should be an xml file that looks like the below:
    # <firm identifier='string'>
    #     <parameter name='string' value='string'></parameter>
    # </firm>
    # -------------------------------------------------------------------------
    def get_parameters_from_file(self,  firm_filename, environment):
        super(Firm, self).get_parameters_from_file(firm_filename, environment)
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_new_investments
    # placeholder for a function determining production size of a firm
    # -------------------------------------------------------------------------
    def get_new_investments(self, low, high):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # check_consistency
    # checks whether the assets and liabilities have the same total value
    # the types of transactions that make up assets and liabilities is
    # controlled by the lists below
    # NOT IMPLEMENTED FOR FIRM YET, NEED TO FILL assets & liabilities
    # -------------------------------------------------------------------------
    def check_consistency(self):
        # assets = []
        # liabilities = []
        # return super(Firm, self).check_consistency(assets, liabilities)
        assets = 0.0
        liabilities = 0.0
        for tranx in self.accounts:
            if tranx.type_ == "loans":
                if tranx.from_ == self:
                    raise LookupError("Companies cannot grant loans to firms.")
                if tranx.to == self:
                    liabilities = liabilities + tranx.amount
            elif tranx.type_ == "shares":
                if tranx.from_ == self:
                    assets = assets + tranx.amount
                if tranx.to == self:
                    raise LookupError("Companies cannot own shares of banks.")
            elif tranx.type_ == "ownership":
                if tranx.from_ == self:
                    raise LookupError("Banks cannot own shares of households.")
                if tranx.to == self:
                    liabilities = liabilities + tranx.amount
            elif tranx.type_ == "deposits":
                if tranx.from_ == self:
                    assets = assets + tranx.amount
                if tranx.to == self:
                    raise LookupError("Deposits cannot be held by banks in firms.")
            elif tranx.type_ == "capital":
                if tranx.from_ == self:
                    assets = assets + tranx.amount
                if tranx.to == self:
                    raise LookupError("Firms cannot own capital of households.")
            else:
                raise LookupError("Unknown transaction type on firm's books.")
        if round(assets, 2) == round(liabilities, 2):
            return True
        else:
            return False
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account
    # returns the value of all transactions of a given type
    # -------------------------------------------------------------------------
    def get_account(self,  type_):
        return super(Firm, self).get_account(type_)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account_num_transactions
    # returns the number of transactions of a given type
    # -------------------------------------------------------------------------
    def get_account_num_transactions(self,  type_):
        return super(Firm, self).get_account_num_transactions(type_)
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
    def add_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default)
        transaction.add_transaction(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # clear_accounts
    # removes all transactions from firm's accounts
    # only for testing, the one in transaction should be used in production
    # -------------------------------------------------------------------------
    def clear_accounts(self):
        super(Firm, self).clear_accounts()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # purge_accounts
    # removes worthless transactions from firm's accounts
    # -------------------------------------------------------------------------
    def purge_accounts(self, environment):
        super(Firm, self).purge_accounts(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_transactions_from_file
    # reads transactions from the config file to the firm's accounts
    # -------------------------------------------------------------------------
    def get_transactions_from_file(self, filename, environment):
        super(Firm, self).get_transactions_from_file(filename, environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __getattr__
    # if the attribute isn't found by Python we tell Python
    # to look for it first in parameters and then in state variables
    # which allows for directly fetching parameters from the Firm
    # i.e. firm.active instead of a bit more bulky
    # firm.parameters["active"]
    # makes sure we don't have it in both containers, which
    # would be bad practice [provides additional checks]
    # -------------------------------------------------------------------------
    def __getattr__(self, attr):
        return super(Firm, self).__getattr__(attr)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # demand_for_labour(price)
    # this is for testing for now, makes the demand labour to be
    # a linear function of price
    # TEST ONLY, REMOVE LATER IF NOT NECESSARY
    # -------------------------------------------------------------------------
    def demand_for_labour(self, price):
        return max(0.0, 100.0 - price * 1.5)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # demand_for_labour_new(price)
    # this is for testing for now, makes the demand labour to be
    # Cobb-Douglas with no capital Y = a * l^b * 1 (for capital)
    # TEST ONLY, REMOVE LATER IF NOT NECESSARY
    # -------------------------------------------------------------------------
    def demand_for_labour_new(self, price):
        a = 5
        b = 0.5
        goods_price = 10.0
        return max(0, (price / (a * b * goods_price)) ** (1 / (b-1)))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # demand_for_labour_solow(price)
    # Demand for labour stemming from the Solow model with C-D function
    # Derived as maximum utility (profit: production*price - wage*labour)
    # given C-D production function Y=a*L^b*C^c
    # -------------------------------------------------------------------------
    def demand_for_labour_solow(self, price_of_labour):
        # The parameters of the production function are read from the config
        # And reassigned here for easier formula below
        a = self.total_factor_productivity
        b = self.labour_elasticity
        c = self.capital_elasticity
        # This is the one price set up, we only consider relative prices in the model
        # as consistent with DSGE models and the rest of macroeconomics
        goods_price = 10.0
        # We calculate the net capital, that is the difference between
        # own capital stock, and owned capital of other agents
        capital = 0.0
        for tranx in self.accounts:
            # Own capital stock is added here
            if tranx.type_ == "loans" and tranx.to == self:
                capital = capital + tranx.amount
            # Owned capital of other agents is subtracted here
            if tranx.type_ == "deposits" and tranx.from_ == self:
                capital = capital - tranx.amount
        # Finally max(U) given particular wage
        return min(self.funding/price_of_labour, max(0, (price_of_labour / (a * b * goods_price * capital ** c)) ** (1 / (b-1))))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # demand_for_labour_grid(price)
    # -------------------------------------------------------------------------
    def demand_for_labour_grid(self, price_of_labour):
        from src.helper import Helper
        helper = Helper()

        # We find minimum and maximum possible amount of capital
        # for Cobb-Douglas function
        minimum = 0.0
        maximum = 0.0
        # Minimum is the current capital held by the firm
        minimum = self.capital
        # And maximum is the minimum plus whatever can be bought by the funding
        # available to the firm
        maximum = max(minimum, self.capital + self.funding/price_of_labour)
        # lump = 0.05
        # if maximum > minimum:
        # The lump specifies the step in the search algorithm
        # We want it to be only 20 iterations, since it's within another loop
        lump = (maximum - minimum) / 20
        # else:
        #     lump = 0.05

        # Then we look for maximum possible production output given above and parameters
        max_production = 0.0
        # And what amount of labour allows for this maximum
        max_labour = 0.0

        # This function allows us to use a for loop with minimum, maximum, and step
        def my_range(start, end, step):
            while start <= end:
                yield start
                start += step

        # We go through the possible amounts of capital stock
        for test_capital in my_range(minimum, maximum, lump):
            # Find what amount of labour can be bought for residual funding
            # We use the fact that Cobb-Douglas production function behaves nicely
            # That is more labour will be better than less labor, ceteris paribus
            test_labour = max(0, self.funding/price_of_labour - (test_capital - self.capital))
            # And check what the production output would be
            test_production = helper.cobb_douglas(test_labour, test_capital, self.total_factor_productivity,
                                                  self.labour_elasticity, self.capital_elasticity)
            # Then we find whiever of these configurations is the best
            if test_production > max_production:
                max_production = test_production
                max_labour = test_labour

        # And return it
        return max_labour
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # update_maturity
    # -------------------------------------------------------------------------
    def update_maturity(self):
        super(Firm, self).update_maturity()
    # -------------------------------------------------------------------------
