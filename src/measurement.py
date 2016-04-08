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

import logging

# ============================================================================
#
# class Measurement
#
# ============================================================================


class Measurement(object):
    #
    # VARIABLES
    #

    # identifier for usual purposes
    identifier = ""
    # Now we set up a config for the measurements
    # see notes on the xml config file in the method below
    config = {}
    # environment for access
    environment = type('', (), {})()
    # filename for the output csv
    # runner for access
    runner = type('', (), {})()
    filename = ""
    # and the file we're writing to
    file = None
    # plus the csv writer
    csv_writer = None

    #
    # METHODS
    #

    # -------------------------------------------------------------------------
    # __init__(self, environment, runner)
    # Initialises the Measurements object and reads the config
    # -------------------------------------------------------------------------
    def __init__(self, environment, runner):
        # log that we've started measuring stuff
        logging.info("  measurement started...")
        # We move the variables to class variables
        # so that they are visible to other methods easily
        self.read_xml_config_file(environment.measurement_config)
        self.environment = environment
        self.runner = runner

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # open_file(self)
    # Opens the file and writes the headers
    # -------------------------------------------------------------------------
    def open_file(self):
        # Import the library for csv handling
        import csv
        # Open the file for writing
        # If there are multiple simulations we add a unique identifier
        if self.environment.num_simulations > 1:
            # And split the name into two parts, before .csv and .csv if it exists
            # Then add a unique identifier in the middle
            # (assuming the script does not run faster than a milisecond)
            import datetime
            import time
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H_%M_%S_%f')
            self.filename = self.filename.split(".csv")[0] + timestamp + ".csv"
            # SWITCH: uncomment the below 2 line, and comment the 4 above
            # to switch from unique names based on unix timestamp to uuid4
            # import uuid
            # self.filename = self.filename.split(".csv")[0] + str(uuid.uuid4()) + ".csv"
        self.file = open(self.filename, 'w')
        # Create an object for writing within the file
        # The file will be delimited with \n (not particularly relevant:)
        # That should be simple enough to change in vim in output if needed
        self.csv_writer = csv.writer(self.file, lineterminator='\n')
        # We write the headers first
        headers = []
        # We go through all things in the config
        # But not in the order within the config itself
        # But by the column number, or linearly with respect to output not input
        for i in range(0, len(self.config)):
            # We append the headers with the appropriate value from config
            headers.append(self.config[i+1][0])
        # And finally we write the headers to the file
        self.csv_writer.writerow(headers)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_to_file(self)
    # Writes a row of values for to store the state of the system
    # at the time of calling this method
    # -------------------------------------------------------------------------
    def write_to_file(self):
        # We create an empty row
        out_row = []
        # And go through the config, again in the order of output columns
        for i in range(0, len(self.config)):
            # If the value we want is static (a value to read)
            if self.config[i+1][1] == "static":
                # We append the row with the appropriate value
                out_row.append(eval(self.config[i+1][2]))
            # If the value we want is dynamic (a method to call)
            elif self.config[i+1][1] == "dynamic":
                # We append the row with the appropriate value
                out_row.append(eval(self.config[i+1][2])(*self.config[i+1][3]))
            # If the config states something else, raise an error
            else:
                raise LookupError("Measurement outputs should be static or dynamic.")
        # Finally we write the line to the output file
        self.csv_writer.writerow(out_row)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # close_file(self, filename)
    # Closes the file so we don't have issues with the disk and the file
    # -------------------------------------------------------------------------
    def close_file(self):
        # And we close the file just in case
        self.file.close()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # read_xml_config_file(self, config_file_name)
    # Read the xml config file specifying the config file
    # which is a list of lists
    # For static input, that is a variable gotten from somewhere we need
    # -The number of the output column
    # -Header used for this column
    # -Designation that it is static, i.e. a string "static"
    # -The full variable name as string, e.g. "self.environment.household[0].identifier"
    # For static input, that is a variable gotten from somewhere we need
    # -The number of the output column
    # -Header used for this column
    # -Designation that it is dynamic, i.e. a string "dynamic"
    # -The full method name as string, e.g. "self.environment.household[0].identifier"
    # NOTE: Both variable and method string above must be reachable from Measurement class
    # NOTE: That is why we have access to environment and runner (mostly for updater and step)
    # -A list of arguments for the above method
    # Thus:
    # {column_number: [header,static/dynamic, variable / method, list_of_arguments],...:[...]]
    # [int: [string, string, string / method, list],...:[...]]
    # -------------------------------------------------------------------------
    def read_xml_config_file(self, config_file_name):
        from xml.etree import ElementTree
        xmlText = open(config_file_name).read()
        element = ElementTree.XML(xmlText)
        self.identifier = element.attrib['identifier']

        # loop over all entries in the xml file
        for subelement in element:
            if subelement.attrib['type'] == 'filename':
                value = str(subelement.attrib['value'])
                self.filename = value

            if subelement.attrib['type'] == 'static':
                self.config[int(subelement.attrib['column'])] = [str(subelement.attrib['header']), 'static', str(subelement.attrib['value'])]

            if subelement.attrib['type'] == 'dynamic':
                self.config[int(subelement.attrib['column'])] = [str(subelement.attrib['header']), 'dynamic', str(subelement.attrib['method']), eval(str(subelement.attrib['arguments']))]
        logging.info("  measurement config file have been read")
    # -------------------------------------------------------------------------
