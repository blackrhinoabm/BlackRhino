#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
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

from src.updater import Updater
from src.shock import Shock
from abm_template.src.baserunner import BaseRunner

# -------------------------------------------------------------------------
#
# class Runner
#
# -------------------------------------------------------------------------


class Runner(BaseRunner):
    # from environment import Environment

    #
    # VARIABLES
    #

    identifier = ""
    num_simulations = 0

    #
    # METHODS
    #
    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self):
        pass
    # -------------------------------------------------------------------------

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Runner, self).set_identifier(_value)

    def get_num_simulations(self):
        return self.num_simulations

    def set_num_simulations(self, _value):
        super(Runner, self).set_num_simulaitons(_value)

    # -------------------------------------------------------------------------
    # initialize()
    # -------------------------------------------------------------------------
    def initialize(self,  environment):
        self.identifier = environment.identifier
        self.num_simulations = environment.static_parameters["numSweeps"]
        self.environment = environment
        self.updater = Updater(self.environment)
        self.shocker = Shock()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_run
    # -------------------------------------------------------------------------
    def do_run(self, measurement,  debug):
        # loop over all time steps and do the updating
        for i in range(self.num_simulations):
            # the update step
            self.updater.do_update(self.environment, i, debug)

            # check if there is a shock at the current time step
            if (int(self.environment.get_state(i).static_parameters["shockType"]) != 0):
                self.shocker.do_shock(self.environment, int(i))
                self.environment.get_state(i).static_parameters["shockType"] = 0

            # do the measurement
            measurement.do_measurement(self.environment.banks)
    # ------------------------------------------------------------------------
