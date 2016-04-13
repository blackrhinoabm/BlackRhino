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
    # TENTATIVE FOR LIMIT ORDER BOOKS SO I DON'T FORGET
    #
    #
    # NOTES:
    # - price-time matching
    # - pro rata matching
    # - price-size matching
    #
    # - block list??? may be tricky
    # - clear at the end of the day (step)?
    # - how to cancel orders ???

    lob_lot = 1  # multiplier for orders, order
    lob_resolution = 0.00001
    lob_buy_book = []
    lob_sell_book = []

    def send_order(agent, price, volume, time):
        pass

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
    def __init__(self, identifier):
        self.identifier = identifier
        self.tolerance = 0.01
        self.resolution = 0.01
        self.amplification = 1.1
    # -------------------------------------------------------------------------

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
    def tatonnement(self, sellers, buyers, starting_price, tolerance, resolution, amplification):
        self.tolerance = tolerance
        self.resolution = resolution
        self.amplification = amplification
        return super(Market, self).tatonnement(sellers, buyers, starting_price)
    # -------------------------------------------------------------------------

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
        return super(Market, self).rationing(agents)
    # -------------------------------------------------------------------------

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
