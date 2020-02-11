#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = """Paweł Fiedor (pawel.fiedor@uct.ac.za)"""

import abc
import logging

# -------------------------------------------------------------------------
#
#  class Market
#
# -------------------------------------------------------------------------
class BaseMarket(object):
    """
    Class variables: __metaclass__, identifier, parameters, state_variables
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_identifier(self):
        return
    @abc.abstractmethod
    def set_identifier(self, _identifier):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        if not isinstance(_identifier, str):
            raise TypeError
        else:
            self.identifier = _identifier
        return
    identifier = abc.abstractproperty(get_identifier, set_identifier)
    # identifier of the specific environment used for distinguishing them / logging
    # identifier should be a string

    @abc.abstractmethod
    def get_tolerance(self):
        return
    @abc.abstractmethod
    def set_tolerance(self, tolerance):
        """
        Class variables: tolerance
        Local variables: tolerance
        """
        if not isinstance(tolerance, float):
            raise TypeError
        else:
            self.tolerance = tolerance
        return
    tolerance = abc.abstractproperty(get_tolerance, set_tolerance)
    # tolerance of matching demand and supply with price

    @abc.abstractmethod
    def get_resolution(self):
        return
    @abc.abstractmethod
    def set_resolution(self, resolution):
        """
        Class variables: resolution
        Local variables: resolution
        """
        if not isinstance(resolution, float):
            raise TypeError
        else:
            self.resolution = resolution
        return
    resolution = abc.abstractproperty(get_resolution, set_resolution)
    # resolution in searching the price

    @abc.abstractmethod
    def get_amplification(self):
        return
    @abc.abstractmethod
    def set_amplification(self, amplification):
        """
        Class variables: amplification
        Local variables: amplification
        """
        if not isinstance(amplification, float):
            raise TypeError
        else:
            self.amplification = amplification
        return
    amplification = abc.abstractproperty(get_amplification, set_amplification)
    # amplification factor for exponential search

    @abc.abstractmethod
    def __init__(self):
        """
        Class variables: identifier, tolerance, resolution, amplification
        Local variables:
        """
        self.identifier = ""
        self.tolerance = 0.0
        self.resolution = 0.0
        self.amplification = 0.0
    # an abstract method for initializing the market clearing class

    @abc.abstractmethod
    def tatonnement(self, suppliers, buyers, starting_price):
        import random
        # Initialise a variable which looks for the equilibrium price
        price_dummy = 0.0
        # Set price dummy to the starting value
        # TODO: rethink this, maybe if it's run multiple times start with
        #       previous equilibrium price, the below is tentative
        if starting_price == 0.0:
            price_dummy = random.uniform(0, 10) + 0.01
            print price_dummy
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
            for supplier in suppliers:
                supply = supply + supplier[1](price_dummy)
            # Then, demand:
            for buyer in buyers:
                demand = demand + buyer[1](price_dummy)
            # We check the exit condition, that is the convergence of
            # supply and demand +/- set tolerance
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
    # abstract method for looking for equilibrium price

    @abc.abstractmethod
    def rationing(self, agents):
        # We need random to iterate over agents randomly
        import random
        # Then we initialise the list that we'll be returning to caller
        to_return = []
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
    # abstract method for rationing for agents with excess supply or demand


    @abc.abstractmethod
    def rationing_proportional(self, agents):
        # We need random to iterate over agents randomly
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
                demand = demand + agent[1]
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
    # abstract method for rationing for agents with excess supply or demand
    # with proportional rationing
