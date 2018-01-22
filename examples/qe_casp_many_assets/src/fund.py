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
        self.state_variables["net_demand_bonds"] = 0.0

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


        self.state_variables["riskfree_weight"] = 1 - self.state_variables["risky"]

        self.l_risky.append(self.state_variables["risky"])
        self.l_wa.append(self.state_variables["w_a"])
        self.l_wb.append(self.state_variables["w_b"])


    def calc_optimal_global(self, environment, exp_returns, time):
        from functions.portfolio import *
        # if time> 10:
        returns_panda, cov_mat, avg_rets = create_pandas(environment, exp_returns)
        "No shortselling"
            # pf_risk_aversion(environment, returns, list_assets,  time,  environment.num_assets_total)
        weights = optimal_portfolio_world(returns_panda, cov_mat, avg_rets, self.theta)
        # print weights, time
        np.set_printoptions(suppress=True)

        # Ways to print
        # print(weights.head())
        # print("Optimal weights:\n{}\n".format(weights))
        # print_portfolio_info(returns_panda, avg_rets, weights)

        for i in weights.index:
            if "riskfree" in i:
                self.state_variables["riskfree_weight"]=weights[i]
            if "A" in i:
                self.state_variables['w_a'] = weights[i]
                # print self.state_variables['w_a']
            if "B" in i:
                self.state_variables['w_b'] = weights[i]
                # print self.state_variables['w_b']

        self.state_variables["risky"] = 1 - self.state_variables["riskfree_weight"]
        # We store the results
        self.l_risky.append(self.state_variables["risky"])
        self.l_wa.append(self.state_variables["w_a"])
        self.l_wb.append(self.state_variables["w_b"])

        return weights


    def calc_demand_asset_global(self, asset, price, exchange_rate, time, idend, weights):

        if idend in asset.identifier:

            # print "XXXXXXXXXXXXXX cal net demand A"
            # print "risky:", self.w_a ,  self.get_account("investment_shares"), self.identifier
            return ((  self.w_a * self.get_account("investment_shares"))/max(0.0001, price))

    def get_net_demand_global(self, asset, goal, ident):
        demand = 0

        if asset.identifier == ident:
            x = str("net_demand_" + ident)
            self.state_variables[x] = 0
            if goal >  0 and self.get_account(str(ident)) > 0:
                demand =  goal - self.get_account(ident)

            if goal >  0 and self.get_account(str(ident)) == 0:
                demand =  goal

            if goal ==  0 and self.get_account(str(ident)) > 0:
                demand =  -self.get_account(str(ident))


            return demand
            self.state_variables[x] =  demand


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

    def get_net_demand_bond(self, goal):
        demand = 0
        self.state_variables['net_demand_bond'] = 0

        if goal >  0 and self.get_account("Risk_free") > 0:
            demand =  goal - self.get_account("Risk_free")
        if goal >  0 and self.get_account("Risk_free") == 0:
            demand =  goal
        if goal ==  0 and self.get_account("Risk_free") > 0:
            demand =  -self.get_account("Risk_free")
        self.state_variables['Risk_free'] =  demand
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
        asset_b.funda_v = asset_b.funda_values[time]
        asset_a.funda_v =  asset_a.funda_values[time]

        if self.identifier == "fund-2":
            print 'Funda a ', asset_a.funda_v
            print  'Fundab ', asset_b.funda_v

        if self.strategy == "fundamentalist":
            expected_price_a = round(max(0, asset_a.prices[-1] + self.gamma_f * ( asset_a.funda_v  - asset_a.prices[-1])),4)
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
        self.state_variables['exp_mu_b']=    round( (expected_price_b - asset_b.prices[-1] + asset_b.firm.dividend )/asset_b.prices[-1] , 4)

        exp_mu_a, exp_mu_b = self.state_variables['exp_mu_a'] , self.state_variables['exp_mu_b']
        self.exp_mu_a.append(exp_mu_a)
        self.exp_mu_b.append(exp_mu_b)

        list_returns=[exp_mu_a, exp_mu_b]
        return expected_price_a, expected_price_b, exp_mu_a, exp_mu_b


    def update_belief_global(self, environment,  list_assets, time):
        # Prepare return and price dictionary to return

        dictexpmus = {}
        for i in list_assets:
            dict2 = {  i.identifier : 0}
            # dict2 = { str("exp_mu_" +  i.identifier) : 0}
            dictexpmus.update(dict2)

        dictassets = {}
        for i in list_assets:
            dict2 = { str("asset_" +  i.identifier) : i}
            dictassets.update(dict2)

        dictexpp = {}
        for i in list_assets:
            dict2 = {  i.identifier : 0}
            # dict2 = { str("exp_p_" +  i.identifier) : 0}
            dictexpp.update(dict2)

        if self.strategy == "fundamentalist":
            for asset in list_assets:
                # New expected price
                if str("risky") in str(type(asset)) :
                    # New expected price
                    expected_price = round(max(0, asset.prices[-1] + self.gamma_f * ( asset.funda_v  - asset.prices[-1])),4)
                    x =  round( (expected_price  - asset.prices[-1] + asset.firm.dividend )/asset.prices[-1] , 4)
                    x = x * 100
                    y =   str(asset.identifier)
                    # y = "exp_mu_" + str(asset.identifier)
                    self.state_variables[y] = x

                    #SAve it in expected price dictionary to return
                    for key, value in dictexpp.iteritems():
                        if asset.identifier in key and "riskfree" not in key :
                            dictexpp[key] = expected_price

                    #SAve it in expected returns dictionary to return
                        for key, value in dictexpmus.iteritems():
                            if asset.identifier in key and "riskfree" not in key :

                                dictexpmus[key] = x

                #We need to do the same for bonds
                if str("riskfree") in str(type(asset)):
                     for key, value in dictexpmus.iteritems():
                         if str("riskfree") in key:
                             dictexpmus[key] = environment.variable_parameters["r_f"] * 100
                #
                if str("riskfree") in str(type(asset)) :
                    for key, value in dictexpp.iteritems():
                         if str("riskfree") in key:
                            dictexpp[key] = environment.variable_parameters["price_of_bond"]

        ##################################

        if self.strategy == "chartist":
            for asset in list_assets:

                if str("risky") in str(type(asset)) :
                    #New expected price
                    expected_price = round(max(0, asset.prices[-1] + self.gamma_c * ( asset.funda_v  - asset.prices[-1])),4)
                    #New expected return
                    x =  round( (expected_price  - asset.prices[-1] + asset.firm.dividend )/asset.prices[-1] , 4)
                    x = x * 100
                    # y = "exp_mu_" + str(asset.identifier)
                    y = str(asset.identifier)

                    self.state_variables[y] = x
                    #SAve it in dictionary to return
                    for key, value in dictexpp.iteritems():
                        if asset.identifier in key and "riskfree" not in key :
                            dictexpp[key] = expected_price

                #SAve it in expected returns dictionary to return
                    for key, value in dictexpmus.iteritems():
                        if asset.identifier in key and "riskfree" not in key :

                            dictexpmus[key] = x

                    #We need to save it correclty - yes we repeat it. i don't know how to do this smarter
                    if asset.moving_average(3)!= None:
                        expected_price = round (max(0, asset.prices[-1] + self.gamma_c * ( asset.moving_average(3) - asset.moving_average(2)  )) ,  4)
                        x =  round( (expected_price  - asset.prices[-1] + asset.firm.dividend )/asset.prices[-1] , 4)
                        y =  str(asset.identifier)
                        # y = "exp_mu_" + str(asset.identifier)

                        self.state_variables[y] = x
                        #SAve it in dictionary to return
                        for key, value in dictexpp.iteritems():
                            if asset.identifier in key and "riskfree" not in key :
                                dictexpp[key] = expected_price

                        #SAve it in expected returns dictionary to return
                            for key, value in dictexpmus.iteritems():
                                if asset.identifier in key and "riskfree" not in key :
                                    dictexpmus[key] = x

                #We need to do the same for bonds
                if str("riskfree") in str(type(asset)):
                     for key, value in dictexpmus.iteritems():
                         if str("riskfree") in key:
                             dictexpmus[key] = environment.variable_parameters["r_f"] *100
                #
                if str("riskfree") in str(type(asset)) :
                    for key, value in dictexpp.iteritems():
                         if str("riskfree") in key:
                            dictexpp[key] = environment.variable_parameters["price_of_bond"]
        return dictexpp, dictexpmus


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

    def get_cash(self, environment):
        delta = round(round( self.get_account("A") * environment.variable_parameters['price_of_a'], 4)\
               +  round(self.get_account("B") * environment.variable_parameters['price_of_b'], 4)\
               + round(self.get_account("Risk_free")* environment.variable_parameters['price_of_bond'], 4),2)\
               - round(round( self.get_account("investment_shares"), 4),2)
        return delta

    def check_accounts(self, environment):
        print   self.get_account("Cash"),  "\n"
        print  self.get_account("A"), environment.variable_parameters['price_of_a'], "\n"
        print self.get_account("B"), environment.variable_parameters['price_of_b'], "\n"
        print self.get_account("Risk_free"), environment.variable_parameters['price_of_bond']
        print "**************"

        print  self.get_account("Cash")     \
        +    round(round( self.get_account("A") * environment.variable_parameters['price_of_a'], 4)\
       +  round(self.get_account("B") * environment.variable_parameters['price_of_b'], 4)\
       + round(self.get_account("Risk_free")* environment.variable_parameters['price_of_bond'], 4),2)
        print "==", round(round( self.get_account("investment_shares"), 4),2)

        delta = self.get_account("Cash")  \
                +  round(round( self.get_account("A") * environment.variable_parameters['price_of_a'], 4)\
               +  round(self.get_account("B") * environment.variable_parameters['price_of_b'], 4)\
               + round(self.get_account("Risk_free")* environment.variable_parameters['price_of_bond'], 4),2)\
               - round(round( self.get_account("investment_shares"), 4),2)

        if delta > 0:
            print "negative Cash needed; Delta: ", delta, self.identifier
        if delta < 0:
            print "positive Cash needed; Delta: ", delta, self.identifier

        return delta

    def init_portfolio_transactions(self, environment, time, amount_a, amount_b):
        valuation_a = 0
        valuation_b = 0

        print "Fund init_portfolio_transactions"
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
        # print "Consistency for", self.identifier, ":", self.check_accounts(environment)

    def calc_new_deposits(self,scaleFactor,environment):
        from random import Random
        import numpy as np
        random = Random()
        oldValue = 0.0
        newValue = 0.0
        returnValue = 0.0
        noise = int(np.random.normal(0,1,1))
        for tranx in self.accounts:
            if tranx.type_ == "investment_shares":
                oldValue = tranx.amount
                newValue = max(   round(1.0 - scaleFactor +scaleFactor*random.random()*oldValue,4 ) ,0.0)
                tranx.set_amount(tranx.amount + noise, environment)

    def moving_average(self, list, n):
        history = len(list)
        if history < n+1:
            return None
        else:
            moving_average = sum(list[-n:]) / n
            return moving_average

    def calc_demand_asset(self, asset, price, time):
        if "A" in asset.identifier:
            # print "XXXXXXXXXXXXXX cal net demand A"
            print "risky:", self.risky , self.w_a , self.w_b,  self.get_account("investment_shares"), self.identifier
            return ((self.risky * self.w_a * self.get_account("investment_shares"))/max(0.0001, price))

        if "B" in asset.identifier:
            # print "XXXXXXXXXXXXXX cal net demand B"
            # print "risky:", self.risky_weighted , "B" , self.w_b , self.w_b  + self.w_a, self.identifier
            return ((self.risky  * self.w_b * self.get_account("investment_shares"))/max(0.0001, price))
