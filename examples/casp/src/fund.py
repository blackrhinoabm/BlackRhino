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
        return super(Fund, self).__str__()

    def __getattr__(self, attr):
		return super(Fund, self).__getattr__(attr)


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
        transaction.add_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default,environment )
    def remove_transaction(self,  type_, asset, from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.remove_transaction()

    # -----------------------------------------------------------------------
    # __init__  used to automatically instantiate an agent as an object when
    # the agent class is called
    # ------------------------------------------------------------------------

    def __init__(self):
        self.identifier = ""  # identifier of the specific agent
        self.state_variables = {}
        self.parameters = {}

        #Without putting them here in __init__ they can't called direclty in runner
        self.state_variables["net_demand_a"] = 0.0
        self.state_variables["net_demand_b"] = 0.0
        self.state_variables["exp_mu_a"] = 0.0
        self.state_variables["exp_mu_b"] = 0.0
        self.exp_mu_a = []
        self.exp_mu_b = []
        self.l_risky = []
        self.l_wa = []
        self.l_wb = []
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
        if self.state_variables["w_a"] > 0:
            self.state_variables["w_a"] = min(1, self.state_variables["w_a"])
        if self.state_variables["w_a"] < 0:
            self.state_variables["w_a"] = 0
            # self.state_variables["w_a"] = max(-1, self.state_variables["w_a"] )

        # if self.moving_average(self.l_wa, 5) != None:
        #     self.wa_weighted = self.moving_average(self.l_wa, 5)
        #     self.w_b = 1 - self.wa_weighted
        # else:
        #     self.wa_weighted = self.state_variables["w_a"]

        if self.state_variables["w_a"] > 0:
            self.state_variables["w_b"] = 1 - self.state_variables["w_a"]
        # if self.state_variables["w_a"] < 0:
            # self.state_variables["w_b"] = 1 + abs(self.state_variables["w_a"])



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

        if self.state_variables["risky"] > 0:
            self.state_variables["risky"] = min(1, self.state_variables["risky"] )

        if self.state_variables["risky"] < 0:
            self.state_variables["risky"] = max(-1, self.state_variables["risky"] )


        self.state_variables["risk_free_proportion"] = 1 - self.state_variables["risky"]

        self.l_risky.append(self.state_variables["risky"])
        self.l_wa.append(self.state_variables["w_a"])
        self.l_wb.append(self.state_variables["w_b"])


    def calc_demand_asset(self, asset, price, time):
        if "A" in asset.identifier:
            # print "XXXXXXXXXXXXXX cal net demand A"
            # print "risky:", self.risky , self.w_a , self.w_b,  self.get_account("investment_shares"), self.identifier
            return ((self.risky * self.w_a * self.get_account("investment_shares"))/max(0.0001, price))

        if "B" in asset.identifier:
            # print "XXXXXXXXXXXXXX cal net demand B"
            # print "risky:", self.risky_weighted , "B" , self.w_b , self.w_b  + self.w_a, self.identifier
            return ((self.risky  * self.w_b * self.get_account("investment_shares"))/max(0.0001, price))

    def get_net_demand_a(self, goal):
        demand = 0
        self.state_variables['net_demand_a'] = 0

        if goal >  0 and self.get_account("A") > 0:
            demand =  goal - self.get_account("A")

        if goal >  0 and self.get_account("A") == 0:
            demand =  goal

        if goal ==  0 and self.get_account("A") > 0:
            demand =  -self.get_account("A")

        self.state_variables['net_demand_a'] =  demand
        return demand

    def get_net_demand_b(self, goal):
        demand = 0
        self.state_variables['net_demand_b'] = 0

        if goal >  0 and self.get_account("B") > 0:
            demand =  goal - self.get_account("B")

        if goal >  0 and self.get_account("B") == 0:
            demand =  goal

        if goal == 0 and self.get_account("B") > 0:
            demand =  -self.get_account("B")
        self.state_variables['net_demand_b'] =  demand
        return demand

    def get_net_demand_a_small_trade(self, goal):
        demand = 0
        self.state_variables['net_demand_a'] = 0

        if goal >  0 and self.get_account("A") > 0:
            demand =  goal - self.get_account("A")

        if goal >  0 and self.get_account("A") == 0:
            demand =  goal

        if goal ==  0 and self.get_account("A") > 0:
            demand =  -self.get_account("A")

        self.state_variables['net_demand_a'] =  demand
        return demand *0.01

    def get_net_demand_b_small_trade(self, goal):
        demand = 0
        self.state_variables['net_demand_b'] = 0

        if goal >  0 and self.get_account("B") > 0:
            demand =  goal - self.get_account("B")

        if goal >  0 and self.get_account("B") == 0:
            demand =  goal

        if goal == 0 and self.get_account("B") > 0:
            demand =  -self.get_account("B")
        self.state_variables['net_demand_b'] =  demand
        return demand *0.01

    "Tentative"
    def demand_tatonnement_a(self, price):

        goal = (self.risky * self.w_a * self.get_account("investment_shares"))/price
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
        goal = (self.risky * self.w_b * self.get_account("investment_shares"))/price
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

        # while len(self.accounts) > 0:
        #     self.accounts.pop()        # transaction.add_transaction(environment)
        # transaction = Transaction()
        self.add_transaction("investment_shares", "liabilities",  environment.agents[3].identifier,  self.identifier,  value, 0,  0, -1, environment)
        # print transaction
        # self.accounts.append(transaction)
        # del transaction

    def update_belief(self, environment,  asset_a,  asset_b, time):
        if self.strategy == "fundamentalist":
            expected_price_a = round(max(0, asset_a.prices[-1] + self.gamma_f * ( asset_a.funda_v - asset_a.prices[-1])),4)
            expected_price_b =  round( max(0, asset_b.prices[-1] + self.gamma_f * ( asset_b.funda_v - asset_b.prices[-1])), 4)

        if self.strategy == "chartist":
            if asset_a.moving_average(3)!= None:
                expected_price_a = round (max(0, asset_a.prices[-1] + self.gamma_c * ( asset_a.moving_average(3) - asset_a.moving_average(2)  )) ,  4)
            else:
                expected_price_a = round (max(0, asset_a.prices[-1] + self.gamma_c * ( asset_a.prices[-1] - asset_a.prices[-2])) ,  4)
            if asset_a.moving_average(3) != None:
                expected_price_b= round (max(0, asset_b.prices[-1] + self.gamma_c * ( asset_b.moving_average(3) - asset_b.moving_average(2)  )) ,  4)
            else:
                expected_price_b = round ( max(0, asset_b.prices[-1] + self.gamma_c * ( asset_b.prices[-1] - asset_b.prices[-2])) , 4)

        # print (expected_price_a - asset_a.prices[-1] )/asset_a.prices[-1], asset_a.firm.dividend , self.identifier, time
        self.state_variables['exp_mu_a'] =     round( (expected_price_a - asset_a.prices[-1] + asset_a.firm.dividend )/asset_a.prices[-1] , 4)
        # self.state_variables['exp_mu_a'] = round( (asset_a.calc_exp_return(asset_a.prices[-1], expected_price_a, asset_a.firm.dividend)) , 4)
        # self.state_variables['exp_mu_b'] = round(  (asset_b.calc_exp_return(asset_b.prices[-1], expected_price_b, asset_b.firm.dividend)) , 4)
        self.state_variables['exp_mu_b']=    round( (expected_price_b - asset_b.prices[-1] + asset_b.firm.dividend )/asset_b.prices[-1] , 4)

        exp_mu_a, exp_mu_b = self.state_variables['exp_mu_a'] , self.state_variables['exp_mu_b']
        self.exp_mu_a.append(exp_mu_a)
        self.exp_mu_b.append(exp_mu_b)
        return expected_price_a, expected_price_b, exp_mu_a, exp_mu_b


    def update_books(self, time, environment):
        valuation_a, valuation_b, valuation_bond = 0,0,0
        valuation_a = self.get_account("A") * environment.variable_parameters['price_of_a']
        valuation_b = self.get_account("B") * environment.variable_parameters['price_of_b']
        valuation_bond = self.get_account("Risk_free") * environment.variable_parameters['price_of_bond']

    def net_bond_quantity_demanded(self, time, environment):
        valuation_a, valuation_b, valuation_bond = 0,0,0
        difference = 0.0

        valuation_a = self.get_account("A") * environment.variable_parameters['price_of_a']
        valuation_b = self.get_account("B") * environment.variable_parameters['price_of_b']
        valuation_bond = self.get_account("Risk_free") * environment.variable_parameters['price_of_bond']

        difference = (self.get_account("investment_shares")-valuation_a -  valuation_b -valuation_bond)
        #if difference positive, fill in the gap with more risk-free
        net_demand_quantity = round(difference/environment.variable_parameters['price_of_bond'], 4)
        #if difference negative, sell risk-free asset until accounts balance

        return net_demand_quantity


    def check_accounts(self, environment):
        print  self.get_account("A"), environment.variable_parameters['price_of_a'], "\n"
        print self.get_account("B"), environment.variable_parameters['price_of_b'], "\n"
        print self.get_account("Risk_free"), environment.variable_parameters['price_of_bond']
        print "**************"

        print round(round( self.get_account("A") * environment.variable_parameters['price_of_a'], 4)\
       +  round(self.get_account("B") * environment.variable_parameters['price_of_b'], 4)\
       + round(self.get_account("Risk_free")* environment.variable_parameters['price_of_bond'], 4),2)
        print "==", round(round( self.get_account("investment_shares"), 4),2)

        return round(round( self.get_account("A") * environment.variable_parameters['price_of_a'], 4)\
               +  round(self.get_account("B") * environment.variable_parameters['price_of_b'], 4)\
               + round(self.get_account("Risk_free")* environment.variable_parameters['price_of_bond'], 4),2)\
               == round(round( self.get_account("investment_shares"), 4),2)

    def init_portfolio_transactions(self, environment, time, amount_a, amount_b):
        valuation_a = 0
        valuation_b = 0

        """One must be cautious with the from_ agents for the
        transactions. For the moment it's  harcoded with the agents'
        identifiers, i.e. firm-0, firm-1 and Government.
        If the identifier change, the from code in add_transaction must also
        change."""

        valuation_b = amount_b * environment.variable_parameters['price_of_b']
        self.add_transaction("B", "assets", "firm-1", self.identifier, amount_b, 0, 0, -1, environment)
        # Code to see transctions and keeping track of index, value pairs
        # for num, line in enumerate(self.accounts):
        #     print("{}: {}".format(num, line))

        valuation_a = amount_a * environment.variable_parameters['price_of_a']
        self.add_transaction("A", "assets", "firm-0",self.identifier, amount_a, 0, 0, -1, environment)
        #

        """Be careful with the from_ agent here: environment.agents[2].identifier. Government is the third
        item in environment.agents list"""
        amount = round((self.get_account("investment_shares") - valuation_b - valuation_a)/environment.variable_parameters['price_of_bond'], 4)
        self.add_transaction("Risk_free", "assets", environment.agents[2].identifier ,self.identifier, amount, 0, 0, -1, environment)
        # print "Riskfree", self.get_account("Risk_free")

        # Code to check balance sheet identity
        #  print "Consistency for", self.identifier, ":", self.check_accounts(environment)

    def calc_new_deposits(self,scaleFactor,environment):
        from random import Random
        random = Random()
        oldValue = 0.0
        newValue = 0.0
        returnValue = 0.0

        for tranx in self.accounts:
            if tranx.type_ == "investment_shares":
                oldValue = tranx.amount
                newValue = max(   round(1.0 - scaleFactor + 0.4*scaleFactor*random.random()*oldValue,4 ) ,0.0)
                tranx.set_amount(tranx.amount - newValue, environment)
        print oldValue, newValue, "test"
        returnValue = round(oldValue - newValue, 4)
        self.state_variables['total_assets']= returnValue
        return returnValue

    def moving_average(self, list, n):
        history = len(list)
        if history < n+1:
            return None
        else:
            moving_average = sum(list[-n:]) / n
            return moving_average
