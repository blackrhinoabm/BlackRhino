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

    def add_order(self, asset, quantity):
        pass
        # if quantity <0:
        #
        #
        # else:
        #     self.sell_order

    def show_open_orders(self, time):
    # Code to see demand
        self.accounts=[self.current_demand_a,self.current_supply_a,self.current_demand_b, self.current_supply_b]

        names = ["Current demand for A", "Current supply for A", "Current demand for B", "Current supply for B",]
        for num, line in zip(names, self.accounts):
            if line == 0:
                print "Open market orders at step %s " % time
            print(" {}: {}".format(num, line))




        # self.current_demand_a, self.current_demand_b = 0.0, 0.0
        # self.current_supply_a, self.current_demand_b = 0.0, 0.0
        #
        # self.net_demand_bonds = 0.0

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
