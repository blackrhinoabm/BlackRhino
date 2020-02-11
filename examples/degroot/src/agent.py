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
    opinion = 0.0   #   'opinion' of the agent
    initial_opinion = 0.0   #  initial  'opinion' of the agent

    state_variables = {}
    parameters = {}

    ''' Accounts is not used in our example, but it's in the BaseAgent
    parent class'''
    accounts = []

    '''The below is from an older version, where weights were stored in
    a dictionary We are using network graphs now, so its no needed anymore
    transition_probabilities = {}   '''


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
        ret_str = "  <agent identifier='" + self.identifier + "'>\n "

        ret_str = ret_str + " <parameter type='static' name=opinion value=" + str(self.opinion) + "></parameter>\n"

        for each_agent in self.transition_probabilities:
            weight = self.transition_probabilities[each_agent]
            if isinstance(weight, int) or isinstance(weight, float) or isinstance(weight, str):
                ret_str = ret_str + "    <parameter type='transition' + 'name='" + each_agent + "' value='" + str(weight) + "'></parameter>\n"
            else:
                raise TypeError

        ret_str = ret_str + "</agent>\n"

        return ret_str

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
        self.opinion = 0.0  # opinion of the specific agent
        self.initial_opinion = 0
    # -------------------------------------------------------------------------
    # get_parameters_from_file
    # reads the specified config file given the environment
    # and sets parameters to the ones found in the config file
    # the config file should be an xml file that looks like the below:
    # <agent identifier='string'>
    #     <parameter name='string' value='string'></parameter>
    # </agent>
    # -------------------------------------------------------------------------

    # def get_nodes_for_graph(self, agent_filename, environment):
    #     from xml.etree import ElementTree

    #     try:
    #         xmlText = open(agent_filename).read()
    #         element = ElementTree.XML(xmlText)
    #         # we get the identifier
    #         environment.network.add_node(element.attrib['identifier'])
    #     except:
    #         logging.error("    ERROR: %s could not be parsed", agent_filename)


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
                if subelement.attrib['type'] == 'static':
                    name = subelement.attrib['name']
                    value = subelement.attrib['value']

                    if name == 'starting_opinion':
                        self.opinion = float(value)
                        self.initial_opinion = float(value)

        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)

    # -------------------------------------------------------------------------
    # The next function creates a temporary variable tempv (which needs some
    # kind of starting value, here 0.0),
    # then we go through every agent in the list agents which is defined in the
    # environment class (in the environment script), take its opinion variable,
    # multiply it with the weight stored in the network
    # -------------------------------------------------------------------------

    def create_temp_variable(self, environment):
        tempv = 0.0

        for agent in environment.agents:

            # print(environment.network[self.identifier][agent.identifier]['weight'])
            tempv = tempv + agent.opinion * environment.network[self.identifier][agent.identifier]['weight']

        return tempv

         