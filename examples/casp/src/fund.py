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


class Fund(BaseAgent):
    #
    #
    # VARIABLES
    #
    #
    identifier = ""  # identifier of the specific agent
    state_variables = {}
    parameters = {}

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
    def __str__(self):
		fund_string = super(Fund, self).__str__()
		fund_string = fund_string.replace("\n", "\n    <type value='fund'>\n", 1)
		text = "\n"
		for transaction in self.accounts:
			text = text + transaction.write_transaction()
		text = text + "  </agent>"
		return fund_string.replace("\n  </agent>", text, 1)

    def __getattr__(self, attr):
		return super(Fund, self).__getattr__(attr)
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
        super(Fund, self).append_parameters(values)

    def set_parameters(self, values):
        super(Fund, self).append_parameters(values)

    def append_state_variables(self, values):
        super(Fund, self).append_state_variables(values)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _variables):
        super(Fund, self).set_state_variables(_variables)

    def check_consistency(self, assets, liabilities):
        super(Fund, self).check_consistency(assets,liabilities)

    def clear_accounts(self):
        super(Fund, self).clear_accounts()

    def get_account(self, _type):
        super(Fund, self).get_account(_type)

    def purge_accounts(self, environment):
        super(Fund, self).purge_accounts(environment)

    def get_account_num_transactions(self, _type):
        super(Fund, self).get_account_num_transactions(_type)

    def get_transactions_from_file(self, filename, environment):
        super(Fund, self).get_transactions_from_file(filename, environment)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Fund, self).set_identifier(value)

    def update_maturity(self):
        super(Fund, self).update_maturity()

    # -----------------------------------------------------------------------
    # __init__  used to automatically instantiate an agent as an object when
    # the agent class is called
    # ------------------------------------------------------------------------

    def __init__(self):
        self.identifier = ""  # identifier of the specific agent
        self.state_variables = {}
        self.parameters = {}



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
                    if (name == 'theta'):
							self.theta = float(value)

        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)

        self.state_variables["r_f"] = environment.variable_parameters['r_f']

    def print_variables(self):
        print self.state_variables
        print self.parameters
    # -------------------------------------------------------------------------
    #
    # ---------------------------------------------------------------------

    def calc_optimal_pf(self, environment):
        environment.variable_parameters["cov_ame_eme"] = environment.variable_parameters["std_ame"] * environment.variable_parameters["std_eme"] * environment.variable_parameters["corr_ame_eme"]


        x = ((self.state_variables["r_ame"] - environment.variable_parameters["r_f"]))\
                                        *(environment.variable_parameters["std_eme"] *environment.variable_parameters["std_eme"])\
                                        -((self.state_variables["r_eme"] - environment.variable_parameters["r_f"])\
                                        *environment.variable_parameters["cov_ame_eme"] )
        y =(   (self.state_variables["r_ame"] - environment.variable_parameters["r_f"])\
                                   *(environment.variable_parameters["std_eme"] *environment.variable_parameters["std_eme"]\
                                           + ((self.state_variables["r_eme"] - environment.variable_parameters["r_f"])\
                                          *(environment.variable_parameters["std_ame"]* environment.variable_parameters["std_ame"]))\
                                            - (((self.state_variables["r_ame"] - environment.variable_parameters["r_f"])\
                                             + (self.state_variables["r_eme"] - environment.variable_parameters["r_f"])  )\
                                             *(environment.variable_parameters["cov_ame_eme"]))))
        self.state_variables["w_ame"] = x/y
        self.state_variables["w_eme"] = 1 - self.state_variables["w_ame"]

        self.state_variables["r_ip"] = self.state_variables["w_ame"] * self.state_variables["r_ame"]\
                                    + self.state_variables["w_eme"]  * self.state_variables["r_eme"]

        self.state_variables["variance_ip"] =  self.state_variables["w_ame"]  *  self.state_variables["w_ame"]\
                                                * environment.variable_parameters["std_ame"]  * environment.variable_parameters["std_ame"]\
                                                 + self.state_variables["w_eme"]*self.state_variables["w_eme"]\
                                                 * environment.variable_parameters["std_eme"]*environment.variable_parameters["std_eme"]\
                                                  + 2 * self.state_variables["w_ame"]*self.state_variables["w_eme"]\
                                                  * environment.variable_parameters["cov_ame_eme"]
        self.state_variables["risky"] = ( self.state_variables["r_ip"] - environment.variable_parameters["r_f"])\
                                        / (self.state_variables["theta"] * self.state_variables["variance_ip"] )


        # print ((self.state_variables["r_ame"])),\
        #         (self.state_variables["r_eme"]),\
        #         environment.variable_parameters["r_f"],\
        #         (environment.variable_parameters["std_eme"]),\
        #         (environment.variable_parameters["std_ame"],\
        #         self.state_variables["r_eme"]),\
        #         self.theta, self.state_variables['w_ame']
    def demand_ame(self, p_ame):
        D = self.risky * self.w_ame * self.total_assets/p_ame
        return D

    def demand_eme(self, p_eme):
        D = self.risky * self.w_eme * self.total_assets/p_eme
        return D

    def initialize_transactions(self, time):
        from transaction import Transaction
        from random import Random
        random = Random()

        value = 0.0

        #on the liabilities side, transfer deposits from households into investment_shares

        value = round(float( self.state_variables['total_assets'] ), 4)
        transaction = Transaction()
        transaction.this_transaction("investment_shares", "",  -1,  self.identifier,  value, 0,  0, -1)
        self.accounts.append(transaction)
        del transaction
        #
        #
        # for object in self.accounts:
        #     object.print_transaction()

    def update_balance_sheet(self):
        pass
    def check_accounts(self):
        pass
