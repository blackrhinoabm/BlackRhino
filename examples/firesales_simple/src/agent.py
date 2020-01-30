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
# script. In the degroot learning algorithm a group of individuals observe
# each other's opinions and adapt their subjective propability distribution
# of an unknown value of a parameter theta
# The model (which is executed in the updater script) describes how the group
# forms a collective subjective propability distrbution by revealing their
# individual distribution to each other and pooling their opnion

# Implementation: Every agent has an opinion variable and weights/probabilities
# describing how much it'cares' for the opinion of the other. These weights are
# stored in a dictionary called transition_probabilities

import logging

from src.shock import Shock
from src.runner import Runner

from abm_template.src.baseagent import BaseAgent

# ============================================================================
#
# class Bank
#
# ============================================================================


class Agent(BaseAgent):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""  # identifier of the specific agent

    state_variables = {}

    parameters = {}

    TAS = 0     # Total Asset Sales

    total_assets = 0

    shock_for_agent = 0

    temp = 0

    sale_of_k_assets = {}

    ''' Accounts is not used in our example, but it's in the BaseAgent
    parent class'''
    accounts = []

    #
    #
    # CODE
    #
    #

    #
    #
    # all the methods inherited from the abstract class BaseAgent
    # that we need to include so the agent class gets instantiated
    # we can use them to modify the program easier (e.g. set_num_sweeps)
    #
    #

    def __getattr__(self, attr):
        super(Agent, self).__getattr__(attr)


    def __str__(self):
        super(Agent, self).__str__()

        # ret_str = "  <agent identifier='" + self.identifier + "'>\n "

        # ret_str = ret_str + " <parameter type='static' name=opinion value=" + str(self.opinion) + "></parameter>\n"

        # for each_agent in self.transition_probabilities:
        #     weight = self.transition_probabilities[each_agent]
        #     if isinstance(weight, int) or isinstance(weight, float) or isinstance(weight, str):
        #         ret_str = ret_str + "    <parameter type='transition' + 'name='" + each_agent + "' value='" + str(weight) + "'></parameter>\n"
        #     else:
        #         raise TypeError
        # ret_str = ret_str + "</agent>\n"
        # return ret_str

    def get_parameters(self):
        return self.parameters

    def append_parameters(self, values):
        super(Agent, self).append_parameters(values)

    def set_parameters(self, values):
        super(Agent, self).append_parameters(values)

    def append_state_variables(self, values):
        super(Agent, self).append_state_variables(values)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _variables):
        super(Agent, self).set_state_variables(_variables)

    def check_consistency(self, assets, liabilities):
        super(Agent, self).check_consistency(assets,liabilities)

    def clear_accounts(self):
        super(Agent, self).clear_accounts()

    def get_account(self, _type):
        super(Agent, self).get_account(_type)

    def purge_accounts(self, environment):
        super(Agent, self).purge_accounts(environment)

    def get_account_num_transactions(self, _type):
        super(Agent, self).get_account_num_transactions(_type)

    def get_transactions_from_file(self, filename, environment):
        super(Agent, self).get_transactions_from_file(filename, environment)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Agent, self).set_identifier(value)

    def update_maturity(self):
        super(Agent, self).update_maturity()

    # -----------------------------------------------------------------------
    # __init__  used to automatically instantiate an agent as an object when
    # the agent class is called
    # ------------------------------------------------------------------------

    def __init__(self):
        self.identifier = ""  # identifier of the specific agent
        self.state_variables = {}
        self.parameters = {}
        self.TAS = 0

        self.total_assets = 0
        self.temp = 0
        self.sale_of_k_assets = {}

        self.shock_for_agent = 0



    def get_parameters_from_file(self, agent_filename, environment):
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
        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)

    # -------------------------------------------------------------------------
    #
    # ---------------------------------------------------------------------
    def initialize_total_assets(self):

        self.total_assets = self.parameters['debt'] + self.parameters['equity']
        return self.total_assets
        # self.parameters['total_assets'] = total_assets

    def update_balance_sheet(self):
        self.parameters['debt'] = self.parameters['debt'] + self.TAS
        self.parameters['equity'] = self.parameters['equity'] + self.shock_for_agent * self.total_assets

        self.total_assets = self.parameters['debt'] + self.parameters['equity']

    def check_accounts(self):
        if self.total_assets == self.parameters['equity'] + self.parameters['debt']:
            print("yes, great - the accounting worked for %s" %self.identifier)
        else:
            print('no.. what a bummer')

    def start_shock(self, environment):
        self.shock_for_agent = 0

        for shock in environment.shocks:
            for k in set(self.state_variables) & set(shock.asset_returns):
                self.shock_for_agent +=  self.state_variables[k] * shock.asset_returns[k]

    def calc_total_asset_sales(self, environment, current_step):

            self.TAS = 0

            for shock in environment.shocks:

                for k in set(self.state_variables) & set(shock.asset_returns):
                    self.TAS = self.TAS + self.state_variables[k] * shock.asset_returns[k]

                self.TAS = self.total_assets * self.TAS * self.state_variables['leverage']
