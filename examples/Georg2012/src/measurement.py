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

# ============================================================================
#
# class Measurement
#
# ============================================================================
class Measurement(object):
	#
	# VARIABLES
	#
	activeBanks = []
	I = []
	D = []
	L = []
	LC = []
	
	histoActiveBanks = []
	histoI = []
	histoD = []
	histoL = []
	histoLC = []
	
	
	# 
	# METHODS
	#
	#-------------------------------------------------------------------------
	#
	#-------------------------------------------------------------------------
	def __init__(self):
		logging.info("  measurement started...")
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# def initialize
	#-------------------------------------------------------------------------
	def initialize(self):
		self.activeBanks = []
		self.I = []
		self.D = []
		self.L = []
		self.LC = []
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# def do_measurement()
	#-------------------------------------------------------------------------
	def do_measurement(self,  banks):
		sumActiveBanks = 0
		sumI = 0.0
		sumD = 0.0
		sumL = 0.0
		sumLC = 0.0
		
		for bank in banks:
			# first, check if the bank is active
			if (bank.active >= 0.0):
				sumActiveBanks = sumActiveBanks + 1
				# then, get the different balance sheet items
				sumI = sumI + bank.get_account("I")
				sumD = sumD + bank.get_account("D")
				sumL = sumL + bank.get_account("L")
				sumLC = sumLC + bank.get_account("LC")
		
		self.activeBanks.append(sumActiveBanks)
		self.I.append(sumI)
		self.D.append(sumD)
		self.L.append(sumL)
		self.LC.append(sumLC)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# def do_histograms()
	#-------------------------------------------------------------------------
	def do_histograms(self):
		self.histoActiveBanks.append(self.activeBanks)
		self.histoI.append(self.I)
		self.histoD.append(self.D)
		self.histoL.append(self.L)
		self.histoLC.append(self.LC)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# def write_histograms()
	#-------------------------------------------------------------------------
	def write_histograms(self, baselineDirectory,  environment):
		# first, construct the file name for the parameter set
		baseFileName = baselineDirectory + environment.parameters.identifier
		
		# then, write the different histograms
		fileName = baseFileName + "-histoActiveBanks.dat"
		self.write_histogram(self.histoActiveBanks,  fileName)
		fileName = baseFileName + "-histoI.dat"
		self.write_histogram(self.histoI,  fileName)
		fileName = baseFileName + "-histoD.dat"
		self.write_histogram(self.histoD,  fileName)
		fileName = baseFileName + "-histoL.dat"
		self.write_histogram(self.histoL,  fileName)
		fileName = baseFileName + "-histoLC.dat"
		self.write_histogram(self.histoLC,  fileName)
		
		logging.info("  ....measurement finished")
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# def write_histogram()
	#-------------------------------------------------------------------------
	def  write_histogram(self,  histogram,  fileName):
		file = open(fileName,  "w")
		for line in histogram:
			for entry in line:
				file.write(str(round(float(entry), 4)) + " ")
			file.write("\n")
		file.close()
	#-------------------------------------------------------------------------
