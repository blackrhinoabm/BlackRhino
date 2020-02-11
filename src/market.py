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

    def add_order(self, agent, price, volume, time, ident, type_):
        # We import operator to be able to quickly sort the books
        from operator import itemgetter
        # Note that trades are executed at the price of the active order!!!
        # The topology of an order for simplicity:
        # order[0] = agent
        # order[1] = price
        # order[2] = volume
        # order[3] = time
        # order[4] = ident
        # order[5] = type_
        # In the LOB functions we'll return list of trades
        # These trades will be then used by the models as they see fit
        # We need selling agent, buying agent, quantity and price
        # If we need markets for every single security then add init (TODO)
        # return [seller, buyer, quantity, price]
        # We initialise the container for returning executed trades
        to_return = []
        # We check whether we add a sell or buy order
        # If it is a sell order:
        if type_ == "sell":
            # We check how much buy volume do we have above or on the price of the incoming sell
            volume_above_price = 0.0
            # So we go through the buy book
            for order in self.lob_buy_book:
                # And find orders the price of which is above the incoming sell price
                if order[1] >= price:
                    # We add those to the volume we're looking for
                    volume_above_price = volume_above_price + order[2]
            # If that volume is bigger than the volume of the incoming sell
            # Then all of the incoming sell will be executed
            if volume_above_price >= volume:
                # We need order in the way we execute the trades
                # So we reorder by price and time (price priority first, then time priority)
                self.lob_buy_book = sorted(self.lob_buy_book, key=itemgetter(1, 3))
                # We initialise a helper variable showing volume left to settle
                volume_to_settle = volume
                # We go through the ordered buy book
                for order in self.lob_buy_book:
                    # And if we still have some volume to settle
                    settle_dummy = min(volume_to_settle, order[2])
                    # We execute this bit of the trade
                    # That is add it to the list of trades we'll return
                    to_return.append(agent, order[0], settle_dummy, order[1])
                    # And amend the volume to settle by the current settlement
                    volume_to_settle = volume_to_settle - settle_dummy
                    order[2] = order[2] - settle_dummy
            # If not all of the incoming sell can be executed right away
            else:
                # We execute just parts of the trade and add active trade to the books
                # We need order in the way we execute the trades
                # So we reorder by price and time (price priority first, then time priority)
                self.lob_buy_book = sorted(self.lob_buy_book, key=itemgetter(1, 3))
                # We initialise a helper variable showing volume left to settle
                volume_to_settle = volume
                # We go through the ordered buy book
                for order in self.lob_buy_book:
                    # If the price of the buy trade is still at least the price of the incoming sell
                    if order[1] >= price:
                        # And if we still have some volume to settle
                        settle_dummy = min(volume_to_settle, order[2])
                        # We execute this bit of the trade
                        # That is add it to the list of trades we'll return
                        to_return.append(agent, order[0], settle_dummy, order[1])
                        # And amend the volume to settle by the current settlement
                        volume_to_settle = volume_to_settle - settle_dummy
                        order[2] = order[2] - settle_dummy
                # And we add the unsettled part of the order as an active order to the sell book
                self.lob_sell_book.append([agent, price, volume_to_settle, time, ident, type_])
        # If it is a buy order:
        elif type_ == "buy":
            # We check how much buy volume do we have below or on the price of the incoming buy
            volume_below_price = 0.0
            # So we go through the sell book
            for order in self.lob_sell_book:
                # And find orders the price of which is below the incoming buy price
                if order[1] <= price:
                    # We add those to the volume we're looking for
                    volume_below_price = volume_below_price + order[2]
            # If that volume is bigger than the volume of the incoming sell
            # Then all of the incoming sell will be executed
            if volume_below_price >= volume:
                # We need order in the way we execute the trades
                # So we reorder by price and time (price priority first, then time priority)
                self.lob_sell_book = sorted(self.lob_sell_book, key=itemgetter(1, 3))
                # We initialise a helper variable showing volume left to settle
                volume_to_settle = volume
                # We go through the ordered buy book
                for order in self.lob_sell_book:
                    # And if we still have some volume to settle
                    # We execute this bit of the trade
                    settle_dummy = min(volume_to_settle, order[2])
                    # That is add it to the list of trades we'll return
                    to_return.append(agent, order[0], settle_dummy, order[1])
                    # And amend the volume to settle by the current settlement
                    volume_to_settle = volume_to_settle - settle_dummy
                    order[2] = order[2] - settle_dummy
            # If not all of the incoming sell can be executed right away
            else:
                # We execute just parts of the trade and add active trade to the books
                # We need order in the way we execute the trades
                # So we reorder by price and time (price priority first, then time priority)
                self.lob_sell_book = sorted(self.lob_sell_book, key=itemgetter(1, 3))
                # We initialise a helper variable showing volume left to settle
                volume_to_settle = volume
                # We go through the ordered buy book
                for order in self.lob_sell_book:
                    # If the price of the buy trade is still at least the price of the incoming sell
                    if order[1] <= price:
                        # And if we still have some volume to settle
                        settle_dummy = min(volume_to_settle, order[2])
                        # We execute this bit of the trade
                        # That is add it to the list of trades we'll return
                        to_return.append(agent, order[0], settle_dummy, order[1])
                        # And amend the volume to settle by the current settlement
                        volume_to_settle = volume_to_settle - settle_dummy
                        order[2] = order[2] - settle_dummy
                # And we add the unsettled part of the order as an active order to the sell book
                self.lob_buy_book.append([agent, price, volume_to_settle, time, ident, type_])
        # and finally we return the executed trades
        return to_return

    def cancel_order(self, ident):
        # We go through sell book first
        for order in self.lob_sell_book:
            # If the order has the identifier we're looking for
            if order[4] == ident:
                # We set the order volume to 0
                # This will be pruned with clear_book later
                order[2] = 0.0
                # If we do this then we return True (success)
                return True
        # Then we go through the buy book
        for order in self.lob_sell_book:
            # If the order has the identifier we're looking for
            if order[4] == ident:
                # We set the order volume to 0
                # This will be pruned with clear_book later
                order[2] = 0.0
                # If we do this then we return True (success)
                return True
        # If we didn't find the order with such id
        # Return False (failure)
        return False
        # just cancel based on ident

    def replace_order(self, new_volume, ident):
        # We go through the sell book
        for order in self.lob_sell_book:
            # Find the order with provided identifier
            if order[4] == ident:
                # Check if the new volume is smaller than previous
                if order[2] >= new_volume:
                    # If it is then exchange the volumes
                    order[2] == new_volume
                    # And return True (success)
                    return True
                else:
                    # If the new volume is bigger than old
                    # We return false (failure to replace)
                    return False
        # Then we go through the buy book
        for order in self.lob_buy_book:
            # Find the order with provided identifier
            if order[4] == ident:
                # Check if the new volume is smaller than previous
                if order[2] >= new_volume:
                    # If it is then exchange the volumes
                    order[2] == new_volume
                    # And return True (success)
                    return True
                else:
                    # If the new volume is bigger than old
                    # We return false (failure to replace)
                    return False
        # change the volume to smaller (do not time)
        # We assume unique identifiers (UUID4)

    def market_order(self, agent, volume, time, ident, type_):
        # We import operator to be able to quickly sort the books
        from operator import itemgetter
        to_return = []
        if type_ == "sell":
            # We execute just parts of the trade and add active trade to the books
            # We need order in the way we execute the trades
            # So we reorder by price and time (price priority first, then time priority)
            self.lob_buy_book = sorted(self.lob_buy_book, key=itemgetter(1, 3))
            # We initialise a helper variable showing volume left to settle
            volume_to_settle = volume
            # We go through the ordered buy book
            for order in self.lob_buy_book:
                # If the price of the buy trade is still at least the price of the incoming sell
                # And if we still have some volume to settle
                settle_dummy = min(volume_to_settle, order[2])
                # We execute this bit of the trade
                # That is add it to the list of trades we'll return
                to_return.append(agent, order[0], settle_dummy, order[1])
                # And amend the volume to settle by the current settlement
                volume_to_settle = volume_to_settle - settle_dummy
                order[2] = order[2] - settle_dummy
            # And we add the unsettled part of the order as an active order to the sell book
        elif type_ == "buy":
            # We execute just parts of the trade and add active trade to the books
            # We need order in the way we execute the trades
            # So we reorder by price and time (price priority first, then time priority)
            self.lob_sell_book = sorted(self.lob_sell_book, key=itemgetter(1, 3))
            # We initialise a helper variable showing volume left to settle
            volume_to_settle = volume
            # We go through the ordered buy book
            for order in self.lob_sell_book:
                # If the price of the buy trade is still at least the price of the incoming sell
                # And if we still have some volume to settle
                settle_dummy = min(volume_to_settle, order[2])
                # We execute this bit of the trade
                # That is add it to the list of trades we'll return
                to_return.append(agent, order[0], settle_dummy, order[1])
                # And amend the volume to settle by the current settlement
                volume_to_settle = volume_to_settle - settle_dummy
                order[2] = order[2] - settle_dummy
            # And we add the unsettled part of the order as an active order to the sell book

    def clear_book(self):
        # We remove the orders with 0 volume from the sell book
        self.lob_sell_book = [item for item in self.lob_sell_book if item[2] > 0.0]
        # We remove the orders with 0 volume from the buy book
        self.lob_buy_book = [item for item in self.lob_buy_book if item[2] > 0.0]
        # remove all orders with 0 volume left

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
