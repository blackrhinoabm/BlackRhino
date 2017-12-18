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

# This script contains the Agent class which is called in the Environment
# script.

import logging
from abm_template.src.baseagent import BaseAgent

# ============================================================================
#
# class Fund
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

    def __key__(self):
        return self.identifier

    def __eq__(self, other):
        return self.__key__() == other.__key__()

    def __hash__(self):
        return hash(self.__key__())

    def __str__(self):
		fund_string = super(Fund, self).__str__()
		fund_string = fund_string.replace("\n", "\n    <type value='fund'>\n", 1)
		text = "\n"
		for index, transaction in enumerate(self.accounts, start=1):
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

    def __del__(self):
		pass

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
        volume = 0.0

        for transaction in self.accounts:
            if (transaction.type_ == _type):
                volume = volume + float(transaction.amount)

        return volume
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



    def add_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default)
        transaction.add_transaction(environment)
    def remove_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default)
        transaction.remove_transaction()

    # -----------------------------------------------------------------------
    # __init__  used to automatically instantiate an agent as an object when
    # the agent class is called
    # ------------------------------------------------------------------------

    def __init__(self):
        self.identifier = ""  # identifier of the specific agent
        self.state_variables = {}
        self.parameters = {}
        "I can't stress enough how important self.accounts here is\
        I was stuck about 1,5 days because the same transctions\
        (the last one in the loop) were always initialised and\
        attached to all agents in the updater (for i in environment.funds)"
        self.accounts = []

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

    def calc_optimal_pf(self, environment, mu_a, mu_b):

        environment.variable_parameters["cov_a_b"] = environment.variable_parameters["std_a"] * environment.variable_parameters["std_b"] * environment.variable_parameters["corr_a_b"]


        x = ((mu_a - environment.variable_parameters["r_f"]))\
                                        *(environment.variable_parameters["std_b"] *environment.variable_parameters["std_b"])\
                                        -((mu_b - environment.variable_parameters["r_f"])\
                                        *environment.variable_parameters["cov_a_b"] )
        y =(   (mu_a - environment.variable_parameters["r_f"])\
                                   *(environment.variable_parameters["std_b"] *environment.variable_parameters["std_b"]\
                                           + ((mu_b - environment.variable_parameters["r_f"])\
                                          *(environment.variable_parameters["std_a"]* environment.variable_parameters["std_a"]))\
                                            - (((mu_a - environment.variable_parameters["r_f"])\
                                             + (mu_b - environment.variable_parameters["r_f"])  )\
                                             *(environment.variable_parameters["cov_a_b"]))))
        self.state_variables["w_a"] = x/y
        self.state_variables["w_b"] = 1 - self.state_variables["w_a"]

        self.state_variables["r_ip"] = self.state_variables["w_a"] * mu_a\
                                    + self.state_variables["w_b"]  * mu_b

        self.state_variables["variance_ip"] =  self.state_variables["w_a"]  *  self.state_variables["w_a"]\
                                                * environment.variable_parameters["std_a"]  * environment.variable_parameters["std_a"]\
                                                 + self.state_variables["w_b"]*self.state_variables["w_b"]\
                                                 * environment.variable_parameters["std_b"]*environment.variable_parameters["std_b"]\
                                                  + 2 * self.state_variables["w_a"]*self.state_variables["w_b"]\
                                                  * environment.variable_parameters["cov_a_b"]
        self.state_variables["risky"] = ( self.state_variables["r_ip"] - environment.variable_parameters["r_f"])\
                                        / (self.state_variables["theta"] * self.state_variables["variance_ip"] )



    def calc_demand_asset(self, asset, price):

        if "A" in asset.identifier:
            return (self.risky * self.w_a * self.total_assets)/price

        if "B" in asset.identifier:
            return (self.risky * self.w_b * self.total_assets)/price

    def get_net_demand_a(self, goal):
        if goal <  0 and self.get_account("A") > 0:
            demand =  goal - self.get_account("A")

        elif goal <  0 and self.get_account("A") < 0:
            demand =  goal + self.get_account("A")

        elif goal >  0 and self.get_account("A") > 0:
            demand =  goal - self.get_account("A")

        else:
            demand =  self.get_account("A") - goal
        return demand

    def get_net_demand_b(self, goal):
        if goal <  0 and self.get_account("B") > 0:
            demand =  goal - self.get_account("B")

        elif goal <  0 and self.get_account("B") < 0:
            demand =  goal + self.get_account("A")

        elif goal >  0 and self.get_account("B") > 0:
            demand =  goal - self.get_account("B")

        else:
            demand =  self.get_account("B") - goal
        return demand

    def demand_tatonnement_a(self, price):

        goal = (self.risky * self.w_a * self.total_assets)/price
        if goal <  0 and self.get_account("A") > 0:
            demand =  goal - self.get_account("A")
            demand = demand * (-1)
        elif goal <  0 and self.get_account("A") < 0:
            demand =  goal + self.get_account("A")
            demand = demand * (-1)
        elif goal >  0 and self.get_account("A") > 0:
            demand =  goal - self.get_account("A")

        else:
            demand =  self.get_account("A") - goal
        return demand

    def demand_tatonnement_b(self, price):
        goal = (self.risky * self.w_b * self.total_assets)/price
        if goal <  0 and self.get_account("B") > 0:
            demand =  goal - self.get_account("B")

        elif goal <  0 and self.get_account("B") < 0:
            demand =  goal + self.get_account("A")

        elif goal >  0 and self.get_account("B") > 0:
            demand =  goal - self.get_account("B")

        else:
            demand =  self.get_account("B") - goal
        return demand

    def endow_funds_with_shares(self, environment, time):
        from transaction import Transaction
        from random import Random
        random = Random()

        value = 0.0

            #on the liabilities side, transfer deposits from households into investment_shares
        value = round(float( self.state_variables['total_assets'] ), 4)


        while len(self.accounts) > 0:
            self.accounts.pop()        # transaction.add_transaction(environment)
        transaction = Transaction()
        transaction.this_transaction("investment_shares", "liabilities",  self.identifier,  self.identifier,  value, 0,  0, -1)
        # print transaction
        self.accounts.append(transaction)
        # del transaction

        #
        # for object in self.accounts:
        #     object.print_transaction()

    def update_belief(self, environment,  asset_a,  asset_b):

        if self.strategy == "fundamentalist":
            expected_price_a = asset_a.prices[-1] + self.gamma_f * ( asset_a.funda_v - asset_a.prices[-1]   )
            expected_price_b = asset_b.prices[-1] + self.gamma_f * ( asset_b.funda_v - asset_b.prices[-1]   )
        if self.strategy == "chartist":
            expected_price_a = asset_a.prices[-1] + self.gamma_c * ( asset_a.prices[-1] - asset_a.prices[-2]   )
            expected_price_b = asset_b.prices[-1] + self.gamma_c * ( asset_b.prices[-1] - asset_b.prices[-2]   )
        # print expected_price_a, expected_price_b
        self.state_variables['exp_mu_a'] = (asset_a.calc_exp_return(asset_a.prices[-1], expected_price_a, asset_a.firm.dividend))
        self.state_variables['exp_mu_b']= (asset_b.calc_exp_return(asset_b.prices[-1], expected_price_b, asset_b.firm.dividend))
        exp_mu_a, exp_mu_b = self.state_variables['exp_mu_a'] , self.state_variables['exp_mu_b']

        return expected_price_a, expected_price_b, exp_mu_a, exp_mu_b


    def update_balance_sheet(self):
        pass

    def check_accounts(self, environment):
        return self.get_account("A") * environment.price_of_a\
               +self.get_account("B") * environment.price_of_b\
               + self.get_account("Risk_free")\
               == self.get_account("investment_shares")

    def init_portfolio_transactions(self, environment, time, amount_a, amount_b):

        valuation_a = 0
        valuation_b = 0

        valuation_b = amount_b * environment.price_of_b
        self.add_transaction("B", "assets", "firm-1", self.identifier, amount_b, 0, 0, -1, environment)
        # Code to see transctions and keeping track of index, value pairs
        # for num, line in enumerate(self.accounts):
        #     print("{}: {}".format(num, line))

        valuation_a = amount_a * environment.price_of_a
        self.add_transaction("A", "assets", "firm-0",self.identifier, amount_a, 0, 0, -1, environment)
        #
        amount = self.total_assets - valuation_b - valuation_a
        self.add_transaction("Risk_free", "assets", self.identifier,self.identifier, amount, 0, 0, -1, environment)


        # Code to check balance sheet identity
        # print "Consistency for", self.identifier, ":", self.check_accounts(environment)
