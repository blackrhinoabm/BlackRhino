#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
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

import logging
import os
from abm_template.src.baseconfig import BaseConfig


# -------------------------------------------------------------------------
#
#  class Environment
#
# -------------------------------------------------------------------------
class Environment(BaseConfig):
    #
    #
    # VARIABLES
    #
    #
    identifier = ""

    banks = []
    households = []
    firms = []

    static_parameters = {}
    variable_parameters = {}

    static_parameters["num_simulations"] = 0
    static_parameters["num_sweeps"] = 0
    static_parameters["num_banks"] = 0
    static_parameters["num_firms"] = 0
    static_parameters["num_households"] = 0

    static_parameters["bank_directory"] = ""
    static_parameters["firm_directory"] = ""
    static_parameters["household_directory"] = ""

    static_parameters["interest_rate_loans"] = 0.0  # interest rate on loans
    static_parameters["interest_rate_deposits"] = 0.0  # interest rate on deposits

    #
    #
    # CODE
    #
    #

    # -------------------------------------------------------------------------
    # functions for setting/changing id, parameters, and state variables
    # these either return or set specific value to the above variables
    # with the exception of add (2 first ones) which append the dictionaries
    # which contain static parameters or variable parameters
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # add_static_parameter(self, type, value)
    # -------------------------------------------------------------------------
    def add_static_parameter(self, name, value):
        # add the parameter to the stack of static parameters
        self.static_parameters[name] = value
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # add_variable_parameter(self, type, range_from, range_to)
    # -------------------------------------------------------------------------
    def add_variable_parameter(self, name, range_from, range_to):
        # add the parameter to the stack of variable parameters
        self.variable_parameters[name] = [range_from, range_to]
    # -------------------------------------------------------------------------

    def __init__(self,  environment_directory,  identifier):
        self.initialize(environment_directory,  identifier)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Environment, self).set_identifier(_value)

    def get_static_parameters(self):
        return self.static_parameters

    def set_static_parameters(self, _value):
        super(Environment, self).set_static_parameters(_value)

    def get_variable_parameters(self):
        return self.variable_parameters

    def set_variable_parameters(self, _value):
        super(Environment, self).set_variable_parameters(_value)

    # -------------------------------------------------------------------------
    # Functions for printing and writing
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # __str__
    # -------------------------------------------------------------------------
    def __str__(self):
        environment_string = super(Environment, self).__str__()
        environment_string = environment_string.replace("<config", "<environment", 1)
        environment_string = environment_string.replace("</config>", "</environment>", 1)
        return environment_string
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # print_parameters(self)
    # -------------------------------------------------------------------------
    def print_parameters(self):
        for key in self.static_parameters:
            print str(key) + ": " + str(self.static_parameters[key])
        for key in self.variable_parameters:
            print str(key) + ":" + " range: " + str(self.variable_parameters[key][0]) + "-" + str(self.variable_parameters[key][1])
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_environment_file(file_name)
    # -------------------------------------------------------------------------
    def write_environment_file(self,  file_name):
        out_file = open(file_name + "-check.xml",  'w')
        text = self.__str__()
        out_file.write(text)
        out_file.close()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Functions for reading config files and initializing
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # read_xml_config_file
    # -------------------------------------------------------------------------
    def read_xml_config_file(self, config_file_name):
        super(Environment, self).read_xml_config_file(config_file_name)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize
    # -------------------------------------------------------------------------
    def initialize(self,  environment_directory,  identifier):
        self.identifier = identifier

        self.static_parameters = {}
        self.static_parameters["num_simulations"] = 0
        self.static_parameters["num_sweeps"] = 0
        self.static_parameters["num_banks"] = 0
        self.static_parameters["num_firms"] = 0
        self.static_parameters["num_households"] = 0
        self.static_parameters["bank_directory"] = ""
        self.static_parameters["firm_directory"] = ""
        self.static_parameters["household_directory"] = ""
        self.variable_parameters = {}
        self.static_parameters["interest_rate_loans"] = 0.05  # interbank interest rate
        self.static_parameters["interest_rate_deposits"] = 0.01  # interest rate on deposits

        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_xml_config_file(environment_filename)
        logging.info("  environment file read: %s",  environment_filename)

        # then read in all the banks
        if (self.static_parameters["bank_directory"] != ""):
            if (self.static_parameters["bank_directory"] != "none"):  # none is used for tests only
                self.initialize_banks_from_files(self.static_parameters["bank_directory"])
                logging.info("  banks read from directory: %s",  self.static_parameters["bank_directory"])
        else:
            logging.error("ERROR: no bank_directory given in %s\n",  environment_filename)

        # then read in all the firms
        if (self.static_parameters["firm_directory"] != ""):
            if (self.static_parameters["firm_directory"] != "none"):  # none is used for tests only
                self.initialize_firms_from_files(self.static_parameters["firm_directory"])
                logging.info("  banks read from directory: %s",  self.static_parameters["firm_directory"])
        else:
            logging.error("ERROR: no firm_directory given in %s\n",  environment_filename)

        # then read in all the households
        if (self.static_parameters["household_directory"] != ""):
            if (self.static_parameters["household_directory"] != "none"):  # none is used for tests only
                self.initialize_households_from_files(self.static_parameters["household_directory"])
                logging.info("  banks read from directory: %s",  self.static_parameters["household_directory"])
        else:
            logging.error("ERROR: no household_directory given in %s\n",  environment_filename)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_banks_from_files
    # banks have to be initialized for each simulation as a number of banks might become inactive
    # in the previous simulation
    # -------------------------------------------------------------------------
    def initialize_banks_from_files(self,  bank_directory):
        from src.bank import Bank
        # this routine is called more than once, so we have to reset the list of banks each time
        self.banks = []

        listing = os.listdir(bank_directory)

        if (len(listing) != self.static_parameters["num_banks"]):
            logging.error("    ERROR: number of configuration files in %s (=%s) does not match num_banks (=%s)",  bank_directory,  str(len(listing)), str(self.static_parameters["num_banks"]))

        for infile in listing:
            bank = Bank()
            bank.get_parameters_from_file(bank_directory + infile,  self)
            self.banks.append(bank)
            bank.__del__()  # TODO not sure if this is really safe, but it is better than doing nothing about all those created instances...
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_banks_from_files
    # banks have to be initialized for each simulation as a number of banks might become inactive
    # in the previous simulation
    # -------------------------------------------------------------------------
    def initialize_firms_from_files(self,  firm_directory):
        from src.firm import Firm
        # this routine is called more than once, so we have to reset the list of banks each time
        self.firms = []

        listing = os.listdir(firm_directory)
        if (len(listing) != self.static_parameters["num_firms"]):
            logging.error("    ERROR: number of configuration files in %s (=%s) does not match num_firms (=%s)",  firm_directory,  str(len(listing)), str(self.static_parameters["num_firms"]))

        for infile in listing:
            firm = Firm()
            firm.get_parameters_from_file(firm_directory + infile,  self)
            self.firms.append(firm)
            firm.__del__()  # TODO not sure if this is really safe, but it is better than doing nothing about all those created instances...
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_banks_from_files
    # banks have to be initialized for each simulation as a number of banks might become inactive
    # in the previous simulation
    # -------------------------------------------------------------------------
    def initialize_households_from_files(self,  household_directory):
        from src.household import Household
        # this routine is called more than once, so we have to reset the list of banks each time
        self.households = []

        listing = os.listdir(household_directory)
        if (len(listing) != self.static_parameters["num_households"]):
            logging.error("    ERROR: number of configuration files in %s (=%s) does not match num_households (=%s)",  household_directory,  str(len(listing)), str(self.static_parameters["num_households"]))

        for infile in listing:
            household = Household()
            household.get_parameters_from_file(household_directory + infile,  self)
            self.households.append(household)
            household.__del__()  # TODO not sure if this is really safe, but it is better than doing nothing about all those created instances...
    # -------------------------------------------------------------------------
