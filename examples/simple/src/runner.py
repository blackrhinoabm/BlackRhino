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

from src.updater import Updater
from abm_template.src.baserunner import BaseRunner

# -------------------------------------------------------------------------
#
# class Runner
#
# -------------------------------------------------------------------------


class Runner(BaseRunner):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""
    num_simulations = 0

    #
    #
    # METHODS
    #
    #

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, environment):
        self.initialize(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_identifier
    # -------------------------------------------------------------------------
    def get_identifier(self):
        return self.identifier
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # set_identifier
    # -------------------------------------------------------------------------
    def set_identifier(self, _value):
        super(Runner, self).set_identifier(_value)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_num_simulations
    # -------------------------------------------------------------------------
    def get_num_simulations(self):
        return self.num_simulations
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # set_num_simulations
    # -------------------------------------------------------------------------
    def set_num_simulations(self, _value):
        super(Runner, self).set_num_simulaitons(_value)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize()
    # -------------------------------------------------------------------------
    def initialize(self,  environment):
        self.identifier = environment.identifier
        self.num_sweeps = int(environment.num_sweeps)
        self.updater = Updater(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_run
    # -------------------------------------------------------------------------
    def do_run(self, environment):
        # loop over all time steps and do the updating
        for i in range(self.num_sweeps):
            # the update step
            self.updater.do_update(environment, i)
            print("Sweep number %s" % str(i+1))
            for bank in environment.banks:
                print(bank)
            print("Bank objects:")
            print(environment.banks)
            print("Firm objects:")
            print(environment.firms)
            print("Household objects:")
            print(environment.households)

    # ------------------------------------------------------------------------
