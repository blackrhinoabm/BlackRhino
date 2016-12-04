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

        if ident == "Nedbank total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'NEDBANK':
                    return agent.total_assets

        if ident == "Nedbank total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'NEDBANK':
                    return agent.parameters['equity']

        if ident == "Nedbank total asset sales":
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

        if ident == "AFRICAN BANK total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'AFRICAN BANK':
                    return agent.total_assets

        if ident == "AFRICAN BANK total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'AFRICAN BANK':
                    return agent.parameters['equity']

        if ident == "AFRICAN BANK total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'AFRICAN BANK':
                    return agent.TAS

        if ident == "Bidvest total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'Bidvest':
                    return agent.total_assets

        if ident == "Bidvest total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'Bidvest':
                    return agent.parameters['equity']

        if ident == "Bidvest total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'Bidvest':
                    return agent.TAS

        if ident == "STANDARD CHARTERED total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'STANDARD CHARTERED':
                    return agent.total_assets

        if ident == "STANDARD CHARTERED total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'STANDARD CHARTERED':
                    return agent.parameters['equity']

        if ident == "STANDARD CHARTERED total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'STANDARD CHARTERED':
                    return agent.TAS

        if ident == "Investec total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'INVESTEC':
                    return agent.total_assets

        if ident == "Investec total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'INVESTEC':
                    return agent.parameters['equity']

        if ident == "Investec total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'INVESTEC':
                    return agent.TAS

        if ident == "VBS MUTUAL BANK total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'VBS MUTUAL BANK':
                    return agent.total_assets

        if ident == "VBS MUTUAL BANK total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'VBS MUTUAL BANK':
                    return agent.parameters['equity']

        if ident == "VBS MUTUAL BANK total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'VBS MUTUAL BANK':
                    return agent.TAS

        if ident == "SASFIN total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'SASFIN':
                    return agent.total_assets

        if ident == "SASFIN total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'SASFIN':
                    return agent.parameters['equity']

        if ident == "SASFIN total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'SASFIN':
                    return agent.TAS

        if ident == "BANK OF BARODA total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF BARODA':
                    return agent.total_assets

        if ident == "BANK OF BARODA total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF BARODA':
                    return agent.parameters['equity']

        if ident == "BANK OF BARODA total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF BARODA':
                    return agent.TAS

        if ident == "UBANK total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'UBANK':
                    return agent.total_assets

        if ident == "UBANK total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'UBANK':
                    return agent.parameters['equity']

        if ident == "UBANK total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'UBANK':
                    return agent.TAS

        if ident == "CITIBANK total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'CITIBANK':
                    return agent.total_assets

        if ident == "CITIBANK total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'CITIBANK':
                    return agent.parameters['equity']

        if ident == "CITIBANK total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'CITIBANK':
                    return agent.TAS

        if ident == "DEUTSCHE BANK total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'DEUTSCHE BANK':
                    return agent.total_assets

        if ident == "DEUTSCHE BANK total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'DEUTSCHE BANK':
                    return agent.parameters['equity']

        if ident == "DEUTSCHE BANK total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'DEUTSCHE BANK':
                    return agent.TAS

        if ident == "ALBARAKA BANK total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'ALBARAKA BANK':
                    return agent.total_assets

        if ident == "ALBARAKA BANK total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'ALBARAKA BANK':
                    return agent.parameters['equity']

        if ident == "ALBARAKA BANK total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'ALBARAKA BANK':
                    return agent.TAS

        if ident == "HABIB OVERSEAS total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'HABIB OVERSEAS':
                    return agent.total_assets

        if ident == "HABIB OVERSEAS total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'HABIB OVERSEAS':
                    return agent.parameters['equity']

        if ident == "HABIB OVERSEAS total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'HABIB OVERSEAS':
                    return agent.TAS
        if ident == "HABIB OVERSEAS total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'HABIB OVERSEAS':
                    return agent.total_assets

        if ident == "BANK OF TAIWAN SA BRANCH total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF TAIWAN SA BRANCH':
                    return agent.parameters['equity']

        if ident == "BANK OF TAIWAN SA BRANCH total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'HABIB OVERSEAS':
                    return agent.TAS

        if ident == "GRINDROD total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'GRINDROD':
                    return agent.total_assets

        if ident == "GRINDROD total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'GRINDROD':
                    return agent.parameters['equity']

        if ident == "GRINDROD total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'GRINDROD':
                    return agent.TAS

        if ident == "JPMORGAN total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'JPMORGAN':
                    return agent.total_assets

        if ident == "JPMORGAN total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'JPMORGAN':
                    return agent.parameters['equity']

        if ident == "JPMORGAN total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'JPMORGAN':
                    return agent.TAS

        if ident == "BANK OF CHINA JHB total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF CHINA JHB':
                    return agent.total_assets

        if ident == "BANK OF CHINA JHB total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF CHINA JHB':
                    return agent.parameters['equity']

        if ident == "BANK OF CHINA JHB total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF CHINA JHB':
                    return agent.TAS

        if ident == "SA BANK OF ATHENS total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'SA BANK OF ATHENS':
                    return agent.total_assets

        if ident == "SA BANK OF ATHENS total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'SA BANK OF ATHENS':
                    return agent.parameters['equity']

        if ident == "SA BANK OF ATHENS total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'SA BANK OF ATHENS':
                    return agent.TAS

        if ident == "MERCANTILE BANK total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'MERCANTILE BANK':
                    return agent.total_assets

        if ident == "MERCANTILE BANK total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'MERCANTILE BANK':
                    return agent.parameters['equity']

        if ident == "MERCANTILE total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'MERCANTILE BANK':
                    return agent.TAS

        if ident == "HBZ total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'HBZ':
                    return agent.total_assets

        if ident == "HBZ total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'HBZ':
                    return agent.parameters['equity']

        if ident == "HBZ total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'HBZ':
                    return agent.TAS

        if ident == "FINBOND MUTUAL total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'FINBOND MUTUAL':
                    return agent.total_assets

        if ident == "FINBOND MUTUAL equity":
            for agent in self.environment.agents:
                if agent.identifier == 'FINBOND MUTUAL':
                    return agent.parameters['equity']

        if ident == "FINBOND MUTUAL total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'FINBOND MUTUAL':
                    return agent.TAS

        if ident == "BANK OF INDIA JHB total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF INDIA JHB':
                    return agent.total_assets

        if ident == "BANK OF INDIA JHB total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF INDIA JHB':
                    return agent.parameters['equity']

        if ident == "BANK OF INDIA JHB total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'BANK OF INDIA JHB':
                    return agent.TAS

        if ident == "HONGKONG SHANGHAI BANKING CORP JHB total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'HONGKONG SHANGHAI BANKING CORP JHB':
                    return agent.total_assets

        if ident == "HONGKONG SHANGHAI BANKING CORP JHB total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'HONGKONG SHANGHAI BANKING CORP JHB':
                    return agent.parameters['equity']

        if ident == "HONGKONG SHANGHAI BANKING CORP JHB total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'HONGKONG SHANGHAI BANKING CORP JHB':
                    return agent.TAS

        if ident == "SOCIETE GENERALE JHB total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'SOCIETE GENERALE JHB':
                    return agent.total_assets

        if ident == "SOCIETE GENERALE JHB total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'SOCIETE GENERALE JHB':
                    return agent.parameters['equity']

        if ident == "SOCIETE GENERALE JHB total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'SOCIETE GENERALE JHB':
                    return agent.TAS

        if ident == "CHINA CONSTR BANK JHB total assets":
            for agent in self.environment.agents:
                if agent.identifier == 'CHINA CONSTR BANK JHB':
                    return agent.total_assets

        if ident == "CHINA CONSTR BANK JHB total equity":
            for agent in self.environment.agents:
                if agent.identifier == 'CHINA CONSTR BANK JHB':
                    return agent.parameters['equity']

        if ident == "CHINA CONSTR BANK JHB total asset sales":
            for agent in self.environment.agents:
                if agent.identifier == 'CHINA CONSTR BANK JHB':
                    return agent.TAS
