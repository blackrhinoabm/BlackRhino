#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-

from src.measurement import Measurement
from src.updater import Updater


# from abm_template.src.baserunner import BaseRunner

# -------------------------------------------------------------------------
#
# class Runner
#
# -------------------------------------------------------------------------


class Runner():
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
        self.updater = Updater(environment)

        self.num_sweeps = int(environment.static_parameters['num_sweeps'])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # get_identifier
    # -------------------------------------------------------------------------

    def get_identifier(self):
        return self.identifier


    # -------------------------------------------------------------------------
    # get_num_sweeps
    # -------------------------------------------------------------------------
    def get_num_sweeps(self):
        return self.num_sweeps
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_run
    # -------------------------------------------------------------------------
    def do_run(self, environment):
        # loop over all time steps and do the updating
        # For each update step

        #measurement = Measurement(environment, self)
        #measurement.open_file()

        for i in range(self.num_sweeps):
                self.current_step = i
                self.updater.do_update(environment, i)

                #measurement.write_all_to_file()

        print("***\nThis run had %s sweeps and %s simulations" ) % (self.num_sweeps, environment.static_parameters['num_simulations'])
        #measurement.close_file()
    # ------------------------------------------------------------------------
