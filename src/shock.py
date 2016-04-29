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

    def do_shock(self, environment, time, step):
        shock_type = environment.shock[2]
        logging.info("      shock of type %s executed at time %s", shock_type, time)
        if shock_type == "labour":
            if step == "start":
                for household in environment.households:
                    household.labour = 12
            if step == "end":
                for household in environment.households:
                    household.labour = 24
        if shock_type == 2:
            pass
    # -------------------------------------------------------------------------
