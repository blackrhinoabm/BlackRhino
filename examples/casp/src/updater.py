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
from abm_template.src.basemodel import BaseModel
import logging
import numpy as np


# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------


class Updater(BaseModel):
    #
    #
    # VARIABLES
    #
    #
    identifier = ""
    model_parameters = {}
    #
    #
    # METHODS
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Updater, self).set_identifier(value)

    def __str__(self):
        super(Updater, self).__str__(self)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, values):
        super(Updater, self).set_model_parameters(values)

    def get_interactions(self):
        return self.interactions

    def interactions(self):
        super(Updater, self).interactions(self)

    def set_interactions(self, values):
        super(Updater, self).set_interactions(values)

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, environment):
        if  environment.assets[0].identifier =="A":
            self.asset_a = environment.assets[0]
            self.asset_b = environment.assets[1]
        else:
            self.asset_b = environment.assets[0]
            self.asset_a = environment.assets[1]

        self.scenario = "no_QE"
        # self.scenario = "QE"

        from market import Market
        self.market = Market("market", self.scenario)

        self.count_trade_a = []
        self.count_trade_b = []

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, time):
        import random

        """We set up optimal portfolios and
        initialize accounts """
        if time ==0:
            self.pre_trade(environment, time)

            for firm in environment.firms:
                print firm.number_of_shares, "Number of shares", firm.identifier

            for fund in environment.funds:
                print fund.get_account("investment_shares"), fund.identifier

            self.asset_a.dividends = [0 for i in range(0, environment.num_sweeps)]
            self.asset_b.dividends = [0 for i in range(0, environment.num_sweeps)]
            # self.asset_b.funda_values
            # self.asset_b.funda_values
            # Check if books balance
            # for fund in environment.funds:
            #     if fund.identifier == "fund-3":
            #         print fund.check_accounts(environment), fund.identifier, "check",    time

        else:
            print "********************************"
            print time
            # While market orders are submitted contineously,
            # dividends are only updated infrequent times
            list = [i for i in range(0, environment.num_sweeps)]
            list2 = [0 for i in range(0, environment.num_sweeps)]

            environment.profit_frequency = int(environment.num_sweeps/4)

            for i, value in enumerate(list2):
                if time-1==i and i % environment.profit_frequency==0:
                    "We collect dividends, fluctuate deposits and update profits of firms"
                    for fund in environment.funds:
            			# next, determine stochastic deposit outflows/inflows
                        fund.calc_new_deposits(environment.scaleFactorHouseholds, environment)
                        # print fund.get_account("investment_shares")
                    for firm in environment.firms:
                        profit = firm.calc_profit(time,  environment.profit_frequency )
                        # determine new dividends and total assets after dividends
                        dividend = firm.update_and_distribute_dividends(environment, time)

                        if firm.identifier=="firm-0":
                            self.asset_a.dividends[i]= dividend
                            # print "Dividend a", self.asset_a.dividends, time
                        if firm.identifier=="firm-1":
                            self.asset_b.dividends[i]=dividend
                            # print "Dividend b", self.asset_b.dividends, time
                        funda_v = round (  firm.state_variables['dividend']/firm.discount  , 4)
                        logging.info(" %s's asset's fundamental value is %s per share in step %s", firm.identifier, funda_v , time)

                        if firm.identifier=="firm-0":
                            self.asset_a.funda_v = funda_v
                            self.asset_a.funda_values.append(funda_v)
                        if firm.identifier=="firm-1":
                            self.asset_b.funda_v = funda_v
                            self.asset_b.funda_values.append(funda_v)


            """Now the trading begins. We have two scenarios. QE and no QE"""

            if self.scenario == "QE":

                """Determine new expected prices and
                who is buying and selling"""
                rationed_a, rationed_b = self.update_expectation_demand_logsmalltrade(environment, time)
                """Trade risky assets"""
                self.exchange_assets_create_transactions(environment, rationed_a, rationed_b, time)
                tracking_a, tracking_b = self.exchange_assets_netting(environment, time)
                self.remove_transactions_after_sell(environment, tracking_a, tracking_b)

                #Get excess demand
                omega_a =  self.market.current_demand_a  - self.market.current_supply_a
                omega_b =  self.market.current_demand_b  - self.market.current_supply_b
                omega_bonds = self.exchange_bonds(environment, time)

                # "Now the trading is complete and books should balance"
                # for fund in environment.funds:
                #     if fund.identifier == "fund-3":
                #         print fund.check_accounts(environment), fund.identifier, "check",    time
                "At the end of the period, prices are adjusted"
                self.determine_price_risky_assets(environment, time, omega_a, omega_b, self.scenario )

                if time<environment.num_sweeps/2:
                    self.determine_price_riskfree_asset(environment, time,  omega_bonds, self.scenario)

                # """Introduce Policy action"""
                if time>environment.num_sweeps*0.5 and time <environment.num_sweeps*0.5+environment.num_sweeps*0.3:
                    if environment.variable_parameters['r_f']>0.01:
                         self.policy_action(environment)
                    if environment.variable_parameters['r_f']<0.01:
                        self.determine_price_riskfree_asset(environment, time,  omega_bonds, self.scenario)


                if time>environment.num_sweeps*0.5+environment.num_sweeps*0.3:
                    self.determine_price_riskfree_asset(environment, time,  omega_bonds, self.scenario)


                self.asset_a.update_returns(environment)
                self.asset_b.update_returns(environment)
                # python counts from 0
                if time>2 :
                    environment.assets[0].riskyness.append(environment.variable_parameters["std_a"])
                    environment.variable_parameters["std_a"] =  min( 0.8, np.std(self.asset_a.returns[:time])) * 100
                    # environment.assets[0].riskyness.append(environment.variable_parameters["std_a"])
                    print environment.variable_parameters["std_a"], "standard deviation a"

                    environment.assets[1].riskyness.append(environment.variable_parameters["std_b"])
                    environment.variable_parameters["std_b"] =   min( 0.8,  np.std(self.asset_b.returns[:time])) * 100
                    # environment.assets[2].riskyness.append(environment.variable_parameters["std_a"])
                    print environment.variable_parameters["std_b"], "standard deviation b"

                    from scipy.stats import linregress
                    a = self.asset_a.returns[:time]
                    b = self.asset_b.returns[:time]

                    if len(a)==len(b):
                        environment.variable_parameters["corr_a_b"] = linregress(a, b)[2]
                        print environment.variable_parameters["corr_a_b"]

            if self.scenario == "no_QE":

                """Determine new expected prices and
                who is buying and selling"""
                rationed_a, rationed_b = self.update_expectation_demand_logsmalltrade(environment, time)
                """Trade risky assets"""
                self.exchange_assets_create_transactions(environment, rationed_a, rationed_b, time)
                tracking_a, tracking_b = self.exchange_assets_netting(environment, time)
                self.remove_transactions_after_sell(environment, tracking_a, tracking_b)

                #Get excess demand
                omega_a =  self.market.current_demand_a  - self.market.current_supply_a
                omega_b =  self.market.current_demand_b  - self.market.current_supply_b
                omega_bonds = self.exchange_bonds(environment, time)

                # "Now the trading is complete and books should balance"
                # for fund in environment.funds:
                #     if fund.identifier == "fund-3":
                #         print fund.check_accounts(environment), fund.identifier, "check",    time
                "At the end of the period, prices are adjusted"
                self.determine_price_risky_assets(environment, time, omega_a, omega_b, self.scenario )
                self.determine_price_riskfree_asset(environment, time,  omega_bonds, self.scenario)

                self.asset_a.update_returns(environment)
                self.asset_b.update_returns(environment)
                # python counts from 0
                if time> 2 :
                    environment.assets[0].riskyness.append(environment.variable_parameters["std_a"])
                    environment.variable_parameters["std_a"] = min( 0.8, np.std(self.asset_a.returns[:time]) *100)
                    # environment.assets[0].riskyness.append(environment.variable_parameters["std_a"])
                    print environment.variable_parameters["std_a"], "standard deviation a"

                    environment.assets[1].riskyness.append(environment.variable_parameters["std_b"])
                    environment.variable_parameters["std_b"] = min( 0.8, np.std(self.asset_b.returns[:time]) *100)
                    # environment.assets[2].riskyness.append(environment.variable_parameters["std_a"])
                    print environment.variable_parameters["std_b"], "standard deviation b"

                    from scipy.stats import linregress
                    a = self.asset_a.returns[:time]
                    b = self.asset_b.returns[:time]

                    if len(a)==len(b):
                        environment.variable_parameters["corr_a_b"] = linregress(a, b)[2]
                        print environment.variable_parameters["corr_a_b"]

    def update_expectation_demand_logsmalltrade(self, environment, time):
        trade_limit_a = 0.01 * environment.firms[0].number_of_shares
        trade_limit_b = 0.01 * environment.firms[1].number_of_shares
        expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = 0, 0, 0, 0
        demand_a, demand_b = 0, 0
        supply_a, supply_b = 0, 0
        for_rationing_a = []
        for_rationing_b = []
        # print "********************"
        # print "Demand for risky assets in the market (Quantity)"
        # print "********************"

        for fund in (environment.funds):
            expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = fund.update_belief(environment, self.asset_a, self.asset_b, time)

            fund.calc_optimal_pf(environment,  exp_mu_a, exp_mu_b)
            target_a =  round ( fund.calc_demand_asset(self.asset_a, expected_price_a, time)   , 4)
            if target_a >0:
                target_a=(min(fund.get_account("investment_shares"), target_a))
            if target_a <0:
                target_a = 0
            target_b =   round (  fund.calc_demand_asset(self.asset_b, expected_price_b, time)  , 4)
            if target_b >0:
                target_b=(min(fund.get_account("investment_shares"), target_b))
            if target_b <0:
                target_b = 0

            # Printing
            # print fund.identifier, fund.strategy, "price:", self.asset_a.prices[-1], "expected price a",  expected_price_a,  "expected mu a", "\n"\
            # ,  exp_mu_a, "dividend a", self.asset_a.firm.dividend, "funda_v", self.asset_a.funda_v, "target a ", target_a,\
            #   "has", fund.get_account("A"), "net", fund.get_net_demand_a(target_a),\
            #    fund.get_account("investment_shares"),  time
            #
            # print fund.identifier, fund.strategy, "price:", self.asset_b.prices[-1], "expected price b",  expected_price_b,  "expected mu b", "\n",\
            #  exp_mu_b,"dividend b", self.asset_b.firm.dividend, "funda_v", self.asset_b.funda_v, "target b", target_b,\
            #    "has", fund.get_account("B"), "net", fund.get_net_demand_b(target_b),\
            #     fund.get_account("investment_shares"), time

            if fund.get_net_demand_a(target_a) > 0:
                demand_a += fund.get_net_demand_a(target_a) *1
            if fund.get_net_demand_a(target_a) < 0:
                supply_a += abs(fund.get_net_demand_a(target_a))  *1

            if fund.get_net_demand_b(target_b) > 0:
                demand_b += fund.get_net_demand_b(target_b)  *1
            if fund.get_net_demand_b(target_b) < 0:
                supply_b += abs(fund.get_net_demand_b(target_b))  *1

        order_limit_a = min(trade_limit_a, demand_a, supply_a)
        order_limit_b = min(trade_limit_b, demand_b, supply_b)

        for fund in (environment.funds):
            expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = fund.update_belief(environment, self.asset_a, self.asset_b, time)
            fund.calc_optimal_pf(environment,  exp_mu_a, exp_mu_b)

            target_a =  round ( fund.calc_demand_asset(self.asset_a, expected_price_a, time)   , 4)
            if target_a >0:
                target_a=(min(fund.get_account("investment_shares"), target_a))
            if target_a <0:
                target_a = 0
            target_b =   round (  fund.calc_demand_asset(self.asset_b, expected_price_b, time)  , 4)
            if target_b >0:
                target_b=(min(fund.get_account("investment_shares"), target_b))
            if target_b <0:
                target_b = 0

            """Save quantities demanded and supplied in lists"""
            #Supply side rationing A
            if fund.get_net_demand_a(target_a)<0:
                sold_a = (abs(fund.get_net_demand_a(target_a)) * order_limit_a)/max(supply_a, 0.0000000001)
                for_rationing_a.append([fund, sold_a])
            #DEMAND side rationing A
            if fund.get_net_demand_a(target_a)>0:
                buy_a = (fund.get_net_demand_a(target_a) * order_limit_a)/max(demand_a, 0.0000000001)
                for_rationing_a.append([fund, -buy_a])

            #Supply side rationing B
            if fund.get_net_demand_b(target_b)<0:
                sold_b = (abs(fund.get_net_demand_b(target_b)) * order_limit_b)/max(supply_b, 0.0000000001)
                for_rationing_b.append([fund, sold_b])
            #DEMAND side rationing B
            if fund.get_net_demand_b(target_b)>0:
                buy_b = (fund.get_net_demand_b(target_b) * order_limit_b)/max(demand_b,0.0000000001)
                for_rationing_b.append([fund, -buy_b])

        # now we use rationing to find the actual transactions between agents
        # We also save the aggregate current demand and supply (useful later)
        self.market.current_demand_a =  demand_a
        self.market.current_demand_b =  demand_b

        self.market.current_supply_a =  supply_a
        self.market.current_supply_b = supply_b
        #
        # Count if the trade occurs
        temp = 0
        if self.market.current_demand_a and self.market.current_supply_a >0:
            temp = 1
            self.count_trade_a.append(temp)
        else:
            temp = 0
            self.count_trade_a.append(temp)

        temp = 0
        if self.market.current_demand_b and self.market.current_supply_b >0:
            temp = 1
            self.count_trade_b.append(temp)
        else:
            temp = 0
            self.count_trade_b.append(temp)

        self.count_trade_a
        # #
        # print "********************"
        # print "Aggregate demand and supply for risky assets in the market(Quantity) at step",time
        # print "********************"
        # print "A demand:",self.market.current_demand_a, 'A supply:', self.market.current_supply_a
        # print "B demand:",self.market.current_demand_b, 'B supply:', self.market.current_supply_b
        logging.info("A demand: %s; A supply: %s at step %s", self.market.current_demand_a, self.market.current_supply_a, time)
        logging.info("B demand: %s; B supply: %s at step %s", self.market.current_demand_b, self.market.current_supply_b, time)
        rationed_a = self.market.rationing_proportional(for_rationing_a)
        rationed_b = self.market.rationing_proportional(for_rationing_b)
        # print "**********", "Rations:"
        # self.show_ration(rationed_a, "A")
        # # self.show_ration(rationed_b, "B")
        return rationed_a, rationed_b

    def determine_price_risky_assets(self, environment, time, excess_a , excess_b, scenario):
        """
        Let's try exogenous market maker function for price setting according to
        excess demand (see Joshi & Famer 2002)
        """
        if self.scenario == "QE" or self.scenario == "no_QE" :
            print "A: market maker log impact"
            self.asset_a.prices.append(max(0.01, self.market.market_maker_log( self.asset_a.prices[-1], self.market.current_demand_a,abs(self.market.current_supply_a)  )))

            print "B market maker log impact:"
            self.asset_b.prices.append(max(0.01,   self.market.market_maker_log(self.asset_b.prices[-1], self.market.current_demand_b,abs(self.market.current_supply_b) ) )   )


        # Look at the price series if you want
        # print "new price A", self.asset_a.prices
        # print "new price B", self.asset_b.prices
        #Save the new price in environment
        environment.variable_parameters['price_of_b'] = self.asset_b.prices[-1]
        environment.variable_parameters['price_of_a'] = self.asset_a.prices[-1]
        logging.info("New price for A is %s; new price for B is %s; at step %s", environment.variable_parameters['price_of_a'], environment.variable_parameters['price_of_b'], time)
    # -----------------------------------------------------------------------
    def exchange_assets_create_transactions(self, environment, list_for_a, list_for_b, time):
        """Method to exchange assets via ration.
        We start with the A asset and create new transactions."""

        #Loop over the rationed list of agent pairs
        for index, item in enumerate(list_for_a):
            # if index==2:  # Uncomment to keep track of only one ration
                # print item, "Seller:", item[0].identifier  #This is the seller of the specific ration

            # Create the sell transaction between the agent pair
            environment.new_transaction("A", "assets", item[0].identifier, item[1].identifier,item[2], 0,  0, -1, environment)

        "Now the B asset"
        for index, item in enumerate(list_for_b):
            environment.new_transaction("B", "assets", item[0].identifier, item[1].identifier,item[2], 0,  0, -1, environment)

    def exchange_assets_netting(self, environment, time):
        """
        Method to net the books of the sellers and buyers of asset A and B.
        We net the transactions, so they don't accumulate
        over the course of the simulation

        Argument
        ========
        Environment to loop over buyers and sellers

        Output
        ======
        Two sets with transactions (one for each traded asset) marked for deletion.
        """

        #To keep track of the sell operations, we use these balance floats
        balance_a, balance_b = 0.0, 0.0
        # We create a proxy set for deleting transaction
        to_delete_a = set([])
        to_delete_b = set([])

        # We start with the sellers of A and loop over them
        for seller_a in environment.funds:
            for tranx in seller_a.accounts:
                # Find the selling A-transactions
                if tranx.type_ == "A":
                    if tranx.from_.identifier == seller_a.identifier:
                        balance_a = balance_a + tranx.amount

                        # Add to the tracking set
                        to_delete_a.add(tranx)
                        # Net the books
                        for firm in environment.firms:
                                for tranx in seller_a.accounts:
                                    if tranx.type_ == "A":
                                        if tranx.from_ == firm:
                                            tranx.set_amount(tranx.amount - balance_a, environment)
                                            # This is a little trick so avoid double counting
                                            balance_a = 0
        remaining_a_aggregate = 0
        #Now we loop over the buyers of A
        for fund in environment.funds:
            # We get the balance amount of new A assets aquired
            # Some funds bought nothing, so the next functions returns None
            #In that case we set the balancing amount to 0
            if self.get_buyer_a_balance_amount(fund) is None:
                x = 0

            #otherwise we get x as balancing amount
            else:
                x = self.get_buyer_a_balance_amount(fund)
                # print x, fund.state_variables["net_demand_a"], "a net vs balance"
                remaining_a = abs(fund.state_variables["net_demand_a"]) - abs(x)
                remaining_a_aggregate += remaining_a

            # Set the A account to the new amount
            for tranx in fund.accounts:
                if tranx.type_ == "A" and tranx.to.identifier == fund.identifier and "firm" in tranx.from_.identifier :
                    tranx.set_amount( tranx.amount + x , environment)
        logging.info("  A assets netted on step: %s",  time)


        "Now everything for B"
        for seller_b in environment.funds:
            for tranx in seller_b.accounts:
                # Find the selling b-transactions
                if tranx.type_ == "B":
                    if tranx.from_.identifier == seller_b.identifier:
                        balance_b = balance_b + tranx.amount
                        # Add to the tracking set
                        to_delete_a.add(tranx)
                        # Net the books
                        for firm in environment.firms:
                                for tranx in seller_b.accounts:
                                    if tranx.type_ == "B":
                                        if tranx.from_ == firm:
                                            tranx.set_amount(tranx.amount - balance_b, environment)
                                            # This is a little trick so avoid double counting
                                            balance_b = 0
        remaining_b_aggregate = 0
        #Now we loop over the buyers of A
        for fund in environment.funds:
            # We get the balance amount of new A assets aquired
            # Some funds bought nothing, so the next functions returns None
            #In that case we set the balancing amount to 0
            if self.get_buyer_b_balance_amount(fund) is None:
                x = 0
            #otherwise we get x as balancing amount
            else:
                x = self.get_buyer_b_balance_amount(fund)
                # print x, fund.state_variables["net_demand_a"], "a net vs balance"
                remaining_b = abs(fund.state_variables["net_demand_b"]) - abs(x)
                remaining_b_aggregate += remaining_b

            # Set the A account to the new amount
            for tranx in fund.accounts:
                if tranx.type_ == "B" and tranx.to.identifier == fund.identifier and "firm" in tranx.from_.identifier :
                    tranx.set_amount( tranx.amount + x , environment)
        logging.info("  B assets netted on step: %s",  time)
         # linear market maker with excess orders below
        return to_delete_a,  to_delete_b

    def exchange_bonds(self, environment, time):
        net_demand_bonds = 0.0
        ag_demand_bonds = 0.0
        valuation_a, valuation_b, valuation_bond = 0,0,0
        difference = 0.0

        for fund in environment.funds:
            valuation_a = round( fund.get_account("A") * environment.variable_parameters['price_of_a'], 4)
            valuation_b =  round (fund.get_account("B") * environment.variable_parameters['price_of_b'], 4)
            valuation_bond = round (fund.get_account("Risk_free") * environment.variable_parameters['price_of_bond'], 4)

            # #if difference positive, fill in the gap with more risk-free Assets
            #if difference negative, sell risk-free asset until accounts balance
            difference = (round(fund.get_account("investment_shares"),4)-valuation_a -  valuation_b -valuation_bond)
            ag_demand_bonds+= round(difference/environment.variable_parameters['price_of_bond'], 4)
            net_demand_bonds = round(difference/environment.variable_parameters['price_of_bond'], 4)
            if net_demand_bonds >0:
                self.market.current_demand_bond+=net_demand_bonds
            if net_demand_bonds <0:
                self.market.current_supply_bond+=net_demand_bonds
            x = 0
            for tranx in fund.accounts:
                if tranx.from_.identifier == "Government":
                    tranx.set_amount(tranx.amount + net_demand_bonds , environment)
                    # print tranx.amount, net_demand_bonds , environment.variable_parameters['price_of_bond'] , valuation_b  , valuation_a , fund.get_account("investment_shares")
                    x = ( (tranx.amount + net_demand_bonds ) *environment.variable_parameters['price_of_bond'] + valuation_b   + valuation_a)- fund.get_account("investment_shares")
            # net the residual
                if tranx.type_ == "investment_shares":
                    tranx.set_amount(tranx.amount + x, environment)
        return ag_demand_bonds

    def determine_price_riskfree_asset(self, environment,time,  excess_bond, scenario ):
        "update_bond price and yield"

        if self.scenario == "QE" or self.scenario == "no_QE":
        # excess demand pushes the price upward, excess supply downwards
            # print "Bond market maker log impact:"
            price_bond=(self.market.market_maker_log( environment.variable_parameters['price_of_bond'], self.market.current_demand_bond, abs(self.market.current_supply_bond) ))

        # print environment.variable_parameters['price_of_bond'], price_bond
        environment.assets[2].prices.append(price_bond)
        environment.variable_parameters['price_of_bond'] = environment.assets[2].prices[-1]

        from functions.bond_price import calc_yield
        new_yield = calc_yield( environment.assets[2].years, environment.assets[2].coupon, -environment.variable_parameters['price_of_bond'], environment.assets[2].face_value)
        # The new price has an effect on the yield which will affect the new step
        environment.variable_parameters['r_f'] = new_yield
        logging.info("New price for bond is %s; new yield is %s; at step %s",environment.variable_parameters['price_of_bond'], environment.variable_parameters['r_f'] , time)

    def policy_action(self, environment):
        from random import Random
        random = Random()
        noise = np.random.normal(0,0.0001,1)

        oldValue = 0.0
        newValue = 0.0
        returnValue = 0.0

        oldValue = environment.variable_parameters['r_f']
        newValue = max(round(1 - 0.003 + 0.00000001*random.random()*oldValue,4 ) ,0.0)
        returnValue = round(newValue - oldValue, 4)

        QE = (oldValue - newValue )*0.00001 + noise
        environment.variable_parameters['r_f'] = max(0, environment.variable_parameters['r_f'] - abs(QE))

        from functions.bond_price import calc_bond_price
        p = round(calc_bond_price(100, 10, environment.variable_parameters["r_f"] , 0, 2),4)

        environment.variable_parameters['price_of_bond'] = p
        print "QE", QE

        # for fund in environment.funds:
        #     if environment.variable_parameters["r_f"] < 0.03:
        #         fund.state_variables["theta"] = 3


    def remove_transactions_after_sell(self, environment, tracking_a, tracking_b):
        for tranx in tracking_a:
            tranx.remove_transaction(environment)
        for tranx in tracking_b:
            tranx.remove_transaction(environment)

    def get_buyer_a_balance_amount(self, fund_identifier):
        """
        Method to get buyer's balance amount

        Argument
        =====
        Fund object

        Output
        ===
        None or float
        Call this before transactions are deleted!
        """
        balance_a = 0
        num_transactions = 0.0

        new_list = []
        for tranx in fund_identifier.accounts:
            # Find the transactions
            if tranx.type_ == "A" and tranx.to.identifier == fund_identifier.identifier and "firm" not in tranx.from_.identifier :
                num_transactions +=1
                new_list.append(tranx)
        for index, value in enumerate(new_list):
            if value.type_ == "A" and value.to.identifier == fund_identifier.identifier and "firm" not in value.from_.identifier :
                balance_a = balance_a + value.amount
                if index == (num_transactions-1):
                    return balance_a

    def get_buyer_b_balance_amount(self, fund_identifier):
        """
        Method to get buyer's balance amount

        Argument
        =====
        Fund object

        Output
        ===
        None or float
        Call this before transactions are deleted!
        """
        balance_b = 0
        num_transactions = 0.0

        new_list = []
        for tranx in fund_identifier.accounts:
            # Find the transactions
            if tranx.type_ == "B" and tranx.to.identifier == fund_identifier.identifier and "firm" not in tranx.from_.identifier :
                num_transactions +=1
                new_list.append(tranx)
        for index, value in enumerate(new_list):
            if value.type_ == "B" and value.to.identifier == fund_identifier.identifier and "firm" not in value.from_.identifier :
                balance_b = balance_b + value.amount
                if index == (num_transactions-1):
                    return balance_b
    # -----------------------------------------------------------------------
    def pre_trade(self, environment, time):
        #pre-trade stuff, could also be in environment
        """
        Sets up funds with optimal portfolio and
        initializes accounts
        """
        for fund in (environment.funds):
            fund.endow_funds_with_shares(environment, time)
            fund.calc_optimal_pf(environment, self.asset_a.mu, self.asset_b.mu)
        logging.info(" Optimal portfolio for %s funds calculated", len(environment.funds))
        logging.info(" Endowed funds with transactions and investment_shares ")
    # Now we allocate initial portfolio to funds
        self.allocate_optimal_shares_to_funds(environment, time)

    def trade_a_priced(self, environment, time):
        # We find the market price of A shares
        # given supply and demand of the agents
        # and tolerance of error, resolution of search
        # and amplification factor for exponential search
        suppliers = []
        for agent in environment.firms:
            if agent.domicile==0:
                # print agent.get_account("number_of_shares"), agent.identifier
                suppliers.append([agent, agent.supply_of_shares])
        # And the list of buyers and their demand functions
        buyers = []
        for agent in environment.funds:
            buyers.append([agent, agent.demand_a])
        price_dummy = 75

        from market import Market
        # Put the appropriate settings, i.e. desired identifier
        market = Market("market")
        price = market.tatonnement(suppliers, buyers, price_dummy, 0.001, 0.01, 1.1)
        environment.variable_parameters["price_of_a"] = price
        # print price
        # now we use rationing to find the actual transactions between agents
        for_rationing = []
        for firm in environment.firms:
            if firm.domicile==0:
                for_rationing.append([firm, firm.supply_of_shares(price)])
        for fund in environment.funds:
            for_rationing.append([fund, -fund.demand_a(price)])

        # And we find the rationing, ie the amounts
        # of shares sold between pairs of agents
        rationed = market.rationing_proportional(for_rationing)

    def allocate_optimal_shares_to_funds(self, environment, time):
        sum_a = 0
        sum_b = 0

        for fund in environment.funds:
        #     fund.endow_portfolio_transactions(environment, time)
            amount_a = round(fund.calc_demand_asset(self.asset_a, self.asset_a.prices[-1], time), 4)
            amount_b = round(fund.calc_demand_asset(self.asset_b, self.asset_b.prices[-1], time), 4)
            sum_a += amount_a
            sum_b += amount_b
            if time == 0:
                fund.init_portfolio_transactions(environment, time, amount_a, amount_b)

    def divide_sum(self, n, total):
    #Return a randomly chosen list of n positive integers summing to total.
    #Each such list is equally likely to occur.
        import random
        random.seed(9001)
        dividers = sorted(random.sample(xrange(1, total), n - 1))
        return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

    def show_ration(self, ration_list, ident):
        """
        Look at the rationing lists with the code below.
        """
        if ident == "A":
            for i, valu in enumerate(ration_list):
                print "A ration %s:" %i
                print "this is the seller %s" %valu[0].identifier
                print "this is the buyer %s" %(valu[1].identifier)
                print "Quantity %s" %valu[2]
        if ident == "B":
            for i, valu in enumerate(ration_list):
                print "B ration %s:" %i
                print "this is the seller %s" %valu[0].identifier
                print "this is the buyer %s" %(valu[1].identifier)
                print "Quantity %s" %valu[2]
        else:
            pass

    def drag_out_fund(self, environment, ident):
        """
        Method to print individual fund to screen.
        Useful to see if updater process achieved
        correct output.

        Argument
        =====
        str of fund.identifier

        Output
        ====

        Returns an agent object according to the passed in identifier str()
        """
        for fund in environment.funds:
            if fund.identifier==str(ident):
                print fund

    def altElement(self, a, frequency):
        return a[::frequency]
