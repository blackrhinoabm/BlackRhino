#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
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
    identifier = ""  # identifier of the specific bank

    banks = []  # a list containing all banks (instances of class Bank)
    households = []  # a list containing all households (instances of class Household)
    firms = []  # a list containing all firms (instances of class Firm)

    static_parameters = {}  # a dictionary containing all static parameters (with a fixed value)
    variable_parameters = {}  # a dictionary containing all variable parameters (with a range of possible values)

    static_parameters["num_simulations"] = 0  # number of simulations to be performed
    static_parameters["num_sweeps"] = 0  # numbers of runs in a single simulation
    static_parameters["num_banks"] = 0  # number of banks in a simulation
    static_parameters["num_firms"] = 0  # number of firms in a simulation
    static_parameters["num_households"] = 0  # number of households in a simulation

    static_parameters["bank_directory"] = ""  # directory containing bank config files
    static_parameters["firm_directory"] = ""  # directory containing firm config files
    static_parameters["household_directory"] = ""  # directory containing household config files

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
    # add a given parameter to the stack of static parameters
    # -------------------------------------------------------------------------
    def add_static_parameter(self, name, value):
        super(Environment, self).add_static_parameter(name, value)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # add_variable_parameter(self, type, range_from, range_to)
    # adds a given parameter to the stack of variable parameters
    # -------------------------------------------------------------------------
    def add_variable_parameter(self, name, range_from, range_to):
        super(Environment, self).add_variable_parameter(name, range_from, range_to)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __init__(self,  environment_directory,  identifier)
    # initializes the bank given the directory containing the config
    # files and the identifier (name of the config file)
    # -------------------------------------------------------------------------
    def __init__(self,  environment_directory,  identifier):
        self.initialize(environment_directory,  identifier)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_identifier(self)
    # returns the identifier of the environment
    # -------------------------------------------------------------------------
    def get_identifier(self):
        return self.identifier
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # set_identifier(self, value)
    # changes the environment to the supplied value
    # -------------------------------------------------------------------------
    def set_identifier(self, value):
        super(Environment, self).set_identifier(value)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_static_parameters(self)
    # returns static parameters of the environment
    # -------------------------------------------------------------------------
    def get_static_parameters(self):
        return self.static_parameters
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # set_static_parameters(self, value)
    # changes static parameters to the supplied value
    # -------------------------------------------------------------------------
    def set_static_parameters(self, value):
        super(Environment, self).set_static_parameters(value)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_variable_parameters(self)
    # returns variable parameters of the environment
    # -------------------------------------------------------------------------
    def get_variable_parameters(self):
        return self.variable_parameters
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # set_variable_parameters(self, value):
    # changes variable parameters to the supplied value
    # -------------------------------------------------------------------------
    def set_variable_parameters(self, value):
        super(Environment, self).set_variable_parameters(value)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __getattr__
    # if the attribute isn't found by Python we tell Python
    # to look for it first in static and then in variable parameters
    # which allows for directly fetching parameters from the Environment
    # i.e. environment.num_banks instead of a bit more bulky
    # environment.static_parameters["num_banks"]
    # JUST FOR READING, DO NOT USE SHORTCUTS FOR WRITING
    # -------------------------------------------------------------------------
    def __getattr__(self, attr):
        try:
            return self.static_parameters[attr]
        except:
            try:
                return self.variable_parameters[attr]
            except:
                raise AttributeError('Environment has no attribute "%s".' % attr)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Functions for printing and writing
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # __str__
    # returns the environment as an xml like config file
    # -------------------------------------------------------------------------
    def __str__(self):
        environment_string = super(Environment, self).__str__()
        # abstract class uses config, we use environment, so we amend the string
        environment_string = environment_string.replace("<config", "<environment", 1)
        environment_string = environment_string.replace("</config>", "</environment>", 1)
        return environment_string
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # print_parameters(self)
    # prints the parameters within the environment (static + variable)
    # -------------------------------------------------------------------------
    def print_parameters(self):
        super(Environment, self).print_parameters()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_environment_file(file_name)
    # writes the environment as an xml config file to an .xml file
    # with the given file_name to the current directory
    # -------------------------------------------------------------------------
    def write_environment_file(self,  file_name):
        super(Environment, self).write_environment_file(file_name)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Functions for reading config files and initializing
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # read_xml_config_file(self, config_file_name)
    # reads an xml file with config and sets identifier, static and variable
    # parameters to whatever is in the config file
    # -------------------------------------------------------------------------
    def read_xml_config_file(self, config_file_name):
        super(Environment, self).read_xml_config_file(config_file_name)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize(self,  environment_directory,  identifier)
    # initializes the environment, initializing all the variables
    # reading the config file from supplied environment_directory and
    # identifier, and initializes all agents from the directories
    # supplied in the main config file
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
    # initialize_banks_from_files(self,  bank_directory)
    # banks have to be initialized for each simulation as a number of
    # banks might become inactive in the previous simulation
    # this reads all config files in the provided directory and
    # initializes banks with the contents of these configs
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
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_firms_from_files
    # banks have to be initialized for each simulation as a number of
    # banks might become inactive in the previous simulation
    # this reads all config files in the provided directory and
    # initializes firms with the contents of these configs
    # -------------------------------------------------------------------------
    def initialize_firms_from_files(self,  firm_directory):
        from src.firm import Firm
        # this routine is called more than once, so we have to reset the list of firms each time
        self.firms = []

        listing = os.listdir(firm_directory)
        if (len(listing) != self.static_parameters["num_firms"]):
            logging.error("    ERROR: number of configuration files in %s (=%s) does not match num_firms (=%s)",  firm_directory,  str(len(listing)), str(self.static_parameters["num_firms"]))

        for infile in listing:
            firm = Firm()
            firm.get_parameters_from_file(firm_directory + infile,  self)
            self.firms.append(firm)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_households_from_files
    # households have to be initialized for each simulation as a number of
    # households might become inactive in the previous simulation
    # this reads all config files in the provided directory and
    # initializes households with the contents of these configs
    # -------------------------------------------------------------------------
    def initialize_households_from_files(self,  household_directory):
        from src.household import Household
        # this routine is called more than once, so we have to reset the list of households each time
        self.households = []

        listing = os.listdir(household_directory)
        if (len(listing) != self.static_parameters["num_households"]):
            logging.error("    ERROR: number of configuration files in %s (=%s) does not match num_households (=%s)",  household_directory,  str(len(listing)), str(self.static_parameters["num_households"]))

        for infile in listing:
            household = Household()
            household.get_parameters_from_file(household_directory + infile,  self)
            self.households.append(household)
    # -------------------------------------------------------------------------
