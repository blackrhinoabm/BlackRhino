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

import os
import logging
from initialisation import *

from xml.etree import ElementTree
from abm_template.src.baseconfig import BaseConfig
from src.network import Network

# -------------------------------------------------------------------------
#
#  class Environment
#
# -------------------------------------------------------------------------


class Environment(BaseConfig):
    from state import State
    from parameters import Parameters
    #
    # VARIABLES
    #
    identifier = ""  # identifier of the environment
    static_parameters = {}  # a dictionary containing all environmenet parameters
    agents = []
    variable_parameters = {}
    prices = []
    network = Network("")  # network of transaction
    #
    # parameters = Parameters()
    # state = State()
    #
    # CODE
    #

    def __getattr__(self, attr):
        return super(Environment, self).__getattr__(attr)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Environment, self).set_identifier(value)

    def __str__(self):
        return super(Environment, self).__str__()

    def accrue_interests(self):
        super(Environment, self).accrue_interests()

    def add_shock(self, shock):
        super(Environment, self).add_shock()

    def add_static_parameter(self, params):
        super(Environment, self).add_static_parameters(params)

    def get_static_parameters(self):
        return self.static_parameters

    def set_static_parameters(self, params):
        super(Environment, self).set_static_parameters(params)

    def add_variable_parameter(self, params):
        super(Environment, self).add_static_parameters(params)

    def get_variable_parameters(self):
        return self.variable_parameters

    def set_variable_parameters(self, params):
        super(Environment, self).set_variable_parameters(params)

    def get_assets(self):
        return self.assets

    def set_assets(self, params):
        super(Environment, self).set_assets(params)

    def get_shocks(self):
        return self.shocks

    def set_shocks(self, params):
        super(Environment, self).set_shocks(params)

    def check_global_transaction_balance(self, _type):
        super(Environment, self).check_global_transaction_balance(_type)

    def write_environment_file(self, file_name):
        super(Environment, self).write_environment_file()

    def print_parameters(self):
        super(Environment, self).print_parameters()

    def update_asset_returns(self):
        super(Environment, self).update_asset_returns()

    def new_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        # transaction.this_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default)
        transaction.add_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default,environment)

    def add_cash(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        # transaction.this_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default)
        transaction.add_cash(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default,environment)

    # -------------------------------------------------------------------------

    def __init__(self, environment_directory, identifier):
        self.initialize(environment_directory, identifier)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # read_xml_config_file(self, config_file_name)
    # reads an xml file with config and sets identifier and parameters
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    def read_xml_config_file(self, env_filename):
        try:
            xmlText = open(env_filename).read()
            element = ElementTree.XML(xmlText)  # we tell python it's an xml
            self.identifier = element.attrib['identifier']

            # loop over all entries in the xml file
            for subelement in element:

                try:  # we see whether the value is a int
                    if subelement.attrib['type'] == 'variable_parameters':
                        value = float(subelement.attrib['value'])
                        name = subelement.attrib['name']
                        self.variable_parameters[name] = value

                    else:
                        value = int(subelement.attrib['value'])
                        type_ = subelement.attrib['type']
                        self.static_parameters[type_] = value

                except:  # if not, it is a string
                    value = str(subelement.attrib['value'])
                    type_ = subelement.attrib['type']
                    self.static_parameters[type_] = value

        except:
            logging.error("    ERROR: %s could not be parsed", env_filename)

    # -------------------------------------------------------------------------
    # the next function
    # initializes the environment, initializing all the variables
    # reading the env_config file from supplied environment_directory and
    # identifier, and initializes all agents from the directories
    # supplied in the main config file
    # -------------------------------------------------------------------------

    def initialize(self, environment_directory, identifier):
        self.identifier = identifier
        self.funds = []
        self.firms = []
        self.assets = []
        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_xml_config_file(environment_filename)
        logging.info(" Environment file read: %s", environment_filename)

        # then read in all the agents
        init_firms(self, self.static_parameters['firm_directory'], 0)
        init_funds(self, self.static_parameters['fund_directory'], 0)
        government = Government()
        household = Household()
        self.agents = [self.funds, self.firms, government, household, self.assets]

        # That's our government agent
        # print self.agents[2].identifier

        for i in self.firms:
            i.endow_firms_with_equity(self, 10000)

        #Function called from initialisation.py
        risky_assets_funda_values = init_profits(self, 0)

        #Function called from initialisation.py
        init_assets(self, self.static_parameters['asset_directory'], 0, risky_assets_funda_values )

        #Now we determine the amount of fundamentalists and chartists
        self.variable_parameters['amount_fundamentalists'] = int((self.count_all_agents()[0] + self.count_all_agents()[1])* self.variable_parameters['fundamentalists'])
        self.variable_parameters['amount_chartist'] = int((self.count_all_agents()[0] + self.count_all_agents()[1])* self.variable_parameters['chartists'])


        logging.info(" Initialized %s A funds and %s B funds and stored in environment.funds",\
                            self.sum_a_funds, self.sum_b_funds)
        logging.info(" Initialized %s A firms and %s B firms and stored in environment.firms",\
                                self.sum_a_firms, self.sum_b_firms)
        logging.info(" Global assets under management are %s currency units; A assets are %s currency units; B assets are %s currency units",\
                    self.global_assets_under_management, self.ame_market_cap, self.eme_market_cap)

        logging.info(" We are looking for the price of the A and B equity assets (given an additional risk-free bond asset), introduce QE and look for spillover effects")
        logging.info(" *******Environment initialisation completed*******")

    def agents_generator(self):
        if self.agents is not None:
            for agent_type in self.agents:
                if type(agent_type) == list:
                    for agent in agent_type:
                        yield agent
                else:
                    yield agent_type
        else:
            raise LookupError('There are no agents to iterate over.')

    def get_agent_by_id(self, ident):
        to_return = None
        for agent in self.agents_generator():
            if agent.identifier == ident:
                if to_return is None:  # checks whether something has been found previously in the function
                    to_return = agent
                else:
                    raise LookupError('At least two agents have the same ID.')
                    # if we have found something before then IDs are not unique, so we raise an error
        if to_return is None:
            raise LookupError('No agents have the provided ID.')
            # if we don't find any agent with that ID we raise an error
        else:
            return to_return

    # -------------------------------------------------------------------------
    def count_all_agents(self):
        sum = 0
        for fund in self.funds:
            if fund.parameters['domicile'] == 0:
                sum += 1
        self.variable_parameters['sum_a_funds'] = sum

        sum = 0
        for fund in self.funds:
            if fund.parameters['domicile'] == 1:
                sum += 1
        self.variable_parameters['sum_b_funds'] = sum

################## FIRMS

        sum = 0
        for firm in self.firms:
            if firm.parameters['domicile'] == 0:
                sum += 1
        self.variable_parameters['sum_a_firms'] = sum

        sum = 0
        for firm in self.firms:
            if firm.parameters['domicile'] == 1:
                sum += 1
        self.variable_parameters['sum_b_firms'] = sum

        return self.variable_parameters['sum_a_funds'] , self.variable_parameters['sum_b_funds']

class Government(object):
    def __init__(self):
        self.identifier = "Government"
        self.accounts = []

    def __key__(self):
        return self.identifier


    def add_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.add_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default,environment )
    def remove_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.remove_transaction()

class Household(object):
    def __init__(self):
        self.identifier = "Household"
        self.accounts = []
        self.scaleFactorHouseholds=0


    def __key__(self):
        return self.identifier
