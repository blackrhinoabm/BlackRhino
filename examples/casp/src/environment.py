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

from xml.etree import ElementTree
from abm_template.src.baseconfig import BaseConfig

# -------------------------------------------------------------------------
#
#  class Environment
#
# -------------------------------------------------------------------------


class Environment(BaseConfig):
    from state import State
    from parameters import Parameters
    #
    #
    # VARIABLES
    #
    #
    identifier = ""  # identifier of the environment
    static_parameters = {}  # a dictionary containing all environmenet parameters

    static_parameters["num_simulations"] = 0  # number of simulations
    static_parameters["num_sweeps"] = 0  # numbers of runs in a single simulation
    static_parameters["num_agents"] = 0  # number of agents in a simulation
    static_parameters["fund_directory"] = ""  # directory containing agent xmls

    agents = []
    funds = []
    firms = []
    variable_parameters = {}
    parameters = Parameters()
    state = State()
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

    # def agents_generator(self):
    #     # self.agents = [self.funds]
    #     super(Environment, self).agents_generator()

    # def get_agent_by_id(self, ident):
    #     super(Environment, self).get_agent_by_id(ident)

    def check_global_transaction_balance(self, _type):
        super(Environment, self).check_global_transaction_balance(_type)

    def write_environment_file(self, file_name):
        super(Environment, self).write_environment_file()

    def print_parameters(self):
        super(Environment, self).print_parameters()

    def update_asset_returns(self):
        super(Environment, self).update_asset_returns()

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

        self.static_parameters = {}
        self.static_parameters["num_simulations"] = 0
        self.static_parameters["num_sweeps"] = 0
        self.static_parameters["num_agents"] = 0
        self.static_parameters["fund_directory"] = ""
        self.static_parameters["firm_directory"] = ""

        self.variable_parameters["sum_a_funds"] = 0
        self.variable_parameters["sum_b_funds"] = 0


        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_xml_config_file(environment_filename)
        logging.info(" Environment file read: %s", environment_filename)


        # then read in all the agents
        self.initialize_funds_from_files(self.static_parameters['fund_directory'], 0)
        self.initialize_firms_from_files(self.static_parameters['firm_directory'], 0)


        self.agents = [self.funds, self.firms]


        self.allocate_fund_size()
        logging.info("Determined fund size according to global market cap and data given in the agents configs")

        self.count_all_agents()

        logging.info(" Initialized %s A funds and %s B funds and stored in environment.funds",\
                            self.sum_a_funds, self.sum_b_funds)
        logging.info(" Initialized %s A firms and %s B firms and stored in environment.firms",\
                                self.sum_a_firms, self.sum_b_firms)
        logging.info(" Global assets under management are %s currency units; A assets are %s currency units; B assets are %s currency units",\
                    self.global_assets_under_management, self.ame_market_cap, self.eme_market_cap)

        logging.info(" So we are looking for the price of the A and B equity assets (given an additional risk-free bond asset), introduce QE and look for spillover effects")
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
    def initialize_funds_from_files(self, fund_directory, time):

        from src.fund import Fund
        while len(self.funds) > 0:
            self.funds.pop()

        agent_files = os.listdir(fund_directory)

        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                agent = Fund()
                agent_filename = fund_directory + each_agent_file
                agent.get_parameters_from_file(agent_filename, self)
                self.funds.append(agent)

        logging.info('Fetched funds data and read into program')

        # check if agents were read in correctly
        # for i in self.funds:
        #     print i.identifier
        #     print i.print_variables()
        #     print i

    def initialize_firms_from_files(self, firm_directory, time):

        from src.firm import Firm
        while len(self.firms) > 0:
            self.firms.pop()

        agent_files = os.listdir(firm_directory)

        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                agent = Firm()
                agent_filename = firm_directory + each_agent_file
                agent.get_parameters_from_file(agent_filename, self)
                self.firms.append(agent)

        logging.info('Fetched firms data and read into program')

    def initialize_returns(self, environment):
        import numpy as np
        import random

        for i in self.firms:
            if i.domicile == 0:
                self.fair_value_a = i.dividend_firm/i.discount
                self.mu_a = i.dividend_firm/self.fair_value_a
            else:
                self.fair_value_b = i.dividend_firm/i.discount
                self.mu_b= i.dividend_firm/self.fair_value_b


        environment.variable_parameters["price_of_b"] = self.fair_value_b
        environment.variable_parameters["price_of_a"] = self.fair_value_a
        return self.fair_value_a, self.fair_value_a, self.mu_a, self.mu_b

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


    def allocate_fund_size(self):
        # default is 20% B and 80% A market cap
        sum_a = 0
        sum_b = 0
        for fund in self.funds:
            if fund.parameters['domicile'] == 0:
                sum_a += 1
            if fund.parameters['domicile'] == 1:
                sum_b += 1

        list_temp_b  = []
        list_b = []
        eme_market_cap = 0
        for fund in self.funds:
            if fund.domicile == 1.0:
                list_temp_b = self.divide_sum(int(sum_b), int((self.global_assets_under_management)*0.2))
                list_b.append(fund)
        # itrange = list(range(0, len(list_temp)))
        for index, elem in enumerate(list_b):
            for index2, elem2 in enumerate(list_temp_b):
                if index == index2:
                    dict={"total_assets" : elem2}
                    elem.append_state_variables(dict)
                    eme_market_cap+=elem.total_assets
        self.variable_parameters["eme_market_cap"] = eme_market_cap

        "The same for A funds"

        list_temp_a  = []
        list_a = []
        ame_market_cap = 0
        for fund in self.funds:
            if fund.domicile == 0:
                list_temp_a = self.divide_sum(int(sum_a), int((self.global_assets_under_management)*0.8))
                list_a.append(fund)
        # itrange = list(range(0, len(list_temp)))
        for index, elem in enumerate(list_a):
            for index2, elem2 in enumerate(list_temp_a):
                if index == index2:
                    dict={"total_assets" : elem2}
                    elem.append_state_variables(dict)
                    ame_market_cap += elem.total_assets
        self.variable_parameters["ame_market_cap"] = ame_market_cap

    def divide_sum(self, n, total):
    #Return a randomly chosen list of n positive integers summing to total.
    #Each such list is equally likely to occur.
        import random
        random.seed(9001)
        dividers = sorted(random.sample(xrange(1, total), n - 1))
        return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
