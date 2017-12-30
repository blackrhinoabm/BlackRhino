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

# This script contains the Agent class which is later called in the Environment
# script.

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
    identifier = ""  # identifier of the specific agent
    state_variables = {}
    parameters = {}

    accounts = []

    #
    #
    # CODE
    #
    #

    # -----------------------------------------------------------------------
    # __init__  used to automatically instantiate an agent as an object when
    # the agent class is called
    # ------------------------------------------------------------------------

    def __init__(self):
        self.identifier = ""  # identifier of the specific agent
        self.state_variables = {} # stores all state_variables
        self.parameters = {} # stores all parameters
        self.accounts = [] # accounts with transactions for the agent
        self.profit_results = [] # list containing profit result per time period
        self.dividends = []
        self.growth_results =  []


    def get_parameters_from_file(self, agent_filename, environment):
        """
        Method to read in data given in an xml file and stored in
        dictionaries attached to the agent object.

        Arguments
        ---
        agent_filename - Individual xml file given in the agent directory
        Example: fund-01.xml

        Output
        ---
        Stores all parameters and state_variables read from the config
        files in dictionaries self.parameters and self.state_variables

        Called
        ---
        In environment.py when instantiation happens
        """
        from xml.etree import ElementTree

        try:
            xmlText = open(agent_filename).read()
            element = ElementTree.XML(xmlText)
            # we get the identifier
            self.identifier = element.attrib['identifier']

            # and then we're only interested in <parameter> fields
            element = element.findall('parameter')

            # loop over all <parameter> entries in the xml file
            for subelement in element:

                if subelement.attrib['type'] == 'parameters':
                    name = str(subelement.attrib['name'])
                    value = float(subelement.attrib['value'])
                    self.parameters[name] = value

                if subelement.attrib['type'] == 'state_variables':
                    name = str(subelement.attrib['name'])
                    value = float(subelement.attrib['value'])
                    self.state_variables[name] = value
                    # if (name == 'theta'):
					# 		self.theta = float(value)

        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)


    # -------------------------------------------------------------------------
    #
    # ---------------------------------------------------------------------
    def supply_of_shares(self, price):
        return self.get_account("number_of_shares")
    # -------------------------------------------------------------------------

    def get_account(self, _type):
        volume = 0.0

        for transaction in self.accounts:
            if (transaction.type_ == _type):
                volume = volume + float(transaction.amount)

        return volume

    def add_stuff(self, initial_profit=[100000],growth = [0]):
        self.growth_results = growth
        self.profit_results = initial_profit


    def calc_profit(self):
        """
        Using the stochastic process brownian motion to calculate firm profit.
        Import method from folder "function"
        ---
        returns profit as float

        Where do parameters come from?
        Parameters are passed into agent objects after initializing in
        function add_stuff() (see above)

        """
        from functions.brownian_drift import brownian_drift

        self.state_variables['profit'] = self.profit_results[-1] * (brownian_drift(self.brown_dt, self.brown_mu, self.brown_sigma))

        self.state_variables['growth'] = (self.state_variables['profit'] - self.profit_results[-1]  )/self.profit_results[-1]
        self.growth_results.append(self.state_variables['growth'])
        self.profit_results.append(self.state_variables['profit'])
        return self.state_variables['profit']

    def initialize_profits(self):
        import itertools
        # creates profits.
        for _ in itertools.repeat(0,1):
            self.calc_profit()

    def endow_firms_with_equity(self, environment, number_of_shares):
        self.number_of_shares = number_of_shares
        amount = self.number_of_shares
        self.add_transaction("number_of_shares", "", self.identifier,self.identifier, amount, 0, 0, -1, environment)

    def print_variables(self):
        print self.state_variables
        print self.parameters

    """
    Black Rhino abm_template functions. These functions
    need to be included for inheritance.
    All the methods inherited from the abstract class BaseAgent
    that we need to include so the agent class gets instantiated
    """
    def __key__(self):
        return self.identifier

    def __eq__(self, other):
        return self.__key__() == other.__key__()

    def __hash__(self):
        return hash(self.__key__())

    def __str__(self):
		firm_string = super(Firm, self).__str__()
		firm_string = firm_string.replace("\n", "\n    <type value='firm'>\n", 1)
		text = "\n"
		for transaction in self.accounts:
			text = text + transaction.write_transaction()
		text = text + "  </agent>"
		return firm_string.replace("\n  </agent>", text, 1)

    def __getattr__(self, attr):
		return super(Firm, self).__getattr__(attr)

    def __del__(self):
		pass

    def get_parameters(self):
        return self.parameters

    def append_parameters(self, values):
        super(Firm, self).append_parameters(values)

    def set_parameters(self, values):
        super(Firm, self).append_parameters(values)

    def append_state_variables(self, values):
        super(Firm, self).append_state_variables(values)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _variables):
        super(Firm, self).set_state_variables(_variables)

    def check_consistency(self):
        assets = []
        liabilities = []
        return super(Firm, self).check_consistency(assets, liabilities)

    def clear_accounts(self):
        super(Firm, self).clear_accounts()

    def purge_accounts(self, environment):
        super(Firm, self).purge_accounts(environment)

    def get_account_num_transactions(self, _type):
        super(Firm, self).get_account_num_transactions(_type)

    def get_transactions_from_file(self, filename, environment):
        super(Firm, self).get_transactions_from_file(filename, environment)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Firm, self).set_identifier(value)

    def update_maturity(self):
        super(Firm, self).update_maturity()

    def add_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.add_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default, environment)
    def remove_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.remove_transaction()

    def clear_accounts(self):
        super(Firm, self).clear_accounts()

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
