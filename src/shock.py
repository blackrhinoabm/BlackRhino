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

from abm_template.src.baseshock import BaseShock
import random
import logging

# -------------------------------------------------------------------------
#  class Shock
# -------------------------------------------------------------------------


class Shock(BaseShock):
    #
    #
    # VARIABLES
    #
    #

    #
    #
    # METHODS
    #
    #

    # -------------------------------------------------------------------------
    # do_shock(environment, time, step)
    # This is the main wrapper function for the shocks
    # Here we specify what shocks are doing to the environment at the
    # beginning and the end (step) of the affected sweeps
    # Shocks are distinguished by the shock_type saved in the environment's
    # variables, these are strings for our purposes.
    # -------------------------------------------------------------------------
    def do_shock(self, environment, time, shock_type, step):
        # Send a logging message so we know it happened
        logging.info("      shock of type %s executed at time %s", shock_type, time)
        # Then we check the shock type
        # This shock changes the endwoment of labour of all
        # households temporarily
        if shock_type == "labour":
            # And run the shock for the beginning of the step
            # This is usually changing the environment to the
            # state of emergency
            if step == "start":
                for household in environment.households:
                    household.labour = 12
            # And run the things at the end of the step
            # This is usually for reverting to the original state
            if step == "end":
                for household in environment.households:
                    household.labour = 24
        # This shock changes the propensity to save of all households
        # temporarily, making them save more duing the shock (consume less)
        if shock_type == "savings":
            if step == "start":
                for household in environment.households:
                    household.propensity_to_save = 0.6
            if step == "end":
                for household in environment.households:
                    household.propensity_to_save = 0.4
        # This shock changes the total factor productivity parameter
        # in the C-D production function, temporarily making production
        # much less efficient, simulating malfunctions in the equipment,
        # mismanagement of labour and capital, or some external crisis
        if shock_type == "productivity":
            if step == "start":
                for firm in environment.firms:
                    firm.total_factor_productivity = 0.5
            if step == "end":
                for firm in environment.firms:
                    firm.total_factor_productivity = 1.8
        # This shock changes the elasticities within the C-D production
        # function, simulating a shift in the production technology
        if shock_type == "elasticity":
            if step == "start":
                for firm in environment.firms:
                    firm.labour_elasticity = 0.7
                    firm.capital_elasticity = 0.3
            if step == "end":
                for firm in environment.firms:
                    firm.labour_elasticity = 0.3
                    firm.capital_elasticity = 0.7
        # This shock changes the interest rates charged on loans and
        # deposits, simulating a banking shift
        if shock_type == "interests":
            if step == "start":
                for bank in environment.banks:
                    bank.interest_rate_loans = 0.07
                    bank.interest_rate_deposits = 0.03
            if step == "end":
                for bank in environment.banks:
                    bank.interest_rate_loans = 0.0
                    bank.interest_rate_deposits = 0.0
    # -------------------------------------------------------------------------
