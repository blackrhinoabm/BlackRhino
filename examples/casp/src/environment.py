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
import os
from abm_template.src.baseconfig import BaseConfig


# -------------------------------------------------------------------------
#
#  class Environment
#
# -------------------------------------------------------------------------
class Environment(BaseConfig):

    from state import State
    from parameters import Parameters
    #
    #
    # VARIABLES
    #
    parameters = Parameters()
    state = State()

    identifier = ""  # identifier of the specific bank

    funds = []  # a list containing all funds (instances of class fund)
    firms = []  # a list containing all firms (instances of class Firm)
    agents = []

    static_parameters = {}  # a dictionary containing all static parameters (with a fixed value)
    variable_parameters = {}  # a dictionary containing all variable parameters (with a range of possible values)

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
    # agents_generator(self):
    # generator yielding all agents
    # -------------------------------------------------------------------------
    def agents_generator(self):
        # self.agents = [self.funds, self.firms, self.households]
        return super(Environment, self).agents_generator()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_agent_by_id
    # returns an agent based on the id
    # -------------------------------------------------------------------------
    def get_agent_by_id(self, ident):
        # self.agents = [self.funds, self.firms, self.households]
        return super(Environment, self).get_agent_by_id(ident)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __getattr__
    # if the attribute isn't found by Python we tell Python
    # to look for it first in static and then in variable parameters
    # which allows for directly fetching parameters from the Environment
    # i.e. environment.num_funds instead of a bit more bulky
    # environment.static_parameters["num_funds"]
    # makes sure we don't have it in both containers, which
    # would be bad practice [provides additional checks]
    # -------------------------------------------------------------------------
    def __getattr__(self, attr):
        return super(Environment, self).__getattr__(attr)
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
    	from xml.etree import ElementTree
        xmlText = open(config_file_name).read()
        element = ElementTree.XML(xmlText)
        self.identifier = element.attrib['identifier']
        self.parameters.identifier = self.identifier

		# loop over all entries in the xml file
        for subelement in element:
			# the first set of parameters will be valid for the whole simulation
			if (subelement.attrib['name'] == 'num_sweeps'):
				self.parameters.num_sweeps = int(subelement.attrib['value'])
			if (subelement.attrib['name'] == 'num_simulations'):
				self.parameters.num_simulations = int(subelement.attrib['value'])
			if (subelement.attrib['name'] == 'num_firms'):
				self.parameters.num_firms = int(subelement.attrib['value'])
			if (subelement.attrib['name'] == 'fund_directory'):
				self.parameters.fund_directory = str(subelement.attrib['value'])
			if (subelement.attrib['name'] == 'firm_directory'):
				self.parameters.firm_directory = str(subelement.attrib['value'])

			# now also read in the parameters that can change during the simulation
			if (subelement.attrib['type'] == 'changing'):
				name = subelement.attrib['name']
				value = float(subelement.attrib['value'])
				validFrom = subelement.attrib['validity'].rsplit("-")[0]
				validTo = subelement.attrib['validity'].rsplit("-")[1]
				self.parameters.add_parameter(name,  value,  validFrom, validTo)

        # loop over all entries in the xml file
        for subelement in element:
            name = subelement.attrib['name']

            if subelement.attrib['type'] == 'static':
                try:  # we see whether the value is a float
                    value = float(subelement.attrib['value'])
                except:  # if not, it is a string
                    value = str(subelement.attrib['value'])
                self.static_parameters[name] = value

            if subelement.attrib['type'] == 'changing':
                try:  # we see whether the value is a float
                    value = float(subelement.attrib['value'])
                except:  # if not, it is a string
                    value = str(subelement.attrib['value'])
                self.variable_parameters[name] = value

        # print self.variable_parameters
        # print self.static_parameters
        # print self.parameters.print_parameters()
    # -----------------------------------------------------------------

    # -----------------------------------------------------------------
    # initialize(self,  environment_directory,  identifier)
    # initializes the environment, initializing all the variables
    # reading the config file from supplied environment_directory and
    # identifier, and initializes all agents from the directories
    # supplied in the main config file
    #
    # -------------------------------------------------------------------------
    def initialize(self,  environment_directory,  identifier):
        self.identifier = identifier

        self.static_parameters = {}
        self.static_parameters["num_simulations"] = 0
        self.static_parameters["num_sweeps"] = 0
        self.static_parameters["num_firms"] = 0
        self.static_parameters["fund_directory"] = ""
        self.static_parameters["firm_directory"] = ""
        self.variable_parameters = {}

        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_xml_config_file(environment_filename)
        logging.info("  environment file read: %s",  environment_filename)

        # then read in all the funds
        if (self.fund_directory != ""):
            if (self.fund_directory != "none"):  # none is used for tests only
                self.initialize_funds_from_files(self.fund_directory, 0, 0)
                logging.info("  funds read from directory: %s",  self.fund_directory)
        else:
            logging.error("ERROR: no bank_directory given in %s\n",  environment_filename)


        #
        # # then read in all the firms
        # if (self.firm_directory != ""):
        #     if (self.firm_directory != "none"):  # none is used for tests only
        #         self.initialize_firms_from_files(self.firm_directory)
        #         logging.info("  firms read from directory: %s",  self.firm_directory)
        # else:
        #     logging.error("ERROR: no firm_directory given in %s\n",  environment_filename)
        #
        # # add agents to the list of all agents
        # self.agents = [self.funds, self.firms]


    # transaction
    # #
    # #
    #     # then, initialize transactions from the config files for funds
    #     if (self.fund_directory != ""):
    #         if (self.fund_directory != "none"):  # none is used for tests only
    #             self.read_transactions_for_funds(self.fund_directory)
    #             logging.info("  funds' transactions read from directory: %s",  self.fund_directory)
    #     else:
    #         logging.error("ERROR: no fund_directory given in %s\n",  environment_filename)
    #
    #     # then, initialize transactions from the config files for firms
    #     if (self.firm_directory != ""):
    #         if (self.firm_directory != "none"):  # none is used for tests only
    #             self.read_transactions_for_firms(self.firm_directory)
    #             logging.info("  firms' transactions read from directory: %s",  self.firm_directory)
    #     else:
    #         logging.error("ERROR: no firm_directory given in %s\n",  environment_filename)


    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_funds_from_files(self,  fund_directory)
    # funds have to be initialized for each simulation as a number of
    # funds might become inactive in the previous simulation
    # this reads all config files in the provided directory and
    # initializes funds with the contents of these configs
    # -------------------------------------------------------------------------
    def initialize_funds_from_files(self,  fund_directory, time, state):
        from src.fund import Fund
        # this routine is called more than once, so we have to reset the list of funds each time
        while len(self.funds) > 0:
            self.funds.pop()
        # we list all the files in the specified directory
        listing = os.listdir(fund_directory)
        # and check if the number of files is in line with the parameters
        self.num_funds = len(listing) 

        # we read the files sequentially

        for infile in listing:
            fund = Fund()
            fund.get_parameters_from_file(fund_directory + infile,  self, self.num_funds, time, self.get_state(0))
            # and read parameters to the funds, only to add them to the environment
            self.funds.append(fund)


            # print fund
            # print "Accounts:" , self.funds[0].identifier, self.funds[0].accounts
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_firms_from_files
    # funds have to be initialized for each simulation as a number of
    # funds might become inactive in the previous simulation
    # this reads all config files in the provided directory and
    # initializes firms with the contents of these configs
    # -------------------------------------------------------------------------
    def initialize_firms_from_files(self,  firm_directory):
        from src.firm import Firm
        # this routine is called more than once, so we have to reset the list of firms each time
        while len(self.firms) > 0:
            self.firms.pop()
        # we list all the files in the specified directory
        listing = os.listdir(firm_directory)
        # and check if the number of files is in line with the parameters
        if (len(listing) != self.num_firms):
            logging.error("    ERROR: number of configuration files in %s (=%s) does not match num_firms (=%s)",
                          firm_directory,  str(len(listing)), str(self.num_firms))
        # we read the files sequentially
        for infile in listing:
            firm = Firm()
            firm.get_parameters_from_file(firm_directory + infile,  self)
            # and read parameters to the firms, only to add them to the environment
            self.firms.append(firm)
    # -------------------------------------------------------------------------

	#-------------------------------------------------------------------------
	# get_state
	#-------------------------------------------------------------------------
    def get_state(self,  time): # TODO bring parameters in same order as in environment file and in state.__str__()
		# for each time t in the simulation return the actual set of paramet

        for parameter in self.parameters.parameters:
			validFrom = int(parameter['validity'][0])
			validTo = int(parameter['validity'][1])
			if (int(time) >= int(validFrom)) and (int(time) <= int(validTo)): # we have a valid parameterset
                # if parameter['type']=='thetaBank':
                #     self.state.thetaBank = float(parameter['value'])
				if parameter['type']=='global_assets_under_management':
					self.state.global_assets_under_management = float(parameter['value'])
                # if parameter['type']=='rb':
				# 	self.state.rb = float(parameter['value'])
				# if parameter['type']=='rd':
				# 	self.state.rd = float(parameter['value'])
				# if parameter['type']=='r':
				# 	self.state.r = float(parameter['value'])
				# if parameter['type']=='collateralQuality':
				# 	self.state.collateralQuality = float(parameter['value'])
				# if parameter['type']=='successProbabilityFirms':
				# 	self.state.successProbabilityFirms = float(parameter['value'])
				if parameter['type']=='num_funds':
					self.state.num_funds = float(parameter['value'])
				if parameter['type']=='scaleFactorHouseholds':
					self.state.scaleFactorHouseholds = float(parameter['value'])
				# if parameter['type']=='dividendLevel':
				# 	self.state.dividendLevel = float(parameter['value'])
				# if parameter['type']=='pFinancial':
				# 	self.state.pFinancial = float(parameter['value'])
				# if parameter['type']=='rhoFinancial':
				# 	self.state.rhoFinancial = float(parameter['value'])
				# if parameter['type']=='pReal':
				# 	self.state.pReal = float(parameter['value'])
				# if parameter['type']=='rhoReal':
				# 	self.state.rhoReal = float(parameter['value'])
				# if parameter['type']=='xiBank':
				# 	self.state.xiBank = float(parameter['value'])
				# if parameter['type']=='thetaBank':
				# 	self.state.thetaBank = float(parameter['value'])
				# if parameter['type']=='rhoBank':
				# 	self.state.rhoBank = float(parameter['value'])
				# if parameter['type']=='shockType':
				# 	self.state.shockType = int(parameter['value'])
				# if parameter['type']=='gammaBank':
				# 	self.state.gammaBank = float(parameter['value'])
				# if parameter['type']=='assetNumber':
				# 	self.state.assetNumber=float(parameter['value'])
				# if parameter['type']=='liquidationDiscountFactor':
				# 	self.state.liquidationDiscountFactor = float(parameter['value'])
				# if parameter['type']=='riskAversionDiscountFactor':
				# 	self.state.riskAversionDiscountFactor = float(parameter['value'])
				# if parameter['type']=='riskAversionAmplificationFactor':
				# 	self.state.riskAversionAmplificationFactor = float(parameter['value'])
				# if parameter['type']=='interbankLoanMaturity':
				# 	self.state.interbankLoanMaturity = float(parameter['value'])
				# if parameter['type']=='firmLoanMaturity':
				# 	self.state.firmLoanMaturity = float(parameter['value'])
				# if parameter['type']=='sifiSurchargeFactor':
				# 	self.state.sifiSurchargeFactor = float(parameter['value'])
				# if parameter['type']=='requiredCapitalRatio':
				# 	self.state.requiredCapitalRatio = float(parameter['value'])
				# if parameter['type']=='liquidityCoverageRatio':
				# 	self.state.liquidityCoverageRatio = float(parameter['value'])
				# if parameter['type']=='netStableFundingRatio':
				# 	self.state.netStableFundingRatio = float(parameter['value'])
				# if parameter['type']=='leverageRatio':
				# 	self.state.leverageRatio = float(parameter['value'])

		#
		# at this point we have all the variables from the parameters[] list
		# now we need to update them to incorporate past defaults to calculate
		# new return and volatility for real and financial assets
		# self.state.update_state(time)
        return self.state
	#--------------------------------------------

    # -------------------------------------------------------------------------
    # read_transactions_from_files(self,  bank_directory)
    # reads transactions for funds from the config files
    # -------------------------------------------------------------------------
    def allocate_fund_size(self, state, time):

        print state.global_assets_under_management

        self.num_funds = num_funds



    def read_transactions_for_funds(self,  bank_directory):
        from xml.etree import ElementTree
        # we list all the files in the specified directory
        listing = os.listdir(bank_directory)
        # and check if the number of files is in line with the parameters
        if (len(listing) != self.num_funds):
            logging.error("    ERROR: number of configuration files in %s (=%s) does not match num_funds (=%s)",
                          bank_directory,  str(len(listing)), str(self.num_funds))
        # we read the files sequentially)
        for infile in listing:
            # we open the file and find the identifier of the config
            xmlText = open(bank_directory + infile).read()
            element = ElementTree.XML(xmlText)
            identifier = element.attrib['identifier']
            # and we find the bank with this identifier
            bank = self.get_agent_by_id(identifier)
            # then we read the transactions from the config to the appropriate bank
            bank.get_transactions_from_file(bank_directory + infile, self)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # read_transactions_for_firms
    # reads transactions for firms from the config files
    # -------------------------------------------------------------------------
    def read_transactions_for_firms(self,  firm_directory):
        from xml.etree import ElementTree
        # we list all the files in the specified directory
        listing = os.listdir(firm_directory)
        # and check if the number of files is in line with the parameters
        if (len(listing) != self.num_firms):
            logging.error("    ERROR: number of configuration files in %s (=%s) does not match num_firms (=%s)",
                          firm_directory,  str(len(listing)), str(self.num_firms))
        # we read the files sequentially
        for infile in listing:
            # we open the file and find the identifier of the config
            xmlText = open(firm_directory + infile).read()
            element = ElementTree.XML(xmlText)
            identifier = element.attrib['identifier']
            # and we find the firm with this identifier
            firm = self.get_agent_by_id(identifier)
            # then we read the transactions from the config to the appropriate firm
            firm.get_transactions_from_file(firm_directory + infile, self)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # check_global_transaction_balance
    # checks if transaction type (ie 'deposits') balances out globally
    # I suppose this should presumably be used in the Updater after every
    # step to ensure consistency, along with appropriately using the
    # check_consistency function, and appropriately synchronising the update
    # itself
    # -------------------------------------------------------------------------
    def check_global_transaction_balance(self, type_):
        super(Environment, self).check_global_transaction_balance(type_)
    # -------------------------------------------------------------------------
