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

    state_variables = {}

    parameters = {}

    state_variables['private_belief'] = 0

    state_variables['social_belief'] = 0

    state_variables['choice'] = 0


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
        self.state_variables['private_belief'] = 0
        self.state_variables['social_belief'] = 0
        self.state_variables['choice'] = 0
        self.weight_var = 0

    def get_nodes_for_graph(self, agent_filename, environment):
        from xml.etree import ElementTree

        try:
            xmlText = open(agent_filename).read()
            element = ElementTree.XML(xmlText)
            # we get the identifier
            environment.network.add_node(element.attrib['identifier'])

        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)

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

                if subelement.attrib['type'] == 'link':
                    name = str(subelement.attrib['name'])
                    value = int(subelement.attrib['value'])
                    environment.network.add_edge(self.identifier, name, weight=value)
        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)

    # -------------------------------------------------------------------------
    #
    # ---------------------------------------------------------------------

    def calc_private_belief(self, environment):
        import math

        self.private_belief = math.pow(1 + environment.static_parameters['m'], -1)

    def calc_social_belief(self, environment):

        '''only 'in' the second step when current step ''>'' 1
        average of private belief of neighbors'''

        count_neighbors = 0

        sum_social_belief = 0

        for agent in environment.agents:

            if self.identifier != agent.identifier:
                if environment.network[self.identifier][agent.identifier]['weight'] == 1:
                        count_neighbors = count_neighbors + 1
                        sum_social_belief = sum_social_belief + agent.state_variables['choice']

        if count_neighbors != 0:
            self.social_belief = sum_social_belief / count_neighbors
        else:
            self.social_belief = None

    '''scenario 1: equal weighting function'''
    def weighting_f_equal(self, environment):
        count_neighbors = 0
        for agent in environment.agents:

            if self.identifier != agent.identifier:
                if environment.network[self.identifier][agent.identifier]['weight'] == 1:
                        count_neighbors = count_neighbors + 1

                        if count_neighbors != 0:
                                weight_var = (self.private_belief + self.social_belief) / 2
                                return weight_var
                        else:
                                weight_var = self.private_belief
                                return weight_var

    def investment_decision(self, environment):
        print("hello")
        if self.weighting_f_equal(environment) > 0.5:
                self.choice = 1

        else:
                self.choice = 0
