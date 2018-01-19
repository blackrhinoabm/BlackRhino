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


#------------------------------------------------------------------------------
#  class State
#------------------------------------------------------------------------------
class State(object):
	#
	# VARIABLES
	#
	# parameters determining the cash flow of banks
	global_assets_under_management = 0
	num_agents= 0

	scaleFactorHouseholds = 0.0 # scaling factor for deposit fluctuations

	assetNumber = 0 # number of assets in the economy

	riskAversionAmplificationFactor = 0.0 # the risk aversion amplification when there *was* a default in the previous or current period
	# regulation specific parameters


	# bookkeeping parameters
	insolvencyHistory= [] # [num, time] the number of bank insolvencies and when they occured

	#
	# METHODS
	#
	def __init__(self):
		pass


	#-------------------------------------------------------------------------
	# __str__
	#-------------------------------------------------------------------------
	def __str__(self):
		text =   "<state>\n"
		text += "  <parameter type='variable' name='global_assets_under_management' value='" + str(self.global_assets_under_management) + "'></parameter>\n"
		text += "  <parameter type='variable' name='num_agents' value='" + str(self.num_agents) + "'></parameter>\n"

		text += "  <parameter type='changing' name='scaleFactorHouseholds' value='" + str(self.scaleFactorHouseholds) + "'></parameter>\n"

		text += "  <parameter type='changing' name='assetNumber' value='" + str(self.assetNumber) + "'></parameter>\n"

		text += "  <parameter type='changing' name='riskAversionDiscountFactor' value='" + str(self.riskAversionDiscountFactor) + "'></parameter>\n"

		# find the number of total insolvencies
		numberInsolvencies = 0
		for entry in self.insolvencyHistory:
			numberInsolvencies += entry[0]
		text += "  <variable name='numberInsolvencies' value='" + str(numberInsolvencies) + "'></variable>\n"
		text += "</state>\n"

		return text
	#------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# print_state
	#-------------------------------------------------------------------------
	def print_state(self):
		print "global_assets_under_management: " + str(self.global_assets_under_management)
		print "assetNumber: " + str(self.assetNumber)
		print "	scaleFactorHouseholds: " + str(self.scaleFactorHouseholds)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# addInsolvencyToHistory(time)
	#-------------------------------------------------------------------------
	def addInsolvencyToHistory(self, time):
		lastInsolvency = [0, -1] # if we have no insolvency yet
		for insolvency in self.insolvencyHistory: # loop over the insolvencyHistory
			if insolvency[1] == time: # to see if we have an insolvency in this time period
				lastInsolvency = insolvency # if we do, update lastInsolvency

		if lastInsolvency[1] > -1: # see if we found an insolvency in this time step
			lastInsolvency[0] += 1 # add one to the number of insolvencies
		else: # there has not been an insolvency yet, so add one
			self.insolvencyHistory.append([1, time])
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# update_state(time)
	# this method calculates the new expected returns for real and
	# financial assets
	#-------------------------------------------------------------------------
	def update_state(self,  time):
		#
		# real assets have an expected return as given in the environment file
		#
		pReal = self.pBank # TODO change pBank to pReal everywhere in code
		rhoReal = self.rhoBank # TODO change rhoBank to rhoReal everywhere in code
		# TODO: now one could make the process for real assets a bit more interesting
		self.pBank = pReal
		self.rhoBank = rhoReal

		# financial assets start with some initial expected return and mean
		# then they are updated when the simulation proceeds and become
		# more volatile when more banks go into insolvency
		pFinancial = self.pFinancial
		rhoFinancial = self.rhoFinancial
		# TODO now we could make something interesting
		self.pFinancial = pFinancial
		self.rhoFinancial = rhoFinancial
