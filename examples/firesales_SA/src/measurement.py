#!/usr/bin/env python
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
from abm_template.src.basemeasurement import BaseMeasurement
from src.updater import Updater
# -------------------------------------------------------------------------
#  class Measurement
# -------------------------------------------------------------------------


class Measurement(BaseMeasurement):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""

    # this we need to tell python measurment is passing in objects
    runner = type('', (), {})()

    environment = type('', (), {})()

    filename = ""

    config = {}

    file = None

    csv_writer = None

    #
    #
    # METHODS
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        super(Measurement, self).set_identifier(identifier)

    def get_config(self):
        return self.config

    def set_config(self, config):
        super(Measurement, self).set_config(config)

    def get_environment(self):
        return self.environment

    def set_environment(self, environment):
        super(Measurement, self).set_environment(environment)

    def get_runner(self):
        return self.runner

    def set_runner(self, runner):
        super(Measurement, self).set_runner(runner)

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        super(Measurement, self).set_filename(filename)

    def get_file(self):
        return self.file

    def set_file(self, file):
        super(Measurement, self).set_file(file)

    def get_csv_writer(self):
        return self.csv_writer

    def set_csv_writer(self, csv_writer):
        super(Measurement, self).set_csv_writer(csv_writer)

    # -------------------------------------------------------------------------
    # __init__(self, environment, runner)
    # Initialises the Measurements object and reads the config
    # -------------------------------------------------------------------------
    def __init__(self, environment, runner):
        super(Measurement, self).__init__(environment, runner)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # open_file(self)
    # Opens the file and writes the headers
    # -------------------------------------------------------------------------
    def open_file(self):
        super(Measurement, self).open_file()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_to_file(self)
    # Writes a row of values for to store the state of the system
    # at the time of calling this method
    # -------------------------------------------------------------------------
    def write_to_file(self):
        super(Measurement, self).write_to_file()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # 
    # -------------------------------------------------------------------------
    def write_all_to_file(self):
        # We create an empty row
        out_row = []
        # loop over agents and add their properties to the out_row
        for agent in self.environment.agents:
            out_row.append(self.runner.current_step + 1)
            out_row.append(agent.identifier)
            out_row.append(agent.state_variables['total_asset_sales'])
            out_row.append(agent.state_variables['total_assets'])
            out_row.append(agent.parameters['equity'])
            out_row.append(agent.systemicness)
            out_row.append(agent.state_variables['shock_for_agent'])
            out_row.append(self.runner.updater.AV)
        # Finally we write the line to the output file
        self.csv_writer.writerow(out_row)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # close_file(self, filename)
    # Closes the file so we don't have issues with the disk and the file
    # -------------------------------------------------------------------------
    def close_file(self):
        super(Measurement, self).close_file()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # read_xml_config_file(self, config_file_name)
    # Read the xml config file specifying the config file
    # which is a list of lists
    # We need to specify the filename
    # We also need to specify each output:
    # - type: 'output'
    # - column: integer specifying which column will be used for this
    # - header: string written as header in the csv file in the column
    # - value: string or number, identifier for the wrapper function
    # specifying what the wrapper function returns
    # Thus:
    # {column_number: [header, output, wrapper_id],...:[...]]
    # [int: [string, string, string],...:[...]]
    #
    # Now we pass this on to the Measurement class through an xml file
    # which should look like this
    #
    # <measurement identifier='output_identifier'>
    #     <parameter type='filename' value='TestMeasurement.csv'></parameter>
    #     <parameter type='output' column='1' header='Step' value='current_step'></parameter>
    #     <parameter type='output' column='2' header='Deposits' value='column2_head' ></parameter>
    # </measurement>
    #
    # -------------------------------------------------------------------------
    def read_xml_config_file(self, config_file_name):
        super(Measurement, self).read_xml_config_file(config_file_name)
    # -------------------------------------------------------------------------


    def wrapper(self, ident, agent):
        if ident == "equity":
            return agent.parameters['equity']
        if ident == "total_asset_sales":
            return agent.state_variables['total_asset_sales']
        if ident == "shock_on_assets":
            return agent.state_variables['shock_on_assets']
        if ident == "systemicness":
            return agent.systemicness

    # -------------------------------------------------------------------------
    # wrapper(self, id)
    # Wrapper for functions returning the desired values to be written
    # -------------------------------------------------------------------------
    def wrapper(self, ident):
        if ident == "current_step":
            return self.runner.current_step + 1

        if ident == "global TAS":
            return self.runner.updater.system_TAS

        if ident == "indirect equity losses":
            return self.runner.updater.system_loss_equity_from_indirect_effects

        if ident == "AV":
            return self.runner.updater.system_vulnerability