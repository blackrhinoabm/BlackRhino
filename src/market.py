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
from src.transaction import Transaction

# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------


class Market(BaseMarket):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""

    #
    #
    # METHODS
    #
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Market, self).set_identifier(_value)

    # -------------------------------------------------------------------------
    # tatonnement([suppliers], [buyers])
    # This function performs a Walrasian auction to determine the
    # price at equilibrium (market clearing).
    # Note that the input to this method are two lists, first contains pairs
    # of agents and their supply functions (methods), and seconds contains pairs
    # of agents and their demand functions (methods), so that:
    # [suppliers] = [[agent_1, supply_function_1],[agent_2, supply_function_2],...]
    # [buyers] = [[agent_1, demand_function_1],[agent_2, demand_function_2],...]
    # -------------------------------------------------------------------------
    def tatonnement(self, suppliers, buyers):
        pass
        # set tolerance of some description
        # maybe as a variable above
        #
        # starting point? 0?
        # resolution? depends on the error? making it faster after 2 fails
        #
        # otherwise simple counting
        # demand * price = supply * price +- tolerance
    # -------------------------------------------------------------------------
