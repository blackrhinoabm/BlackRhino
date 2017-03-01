#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2012 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)

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

from updater import Updater
from environment import Environment

#-------------------------------------------------------------------------
#
# class Runner
#
#-------------------------------------------------------------------------
class Runner(object):	
    #
    # VARIABLES
    #
    identifier = ""
    num_sweeps = 0

    # 
    # METHODS
    #

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, environment):
        self.initialize(environment)
    # -------------------------------------------------------------------------


    #-------------------------------------------------------------------------
    # initialize()
    #-------------------------------------------------------------------------
    def initialize(self, environment):
        self.identifier = environment.identifier
        self.updater = Updater(environment)
        self.num_sweeps = int(environment.static_parameters['num_sweeps'])
    #-------------------------------------------------------------------------


    #-------------------------------------------------------------------------
    # do_run
    #-------------------------------------------------------------------------
    # loop over all time steps and do the updating
    def do_run(self, environment, time, debug):
        for i in range(self.num_sweeps):

                self.current_step = i

                self.updater.do_update(environment, i, debug)
    		# do the measurement
    		# measurement.do_measurement(self.environment.banks)
    #------------------------------------------------------------------------
