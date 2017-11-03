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

#-------------------------------------------------------------------------
#
#  class Parameters
#
#-------------------------------------------------------------------------
class Parameters(object):
	#
	# VARIABLES
	#
	# simulation specific parameters that will never change during the simulation
	identifier = ""
	numSimulations = 0
	numSweeps = 0
	numBanks = 0
	bankDirectory = ""
	# parameters for the networks
	graphType = ""
	graphParameter1 = 0.0
	graphParameter2 = 0.0
	contractsNetworkFile = ""
	# the array of parameters that changes during the simulation
	parameters = [] # this contains all parameters for all times with one parameter per validity
	
	#
	# METHODS
	#
	#-------------------------------------------------------------------------
	# __init__(self)
	#-------------------------------------------------------------------------
	def __init__(self):
		pass
	#-------------------------------------------------------------------------

	#-------------------------------------------------------------------------
	# print_parameters(self)
	#-------------------------------------------------------------------------
	def print_parameters(self):
		print "identifier: " + self.identifier
		print "numSweeps: " + str(self.numSweeps)
		print "numSimulations: " + str(self.numSimulations)
		print "numBanks: " + str(self.numBanks)
		print "graphType: " + str(self.graphType)
		for entry in self.parameters:
			print str(entry['type']) + " ; " + str(entry['value']) + " ; " + str(entry['validity'][0]) + "-" + str(entry['validity'][1])
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# add_parameter(self, type, value, validFrom, validTo)
	#-------------------------------------------------------------------------
	def add_parameter(self,  type,  value,  validFrom,  validTo):
		parameter = {'type': "",  'value': 0.0,  'validity': []} 
		parameter['type'] = type
		parameter['value'] = value
		parameter['validity'].append(validFrom)
		parameter['validity'].append(validTo)
		# add the parameter to the stack of parameters
		self.parameters.append(parameter)
	#-------------------------------------------------------------------------
