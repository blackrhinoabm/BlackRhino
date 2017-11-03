#!/usr/bin/env python
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
import networkx as nx

#-------------------------------------------------------------------------
#
#  class Environment
#
#-------------------------------------------------------------------------
class Environment(object):
	from state import State
	from parameters import Parameters
	from network import Network

	#
	# VARIABLES
	#
	identifier = ""
	
	parameters = Parameters()
	state = State()
	banks = []
	network = Network("")

	#
	# METHODS
	#
	#-------------------------------------------------------------------------
	# __init__
	#-------------------------------------------------------------------------
	def __init__(self):
		pass


	#-------------------------------------------------------------------------
	# initialize
	#-------------------------------------------------------------------------
	def initialize(self,  environment_directory,  identifier):
		self.identifier = identifier
		# first, read in the environment file
		environment_filename = environment_directory + identifier + ".xml"
		self.read_environment_file(environment_filename)
		logging.info("  environment file read: %s",  environment_filename)
		
		# then read in all the banks
		if (self.parameters.bankDirectory  != ""):
			if (self.parameters.bankDirectory != "none"): # none is used for tests only
				self.initialize_banks_from_files(self.parameters.bankDirectory,  self.get_state(0), 0)
				logging.info("  banks read from directory: %s",  self.parameters.bankDirectory)
		else: 
			logging.error("ERROR: no bankDirectory given in %s\n",  environment_filename)
		
		self.initial_assets = 0.0 # the initial assets are needed to determine the fire-sale price in bank.liquidate_assets
		for bank in self.banks:
			self.initial_assets += bank.get_account("I")
		
		# finally, create the network
		# note: this has to be done after creating the banks, as they are
		# passed to the network as node objects
		self.network.identifier = self.identifier
		self.network.initialize_networks(self)
		
		# when there is a SIFI surcharge, implement it now on the banking capital
		self.apply_sifi_surcharge()
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# read_environment_file
	#-------------------------------------------------------------------------
	def read_environment_file(self,  environmentFilename):
		from xml.etree import ElementTree
		xmlText = open(environmentFilename).read()
		
		element = ElementTree.XML(xmlText)
		self.identifier = element.attrib['title']
		
		self.parameters.identifier = self.identifier
		
		# loop over all entries in the xml file
		for subelement in element:
			# the first set of parameters will be valid for the whole simulation
			if (subelement.attrib['type'] == 'numSweeps'):
				self.parameters.numSweeps = int(subelement.attrib['value'])
			if (subelement.attrib['type'] == 'numSimulations'):
				self.parameters.numSimulations = int(subelement.attrib['value'])
			if (subelement.attrib['type'] == 'numBanks'):
				self.parameters.numBanks = int(subelement.attrib['value'])
			if (subelement.attrib['type'] == 'bankDirectory'):
				self.parameters.bankDirectory = str(subelement.attrib['value'])
			if (subelement.attrib['type'] == 'graphType'): 
				self.parameters.graphType = str(subelement.attrib['value'])
			if (subelement.attrib['type'] == 'graphParameter1'): 
				self.parameters.graphParameter1 = float(subelement.attrib['value'])
			if (subelement.attrib['type'] == 'graphParameter2'): 
				self.parameters.graphParameter2 = float(subelement.attrib['value'])
			if (subelement.attrib['type'] == 'contractsNetworkFile'): 
				self.parameters.contractsNetworkFile = str(subelement.attrib['value'])
			# now also read in the parameters that can change during the simulation
			if (subelement.attrib['type'] == 'changing'):
				name = subelement.attrib['name']
				value = float(subelement.attrib['value'])
				validFrom = subelement.attrib['validity'].rsplit("-")[0]
				validTo = subelement.attrib['validity'].rsplit("-")[1]
				self.parameters.add_parameter(name,  value,  validFrom, validTo)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# write_environment_file(file_name)
	#-------------------------------------------------------------------------
	def write_environment_file(self,  file_name):
		out_file = open(file_name + "-check.xml",  'w')
		
		text = "<environment title='" + self.identifier + "'>\n"
		text += "    <parameter type='numSweeps' value='" + str(self.parameters.numSweeps) + "'></parameter>\n"
		text += "    <parameter type='numSimulations' value='" + str(self.parameters.numSimulations) + "'></parameter>\n"
		text += "    <parameter type='numBanks' value='" + str(self.parameters.numBanks) + "'></parameter>\n"
		text += "    <parameter type='bankDirectory' value='" + str(self.parameters.bankDirectory) + "'></parameter>\n"
		text += "    <parameter type='graphType' value='" + str(self.parameters.graphType) + "'></parameter>\n"        
		text += "    <parameter type='contractsNetworkFile' value='" + str(self.parameters.contractsNetworkFile) + "'></parameter>\n" 
		
		for entry in self.parameters.parameters:
			text += "    <parameter type='changing' name='" +  str(entry['type']) + "' value='" + str(entry['value']) + "' validity='" + str(entry['validity'][0]) + "-" + str(entry['validity'][1]) + "'></parameter>\n"
		
		text += "</environment>\n"    
		
		out_file.write(text)
		out_file.close()
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# initialize_banks_from_files
	# banks have to be initialized for each simulation as a number of banks might become inactive
	# in the previous simulation
	#-------------------------------------------------------------------------
	def initialize_banks_from_files(self,  bankDirectory, state,  time):
		from bank import Bank
		# this routine is called more than once, so we have to reset the list of banks each time
		self.banks = []

		listing = os.listdir(bankDirectory)
		if (len(listing) != self.parameters.numBanks):
			logging.error("    ERROR: number of configuration files in %s (=%s) does not match numBanks (=%s)",  bankDirectory,  str(len(listing)), str(self.parameters.numBanks))
		
		for infile in listing:
			bank = Bank()
			bank.get_parameters_from_file(bankDirectory + infile,  self.get_state(0),  self.parameters.numBanks, time)
			self.banks.append(bank)
			bank.__del__() # TODO not sure if this is really safe, but it is better than doing nothing about all those created instances...
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# get_state
	#-------------------------------------------------------------------------
	def get_state(self,  time): # TODO bring parameters in same order as in environment file and in state.__str__()
		# for each time t in the simulation return the actual set of parameters
		for parameter in self.parameters.parameters:
			validFrom = int(parameter['validity'][0])
			validTo = int(parameter['validity'][1])
			if (int(time) >= int(validFrom)) and (int(time) <= int(validTo)): # we have a valid parameterset
				if parameter['type']=='rb':
					self.state.rb = float(parameter['value'])
				if parameter['type']=='rd':
					self.state.rd = float(parameter['value'])
				if parameter['type']=='r':
					self.state.r = float(parameter['value'])
				if parameter['type']=='collateralQuality':
					self.state.collateralQuality = float(parameter['value'])
				if parameter['type']=='successProbabilityFirms':
					self.state.successProbabilityFirms = float(parameter['value'])
				if parameter['type']=='positiveReturnFirms':
					self.state.positiveReturnFirms = float(parameter['value'])
				if parameter['type']=='scaleFactorHouseholds':
					self.state.scaleFactorHouseholds = float(parameter['value'])
				if parameter['type']=='dividendLevel':
					self.state.dividendLevel = float(parameter['value'])
				if parameter['type']=='pFinancial':
					self.state.pFinancial = float(parameter['value'])
				if parameter['type']=='rhoFinancial':
					self.state.rhoFinancial = float(parameter['value'])
				if parameter['type']=='pReal':
					self.state.pReal = float(parameter['value'])
				if parameter['type']=='rhoReal':
					self.state.rhoReal = float(parameter['value'])
				if parameter['type']=='xiBank':
					self.state.xiBank = float(parameter['value'])
				if parameter['type']=='thetaBank':
					self.state.thetaBank = float(parameter['value'])
				if parameter['type']=='rhoBank':
					self.state.rhoBank = float(parameter['value'])
				if parameter['type']=='shockType':
					self.state.shockType = int(parameter['value'])
				if parameter['type']=='gammaBank':
					self.state.gammaBank = float(parameter['value'])
				if parameter['type']=='assetNumber':
					self.state.assetNumber=float(parameter['value'])
				if parameter['type']=='liquidationDiscountFactor':
					self.state.liquidationDiscountFactor = float(parameter['value'])
				if parameter['type']=='riskAversionDiscountFactor':
					self.state.riskAversionDiscountFactor = float(parameter['value'])
				if parameter['type']=='riskAversionAmplificationFactor':
					self.state.riskAversionAmplificationFactor = float(parameter['value'])
				if parameter['type']=='interbankLoanMaturity':
					self.state.interbankLoanMaturity = float(parameter['value'])
				if parameter['type']=='firmLoanMaturity':
					self.state.firmLoanMaturity = float(parameter['value'])
				if parameter['type']=='sifiSurchargeFactor':
					self.state.sifiSurchargeFactor = float(parameter['value'])
				if parameter['type']=='requiredCapitalRatio':
					self.state.requiredCapitalRatio = float(parameter['value'])
				if parameter['type']=='liquidityCoverageRatio':
					self.state.liquidityCoverageRatio = float(parameter['value'])
				if parameter['type']=='netStableFundingRatio':
					self.state.netStableFundingRatio = float(parameter['value'])
				if parameter['type']=='leverageRatio':
					self.state.leverageRatio = float(parameter['value'])
		
		#
		# at this point we have all the variables from the parameters[] list
		# now we need to update them to incorporate past defaults to calculate 
		# new return and volatility for real and financial assets
		self.state.update_state(time)
		
		return self.state
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# apply_sifi_surcharge
	#-------------------------------------------------------------------------
	def apply_sifi_surcharge(self):
		degree_sum = 0
		for bank in self.network.contracts:
			degree_sum += float(nx.degree(self.network.contracts)[bank])
		average_degree = float(degree_sum / len(self.network.contracts.nodes()))
		
		for bank in self.network.contracts:
			# the sifi surcharge is the product of the sifiSurchargeFactor and the connectedness as measured
			# by degree/average_degree 
			# the maximum ensures that no bank has to hold less than 1.0 times their banking capital
			sifiSurcharge = max(self.get_state(0).sifiSurchargeFactor*( float(nx.degree(self.network.contracts)[bank]) / average_degree), 1.0)
			bank.apply_sifi_surcharge(sifiSurcharge)
	#-------------------------------------------------------------------------
