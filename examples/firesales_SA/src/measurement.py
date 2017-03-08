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
    environment = type('', (), {})()

    runner = type('', (), {})()

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
    # -------------------------------------------------------------------------
    # wrapper(self, id)
    # Wrapper for functions returning the desired values to be written
    # -------------------------------------------------------------------------

    def wrapper(self, ident):
        if ident == "current_step":
            return self.runner.current_step + 1

        if ident == "global TAS":
            return self.runner.updater.sum

        if ident == "ABSA total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'ABSA':
                    return agent.total_assets

        if ident == "ABSA total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'ABSA':
                    return agent.parameters['equity']

        if ident == "ABSA total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'ABSA':
                    return agent.TAS

        if ident == "SBSA total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'ABSA':
                    return agent.total_assets

        if ident == "SBSA total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'SBSA':
                    return agent.parameters['equity']

        if ident == "SBSA total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'SBSA':
                    return agent.total_assets

        if ident == "SBSA total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'SBSA':
                    return agent.TAS

        if ident == "CAPITEC total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'CAPITEC':
                    return agent.total_assets

        if ident == "CAPITEC total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'CAPITEC':
                    return agent.parameters['equity']

        if ident == "CAPITEC total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'CAPITEC':
                    return agent.TAS

        if ident == "NEDBANK total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'NEDBANK':
                    return agent.total_assets

        if ident == "NEDBANK total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'NEDBANK':
                    return agent.parameters['equity']

        if ident == "NEDBANK total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'NEDBANK':
                    return agent.TAS

        if ident == "FNB total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'FNB':
                    return agent.total_assets

        if ident == "FNB total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'FNB':
                    return agent.parameters['equity']

        if ident == "FNB total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'FNB':
                    return agent.TAS

        if ident == "African Bank total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'African Bank':
                    return agent.total_assets

        if ident == "African Bank total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'African Bank':
                    return agent.parameters['equity']

        if ident == "African Bank total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'African Bank':
                    return agent.TAS

        if ident == "CHARTERED total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'CHARTERED':
                    return agent.total_assets

        if ident == "CHARTERED total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'CHARTERED':
                    return agent.parameters['equity']

        if ident == "CHARTERED total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'CHARTERED':
                    return agent.TAS

        if ident == "INVESTEC total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'INVESTEC':
                    return agent.total_assets

        if ident == "INVESTEC total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'INVESTEC':
                    return agent.parameters['equity']

        if ident == "INVESTEC total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'INVESTEC':
                    return agent.TAS

        if ident == "CITYBANK total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'CITYBANK':
                    return agent.total_assets

        if ident == "CITYBANK total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'CITYBANK':
                    return agent.parameters['equity']

        if ident == "CITYBANK total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'CITYBANK':
                    return agent.TAS

        if ident == "DB total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'DB':
                    return agent.total_assets

        if ident == "DB total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'DB':
                    return agent.parameters['equity']

        if ident == "DB total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'DB':
                    return agent.TAS

        if ident == "grindrod total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'grindrod':
                    return agent.total_assets

        if ident == "grindrod total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'grindrod':
                    return agent.parameters['equity']

        if ident == "grindrod total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'grindrod':
                    return agent.TAS

        if ident == "JPMORGAN total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'JpM':
                    return agent.total_assets

        if ident == "JPMORGAN total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'JpM':
                    return agent.parameters['equity']

        if ident == "JPMORGAN total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'JpM':
                    return agent.TAS

        if ident == "BoC total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'BoC':
                    return agent.total_assets

        if ident == "BoC total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'BoC':
                    return agent.parameters['equity']

        if ident == "BoC total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'BoC':
                    return agent.TAS

        if ident == "HSBC total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'HSBC':
                    return agent.total_assets

        if ident == "HSBC total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'HSBC':
                    return agent.parameters['equity']

        if ident == "HSBC total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'HSBC':
                    return agent.TAS

        if ident == "SOCIETE total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'SOCIETE':
                    return agent.total_assets

        if ident == "SOCIETE total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'SOCIETE':
                    return agent.parameters['equity']

        if ident == "SOCIETE total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'SOCIETE':
                    return agent.TAS

# columns for shocks
        if ident =="SBSA shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "SBSA":
                    return agent.shock_for_agent

        if ident =="CITYBANK shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "CITYBANK":
                    return agent.shock_for_agent

        if ident =="DB shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "DB":
                    return agent.shock_for_agent

        if ident =="grindrod shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "grindrod":
                    return agent.shock_for_agent

        if ident =="BoC shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "BoC":
                    return agent.shock_for_agent

        if ident =="ABSA shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "ABSA":
                    return agent.shock_for_agent

        if ident =="SOCIETE shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "SOCIETE":
                    return agent.shock_for_agent

        if ident =="HSBC shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "HSBC":
                    return agent.shock_for_agent

        if ident =="JPMORGAN shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "JpM":
                    return agent.shock_for_agent

        if ident =="CAPITEC shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "CAPITEC":
                    return agent.shock_for_agent

        if ident =="NEDBANK shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "NEDBANK":
                    return agent.shock_for_agent

        if ident =="FNB shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "FNB":
                    return agent.shock_for_agent

        if ident =="CHARTERED shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "CHARTERED":
                    return agent.shock_for_agent

        if ident =="African bank shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "African Bank":
                    return agent.shock_for_agent

        if ident =="INVESTEC shock on assets":
            for agent in self.environment.agents:
                if agent.identifier == "INVESTEC":
                    return agent.shock_for_agent
