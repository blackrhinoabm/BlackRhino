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
from src.measurement import Measurement
from src.shock import Shock

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
    current_step = 0

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
    # get_num_sweeps
    # -------------------------------------------------------------------------
    def get_num_sweeps(self):
        return self.num_sweeps
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # set_num_sweeps
    # -------------------------------------------------------------------------
    def set_num_sweeps(self, _value):
        super(Runner, self).set_num_sweeps(_value)
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
        # We initialise the measurement class for writing outputs to csv
        # measurement = Measurement("Measurement", environment, self, {1: ["Step", "static", "self.runner.current_step"],
        # 2: ["Deposits", "dynamic", "self.environment.households[0].get_account", ["deposits"]]}, "TestMeasurement.csv")
        measurement = Measurement(environment, self)
        # And open the output file
        measurement.open_file()
        # We start the shock class as well
        shock_class = Shock()
        # For each update step
        for i in range(self.num_sweeps):
            # Do the shock:
            # First we check if the shock occurs at the current sweep
            # Then we run the shock procedure at the start of the update
            for shock in environment.shocks:
                if int(shock[0]) <= i+1 and int(shock[1]) >= i+1:
                    shock_class.do_shock(environment, i, shock[2], "start")
            # the update step
            # append current step, this is mostly for measurements
            self.current_step = i
            # do the actual update
            self.updater.do_update(environment, i)
            # write the state of the system
            measurement.write_to_file()
            # Do the shock (revert the shock if necessary):
            # First we check if the shock occurs at the current sweep
            # Then we run the shock procedure at the end of the update
            for shock in environment.shocks:
                if int(shock[0]) <= i+1 and int(shock[1]) >= i+1:
                    shock_class.do_shock(environment, i, shock[2], "end")
            # HELPER, to be removed in production
            # for firm in environment.households:
            #    print(firm)
            # print(environment.households[0])
            # print(environment.firms[0])
            # capital = 0.0
            # for tranx in environment.firms[0].accounts:
            #     if tranx.type_ == "capital" and tranx.from_ == environment.firms[0]:
            #         capital = capital + tranx.amount
            #     if tranx.type_ == "capital" and tranx.to == environment.firms[0]:
            #         capital = capital - tranx.amount
            # print(environment.firms[0].get_account("deposits")+capital-environment.firms[0].get_account("loans"))
            # capital = 0.0
            # for tranx in environment.firms[1].accounts:
            #     if tranx.type_ == "capital" and tranx.from_ == environment.firms[1]:
            #         capital = capital + tranx.amount
            #     if tranx.type_ == "capital" and tranx.to == environment.firms[1]:
            #         capital = capital - tranx.amount
            # print(environment.firms[1].get_account("deposits")+capital-environment.firms[1].get_account("loans"))
            # capital = 0.0
            # for tranx in environment.firms[2].accounts:
            #     if tranx.type_ == "capital" and tranx.from_ == environment.firms[2]:
            #         capital = capital + tranx.amount
            #     if tranx.type_ == "capital" and tranx.to == environment.firms[2]:
            #         capital = capital - tranx.amount
            # print(environment.firms[2].get_account("deposits")+capital-environment.firms[2].get_account("loans"))
            print(environment.banks[0])
            # print(environment.firms[0])
        # Close the output file at the end of the simulation
        measurement.close_file()
    # ------------------------------------------------------------------------
