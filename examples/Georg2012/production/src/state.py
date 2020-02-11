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


#------------------------------------------------------------------------------
#  class State
#------------------------------------------------------------------------------
class State(object):
	#
	# VARIABLES
	#
	# parameters determining the cash flow of banks
	rb = 0.0 # interbank interest rate
	rd = 0.0 # interest rate on deposits
	# parameters for the central bank
	collateralQuality = 0.0 # the fraction of a bank's portfolio that the central bank accepts as collateral
	# firm parameters
	successProbabilityFirms = 0.0 # probability of successful credit
	positiveReturnFirms = 0.0 # return for a successful credit
	firmLoanMaturity = 0.0 # maturity of loans to firms
	#household parameters
	scaleFactorHouseholds = 0.0 # scaling factor for deposit fluctuations
	# bank parameters
	dividendLevel = 0.0 # dividend level as paid out by banks
	pBank = 0.0 # bank's assumed credit success probability
	rhoBank = 0.0 # expected return of banks
	pFinancial = 0.0 # bank's assumed credit success probability
	rhoFinancial = 0.0 # expected return of banks
	thetaBank = 0.0 # bank's risk aversion parameter
	xiBank = 0.0 # scaling factor for CRRA
	gammaBank = 0.0 # fraction of interbank lending in overall balance sheet
	assetNumber = 0 # number of assets in the economy
	interbankLoanMaturity = 0.0 # the maturity of interbank loans
	# simulation specific parameters
	shockType = 0 # type of shock that hits the system in the current state
	liquidationDiscountFactor =0.0 # the discount factor delta in exp(-delta x) when liquidating assets
	riskAversionDiscountFactor = 0.0 # the risk aversion discount when there was no default in the previous period
	riskAversionAmplificationFactor = 0.0 # the risk aversion amplification when there *was* a default in the previous or current period
	# regulation specific parameters
	r = 0.0 # minimum required deposit rate
	sifiSurchargeFactor = 1.0 # the surcharge on banking capital that SIFIs have to hold
	liquidityCoverageRatio = 0.0 # the fraction of assets that must have a high liquidation value
	netStableFundingRatio = 0.0 # the fraction of deposits that must have low volatility
	leverageRatio = 0.0 # the minimal ratio of banking capital to total assets
	requiredCapitalRatio = 0.08 # the required capital ratio for banks
	
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
		text += "  <!-- parameters determining the payment flow of banks -->\n"
		text += "  <parameter type='changing' name='rb' value='" + str(self.rb) + "'></parameter>\n"
		text += "  <parameter type='changing' name='rd' value='" + str(self.rd) + "'></parameter>\n"
		text += "  <!-- parameters for the central bank -->\n"
		text += "  <parameter type='changing' name='collateralQuality' value='" + str(self.collateralQuality) + "'></parameter>\n"
		text += "  <!-- firm parameters-->\n"
		text += "  <parameter type='changing' name='successProbabilityFirms' value='" + str(self.successProbabilityFirms) + "'></parameter>\n"
		text += "  <parameter type='changing' name='positiveReturnFirms' value='" + str(self.positiveReturnFirms) + "'></parameter>\n"
		text += "  <parameter type='changing' name='firmLoanMaturity' value='" + str(self.firmLoanMaturity) + "'></parameter>\n"
		text += "  <!-- household parameters -->\n"
		text += "  <parameter type='changing' name='scaleFactorHouseholds' value='" + str(self.scaleFactorHouseholds) + "'></parameter>\n"
		text += "  <!-- bank parameters -->\n"
		text += "  <parameter type='changing' name='dividendLevel' value='" + str(self.dividendLevel) + "'></parameter>\n"
		text += "  <parameter type='changing' name='pBank' value='" + str(self.pBank) + "'></parameter>\n"
		text += "  <parameter type='changing' name='rhoBank' value='" + str(self.rhoBank) + "'></parameter>\n"
		text += "  <parameter type='changing' name='pFinancial' value='" + str(self.pFinancial) + "'></parameter>\n"
		text += "  <parameter type='changing' name='rhoFinancial' value='" + str(self.rhoFinancial) + "'></parameter>\n"
		text += "  <parameter type='changing' name='thetaBank' value='" + str(self.thetaBank) + "'></parameter>\n"
		text += "  <parameter type='changing' name='xiBank' value='" + str(self.xiBank) + "'></parameter>\n"
		text += "  <parameter type='changing' name='gammaBank' value='" + str(self.gammaBank) + "'></parameter>\n"
		text += "  <parameter type='changing' name='assetNumber' value='" + str(self.assetNumber) + "'></parameter>\n"
		text += "  <!-- simulation specific parameters -->\n"
		text += "  <parameter type='changing' name='shockType' value='" + str(self.shockType) + "'></parameter>\n"
		text += "  <parameter type='changing' name='liquidationDiscountFactor' value='" + str(self.liquidationDiscountFactor) + "'></parameter>\n"
		text += "  <parameter type='changing' name='riskAversionDiscountFactor' value='" + str(self.riskAversionDiscountFactor) + "'></parameter>\n"
		text += "  <parameter type='changing' name='riskAversionAmplificationFactor' value='" + str(self.riskAversionAmplificationFactor) + "'></parameter>\n"
		text += "  <!-- regulation specific parameters -->\n"
		text += "  <parameter type='changing' name='r' value='" + str(self.r) + "'></parameter>\n"
		text += "  <parameter type='changing' name='sifiSurchargeFactor' value='" + str(self.sifiSurchargeFactor) + "'></parameter>\n"
		text += "  <parameter type='changing' name='liquidityCoverageRatio' value='" + str(self.liquidityCoverageRatio) + "'></parameter>\n"
		text += "  <parameter type='changing' name='netStableFundingRatio' value='" + str(self.netStableFundingRatio) + "'></parameter>\n"
		text += "  <parameter type='changing' name='leverageRatio' value='" + str(self.leverageRatio) + "'></parameter>\n"
		text += "  <parameter type='changing' name='requiredCapitalRatio' value='" + str(self.requiredCapitalRatio) + "'></parameter>\n"
		text += "  <!-- bookkeeping parameters -->\n"
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
		print "rb: " + str(self.rb)
		print "rd: " + str(self.rd)
		print "r: " + str(self.r)
		print "sifiSurchargeFactor: " + str(self.sifiSurchargeFactor)
		print "successProbabilityFirms: " + str(self.successProbabilityFirms)
		print "positiveReturnFirms: " + str(self.positiveReturnFirms)
		print "scaleFactorHouseholds: " + str(self.scaleFactorHouseholds)
		print "dividendLevel: " + str(self.dividendLevel)
		print "shockType: " + str(self.shockType)
		print "pBank: " + str(self.pBank)
		print "xiBank: " + str(self.xiBank)
		print "thetaBank: " + str(self.thetaBank)
		print "rhoBank: " + str(self.rhoBank)
		print "gammaBank: " + str(self.gammaBank)
		print "assetNumber: " + str(self.assetNumber)
		print "liquidationDiscountFactor: " + str(self.liquidationDiscountFactor)
		print "interbankLoanMaturity: " + str(self.interbankLoanMaturity)
		print "firmLoanMaturity: " + str(self.firmLoanMaturity)
		print "requiredCapitalRatio: " + str(self.requiredCapitalRatio)
		print "liquidityCoverageRatio: " + str(self.liquidityCoverageRatio)
		print "netStableFundingRatio: " + str(self.netStableFundingRatio)
		print "leverageRatio: " + str(self.leverageRatio)
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
		
