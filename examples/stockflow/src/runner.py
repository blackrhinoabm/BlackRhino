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
    def __init__(self, environment, scenario):
        self.initialize(environment, scenario)
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # initialize()
    # -------------------------------------------------------------------------

    def initialize(self, environment, scenario):
        self.identifier = environment.identifier
        self.updater = Updater(environment, self)

        self.scenario = scenario
        self.num_sweeps = int(environment.static_parameters['num_sweeps'])

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
    def do_run(self, environment, scenario):
        # loop over all time steps and do the updating
        # For each update step

        measurement = Measurement(environment, self)
        measurement.open_file()

        for i in range(self.num_sweeps):

                self.current_step = i

                if scenario == 'benchmark' or 'normal':
                   self.updater.do_update_benchmark(environment, self.current_step, self.scenario)

                # self.updater.do_update_GB_shock(environment, self.current_step)
                # self.updater.do_update_CB_shock(environment, self.current_step)#
                # self.updater.do_update_Redemption_shock(environment, self.current_step)

                measurement.write_all_to_file()

        print("***\nThis run had %s sweeps and %s simulations" ) % (self.num_sweeps, environment.static_parameters['num_simulations'])

        #measurement.close_file()
    # ------------------------------------------------------------------------
    def write_all_to_file(self):
        # We create an empty row
        out_row = []
        # loop over agents and add their properties to the out_row

        out_row.append(self.runner.updater.system_vulnerability)

        for agent in self.environment.agents:
            out_row.append(self.runner.current_step + 1)
            out_row.append(agent.identifier)
            out_row.append(agent.state_variables['direct_losses'])
            out_row.append(agent.state_variables['direct_losses'])
            out_row.append(agent.state_variables['total_asset_sales'])
            out_row.append(agent.state_variables['leverage'])
            out_row.append(agent.state_variables['total_assets'])
            out_row.append(agent.parameters['equity'])
            out_row.append(agent.parameters['debt'])
            out_row.append(agent.systemicness)
            out_row.append(agent.state_variables['shock_for_agent'])
        # Finally we write the line to the output file
        self.csv_writer.writerow(out_row)
