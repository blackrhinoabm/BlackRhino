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

from abm_template.src.basemarket import BaseMarket
import numpy as np
import math


class Market(BaseMarket):
    #
    #
    # VARIABLES
    #
    #


    identifier = ""  # Identifier
    tolerance = 0.01  # Tolerance when matching demand and supply
    resolution = 0.01  # Resolution by which we crawl in price finding
    amplification = 1.1  # Factor for exponential search (Wolffgang 2015 "A multi-agent non-stochastic economic simulator.")




    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Market, self).set_identifier(_value)

    def get_tolerance(self):
        return self.tolerance

    def set_tolerance(self, _value):
        super(Market, self).set_tolerance(_value)

    def get_resolution(self):
        return self.resolution

    def set_resolution(self, _value):
        super(Market, self).set_resolution(_value)

    def get_amplification(self):
        return self.amplification

    def set_amplification(self, _value):
        super(Market, self).set_amplification(_value)

    # -------------------------------------------------------------------------
    # __init__(environment)
    # -------------------------------------------------------------------------
    def __init__(self, identifier, scenario):
        self.identifier = identifier
        self.tolerance = 0.01
        self.resolution = 0.01
        self.amplification = 1.1
        self.lambda_ = 0.001


        self.current_demand_a, self.current_demand_b = 0.0, 0.0
        self.current_supply_a, self.current_supply_b = 0.0, 0.0

        self.net_demand_bonds = 0.0
        self.current_demand_bond, self.current_supply_bond = 0.0, 0.0

        self.accounts = []

        self.current_demand = {}
        self.current_supply = {}
        self.current_demand_bond = {}
        self.current_supply_bond = {}

        self.count_trades = {}

        # self.inventory['A'] = 0.0
        # self.inventory['B'] = 0.0
 # -------------------------------------------------------------------------
    def market_maker(self, price, excess_demand ):
        noise = np.random.normal(0,0.1,1)
        # print "price", price , "lambda", self.lambda_, "excess demand", (excess_demand), "noise",  noise
        new_price  = (price + self.lambda_*(excess_demand) + noise)
        return float(new_price)
    # -------------------------------------------------------------------------
    def market_maker_log(self, price, demand, supply  ):
        noise = np.random.normal(0,0.1,1)
        # print "price", price , "lambda", self.lambda_, "net_demand", (demand), math.log10(demand+1), " net_supply", supply, math.log10(supply +1), "noise",  noise
        new_price  = price + self.lambda_* (math.log10(demand+1) - math.log10(supply +1)  ) + noise
        return float(new_price)

    def determine_price_risky_assets(self, environment, time, global_assets):
        """
        Let's try exogenous market maker function for price setting according to
        excess demand (see Joshi & Famer 2002)
        """

        for asset in global_assets:
            if "riskfree" not in asset.identifier:
                asset.prices.append(max(0.01, self.market_maker_log(asset.prices[-1], self.current_demand[asset.identifier]['current_demand'] ,abs(self.current_supply[asset.identifier]['current_supply'])  )))
                #Save the new price in environment
                x = str('price_of_' + asset.identifier)
                environment.variable_parameters[x] = asset.prices[-1]

        # Look at the price series if you want
        # print "new price  ", asset.prices


    def determine_price_riskfree_asset(self, environment,time, global_assets ):
        "update_bond price and yield"

         # excess demand pushes the price upward, excess supply downwards
            # print "Bond market maker log impact:"
        for asset in global_assets:
            if "riskfree" in asset.identifier:
                #Careful with domicile
                domicile = asset.domicile
                # print self.current_demand_bond[domicile] , self.current_supply_bond[domicile], "here"
                price_bond =(self.market_maker_log( environment.variable_parameters['price_of_bond'], self.current_demand_bond[0], abs(self.current_supply_bond[0]) ))

        # print environment.variable_parameters['price_of_bond'], price_bond
        environment.assets[2].prices.append(price_bond)
        environment.variable_parameters['price_of_bond'] = environment.assets[2].prices[-1]

        from src.functions.bond_price import calc_yield
        new_yield = calc_yield( environment.assets[2].years, environment.assets[2].coupon, -environment.variable_parameters['price_of_bond'], environment.assets[2].face_value)
        # The new price has an effect on the yield which will affect the new step
        environment.variable_parameters['r_f'] = new_yield
        # logging.info("New price for bond is %s; new yield is %s; at step %s",environment.variable_parameters['price_of_bond'], environment.variable_parameters['r_f'] , time)

# -----------------------------------------------
    def exchange_risky_assets_create_transactions_global(self, environment, global_assets, dict_rationed, time):
        # Method to exchange assets via rationing.
        # print dict_rationed, "risky asset rationed dictionary"
        for asset in global_assets:
            if "riskfree" not in asset.identifier:
        #Loop over the rationed list of agent pairs
            # Check if list is not empty
                if len(dict_rationed[asset.identifier]) != 0:
                    for index, item in dict_rationed.iteritems():
                    # Check if list is not empty
                    # To access list inside dictionary use item[0]
                        if asset.identifier == index:
                        # Create the sell transaction between the agent pair
                            environment.new_transaction(asset.identifier, "assets",  item[0][0].identifier,   item[0][1].identifier,  item[0][2], 0,  0, -1, environment)
                else:
                    print "No trade for", asset.identifier

    def exchange_assets_netting_global(self, environment, time, global_assets):
        """
        Method to net the books of the sellers and buyers of share assets.
        We net the transactions, so they don't accumulate
        over the course of the simulation

        Argument
        ========
        Environment to loop over buyers and sellers

        Output
        ======
        A dictionary with transactions (one for each traded asset) marked for deletion.
        """

        #To keep track of the sell operations, we use these balance floats and dictionary
        balances = {}
        balance = 0.0

        for i in global_assets:
            if "riskfree" not in i.identifier:

                temp = {
                        i.identifier : 0.0
                        }
                balances.update(temp)

        #Same for delete sets
        to_delete = {}
        to_delete_set = set([])
        # Create a dictionary with sets for every trade
        # We create a proxy set for deleting transaction
        for i in global_assets:
            if "riskfree" not in i.identifier:

                temp = {
                        i.identifier : set([])
                        }
                to_delete.update(temp)

        ###########################

        for i in global_assets:
            # Let's get the ident
            ident = i.identifier
            # We start with the sellers of ident and loop over them
            for seller in environment.funds:
                for tranx in seller.accounts:
                    # Find the selling ident-transactions
                    if tranx.type_ == ident:
                        # print tranx.from_.identifier, seller.identifier
                        if tranx.from_.identifier == seller.identifier:
                            balances[ident] = balances[ident] + tranx.amount
                            # Add to the tracking set
                            to_delete_set.add(tranx)

                            to_delete[ident] =  to_delete_set

                            # Net the books
                            for firm in environment.firms:
                                    for tranx in seller.accounts:
                                        if tranx.type_ == ident:
                                            if tranx.from_ == firm:
                                                tranx.set_amount(tranx.amount - balances[ident], environment)
                                                # This is a little trick so avoid double counting
                                                balances[ident] = 0
           ###############
            #Now we loop over the buyers of ident
            for fund in environment.funds:
                # We get the balance amount of new assets aquired
                # Some funds bought nothing, so the next functions returns None
                #In that case we set the balancing amount to 0
                if self.get_buyer_balance_amount_global(fund, ident ) is None:
                    x = 0
                #otherwise we get x as balancing amount
                else:
                    x = self.get_buyer_balance_amount_global(fund, ident )
                 # Set the A account to the new amount
                for tranx in fund.accounts:
                    if tranx.type_ == ident and tranx.to.identifier == fund.identifier and "firm" in tranx.from_.identifier :
                        tranx.set_amount( tranx.amount + x , environment)

        return to_delete

    # tatonnement([sellers], [buyers], starting_price)
    # This function performs a Walrasian auction to determine the
    # price at equilibrium (market clearing).
    # Note that the input to this method are two lists, first contains pairs
    # of agents and their supply functions (methods), and seconds contains pairs
    # of agents and their demand functions (methods), so that:
    # [sellers] = [[agent_1, supply_function_1],[agent_2, supply_function_2],...]
    # [buyers] = [[agent_1, demand_function_1],[agent_2, demand_function_2],...]
    # -------------------------------------------------------------------------
    def tatonnement(self, sellers, buyers, starting_price, tolerance, resolution, amplification):
        self.tolerance = tolerance
        self.resolution = resolution
        self.amplification = amplification

        # return super(Market, self).tatonnement(sellers, buyers, starting_price)
        import random
        # Initialise a variable which looks for the equilibrium price
        price_dummy = 0.0
        # Set price dummy to the starting value
        if starting_price == 0.0:
            price_dummy = 0.00001
        else:
            price_dummy = starting_price
        # Initialise dummy variables for exponential search
        # First counts how many times we've moved in the same direction
        same_direction_in_a_row = 0
        # The second stores the last know direction:
        #  1 = price moved upwards
        # -1 = prive moved downwards
        directon = 0
        # The factor by which we change the price
        # It's based on the resolution parameter but is adjusted
        # in the course of exponential search
        delta = self.resolution
        # The search runs until we return the equilibrium price
        # This is potentially dangerous, but if it doesn't work
        # the whole model will not work, so this can be checked
        # on runtime, if suspicious make a counter and error on
        # given number of loops
        iteration_counter = 0
        while True:
            iteration_counter = iteration_counter + 1
            if price_dummy <= 0.0:

                raise LookupError("Price search in tatonnement went to 0. Something's amiss.")

            if iteration_counter > 1000:
                raise LookupError("Price search in tatonnement took too long. Something's amiss.")
            # On every run we compare tentative demand and supply
            # given the price we try out, so we initialise the
            # dummy demand and supply variables
            demand = 0.0
            supply = 0.0
            # Then we calculate supply and demand for a given price
            # by calculating supply and demand of all respective
            # agents through their supply demand functions ran
            # with the dummy price, and these are summed to
            # total supply and total demand at the tried price
            # First, supply:
            for supplier in sellers:
                supply = supply + supplier[1](price_dummy)
             # Then, demand:
            for buyer in buyers:
                demand = demand + buyer[1](price_dummy)
             # We check the exit condition, that is the convergence of
            # supply and demand +/- set tolerance
            if demand == 0.0 and supply == 0.0:
                raise LookupError("Both supply and demand have yielded 0.0 in price search, check the supply and demand functions supplied.")
            if abs(demand - supply) / (demand + supply) <= self.tolerance:
                # If we found equilibrium price we return it to the caller
                return price_dummy
            # If we haven't found the equilibrium price we start the
            # exponential search
            # Alt implementation in Java:
            # https://github.com/kronrod/agentecon/blob/ComputationalEconomicsPaper/src/com/agentecon/price/ExpSearchPrice.java
            else:
                # We have two cases, either we need to increase or decrease
                # the price dummy, we start with excess demand
                if (demand - supply) > 0:
                    # Now, we have three cases:
                    # 1. It's the first run, and we haven't had any adjustments
                    # In this case we just adjust the price dummy by the
                    # standard delta gotten from the parameters
                    if directon == 0:
                        # We change the direction to upwards
                        directon = 1
                        # And adjust the price dummy by starting delta
                        price_dummy = price_dummy * (1 + delta)
                    # 2. We have the change in the same direction as previously
                    # Then we need to adjust delta accordingly and only then
                    # adjust the dummy price for further runs
                    elif directon == 1:
                        # The direction is already correct, so we
                        # only adjust the number of times we've enountered
                        # the same direction in a row by 1
                        same_direction_in_a_row = same_direction_in_a_row + 1
                        # If if was 2 or multiple of 2 times then we widen the
                        # gap by which we adjust the dummy price by amplification factor
                        if (same_direction_in_a_row > 0 and same_direction_in_a_row % 2 == 0):
                            delta = delta * self.amplification
                        # And adjust the price dummy accordingly
                        price_dummy = price_dummy * (1 + delta)
                    # 3. We have the change in opposite direction from previous one
                    # Then we need to adjust delta accordingly and only then
                    # adjust the dummy price for further runs
                    else:
                        # We reset the number of changes in the same direction
                        # since we change direction with this adjustment
                        same_direction_in_a_row = 0
                        # And set direction upwards
                        directon = 1
                        # On changing direction we shorten the gap by which
                        # we adjust the dummy price by amplification factor
                        delta = delta / self.amplification
                        # And adjust the price dummy accordingly
                        price_dummy = price_dummy * (1 + delta)
                # Now we move to the case with excess supply at last checked price
                else:
                    # Now, we have three cases:
                    # 1. It's the first run, and we haven't had any adjustments
                    # In this case we just adjust the price dummy by the
                    # standard delta gotten from the parameters
                    if directon == 0:
                        # We change the direction to downwards
                        directon = -1
                        # And adjust the price dummy by starting delta
                        price_dummy = price_dummy * (1 - delta)
                    # 2. We have the change in the same direction as previously
                    # Then we need to adjust delta accordingly and only then
                    # adjust the dummy price for further runs
                    elif directon == -1:
                        # The direction is already correct, so we
                        # only adjust the number of times we've enountered
                        # the same direction in a row by 1
                        same_direction_in_a_row = same_direction_in_a_row + 1
                        # If if was 2 or multiple of 2 times then we widen the
                        # gap by which we adjust the dummy price by amplification factor
                        if (same_direction_in_a_row > 0 and same_direction_in_a_row % 2 == 0):
                            delta = delta * self.amplification
                        # And adjust the price dummy accordingly
                        price_dummy = price_dummy * (1 - delta)
                    # 3. We have the change in opposite direction from previous one
                    # Then we need to adjust delta accordingly and only then
                    # adjust the dummy price for further runs
                    else:
                        # We reset the number of changes in the same direction
                        # since we change direction with this adjustment
                        same_direction_in_a_row = 0
                        # And set direction downwards
                        directon = -1
                        # On changing direction we shorten the gap by which
                        # we adjust the dummy price by amplification factor
                        delta = delta / self.amplification
                        # And adjust the price dummy accordingly
                        price_dummy = price_dummy * (1 - delta)

    # -------------------------------------------------------------------------
    # tatonnement([sellers], [buyers], starting_price)
    # This function performs a Walrasian auction to determine the
    # price at equilibrium (market clearing).
    # Note that the input to this method are two lists, first contains pairs
    # of agents and their supply functions (methods), and seconds contains pairs
    # of agents and their demand functions (methods), so that:
    # [sellers] = [[agent_1, supply_function_1],[agent_2, supply_function_2],...]
    # [buyers] = [[agent_1, demand_function_1],[agent_2, demand_function_2],...]
    # -------------------------------------------------------------------------
    def tatonnement_parallel(self, sellers, buyers, starting_price, tolerance, resolution, amplification):
        self.tolerance = tolerance
        self.resolution = resolution
        self.amplification = amplification
        return super(Market, self).tatonnement_parallel(sellers, buyers, starting_price)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # rationing(agents)
    # This function performs a rationing mechanism to clear the market.
    # Note that the input to this method is a lists containing pairs
    # of agents and their supply or demand (supply + demand -)
    # [agents] = [[agent_1, supply_1],[agent_2, supply_2],...]
    # and returns a list of pairs and their exchange amounts
    # [to_return] = [[agent_selling_1, agent_buying_1, amount_sold_1],
    #                [agent_selling_2, agent_buying_2, amount_sold_2]]
    # The rationing is done by matching pairs randomly and making transactions
    # of the maximum possible amount for that pair until all demand or supply
    # is extinguished
    # -------------------------------------------------------------------------
    def rationing(self, agents):
        import random
        # Then we initialise the list that we'll be returning to caller
        to_return = []
        # We create the variables that will hold total demand,
        # total supply, and their minimum or what will be exchanged
        supply = 0.0
        demand = 0.0
        exchange = 0.0
        # We go through agents and their supply or demand and calculate
        # the above values
        for agent in agents:
            if agent[1] > 0:
                supply = supply + agent[1]
            else:
                demand = demand - agent[1]
        exchange = min(supply, demand)
         # Then we adjust the supply or demand of all agents
        # proportionately to the mismatch between supply and demand
        # so that final allocations are proportionate to the original
        # supply or demand
        for agent in agents:
            if agent[1] > 0:  # supply
                agent[1] = agent[1] * (exchange / supply)
            if agent[1] < 0:  # demand
                agent[1] = agent[1] * (exchange / demand)
        # We create a list of integers the length of the agents we get
        itrange = list(range(0, len(agents)))
        # And randomise this list for the purposes of iterating randomly
        random.shuffle(itrange)
        # And we iterate over the agents randomly by proxy of iterating
        # through their places on the list [agents]
        for i in itrange:
            # Then we need another random pass through agents for the pairs
            itrange_inner = list(range(0, len(agents)))
            # But this time we remove the number belonging to the agent
            # from the outer loop, since agents cannot trade with themselves
            itrange_inner.remove(i)
            # And randomise as above
            random.shuffle(itrange_inner)
            # Finally, we have the inner loop for the random pair iteration
            for j in itrange_inner:
                # We only trade if one agent has excess supply (positive value)
                # while the other has excess demand (negative value)
                if agents[i][1] * agents[j][1] < 0:
                    # If the agent i is the one with excess demand
                    if agents[i][1] < 0:
                        # We find the value that will be traded as the minimum
                        # between the agents' respective excess supply and demand
                        value = min(abs(agents[i][1]), abs(agents[j][1]))
                        # And append the resulting transaction to the list we
                        # will return later with a list of three items:
                        # [the_seller, the_buyer, amount_sold]
                        to_return.append([agents[j][0], agents[i][0], value])
                        # Finally, we need to amend the values of excess
                        # supply and excess demand for the purpose of further
                        # trades within the loops
                        agents[i][1] = agents[i][1] + value
                        agents[j][1] = agents[j][1] - value
                    # If the agent j is the one with excess demand
                    elif agents[i][1] > 0:
                        # We find the value that will be traded as the minimum
                        # between the agents' respective excess supply and demand
                        value = min(abs(agents[i][1]), abs(agents[j][1]))
                        # And append the resulting transaction to the list we
                        # will return later with a list of three items:
                        # [the_seller, the_buyer, amount_sold]
                        to_return.append([agents[i][0], agents[j][0], value])
                        # Finally, we need to amend the values of excess
                        # supply and excess demand for the purpose of further
                        # trades within the loops
                        agents[i][1] = agents[i][1] - value
                        agents[j][1] = agents[j][1] + value
        # And return the list to the caller
        return to_return
        # return super(Market, self).rationing(agents)
    # -------------------------------------------------------------------------
    def return_total_demand(self, agents):
        demand = 0.0
        supply = 0.0
        for agent in agents:
            if agent[1] > 0:
                supply = supply + agent[1]
            else:
                demand = demand - agent[1]
        return demand
    # -------------------------------------------------------------------------
    def return_total_supply(self, agents):
        demand = 0.0
        supply = 0.0
        for agent in agents:
            if agent[1] > 0:
                supply = supply + agent[1]
            else:
                demand = demand - agent[1]
        return supply
    # -------------------------------------------------------------------------
    # rationing_proportional(agents)
    # This function performs a rationing mechanism to clear the market.
    # Note that the input to this method is a lists containing pairs
    # of agents and their supply or demand (supply + demand -)
    # [agents] = [[agent_1, supply_1],[agent_2, supply_2],...]
    # and returns a list of pairs and their exchange amounts
    # [to_return] = [[agent_selling_1, agent_buying_1, amount_sold_1],
    #                [agent_selling_2, agent_buying_2, amount_sold_2]]
    # This version makes sure the agents get to sell or buy amounts
    # proportionately to their original supply or demand, the pairings are
    # still random however
    # -------------------------------------------------------------------------
    def rationing_proportional(self, agents):
        return super(Market, self).rationing_proportional(agents)


    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # rationing_abstract(agents, matching_function, allow_match)
    # This function performs a rationing mechanism to clear the market.
    # Note that the input to this method is a lists containing pairs
    # of agents and their supply or demand (supply + demand -)
    # [agents] = [[agent_1, supply_1],[agent_2, supply_2],...]
    # and returns a list of pairs and their exchange amounts
    # [to_return] = [[agent_selling_1, agent_buying_1, amount_sold_1],
    #                [agent_selling_2, agent_buying_2, amount_sold_2]]
    # The matching_function is a method which for a pair of agents returns
    # a float representing their priority in the market rationing queue
    # The allow_match is a method which returns True for a pair of agents
    # which is allowed to exchange, and False otherwise
    # -------------------------------------------------------------------------
    def rationing_abstract(self, agents, matching_function, allow_match):
        return super(Market, self).rationing_abstract(agents, matching_function, allow_match)
    # -------------------------------------------------------------------------
    def exchange_bonds_global(self, environment, global_assets, time):
        rationed_bond  =  self.collect_orders_bonds(environment, global_assets, time)
        # Check if there is a trade
        if len(rationed_bond ) != 0:
            self.exchange_rfree_assets_create_transactions_global(environment, rationed_bond, global_assets, time)
            tracking_bond = self.exchange_assets_netting_riskfree(environment, time)
            self.remove_transactions_after_sell(environment, tracking_bond)
        else:
            print "there is no trade"


    def collect_orders_bonds(self, environment, global_assets, time):
        demand_bond, supply_bond = 0, 0
        #Helper
        for_rationing_bond = []

        trade_limit_bond = 0
        order_limit_bond = 0
        net_demand_bonds, ind_demand_bonds = 0.0, 0.0
        ag_demand_bonds = 0.0
        valuation_a, valuation_b, valuation_bond = 0,0,0
        difference = 0.0
        current_demand_bond = 0.0
        current_supply_bond = 0.0

        rationed_bond_dict = {}

        for asset in global_assets:
            if "riskfree" in asset.identifier:
                    # print "hei"
                domicile = asset.domicile
                # careful !! change this if there are more assets
                if asset.domicile == 0:
                    for fund in environment.funds:
                        ind_demand_bonds= (fund.state_variables["riskfree_weight"] * fund.get_account("investment_shares"))/  (environment.variable_parameters['price_of_bond'])
                        # print ind_demand_bonds - fund.get_account("Risk_free")
                        net_demand_bonds = fund.get_account("Risk_free") - ind_demand_bonds

                        if net_demand_bonds >0:
                             current_demand_bond+=net_demand_bonds
                        if net_demand_bonds <0:
                            current_supply_bond+=net_demand_bonds

                    demand_bond = abs(current_demand_bond)
                    temp  = {
                            domicile : demand_bond}
                    self.current_demand_bond.update(temp)
                    supply_bond = abs(current_supply_bond)
                    temp  = {
                            domicile : supply_bond}
                    self.current_supply_bond.update(temp)
                ind_demand_bonds = 0 #reset value

                percent = 0.01
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

                rationed_bonds = self.rationing_proportional(for_rationing_bond)
                # print rationed
                temp = {
                        asset.identifier :  rationed_bonds  }
                rationed_bond_dict.update(temp)
        return rationed_bond_dict

    def exchange_rfree_assets_create_transactions_global(self, environment, dict_bond, global_assets, time):
        #Loop over the rationed list of agent pairs
        print dict_bond, "riskfree"
        # Method to exchange assets via rationing.
        for asset in global_assets:
            if "riskfree"  in asset.identifier:
                if len(dict_bond[asset.identifier]) != 0:
        #Loop over the rationed list of agent pairs
                    for index, item in dict_bond.iteritems():
                            # To access list inside dictionary use item[0][0] etc
                        if asset.identifier == index:
                            # print    item[0][0].identifier,   item[0][1].identifier,  item[0][2]
                            # Create the sell transaction between the agent pair #
                            "Careful - todo - what happens if there are many domiciles?"
                            # environment.new_transaction("Risk_free", "assets",    item[0][0].identifier,   item[0][1].identifier,  item[0][2], 0,  0, -1, environment)
                else:
                    print("No trade for %s at time %s ") % (asset.identifier, time)
    def show_open_orders(self, time):
    # Code to see demand
        self.accounts=[self.current_demand_a,self.current_supply_a,self.current_demand_b, self.current_supply_b]

        names = ["Current demand for A", "Current supply for A", "Current demand for B", "Current supply for B",]
        for num, line in zip(names, self.accounts):
            if line == 0:
                print "Open market orders at step %s " % time
            print(" {}: {}".format(num, line))

    def get_buyer_balance_amount_global(self, identifier, ident):
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
        balance = 0
        num_transactions = 0.0

        new_list = []
        for tranx in identifier.accounts:
            # Find the transactions
            if tranx.type_ == ident and tranx.to.identifier == identifier.identifier and "firm" not in tranx.from_.identifier :
                num_transactions +=1
                new_list.append(tranx)
        for index, value in enumerate(new_list):
            if value.type_ == ident and value.to.identifier == identifier.identifier and "firm" not in value.from_.identifier :
                balance = balance  + value.amount
                if index == (num_transactions-1):
                    return balance

    def remove_transactions_after_sell_global(self, environment, transaction, global_assets):
        for asset in global_assets:
            for i, v in transaction.iteritems():
                if asset.identifier ==  i:

                    if "risk_free" not in asset.identifier:
                        for tranx in transaction[i]:
                            tranx.remove_transaction(environment)


    def get_buyer_bond_balance_amount_global(self, fund_identifier):
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
                "Careful with acessing the domicile here" #To do!!!

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
            if self.get_buyer_bond_balance_amount_global(fund) is None:
                x = 0

            #otherwise we get x as balancing amount
            else:
                x = self.get_buyer_bond_balance_amount_global(fund)
                # print x, fund.state_variables["net_demand_a"], "a net vs balance"
                remaining_bond = abs(fund.state_variables["net_demand_bonds"]) - abs(x)
                remaining_bond_aggregate += remaining_bond

            # Set the bond account to the new amount
            for tranx in fund.accounts:
                if tranx.type_ == "Risk_free" and tranx.to.identifier == fund.identifier and "Government" in tranx.from_.identifier :
                    tranx.set_amount( tranx.amount + x , environment)
        return to_delete_bond

    def remove_transactions_after_sell(self, environment, list_with_tranx):
            for tranx in list_with_tranx:
                tranx.remove_transaction(environment)
