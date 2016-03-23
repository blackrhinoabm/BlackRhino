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
import random

# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------


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

    #
    #
    # METHODS
    #
    #

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
    def __init__(self, identifier, tolerance, resolution):
        self.identifier = identifier
        self.tolerance = tolerance
        self.resolution = resolution
        self.amplification = 1.1
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # tatonnement([suppliers], [buyers], starting_price)
    # This function performs a Walrasian auction to determine the
    # price at equilibrium (market clearing).
    # Note that the input to this method are two lists, first contains pairs
    # of agents and their supply functions (methods), and seconds contains pairs
    # of agents and their demand functions (methods), so that:
    # [suppliers] = [[agent_1, supply_function_1],[agent_2, supply_function_2],...]
    # [buyers] = [[agent_1, demand_function_1],[agent_2, demand_function_2],...]
    # -------------------------------------------------------------------------
    def tatonnement(self, suppliers, buyers, starting_price):
        # Initialise a variable which looks for the equilibrium price
        price_dummy = 0.0
        # Set price dummy to the starting value
        # TODO: rethink this, maybe if it's run multiple times start with
        #       previous equilibrium price, the below is tentative
        if starting_price == 0.0:
            price_dummy = random.randrange(0, 10, 0.1)
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
        while True:
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
                supply = supply + supplier[0].supplier[1](price_dummy)
            # Then, demand:
            for buyer in buyers:
                demand = demand + buyer[0].buyer[1](price_dummy)
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
    # -------------------------------------------------------------------------
