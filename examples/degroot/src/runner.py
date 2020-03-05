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
from src.agent import Agent
from src.measurement import Measurement
from src.updater import Updater
from abm_template.src.baserunner import BaseRunner


# from abm_template.src.baserunner import BaseRunner

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
    num_sweeps = 0

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
    # initialize()
    # -------------------------------------------------------------------------

    def initialize(self, environment):
        self.identifier = environment.identifier
        self.num_sweeps = int(environment.static_parameters['num_sweeps'])
        self.updater = Updater(environment)
    # -------------------------------------------------------------------------

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
    def set_identifier(self, value):
        return super(Runner, self).set_identifier(value)

    # -------------------------------------------------------------------------
    # get_num_sweeps
    # -------------------------------------------------------------------------
    def get_num_sweeps(self):
        return self.num_sweeps
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # set_num_simulations
    # -------------------------------------------------------------------------
    def set_num_sweeps(self, value):
        super(Runner, self).set_num_sweeps(value)

    # -------------------------------------------------------------------------
    # do_run
    # -------------------------------------------------------------------------
    def do_run(self, environment):
        # loop over all time steps and do the updating

        # For each update step

        measurement = Measurement(environment, self)
        measurement.open_file()

        for i in range(self.num_sweeps):

            self.current_step = i

            self.updater.do_update(environment)
            measurement.write_to_file()

        print("***\nThis run had {}s sweeps and {}s simulations".format(self.num_sweeps, environment.static_parameters['num_simulations']))
        print("Check the output file that was written as csv in the measurements folder\n***")

        # environment.print_parameters()

        # agent = Agent()
        # print(self.get_identifier())
        # print(self.get_num_sweeps())
        # print(environment.agents[0])
        # print(environment.agents[1])

        # parameters={'deposit_rate':-0.02}
        # agent.append_parameters(parameters)
        # print(agent.get_parameters())

        measurement.close_file()
    # ------------------------------------------------------------------------
