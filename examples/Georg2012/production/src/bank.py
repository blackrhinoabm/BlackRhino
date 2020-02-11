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
import math

# ============================================================================
#
# class Bank
#
# ============================================================================
class Bank(object):
#
#
# VARIABLES
#
#
	identifier = ""
	V = 0.0 # planned optimal portfolio volume of the bank
	lamb = 0.0 # planned optimal portfolio structure of the bank
	rb = 0.0 # refinancing costs of the bank -> tbd in environment
	rd = 0.0 # interest rate on deposits
	r = 0.0 # required reserve rate -> tbd in environment
	pReal = 0.0 # probability of credit success
	rhoReal = 0.0 # interest charged on risky investment
	pFinancial = 0.0 # probability of interbank loan success
	rhoFinancial = 0.0 # variance of interbank loan success
	xi = 0.0 # scaling parameter in CRRA
	theta = 0.0 # risk aversion parameter of bank
	gamma = 0.0 # fraction of interbank loans in overall volume
	assetNumber = 0 # number of assets available to bank
	numBanks = 0 # number of banks in the economy
	accounts = [] # all accounts of a bank
	Q = 0.0 # the current liquidity position of the bank
	Ip = 0.0 # the planned optimal investment
	Ep = 0.0 # the planned excess reserves
	Lp = 0.0 # the planned interbank loans; L > 0: excess supply of interbank liquidity
	
	# keep track whether a bank is active or not. This variable is necessary since it is not good
	# to remove inactive banks from banks[] while looping through them...
	active = 0 
	# filled during initialize_transactions() and equal to the size of an initial transaction
	# keeping track will ensure that later transactions are not larger than average
	averageTransactionSize = 0.0 


#
#
# CODE
#
#

	#-------------------------------------------------------------------------
	# functions needed to make Bank() hashable
	#-------------------------------------------------------------------------
	def __key(self):
		return self.identifier

	def __eq__(self, other):
		return self.__key() == other.__key()

	def __hash__(self):
		return hash(self.__key())
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# __init__
	#-------------------------------------------------------------------------
	def __init__(self):
		self.accounts=[] # clear transactions when bank is initialized
		self.Q = 0.0 # bank liquidity is reset
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# __del__
	#-------------------------------------------------------------------------
	def __del__(self):
		pass
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# __str__
	#-------------------------------------------------------------------------
	def __str__(self):
		text =   "<bank identifier='" + self.identifier + "'>\n"
		text += "    <value name='active' value='" + str(self.active) + "'></value>\n"
		text += "    <parameter type='changing' name='pReal' value='" + str(self.pReal) + "'></parameter>\n"
		text += "    <parameter type='changing' name='rhoReal' value='" + str(self.rhoReal) + "'></parameter>\n"
		text += "    <parameter type='changing' name='pFinancial' value='" + str(self.pFinancial) + "'></parameter>\n"
		text += "    <parameter type='changing' name='rhoFinancial' value='" + str(self.rhoFinancial) + "'></parameter>\n"
		text += "    <parameter type='changing' name='thetaBank' value='" + str(self.theta) + "'></parameter>\n"
		text += "    <parameter type='changing' name='xiBank' value='" + str(self.xi) + "'></parameter>\n"
		text += "    <parameter type='changing' name='gammaBank' value='" + str(self.gamma) + "'></parameter>\n"
		text += "    <transactions>\n"
		for transaction in self.accounts:
			text += transaction.write_transaction()
		text += "    </transactions>\n"
		text += "    <value name='Q' value='" + str(self.Q) + "'></value>\n"
		text += "    <value name='Lp' value='" + str(self.Lp) + "'></value>\n"
		text += "</bank>\n"
		
		return text
	#------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# get_parameters_from_file
	#-------------------------------------------------------------------------
	def get_parameters_from_file(self,  bankFilename, state,  numBanks,  time):
		from xml.etree import ElementTree
		
		try:
			xmlText = open(bankFilename).read()
			element = ElementTree.XML(xmlText)
			self.identifier = element.attrib['identifier']
			
			self.rb = state.rb
			self.r = state.r
			self.rd = state.rd
			self.assetNumber = state.assetNumber
			self.numBanks = numBanks
		
			# loop over all entries in the xml file
			for subelement in element:
				if (subelement.attrib['type'] == 'changing'):
					name = subelement.attrib['name']
					value = subelement.attrib['value']
					validFrom = subelement.attrib['validity'].rsplit("-")[0]
					validTo = subelement.attrib['validity'].rsplit("-")[1]
					if (int(time) >= int(validFrom)) and (int(time) <= int(validTo)): # we have a valid parameterset
						if (name == 'xiBank'):
							self.xi = float(value)
						if (name == 'thetaBank'):
							self.theta = float(value)
						if (name == 'pReal'): # success probability of real assets TODO change stupid name
							self.pReal = float(value)
						if (name == 'rhoReal'): # return of real assets TODO change stupid name
							self.rhoReal = float(value)
						if (name == 'pFinancial'): # success probability of financial assets
							self.pFinancial = float(value)
						if (name == 'rhoFinancial'): # return of financial assets
							self.rhoFinancial = float(value)
						if (name == 'gammaBank'):
							self.gamma = float(value)

			# and finally, calculate optimal investment
			self.calculate_optimal_investment_volume(state)
			self.initialize_transactions(state)
		except:
			logging.error("    ERROR: %s could not be parsed",  bankFilename)
	#------------------------------------------------------------------------


	#------------------------------------------------------------------------
	# apply_sifi_surcharge
	#------------------------------------------------------------------------
	def apply_sifi_surcharge(self,  sifiSurchargeFactor):
		old_D = self.get_account("D")
		old_BC = self.get_account("BC")
		new_BC  = sifiSurchargeFactor*old_BC
		new_D = old_D - (new_BC - old_BC)
		
		#str(sifiSurchargeFactor) + " || " + str(old_D) + " -> " + str(new_D) + " | " + str(old_BC) + " -> " + str(new_BC)
		
		for transaction in self.accounts:
			if transaction.transactionType == "D": # reduce central bank liabilities
				transaction.transactionValue = new_D
			if transaction.transactionType == "BC": # and increase banking capital
				transaction.transactionValue = new_BC
	#------------------------------------------------------------------------


#
# ROUTINES CALLED IN UPDATER
#

	#-------------------------------------------------------------------------
	# update_maturity
	#-------------------------------------------------------------------------
	def update_maturity(self):
		for transaction in self.accounts:
			if (int(transaction.transactionMaturity) > 0): # reduce maturity if duration longer than 0
				transaction.transactionMaturity = int(transaction.transactionMaturity) - 1
				if ((transaction.transactionType == "I") and (int(transaction.transactionTimeOfDefault) > 0)):  # only investments have a time of default
					transaction.transactionTimeOfDefault = int(transaction.transactionTimeOfDefault) - 1
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# update_risk_aversion
	# this method checks if there was a default in the previous period
	#-------------------------------------------------------------------------
	def update_risk_aversion(self,  state,  time): 
		lastInsolvency = [0, -2] # dummy if we did not have any insolvency yet
		#-2 since we check time-1 later and in t=0 would run into problems
		
		# decrease risk aversion every time there was no default in the previous period
		# increase risk aversion if there was a default
		# find the number of total insolvencies
		numInsolvencies = 0
		for entry in state.insolvencyHistory:
			numInsolvencies += entry[0]
		
		if numInsolvencies > 0:
			lastInsolvency = state.insolvencyHistory.pop()
		
		# check if we had an insolvency in the last or current period
		if lastInsolvency[1] == (time - 1) or lastInsolvency[1] == time: 
			# if so, increase risk aversion
			self.theta = round(self.theta*(1.0 + state.riskAversionAmplificationFactor), 3) # we round to be on the safe side with float numbers
		else: # if not, decrease risk aversion
			self.theta = round(self.theta*(1.0 - state.riskAversionDiscountFactor), 3) # we round to be on the safe side with float numbers
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# get_interest
	#-------------------------------------------------------------------------
	def get_interest(self,  type):
		from random import Random
		
		random = Random()
		volume = 0.0 
		sign = 1.0 # will be negative if interest has to be paid by the bank
		
		for transaction in self.accounts:
			if (transaction.transactionType == type):
				if (transaction.transactionType == "I"): # check if we have an investment
					if (transaction.transactionTimeOfDefault == 0): # check if the investment defaulted
						transaction.transactionInterest = 0.0 # if the loan defaulted, it will pay no interest
						#
						# now we check what happens if a loan defaults
						#
						self.reduce_banking_capital(transaction.transactionValue) # reduce the banking capital if the loan defaults
				#
				#
				#
				if (transaction.transactionTo == self.identifier):
					volume = volume - float(transaction.transactionValue)*float(transaction.transactionInterest)
				else:
					volume = volume + float(transaction.transactionValue)*float(transaction.transactionInterest)
			
		return volume
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# liquidate_due_transactions
	#------------------------------------------------------------------------- 
	def liquidate_due_transactions(self,  type):
		volume = 0.0
		residual = []
		
		for transaction in self.accounts:
			if ((transaction.transactionType == type) and (int(transaction.transactionMaturity) == 0)):
				volume = volume + float(transaction.transactionValue)
			else: # if transaction is not matching, copy it to the residual list...
				residual.append(transaction)
		self.accounts = residual # ...and then make the residual list the accounts
		
		return round(volume, 4)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# def get_new_deposits(scaleFactor)
	# This method returns the NET flow of deposits, not the absolute value
	#-------------------------------------------------------------------------
	def get_new_deposits(self,  scaleFactor):
		from random import Random
		random = Random()
		oldValue = 0.0
		newValue = 0.0
		returnValue = 0.0
		
		for transaction in self.accounts:
			if (transaction.transactionType == "D"):
				oldValue = transaction.transactionValue # the old value
				newValue = max(round((1.0 - scaleFactor + 2.0*scaleFactor*random.random())*oldValue, 4), 0.0) # make sure we have only positive deposit levels
				transaction.transactionValue = newValue
			
		
		returnValue = round(newValue - oldValue, 4) # convention is that outflows are negative, this is the bank's viewpoint
		
		return returnValue
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# transfer_required_deposits
	#-------------------------------------------------------------------------
	def transfer_required_deposits(self):
		from transaction import Transaction
		
		transaction = Transaction()
		value = round(float(self.r*self.get_account("D")), 4)
		transaction.this_transaction("rD",  self.identifier,  -3,  value,  self.rb,  0,  -1)
		self.accounts.append(transaction)
		
		return  -1.0*value
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# reduce_banking_capital
	#-------------------------------------------------------------------------
	def reduce_banking_capital(self,  value):
		for transaction in self.accounts:
			if (transaction.transactionType == "BC"):
				transaction.transactionValue = max(0.0,  transaction.transactionValue - value)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# check_solvency
	#-------------------------------------------------------------------------
	def check_solvency(self,  state,  debug,  time):
		# variables needed to check solvency
		required_capital_ratio = state.requiredCapitalRatio 
		BC = self.get_account("BC")
		I = self.get_account("I")
				
		# here, the assumption is that banking capital has to account for 8%
		# of the risk weighted assets and that all risky assets have a risk-weight
		# of 1.0
		if ((self.active > -1 ) and (I > 0.0)):
			if (round(float(BC/I),4) < required_capital_ratio):
				self.active = -1
				# store in state.numberInsolvencies when we had an insolvency
				state.addInsolvencyToHistory(time)
				if (debug == "info" or debug == "debug"):
					try:
						capital_adequacy = BC/I
					except:
						capital_adequacy = 0.0
					logging.info("    time: %s: <bank %s is insolvent: %s < %s>",  time,  self.identifier,  capital_adequacy,  required_capital_ratio)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# check_liquidity
	#-------------------------------------------------------------------------
	def check_liquidity(self):
		# since illiquidity is different from insolvency, we need an additional 
		# liquidity check. if a bank is short on liquitiy after going to the interbank
		# market and the central bank, it has to sell off some of its assets in a possible fire-sale
		if (self.active > -1):
			if (self.Q < 0.0):
				self.active = -1
				#string = "Bank " + self.identifier + " is illiquid" + str(self.Q)
				#print helper.highlight(string,  "red")
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# calculate_liquidity_demand
	#
	# This function calculates the liquidity demand that has to be satisfied on either
	# the interbank market or by the central bank
	# Note: for Lp > 0 the bank has excess liquidity supply
	#-------------------------------------------------------------------------
	def calculate_liquidity_demand(self):
		# first, calculate the optimal investments
		self.Ip = round(float(self.gamma*(self.lamb)*self.V),  4)
		self.Ep = round(float(self.gamma*(1.0-self.lamb)*self.V),  4)
		#print str(self.Ip) + " " + str(self.Ep) + " " + str(self.get_account("I")) + " " + str(self.get_account("E"))
		# the liquidity demand is given by Q - ((Ip-I) + (Ep-E))
		self.Lp = self.Q - ( (self.Ip - self.get_account("I")) + (self.Ep -self.get_account("E")) )
		#print str(self.identifier)  + " " + str(self.Lp)
		self.Q = 0.0 # reduce Q, since all liquidity demand is now in the planned interbank liquidity
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# get_central_bank_liquidity(self, state)
	#-------------------------------------------------------------------------
	def get_central_bank_liquidity(self,  state):
		interest = state.rb
		maturity = 0
		timeOfDefault = -1
		
		# banks can obtain liquidity from the central bank if they have adequate collateral
		if (self.Lp < 0.0):
			# check how much central bank liquidity is available
			maxValue = state.collateralQuality * self.get_account("I")
			# calculate the actual transferred value
			value = min(maxValue, abs(self.Lp))
			# update the accounts to keep track of the loan
			self.add_transaction("LC",  -3,  self.identifier,  value,  interest,  maturity,  timeOfDefault)
			# and update the liquidity demand
			self.Lp = self.Lp + value
	#------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# liquidate_assets()
	#-------------------------------------------------------------------------
	def liquidate_assets(self,  initial_assets,  current_assets,  state,  debug,  time):
		# variables needed to calculate discounts
		liquidation_discount_factor = state.liquidationDiscountFactor
		required_capital_ratio = state.requiredCapitalRatio
		liquidated_assets = 0.0 # the amount of assets already liquidated by the bank in the current period
		
		if (self.Lp < 0.0): # we have a shortfall in liquidity
			current_I = self.get_account("I") # store the current amount of investments
			current_E = self.get_account("E") # store the current amount of excess reserves
			
			# when banks do not have liquidity, they will cut back their planned investment
			if (self.Ip > current_I):
				self.Ip -= current_I
				self.Lp += (self.Ip - current_I)
			if (self.Ep > current_E):
				self.Ep -= current_E
				self.Lp += (self.Ep - current_E)
			
			# if cutting back planned investment is not enough, the bank will have to sell assets
			if (self.Lp < 0.0):
				# the price for assets is determined by the total share of liquidated assets, including the planned liquidation volume
				liquidation_volume = min(-1.0*self.Lp, current_I)
				# the asset price will be low for high values of the liquidation_discount_factor and large amounts of liquidated assets
				liquidation_price = round(float(math.exp(  -liquidation_discount_factor*( (initial_assets - current_assets + liquidation_volume)/(initial_assets) )  )),  4)
				# now loop over all investments and liquidate as many as necessary
				for transaction in self.accounts:
					if (transaction.transactionType == "I") and (liquidated_assets < liquidation_volume) and (transaction.transactionValue > 0.0):
						liquidated_assets += transaction.transactionValue
						self.Lp += liquidation_price*transaction.transactionValue # we get liquidity for our assets
						self.reduce_banking_capital( (1.0 - liquidation_price) * transaction.transactionValue ) # but suffer a loss from costly liquidation
						transaction.transactionValue = 0.0
						# check if we are still alive
						self.check_solvency(state,  debug,  time) # note that this has to be done before purge_accounts (afterwards, I=0)
				
		# once we are done, purge the assets that have been sold from the accounts
		self.purge_accounts()
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# transfer_investments
	#-------------------------------------------------------------------------
	def transfer_investments(self,  state):
		from random import Random
		from transaction import Transaction
		
		random = Random()
		
		currentVolume = 0.0
		optimalVolume = 0.0
		plannedVolume = 0.0
		availableVolume = 0.0
		transactionVolume = 0.0
		transaction = Transaction()

		# calculate the optimal investment volume and compare to current volume
		self.calculate_optimal_investment_volume(state)
		optimalVolume = round(float(self.gamma*self.lamb*self.V), 4)
		currentVolume = round(self.get_account("I"), 4)
		# add new transactions of average size
		plannedVolume = currentVolume + optimalVolume
		availableVolume = self.lamb*self.Q # we can only spend a fraction of the available Q
		transactionVolume = min(plannedVolume,  availableVolume)
		
		while ((transactionVolume >= self.averageTransactionSize) and (self.averageTransactionSize > 0.0)):
			
			transactionVolume = round(transactionVolume - self.averageTransactionSize, 5) # reduce remaining transactionVolume
			self.Q = self.Q - self.averageTransactionSize # reduce available liquidity
			
			# account for different maturities of investments
			maturity = int(round(random.random()*state.firmLoanMaturity, 1)) # this is done very roughly and implies loans are up to 3 years
			
			# and determine whether the loan will default
			if (random.random() >= state.successProbabilityFirms):
				# the loan defaults: determine timeOfDefault
				timeOfDefault = int(round(random.random()*maturity))
			else:
				timeOfDefault = -1
			
			# and add transaction to the stack
			transaction = Transaction()
			transaction.this_transaction("I",  self.identifier, -2,  self.averageTransactionSize,  self.rhoReal,  maturity,  timeOfDefault)
			self.accounts.append(transaction)
			del transaction
		
		transactionVolume = round(transactionVolume, 5)
		# finally, add the remaining transaction to the stack if the transactionVolume was positive in the first place
		if (transactionVolume > 0.0):
			self.Q = round(self.Q - transactionVolume, 4)
			
			# account for different maturities of investments
			maturity = int(round(random.random()*state.firmLoanMaturity, 1)) # this is done very roughly and implies loans are up to 3 years
			
			# and determine whether the loan will default
			if (random.random() >= state.successProbabilityFirms):
				# the loan defaults: determine timeOfDefault
				timeOfDefault = int(round(random.random()*maturity))
			else:
				timeOfDefault = -1
			
			transaction = Transaction()
			transaction.this_transaction("I",  self.identifier, -2,  transactionVolume,  self.rhoReal,  maturity,  timeOfDefault)
			self.accounts.append(transaction)
			del transaction
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# transfer_excess_reserves
	#-------------------------------------------------------------------------
	def transfer_excess_reserves(self):
		from transaction import Transaction
		availableVolume = self.Q
		plannedVolume = self.gamma*(1.0-self.lamb)*self.V
		transactionVolume = round(min(plannedVolume,  availableVolume), 4)
		self.Q = round(self.Q - transactionVolume, 4)
		if (self.Q < 0.0):
			logging.info("ERROR: Q negative in transfer_excess_reserves")
		transaction = Transaction()
		transaction.this_transaction("E",  self.identifier, -3,  transactionVolume,  self.rb,  0,  -1)
		self.accounts.append(transaction)
		del transaction
	#-------------------------------------------------------------------------


#
# HELPER ROUTINES
#

	#-------------------------------------------------------------------------
	# calculate_optimal_investment_volume
	#-------------------------------------------------------------------------
	def calculate_optimal_investment_volume(self,  state): # TODO this is not a good name, better would be calculate_optimal_portfolio
		import math
		
		# TODO this is where we could update the p and rho for investments in the real economy
		# TODO in a more elaborate model, financial assets can be treated as another set of risky assets
		# learning can be done by checking the *actual* number of defaulted loans in the economy
		# we can also include memory effects when agents "forget" past defaults
		# for the interbank assets, life is even more interesting when agents now about recent defaults
		mu = self.pReal*self.rhoReal - (1.0 - self.pReal)
		sigma2 = self.pReal*(self.rhoReal - mu)*(self.rhoReal - mu) + (1-self.pReal)*((-1-mu)*(-1-mu))
		
		if (sigma2 > 0.0): # this test ensures there are no floating errors from division by zero
			# TODO here we have to impose regulatory measures on the portfolio structure in a VaR sense
			self.lamb= max(0.0,  min((mu/(self.theta*sigma2)), 1.0)) # lamb is the fraction of risky assets in the portfolio
			self.V = math.pow( self.xi*(1.0/self.rb)*pow( (1.0+self.lamb*mu-0.5*self.lamb*self.lamb*sigma2) , (1.0-self.theta) ), (1.0/self.theta) )
			#print [mu, sigma2, self.theta, mu/(self.theta*sigma2),  self.lamb,  self.V]
			
			# now apply the VaR on the portfolio volume
			leverage = self.get_account("BC")/self.V
			if (state.leverageRatio > leverage) and (leverage > 0.0):
				#logging.info("  leverageRatio binding") # TODO also log how much it is binding
				self.V = (1.0/state.leverageRatio)*self.get_account("BC")
		else: 
			print "WARNING: sigma2 <= 0.0; mu,sigma2=", mu,sigma2
			print self.pReal, self.rhoReal
			self.lamb = 0.0
			self.V = 0.0
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# initialize_transactions
	#-------------------------------------------------------------------------
	def initialize_transactions(self, state):
		from transaction import Transaction
		from random import Random
		random = Random()
		
		value = 0.0
		
		# first, calculate number of transactions for investments
		numTransactions = int(round(self.assetNumber / self.numBanks))
		if (numTransactions == 0): # we want some error message if there are two few assets in the economy
			logging.info("  ERROR: number of  assets in the economy has to be at least half the number of banks")
		# now, calculate value of each transaction and note that the *product* of all individual transactions
		# is supposed to have precision 4. Hence, each individual transaction should have precision 5

		value = round(float(self.gamma*self.lamb*self.V / numTransactions), 5)
		# finally, put them on the transaction stack
		for i in range(numTransactions):
			transaction = Transaction()
			# 
			# account for different maturities
			#
			maturity = int(round(random.random()*state.firmLoanMaturity, 1)) # maturity is between 0 and firmLoanMaturity
			# and determine whether the loan will default
			if (random.random() >= state.successProbabilityFirms): # TODO this is superfluous, we could get rid of this doubling
				# the loan defaults: determine timeOfDefault
				timeOfDefault = int(round(random.random()*maturity))
			else:
				timeOfDefault = -1
			# then, generate the transaction, append it to the accounts, and delete it from memory
			transaction.this_transaction("I",  self.identifier, -2,  value,  self.rhoReal,  maturity, timeOfDefault)
			self.accounts.append(transaction)
			del transaction
		# store averageTransactionSize
		self.averageTransactionSize = value
		
		# then, calculate excess reserves
		value = round(float(self.gamma*(1.0-self.lamb)*self.V),  4)
		transaction = Transaction()
		transaction.this_transaction("E",  self.identifier,  -3,  value,  self.rb,  0, -1)
		self.accounts.append(transaction)
		del transaction
		
		# on the liabilities side, banks are endowed with banking capital
		# (see comments in get_initial_banking_capital() for further details)
		value = round(float(self.get_initial_banking_capital(state.requiredCapitalRatio)), 4)
		transaction = Transaction()
		transaction.this_transaction("BC",  self.identifier,  self.identifier,  value,  0.0,  0, -1)
		self.accounts.append(transaction)
		del transaction
		
		# now, transfer deposits from households to banks
		value = round(float(self.gamma*self.V-self.get_account("BC")), 4)
		transaction = Transaction()
		transaction.this_transaction("D",  -1,  self.identifier,  value,  self.rd,  0, -1)
		self.accounts.append(transaction)
		del transaction
		
		# as well as required deposits to the central bank
		value = round(float(self.r*self.get_account("D")), 4)
		transaction = Transaction()
		transaction.this_transaction("rD",  self.identifier,  -3,  value,  self.rb,  0, -1)
		self.accounts.append(transaction)
		del transaction
		
		# finally, determine central bank loans
		value = round(float (self.get_account("I") + self.get_account("E") + self.get_account("rD") - self.get_account("D") - self.get_account("BC") ), 4)
		transaction = Transaction()
		transaction.this_transaction("LC",  self.identifier,  -3,  value,  self.rb,  0, -1)
		self.accounts.append(transaction)
		del transaction
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# get_initial_banking_capital
	#-------------------------------------------------------------------------
	def get_initial_banking_capital(self,  required_capital_ratio):
		value = 0.0
		# the assumption here is that banks' actual capital is larger than their regulatory
		# capital. for a motivation see Elizalde and Repullo (2007), IJCB
		# however, we do not care about the details (i.e. how much actual capital exceeds
		# regulatory capital) and just assume a fixed value for all banks
		value = 1.25*required_capital_ratio*self.get_account("I")
		
		return value
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# get_account
	#-------------------------------------------------------------------------
	def get_account(self,  type):
		volume = 0.0
		
		for transaction in self.accounts:
			if (transaction.transactionType == type):
				volume = volume + float(transaction.transactionValue)
		
		return volume
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# get_account_num_transactions
	#-------------------------------------------------------------------------
	def get_account_num_transactions(self,  type): # returns the number of transactions in a given account
		num_transactions = 0.0
		
		for transaction in self.accounts:
			if (transaction.transactionType == type):
				num_transactions += 1
		
		return num_transactions
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# add_transaction
	#-------------------------------------------------------------------------
	def add_transaction(self,  type,  fromID,  toID,  value,  interest,  maturity, timeOfDefault):
		from transaction import Transaction
		transaction = Transaction()
		transaction.this_transaction(type,  fromID,  toID,  value,  interest,  maturity,  timeOfDefault)
		self.accounts.append(transaction)
		del transaction
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# clear_accounts
	#-------------------------------------------------------------------------
	def clear_accounts(self):
		self.accounts = []
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# purge_accounts
	#-------------------------------------------------------------------------
	def purge_accounts(self):
		new_accounts = []
		
		for transaction in self.accounts:
			if transaction.transactionValue > 0.0:
				new_accounts.append(transaction)
		
		self.accounts = new_accounts
	#-------------------------------------------------------------------------


#
# ROUTINES THAT MAKE DEBUGGING EASIER
#
	#-------------------------------------------------------------------------
	# change_deposits(self, change)
	#-------------------------------------------------------------------------
	def change_deposits(self,  change):
		old_value = 0.0
		new_value = 0.0
		
		for transaction in self.accounts:
			if (transaction.transactionType == "D"):
				old_value = transaction.transactionValue # the old value
				new_value = old_value + change
				transaction.transactionValue = new_value
		
		return (old_value - new_value)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# initialize_standard_bank
	# 
	# this routine initializes a bank with a standard balance sheet,
	# which can be used to make the tests more handy
	#-------------------------------------------------------------------------
	def initialize_standard_bank(self):
		from transaction import Transaction
		
		self.identifier = "0" # identifier
		self.V = 250.0 # planned optimal portfolio volume of the bank
		self.lamb = 0.5 # planned optimal portfolio structure of the bank
		self.rb = 0.02 # refinancing costs of the bank -> tbd in environment
		self.rd = 0.01 # interest rate on deposits
		self.r = 0.05 # required reserve rate -> tbd in environment
		self.pReal = 0.9 # probability of credit success
		self.rhoReal = 0.03 # interest charged on risky investment
		self.xi = 1.0 # scaling parameter in CRRA
		self.theta = 1.5 # risk aversion parameter of bank
		self.gamma = 0.8 # fraction of interbank loans in overall volume
		
		self.Q = 0.0 # the current liquidity position of the bank
		# set 0.0 as standard, but after calculate_liquidity_demand we will return the indicated values
		self.Ip = 0.0 # the planned optimal investment; (gamma * lamb * V) = (0.8 * 0.5 * 250.0) = 100.0
		self.Ep = 0.0 # the planned excess reserves; (gamma * (1-lamb) * V) = (0.8 * 0.5 * 250.0) = 100.0
		self.Lp = 0.0 # the planned interbank loans; Q - ((Ip-I) + (Ep-E)) = 90.0
	
		self.assetNumber = 6.0 # number of assets available to bank
		self.numBanks = 3.0 # number of banks in the economy
		
		# first, calculate number of transactions for investments
		numTransactions = int(round(self.assetNumber / self.numBanks))
		
		#
		# ASSETS
		#
		
		# finally, put them on the transaction stack
		for i in range(numTransactions):
			transaction = Transaction()
			value = 100.0
			maturity = 50.0
			timeOfDefault = -1
			transaction.this_transaction("I",  self.identifier, -2,  value,  self.rhoReal,  maturity, timeOfDefault)
			self.accounts.append(transaction)
			del transaction
		
		# excess reserves
		value = 90.0
		transaction = Transaction()
		transaction.this_transaction("E",  self.identifier,  -3,  value,  self.rb,  0, -1)
		self.accounts.append(transaction)
		del transaction
		
		# required deposits to the central bank
		value = 10.0
		transaction = Transaction()
		transaction.this_transaction("rD",  self.identifier,  -3,  value,  self.rb,  0, -1)
		self.accounts.append(transaction)
		del transaction
		
		
		#
		# LIABILITIES
		#
		
		# banking capital
		value = 40.0
		transaction = Transaction()
		transaction.this_transaction("BC",  self.identifier,  self.identifier,  value,  0.0,  0, -1)
		self.accounts.append(transaction)
		del transaction
		
		# deposits 
		value = 250.0
		transaction = Transaction()
		transaction.this_transaction("D",  -1,  self.identifier,  value,  self.rd,  0, -1)
		self.accounts.append(transaction)
		del transaction
		
		# central bank loans
		value = 10.0
		transaction = Transaction()
		transaction.this_transaction("LC",  -3,  self.identifier,  value,  self.rb,  0, -1)
		self.accounts.append(transaction)
		del transaction
		
	#-------------------------------------------------------------------------
    
