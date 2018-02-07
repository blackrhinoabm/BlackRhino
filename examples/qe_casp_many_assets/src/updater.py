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
import random
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

    # These are functions from the abm template. They have to
    # be defined for the simulation to run
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

    # attach the risky assets to the updater

        self.asset_a = environment.get_agent_by_id("A")
        self.asset_b = environment.get_agent_by_id("B")
        self.riskfree_domestic = environment.get_agent_by_id("riskfree_A")


        # Determine sceario
        self.scenario = "no_QE"
        # self.scenario = "QE"

        # instantiate market class
        from src.exchange_classes.market import Market
        self.market = Market("market", self.scenario)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, time):
        """We set up optimal portfolios and
        initialize accounts """
        # row_holding = 0

        if time ==0:
            self.pre_trade_global(environment, time)

            # for firm in environment.firms:
            #     print firm.number_of_shares, "Number of shares", firm.identifier

            sum_bond_quantity = 0
            for fund in environment.funds:
                sum_bond_quantity+=fund.get_account("Risk_free")
            # print "total_bonds", sum_bond_quantity
            row_holdings = environment.assets[2].parameters["quantity"] - sum_bond_quantity

            for agent in environment.agents_generator():
                if agent.identifier == "Government":
                    agent.add_transaction("Risk_free", "assets", agent.identifier, agent.identifier, row_holdings, 0, 0, -1, environment)

            self.asset_a.dividends = [0 for i in range(0, environment.num_sweeps)]
            self.asset_b.dividends = [0 for i in range(0, environment.num_sweeps)]
            self.asset_a.funda_values
            self.asset_b.funda_values

            "Check if books balance"
            # for fund in environment.funds:
            #     if fund.identifier == "fund-3":
            #         print fund.check_accounts(environment), fund.identifier, "check",    time
        else:
            print "********************************"
            print "TIME", time #  steps to screen
            # While market orders are submitted contineously,
            # dividends are only updated infrequent times
            # list = [i for i in range(0, environment.num_sweeps)]
            list2 = [0 for i in range(0, environment.num_sweeps)]
            environment.profit_frequency = int(environment.num_sweeps)

            # for i, value in enumerate(list2):
            #     if time-1==i and i % environment.profit_frequency==0:
            #         "We collect dividends, fluctuate deposits and update profits of firms"
            #         for fund in environment.funds:
            #             fund.calc_new_deposits(environment.scaleFactorHouseholds, environment)
            #         for firm in environment.firms:
            #             profit = firm.calc_profit(time,  environment.profit_frequency )
            #             # determine new dividends and total assets after dividends
            #             dividend = firm.update_and_distribute_dividends(environment, time)
            #
            #             if firm.identifier=="firm-domestic":
            #                 self.asset_a.dividends[i]= dividend
            #                 # print "Dividend a", self.asset_a.dividends, time #for debugging
            #             if firm.identifier=="firm-abroad":
            #                 self.asset_b.dividends[i]=dividend
            #                 # print "Dividend b", self.asset_b.dividends, time #for debugging

            """Now the trading begins. We have two scenarios. QE and no QE"""
            tracking = {}

            if self.scenario == "no_QE":
                dict_of_rationed_assets, global_assets = self.update_expectation_demand_global(environment, time)
                ##
                # print dict_of_rationed_assets
                for key, value in dict_of_rationed_assets.iteritems():
                    for i in global_assets:
                        if "riskfree" not in i.identifier:
                            if len(dict_of_rationed_assets[i.identifier]) != 0:
                                self.market.exchange_risky_assets_create_transactions_global(environment, global_assets, dict_of_rationed_assets, time)
                                tracking = self.market.exchange_assets_netting_global(environment, time, global_assets)
                                self.market.remove_transactions_after_sell_global(environment, tracking, global_assets)
                            else:
                                print "No trade for", i.identifier

                #The same for bonds
                self.market.exchange_bonds_global(environment,global_assets, time)

                "At the end of the period, prices are adjusted"
                self.market.determine_price_risky_assets(environment, time, global_assets  )
                self.market.determine_price_riskfree_asset(environment, time, global_assets )
                self.valuation_changes(environment, time, global_assets)

            #     delta = 0
            #     for fund in environment.funds:
            #         cash = fund.get_cash(environment)
            #         # delta += fund.check_accounts(environment)
            #         if fund.get_cash(environment) > 0: #it's a buyer
            #             environment.add_cash("Cash", "assets", fund.identifier , fund.identifier , -cash , 0,  0, -1, environment)
            #
            #         if fund.get_cash(environment) < 0: #it's a seller
            #             environment.add_cash("Cash", "assets", fund.identifier , fund.identifier , -cash , 0,  0, -1, environment)
            # #
                # for fund in environment.funds:
                #     fund.check_accounts(environment), fund.identifier
                for asset in global_assets:
                    if "riskfree" not in asset.identifier:
                        asset.update_returns(environment)
                    else:
                        asset.returns.append(environment.variable_parameters['r_f'])
                #############
                #############
                #############
                ############
                #############
                # python counts from 0

                # if time >2:
                #  if time-1==i and i % environment.profit_frequency==0:
                #
                #     environment.assets[0].riskyness.append(environment.variable_parameters["std_a"])
                #     environment.variable_parameters["std_a"] = min( 0.8, np.std(self.asset_a.returns[:time]) *100)
                #     # environment.assets[0].riskyness.append(environment.variable_parameters["std_a"])
                #     # print environment.variable_parameters["std_a"], "standard deviation a"
                #
                #     environment.assets[1].riskyness.append(environment.variable_parameters["std_b"])
                #     environment.variable_parameters["std_b"] = min( 0.8, np.std(self.asset_b.returns[:time]) *100)
                #     # environment.assets[2].riskyness.append(environment.variable_parameters["std_a"])
                #     # print environment.variable_parameters["std_b"], "standard deviation b"
                #
                #     from scipy.stats import linregress
                #     a = self.asset_a.returns[:time]
                #     b = self.asset_b.returns[:time]
                #
                #     if len(a)==len(b):
                #         environment.variable_parameters["corr_a_b"] = linregress(a, b)[2]
                #         # print environment.variable_parameters["corr_a_b"]

    def valuation_changes(self, environment, time, global_assets):
        for asset in global_assets:
            if "riskfree" in asset.identifier :
                delta, effect_on_equity = 0, 0
                delta = environment.assets[2].prices[-1] - environment.assets[2].prices[-2] # Todo This will be a problem! RAther use get_agent_by_id!!
                for fund in environment.funds:
                    effect_on_equity = delta *  fund.get_account("Risk_free")  # The Risk_free is a Problem - rather use identifier!
                    for tranx in fund.accounts:
                        if tranx.type_ == "investment_shares":
                            tranx.set_amount(tranx.amount + effect_on_equity , environment)
            else:
                delta, effect_on_equity = 0, 0
                delta = asset.prices[-1] - asset.prices[-2]
                for fund in environment.funds:
                    effect_on_equity = delta  *  fund.get_account(asset.identifier)
                    for tranx in fund.accounts:
                        if tranx.type_ == "investment_shares":
                            tranx.set_amount(tranx.amount + effect_on_equity , environment)


    def update_expectation_demand_global(self, environment, time):
        "Careful here with accessing supply of shares"
        percent = 0.01 # We limit the total amount of assets traded at the current price

        trade_limits = {}
        #Fetch assets per region
        global_assets = []
        for index, wertpapier in environment.region.iteritems():
            if "domestic" in index:
                 for ii in wertpapier:
                    global_assets.append(ii)
                    #Set order limits
                    for firm in environment.firms:
                        if str("risky") in str(type(ii)) :
                            trade_limits.update( {str(ii.identifier): percent * environment.get_agent_by_id(ii.firm.identifier).number_of_shares   } )

        # print global_assets
        total_orders = self.collect_total_market_orders_determine_demand(environment, global_assets, trade_limits, time)
        #  Now we have the order limit, total demand and supply for the demand
        # We need to collect the individual orders which are normalised
        dict_of_rationed_assets = self.collect_orders_rationing(environment, global_assets,  total_orders, time)
        return dict_of_rationed_assets, global_assets

    def collect_orders_rationing(self, environment, global_assets,  total_orders, time):
        # print total_orders
        dict_of_rationed_assets = {}
        helper_for_rationing = {}

        #We iterate trhough all the shares
        for asset in global_assets:
            if "riskfree" not in asset.identifier:
                # print str(asset.identifier
                # Important Reset before we go into the next assets rationing
                for_rationing = []
                for fund in (environment.funds):

                    if time ==1 or time % 10==0:
                        fund.exp_prices, fund.exp_mus = fund.update_belief_global(environment, global_assets, time)
                        fund.weights = fund.calc_optimal_global(environment, fund.exp_mus, time)
                    print fund.weights
                    #we need the price
                    for identifier, price in fund.exp_prices.iteritems():
                        # fixate asset
                        if asset.identifier == identifier:
                            if "riskfree" not in asset.identifier:
                                target = round (fund.calc_demand_asset_global(asset, price, 1, time, asset.identifier, fund.weights)   , 4)
                                if target >0:
                                    target=(min(fund.get_account("investment_shares"), target))
                                if target <0:
                                    target = 0
                                # Printing for debugging
                                print fund.identifier, fund.strategy, "price:",asset.prices[-1], "expected price a",  price,  "\n"\
                                ,   "dividend a",asset.firm.dividend, "funda_v",asset.funda_v, "target   ", target,\
                                  "has", fund.get_account("A"), "net", fund.get_net_demand_a(target),\
                                   fund.get_account("investment_shares"),  time

                                # Get the minimum for normalisation
                                demand = total_orders[asset.identifier]['demand']
                                supply = total_orders[asset.identifier]['supply']
                                trade_limit = total_orders[asset.identifier]['trade_limit']

                                order_limit = min(trade_limit, supply, demand)
                                # print order_limit, "Demand", demand, "Supply", supply, asset.identifier
                                # print order_limit # if this is zero nothing is traded :((((

                                #We normalise the trade and save quantities demanded and supplied in lists
                                #Supply side rationing
                                if fund.get_net_demand_global(asset, target, identifier)<0:
                                    sold = (abs(fund.get_net_demand_global(asset, target, identifier)) * order_limit)/max(supply, 0.0000000001)
                                    for_rationing.append([fund, sold])

                                #DEMAND side rationing
                                if fund.get_net_demand_global(asset, target, identifier)>0:
                                    buy = (fund.get_net_demand_global(asset, target, identifier) * order_limit)/max(demand, 0.0000000001)
                                    for_rationing.append([fund, -buy])
                # We go outside the fund loop
                # We are still inside the loop for one asset
                x = str(asset.identifier)
                if "riskfree" not in x:
                    #put orders in dictionary
                    temp  = {
                            x : for_rationing}
                    helper_for_rationing.update(temp)
                    #put total demand in dictionary in market
                    temp = {
                        x :{'current_demand': demand }
                             }
                    self.market.current_demand.update(temp)
                    #put total supply in dictionary in market
                    temp = {
                        x :{"current_supply": supply }
                            }
                    self.market.current_supply.update(temp)

                    # We also save the aggregate current demand and supply (useful later)
                    # Count if the trade occurs
                    demand = self.market.current_demand[asset.identifier]['current_demand']
                    supply = self.market.current_supply[asset.identifier]['current_supply']
                if demand and supply >0:
                    temp = {
                            x :  1  }
                else:
                    temp = {
                            x :  0  }

                self.market.count_trades.update(temp)
                # printing for debugging
                # print "********************"
                # print "Aggregate demand and supply for risky assets in the market(Quantity) at step",time
                # print "Market", x
                # print "demand:",self.market.current_demand[x], 'supply:', self.market.current_supply[x]

                # now we use rationing to find the actual transactions between agents
                for_rationing = helper_for_rationing[x]
                rationed  = self.market.rationing_proportional(for_rationing)

                # print rationed
                temp = {
                        x :  rationed  }
                dict_of_rationed_assets.update(temp)
                # print "**********", "Rations:" #To do write function

        return dict_of_rationed_assets
        #
    def collect_total_market_orders_determine_demand(self, environment, global_assets, trade_limits , time):
        total_orders = {}
        trade_limit = 0   # This is the float, not the dictionary passed in
        demand  = 0
        supply = 0

        for asset in global_assets:
            # print str(asset.identifier)
            for fund in (environment.funds):
                if time ==1 or time % 10==0:
                    fund.exp_prices, fund.exp_mus = fund.update_belief_global(environment, global_assets, time)
                    fund.weights = fund.calc_optimal_global(environment, fund.exp_mus, time)
                # print weights
                #we need the price
                for identifier, price in fund.exp_prices.iteritems():
                    # fixate asset
                    if asset.identifier == identifier:
                        if "riskfree" not in asset.identifier:
                            target = round (fund.calc_demand_asset_global(asset, price, 1, time, asset.identifier, fund.weights)   , 4)
                            if target >0:
                                target=(min(fund.get_account("investment_shares"), target))
                            if target <0:
                                target = 0
                            # # Printing for debugging
                            # print fund.identifier, fund.strategy, "price:",asset.prices[-1], "expected price a",  price,  "\n"\
                            # ,   "dividend a",asset.firm.dividend, "funda_v",asset.funda_v, "target   ", target,\
                            #   "has", fund.get_account("A"), "net", fund.get_net_demand_a(target),\
                            #    fund.get_account("investment_shares"),  time

                            if fund.get_net_demand_global(asset, target, identifier ) > 0:
                                demand += abs(fund.get_net_demand_global(asset, target, identifier))
                                # print "Demand", demand,  fund.identifier

                            if fund.get_net_demand_global(asset, target, asset.identifier) < 0:
                                supply  += abs( fund.get_net_demand_global(asset, target, identifier))
                                # print "supply", supply,  fund.identifier

        #We go outside the investor loop to determine order_limits
        # print trade_limit, "demand", demand, "supply", supply
                            x = str(asset.identifier)
                            if "riskfree" not in x:
                                trade_limit = trade_limits[x]
                                #put orders in dictionary
                                temp  = {
                                        x :{'demand':demand,'supply':supply, "trade_limit": trade_limit }
                                                 }
                                total_orders.update(temp)
        # Look at orders with
        #print total_orders
        return total_orders


    def exchange_rfree_assets_create_transactions(self, environment, list_bond,  time):
        #Loop over the rationed list of agent pairs
        for index, item in enumerate(list_bond):
            # if index==2:  # Uncomment to keep track of only one ration
            print item, "Seller Risk_free:", item[0].identifier  #This is the seller of the specific ration
            print item, "Buyer: Risk_free", item[1].identifier  #This is the seller of the specific ration
            # Create the sell transaction between the agent pair
            environment.new_transaction("Risk_free", "assets", item[0].identifier, item[1].identifier,item[2], 0,  0, -1, environment)

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
         # linear market maker with excess total_orders below
        return to_delete_a,  to_delete_b

    def exchange_bonds(self, environment, time):
        demand_bond, supply_bond = 0, 0
        for_rationing_bond = []
        trade_limit_bond = 0
        order_limit_bond = 0
        net_demand_bonds, ind_demand_bonds = 0.0, 0.0
        ag_demand_bonds = 0.0
        valuation_a, valuation_b, valuation_bond = 0,0,0
        difference = 0.0

        for fund in environment.funds:
            ind_demand_bonds= (fund.state_variables["riskfree_weight"] * fund.get_account("investment_shares"))/  (environment.variable_parameters['price_of_bond'])
            net_demand_bonds = fund.get_account("Risk_free") - ind_demand_bonds
            if net_demand_bonds >0:
                self.market.current_demand_bond+=net_demand_bonds
            if net_demand_bonds <0:
                self.market.current_supply_bond+=net_demand_bonds

        demand_bond = abs(self.market.current_demand_bond)
        supply_bond = abs(self.market.current_supply_bond)
        ind_demand_bonds = 0 #reset value

        percent =0.01
        "Careful with acessing asset supply here"
        trade_limit_bond = percent * environment.assets[2].quantity
        order_limit_bond = min(trade_limit_bond, demand_bond , supply_bond)

        # We loop over it again
        for fund in environment.funds:
            ind_demand_bonds= (fund.state_variables["riskfree_weight"] * fund.get_account("investment_shares"))/  (environment.variable_parameters['price_of_bond'])
            net_demand_bonds = fund.get_account("Risk_free") - ind_demand_bonds
            # Selling agents
            if net_demand_bonds<0:
                sold_bond = (abs( net_demand_bonds ) * order_limit_bond)/max(supply_bond, 0.0000000001)
                for_rationing_bond.append([fund, sold_bond ])
            #DEMAND side rationing bonds
            if net_demand_bonds>0:
                buy_a = (net_demand_bonds * order_limit_bond)/max(demand_bond, 0.0000000001)
                for_rationing_bond.append([fund, -buy_a])

        rationed_bonds = self.market.rationing_proportional(for_rationing_bond)
        return rationed_bonds

    def exchange_assets_netting_riskfree(self, environment, time):
        """
        Method to net the books of the sellers and buyers of bonds.
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
        balance_bond = 0.0
        # We create a proxy set for deleting transaction
        to_delete_bond = set([])

        # We start with the sellers of A and loop over them
        for seller_bond in environment.funds:
            for tranx in seller_bond.accounts:
                # Find the selling A-transactions
                if tranx.type_ == "Risk_free":
                    if tranx.from_.identifier == seller_bond.identifier:
                        balance_bond = balance_bond + tranx.amount

                        # Add to the tracking set
                        to_delete_bond.add(tranx)
                        # Net the books
                        "Careful with acessing the government here"
                        for tranx in seller_bond.accounts:
                            if tranx.type_ == "Risk_free":
                                if tranx.from_.identifier == "Government":
                                    tranx.set_amount(tranx.amount - balance_bond, environment)
                                    # This is a little trick so avoid double counting
                                    balance_bond = 0
        remaining_bond_aggregate = 0
        #Now we loop over the buyers of bonds
        for fund in environment.funds:
            # We get the balance amount of new bonds assets aquired
            # Some funds bought nothing, so the next functions returns None
            #In that case we set the balancing amount to 0
            if self.get_buyer_bond_balance_amount(fund) is None:
                x = 0

            #otherwise we get x as balancing amount
            else:
                x = self.get_buyer_bond_balance_amount(fund)
                # print x, fund.state_variables["net_demand_a"], "a net vs balance"
                remaining_bond = abs(fund.state_variables["net_demand_bonds"]) - abs(x)
                remaining_bond_aggregate += remaining_bond

            # Set the bond account to the new amount
            for tranx in fund.accounts:
                if tranx.type_ == "Risk_free" and tranx.to.identifier == fund.identifier and "Government" in tranx.from_.identifier :
                    tranx.set_amount( tranx.amount + x , environment)
        return to_delete_bond


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

    def remove_transactions_after_sell(self, environment, list_with_tranx):
        for tranx in list_with_tranx:
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


    def get_buyer_bond_balance_amount(self, fund_identifier):
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
        balance_bond = 0
        num_transactions = 0.0

        new_list = []
        for tranx in fund_identifier.accounts:
            # Find the transactions
            if tranx.type_ == "Risk_free" and tranx.to.identifier == fund_identifier.identifier and "Government" not in tranx.from_.identifier :
                num_transactions +=1
                new_list.append(tranx)
        for index, value in enumerate(new_list):
            if value.type_ == "Risk_free" and value.to.identifier == fund_identifier.identifier and "Government" not in value.from_.identifier :
                balance_bond = balance_bond + value.amount
                if index == (num_transactions-1):
                    return balance_bond
    # -----------------------------------------------------------------------


    def pre_trade_global(self, environment, time):
        #pre-trade stuff, could also be in environment
        """
        Sets up funds with optimal portfolio and
        initializes accounts
        """
        # assets = [self.asset_a, self.asset_b] Another way to save assets, but can be called directly from updater
        # To do: add more assets!!
        list_of_returns = [self.asset_a.mu, self.asset_b.mu, self.riskfree_domestic.mu]
        for fund in (environment.funds):
            fund.endow_funds_with_shares(environment, time)
            weights = fund.calc_optimal_global(environment, 0, time)

            # Now we allocate initial portfolio to funds
        self.allocate_optimal_shares_to_funds(environment, time)



    def allocate_optimal_shares_to_funds(self, environment, time):
        sum_a = 0
        sum_b = 0

        for fund in environment.funds:
        #     fund.endow_portfolio_transactions(environment, time)
            amount_a = round(fund.calc_demand_asset(self.asset_a, self.asset_a.prices[-1], time), 4)
            amount_b = round(fund.calc_demand_asset(self.asset_b, self.asset_b.prices[-1], time), 4)
            # print amount_a, amount_b, fund.identifier
            sum_a += amount_a
            sum_b += amount_b
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


    def update_expectation_demand(self, environment, time):
        "Careful here with accessing supply of shares"
        percent = 0.01
        trade_limit_a = percent * environment.firms[0].number_of_shares
        trade_limit_b = percent * environment.firms[1].number_of_shares
        expected_price_a, expected_price_b  = 0, 0
        exp_mu_a, exp_mu_b = 0,0
        demand_a, demand_b = 0, 0
        supply_a, supply_b = 0, 0
        for_rationing_a = []
        for_rationing_b = []
        # print "********************"
        # print "Demand for risky assets in the market (Quantity)"
        # print "********************"
        assets = [ self.asset_a,  self.asset_b]

        for fund in (environment.funds):
            expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = fund.update_belief(environment, self.asset_a, self.asset_b, time)
            fund.calc_optimal_pf(environment,   exp_mu_a, exp_mu_b)
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

            # Printing for debugging
            print fund.identifier, fund.strategy, "price:", self.asset_a.prices[-1], "expected price a",  expected_price_a,  "expected mu a",  exp_mu_a, "\n"\
            ,   "dividend a", self.asset_a.firm.dividend, "funda_v", self.asset_a.funda_v, "target a ", target_a,\
              "has", fund.get_account("A"), "net", fund.get_net_demand_a(target_a),\
               fund.get_account("investment_shares"),  time
            #
            print fund.identifier, fund.strategy, "price:", self.asset_b.prices[-1], "expected price b",  expected_price_b,  "expected mu b",  exp_mu_b, "\n",\
            "dividend b", self.asset_b.firm.dividend, "funda_v", self.asset_b.funda_v, "target b", target_b,\
               "has", fund.get_account("B"), "net", fund.get_net_demand_b(target_b),\
                fund.get_account("investment_shares"), time

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
            fund.calc_optimal_pf(environment, exp_mu_a, exp_mu_b)

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

        # for selling_ration in rationed_a:
        #     print selling_ration[0]
        print "**********", "Rations:"
        self.show_ration(rationed_a, "A")
        # self.show_ration(rationed_b, "B")
        return rationed_a, rationed_b
