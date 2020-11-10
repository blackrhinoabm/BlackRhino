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
    num_sweeps = 0

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
        self.updater = Updater(environment)
        self.current_step = 0
        self.num_sweeps = int(environment.static_parameters['num_sweeps'])

        #For measurement
        self.sweep_result_list = []
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

    def traverse(self, item):
        try:
            for i in iter(item):
                for j in self.traverse(i):
                    yield j
        except TypeError:
            yield item
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

        for i in range(self.num_sweeps):

                self.current_step = i
                #DEFAULT IS DO RUN! I added leverage experiment
                self.updater.do_update(environment, i)
                # self.updater.do_update_leverage(environment, i, environment.static_parameters['leverage_increase'])
                self.sweep_result_list.append(self.updater.env_var_par_df)

        self.updater.write_sweep_list_of_results_to_csv(environment, self.current_step)

##########################################################################################
        ##########################################################################################
            ##########################################################################################
    def do_run_one_bank_shock(self, environment,ident):
        # loop over all time steps and do the updating
        # For each update step

        for i in range(self.num_sweeps):
                print(i)
                self.current_step = i

                self.updater.do_update_one_bank(environment, i, ident)
                self.sweep_result_list.append(self.updater.env_var_par_df)

        self.updater.write_sweep_list_of_results_to_csv(environment, self.current_step)
        
    # ------------------------------------------------------------------------
