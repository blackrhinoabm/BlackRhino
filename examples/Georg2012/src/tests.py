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

#-------------------------------------------------------------------------
#  class Tests
#-------------------------------------------------------------------------
class Tests(object):
	#
	# VARIABLES
	#
	
	
	# 
	# METHODS
	#
	
	#-------------------------------------------------------------------------
	# __init__
	#-------------------------------------------------------------------------
	def __init__(self):
		pass
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# print_info(text)
	#-------------------------------------------------------------------------
	def print_info(self, text):
		print '##############################################################################\n'
		print text
		print '##############################################################################\n'
	#-------------------------------------------------------------------------

		
#-------------------------------------------------------------------------
#  TESTS FOR BANK.PY
#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__get_parameters_from_file
	#-------------------------------------------------------------------------
	
	def bank__get_parameters_from_file(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.get_parameters_from_file \n"
		text += "  XXX \n"
		text += "  XXX tricky one, havent tried yet\n"
		text += "  XXX \n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__get_parameters_from_file in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#

		#tricky one, havent tried yet

	#-------------------------------------------------------------------------

	#-------------------------------------------------------------------------
	# bank__apply_sifi_surcharge
	#-------------------------------------------------------------------------
	
	def bank__apply_sifi_surcharge(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.apply_sifi_surcharge \n"
		text += "  XXX \n"
		text += "  XXX tricky one, havent tried yet\n"
		text += "  XXX \n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__apply_sifi_surcharge in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#

		#tricky one, havent tried yet

	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__update_maturity
	#-------------------------------------------------------------------------
	def bank__update_maturity(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.update_maturity() \n"
		text += "  It is successfull if the maturity of all transactions is reduced by one \n"
		text += "  when the bank is printed the second time. \n"
		text += "  Note that for investments also the time of default has to be reduced by one.\n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__update_maturity in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		print bank
		bank.update_maturity()
		print bank
		
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__update_risk_aversion
	#-------------------------------------------------------------------------
	def bank__update_risk_aversion(self, args):
		from environment import Environment
		from updater import Updater
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__update_risk_aversion in run: %s',  environment_directory + identifier + ".xml")
		
		#
		# TEST CODE
		#
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# create a test environment with standardised banks
		
		# first test: a bank in t=0 defaults, check that risk aversion in t=1 increases
		environment.banks[0].reduce_banking_capital(10.0)
		environment.banks[0].check_solvency(environment.get_state(0),  "info",  0)
		print environment.get_state(0)
		environment.banks[1].update_risk_aversion(environment.get_state(1), 1)
		print environment.banks[1]
		# second test: check that risk aversion in t=2 decreases
		environment.banks[1].update_risk_aversion(environment.get_state(2), 2)
		print environment.banks[1]
		environment.banks[1].update_risk_aversion(environment.get_state(3), 3)
		print environment.banks[1]
		
		#
		# MEASUREMENT AND LOGGING
		#
		logging.info('FINISHED logging for test bank__update_risk_aversion in run: %s \n', environment_directory + identifier + ".xml")
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__get_interest
	#-------------------------------------------------------------------------
	def bank__get_interest(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.get_interest() \n"
		text += "  It is successfull if calculated interest equals the\n"
		text += "  difference for interest on assets and interest on liabilities. \n"
		text += "  Note that BC will not recieve any interest.\n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__get_interest in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		interestCalculated = 0.0
		interestAssets = 0.0
		interestLiabilities = 0.0
		print "Bank:"
		print bank
		
		print "Transactions:"
		for transaction in bank.accounts:
			print transaction.transactionType, transaction.transactionValue, transaction.transactionInterest
			if (transaction.transactionType == "I" or transaction.transactionType == "E" or transaction.transactionType == "rD"): # we have an asset
				interestAssets += transaction.transactionValue*transaction.transactionInterest
			else: # we have a liability
				interestLiabilities -= transaction.transactionValue*transaction.transactionInterest
		
		for type in ["I",  "E",  "D",  "rD",  "LC",  "L",  "BC"]:
			interestCalculated += bank.get_interest(type)
			
		print "Interest: " + str(interestCalculated)+ " = " + str(interestAssets) + " + "  + str(interestLiabilities)
		#print transaction.transactionType, transaction.transactionValue, transaction.transactionInterest

	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__liquidate_due_transactions
	#-------------------------------------------------------------------------
	def bank__liquidate_due_transactions(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.liquidate_due_transactions() \n"
		text += "  It is successful if the maturity of the investments is 0 and  \n"
		text += "  if the two investment the retrun their respective vaule \n"
		text += "  (which should be 200 in total for the standard bank). \n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__liquidate_due_transactions in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		for transaction in bank.accounts:
			if (transaction.transactionType == "I"):
				transaction.transactionMaturity = 0.0   # first lower maturity to 0
				print bank                                              # and check maturity

		VolumeCalculated = 0.0
		print VolumeCalculated 

		for type in ["I"]:                                      # now apply the liquidate function and compare voulmes
			VolumeCalculated += bank.liquidate_due_transactions(type)			
		print VolumeCalculated 

	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__get_new_deposits
	#-------------------------------------------------------------------------
	def bank__get_new_deposits(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.get_new_deposits \n"
		text += "  It returns the change of the deposits of the bank (250). \n"
		text += "  With a scaleFactor of 0.02 this change should fluctuate  \n"
		text += "  randomly between +5 and -5. \n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__get_new_deposits in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		DepositsChange = 0.0
		scaleFactor = 0.02

		for transaction in bank.accounts:               # print Deposits 
			if (transaction.transactionType == "D"):
				print transaction.transactionType, transaction.transactionValue

		for type in ["D"]:                              # now apply the get_new_deposits function and print return value
			DepositsChange += bank.get_new_deposits(scaleFactor)
			print DepositsChange


	#-------------------------------------------------------------------------

	
	#-------------------------------------------------------------------------
	# bank__transfer_required_deposits
	#-------------------------------------------------------------------------
	def bank__transfer_required_deposits(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.transfer_required_deposits \n"
		text += "  first we delete the required deposits of the standard bank, \n"
		text += "  afterwards we calculate  the new rD using the respective function. \n"
		text += "  for r=0.05 the output should be -12.5 \n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__transfer_required_deposits in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		for transaction in bank.accounts:
			if (transaction.transactionType == "rD"):
				transaction.transactionValue = 0.0   # first elimnate the rD of standard bank
				print bank                                              # and check bank

		ReqDep = 0.0
		print ReqDep
		
		for type in ["rD"]:                              # now apply the transfer_required_deposits and print new rD value
			ReqDep += bank.transfer_required_deposits()			
			print ReqDep


	#-------------------------------------------------------------------------
			
	
	#-------------------------------------------------------------------------
	# bank__reduce_banking_capital
	#-------------------------------------------------------------------------
	def bank__reduce_banking_capital(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.reduce_banking_capital \n"
		text += "  It returns the reduced banking capital. \n"
		text += "  Suppose the banking capital of our standard bank is \n"
		text += "  reduced by 5, so the new BC will be 40 - 5 = 35 \n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__reduce_banking_capital in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		value = 5.0
		
		for transaction in bank.accounts:
			if (transaction.transactionType == "BC"):
				print transaction.transactionValue
				bank.reduce_banking_capital(value)
				print transaction.transactionValue


	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__check_solvency
	#-------------------------------------------------------------------------
	def bank__check_solvency(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		from state import State
		
		text = "This test checks bank.check_solvency \n"
		text += "  Within this test the required_capital_ratio is set extremely  \n"
		text += "  high so that our standard bank will fail to meet its \n"
		text += "  capital requirement. Subsequently 'active' will be set to -1 \n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__check_solvency in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		
		# for the standard Bank BC/ I = 40 / 200 = 0.2
		# in order to make sure that the bank will not meet their requirements
		# we set requiredCapitalRatio = 0.9
		state = State()
		state.requiredCapitalRatio = 0.9
		required_capital_ratio = state.requiredCapitalRatio 
		print state.print_state()

		#for bank in bankDirectory:
                bank.check_solvency(state,  "info",  0)
		print bank
		
		# and check if "active" is now -1


	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__check_liquidity
	#-------------------------------------------------------------------------
	def bank__check_liquidity(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.check_liquidity \n"
		text += "  Within this test Q is set < 0.0 so that \n"
		text += "  our standard bank will become illiquid. \n"
		text += "  Subsequently 'active' will be set to -1 \n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__check_liquidity in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		
		# nom we just assume that
		bank.Q = -1.0

		#for bank in bankDirectory:
                bank.check_liquidity()

		print bank
		# and check if "active" is now -1


	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__calculate_liquidity_demand
	#-------------------------------------------------------------------------
	def bank__calculate_liquidity_demand(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.calculate_liquidity_demand \n"
		text += "  It will calculate the liquidity demand for the standard bank according to its \n"
		text += "  parameters and the formulas used in bank.calculate_liquidity_demand \n"
		text += "  As a reminder the parameters for the standard bank are: \n"
		text += "\n"
		text += "       gamma = 0.8                                \n"
		text += "       lamb = 0.5                                 \n"
		text += "       V = 250                                     \n"
		text += "       Q = 0.0                                     \n"
		text += "\n"
		text += "  The formulas for bank.calculate_liquidity_demand are: \n"
		text += "\n"
		text += "       Ip = gamma * lamb * V = 0.8 * 0,5 * 250.0 = 100.0  \n"
		text += "       Ep = gamma * (1.0 - lamb) * V = 0.8 * 0,5 * 250.0 = 100.0 \n"
		text += "       Lp = Q - ((Ip-I) + (Ep-E)) = 0.0 - ((100-200) + (90-100)) \n"
		text += "\n"
		text += "  The result should be Lp = 90.0 \n"
		self.print_info(text)

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__calculate_liquidity_demand in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#

                bank.calculate_liquidity_demand()
                print "Ip= " + str(bank.Ip) + "; Ep= " + str(bank.Ep) + "; I= " + str(bank.get_account("I")) + "; E= " + str(bank.get_account("E"))
                print "Lp= " + str(bank.Lp)


	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__get_central_bank_liquidity
	#-------------------------------------------------------------------------
	def bank__get_central_bank_liquidity(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		from state import State
		
		text = "This test checks bank.get_central_bank_liquidity \n"
		text += "  First we have to set Lp < 0.0 in order to set the bank in a position of \n"
		text += "  liquidity shortage (Lp = -50.0). Now suppose that the CB regards only 0.8 of the \n"
		text += "  bank's assets as safe (collateralQuality = 0.8). For I = 200.0 the bank should get \n"
		text += "  enough liquidity (up to 160.0). As a result LC should increase to LC = 60.0 and \n"
		text += "  Lp should be 0 again. \n"
		self.print_info(text)

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__get_central_bank_liquidity in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		state = State()
		state.collateralQuality = 0.8           # make sure that the lokal values are used
		state.rb = 0.02

		# now suppose we are in a liquidity shortage of Lp = -50.0
		bank.Lp = -50.0

                bank.get_central_bank_liquidity(state)
                print bank 
                print "Lp= " + str(bank.Lp)


	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__liquidate_assets
	#-------------------------------------------------------------------------
	def bank__liquidate_assets(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		from state import State
		
		text = "This test checks bank.liquidate_assets \n"
		text += "  First we have to set Lp < 0.0 in order to set the bank in a position of \n"
		text += "  liquidity shortage (Lp = -10.0). Suppose that the liquidity discount factor will be 0.05 \n"
		text += "  and for Ip we have to assume e.g. 250 in order to trigger the loop in the code. \n"
		text += "  The requiredCapitalRatio is = 0.08 for the standard bank \n"
		text += " \n"
		text += "  Under the current circumstances (bug?) this will lead to Lp = -160.0 in the first loop \n"
		text += "  and liquidation price of 0.9608. Both assets have to be sold now and the \n"
		text += "  BC will be decreased from 40.0 to 32.16. Lp will now be 32. 16 \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__liquidate_assets in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		state = State()
		state.liquidationDiscountFactor = 0.05 

		bank.Lp = - 10.0        # let's assume for argument sake that banks are short in liquidity Lp = -10.0          
		bank.Ip = 250.0         # but want to increase their planned investment  Ip = 250.0
                                        # the requiredCapitalRatio is = 0.08
                                        
                bank.liquidate_assets(200.0,  200.0,  state,  "info",  0)
                print bank


	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__transfer_investments
	#-------------------------------------------------------------------------
	def bank__transfer_investments(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		from state import State
		
		text = "This test checks bank.transfer_investments \n"
		text += "  Note that you should first look at bank.calculate_optimal_investment_volume to better) \n"
		text += "  understand this. If we assume pReal = 0.98 than we will will receive lamb = 0.3014 and V = 13.5635  \n"
		text += "  Moreover, for our standard bank the avaiable liquditiy Q should be roughly 105 (reserves + interest gains)  \n"
		text += "  The requiredCapitalRatio is = 0.08 for the standard bank \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__transfer_investments in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		state = State()
		bank.pReal = 0.98                       # we have to assign this value for pReal so that we recieve  
                                                        # lamb = 0.3014 and V = 13.5635
                                                        # see also bank__calculate_optimal_investment_volume for details
                bank.Q = 105.0                          # Q should be roughly 105 (reserves + interest gains)
                bank.averageTransactionSize = 200.0     # For our standard Bank the averageTransactionSize is 200 
               

                bank.transfer_investments(state)


	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__transfer_excess_reserves
	#-------------------------------------------------------------------------
	def bank__transfer_excess_reserves(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.transfer_excess_reserves \n"
		text += "  It is successful  if the excess reserves of our standard bank are increase. \n"
		text += "  Under the assumption that our banks faces a liquidity surplus (available volume)  \n"
		text += "  of Q = +100.0 the balance sheet of our bank should get an additional transaction-position \n"
		text += "  of E with a value of 100.0 \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__transfer_excess_reserves in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		bank.Q = 100.0                          # assume a available volume of Q = 100 (in order to trigger the mehthode)

		bank.transfer_excess_reserves()         # call the mehtode

		print bank                              # check result 


	#-------------------------------------------------------------------------

                
	#-------------------------------------------------------------------------
	# bank__calculate_optimal_investment_volume
	#-------------------------------------------------------------------------
	def bank__calculate_optimal_investment_volume(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		from state import State
		
		text = "This test checks bank.calculate_optimal_investment_volume \n"
		text += "  First of all we have to change pReal in order to ensure that mu will be >0 so that \n"
		text += "  lamb will also be >0 and <1 . Now for our standard bank mu will now be 0.0197, sigma2= 0.0105, \n"
		text += "  lamb = 0.3014 and V = 13.5635. As we have no leverage ratio for our standard Bank the \n"
		text += "  result should be V = 13.5635  \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__calculate_optimal_investment_volume in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		state = State()
		bank.pReal = 0.98                       # we have to assign this value for pReal so that we recieve  
                                                        # lamb = 0.3014 and V = 13.5635
                bank.calculate_optimal_investment_volume(state)
                print "optimal investment volume = " + str(bank.V)


	#-------------------------------------------------------------------------

                
	#-------------------------------------------------------------------------
	# bank__initialize_transactions
	#-------------------------------------------------------------------------
	def bank__initialize_transactions(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		from state import State
		
		text = "This test checks bank.initialize_transactions \n"
		text += "  This method is supposed to create the transactions of banks in BlackRihno. \n"
		text += "  The simplest way to test it is to initialize the standard bank, then to call the \n"
		text += "  method and check whether transactions have been added to our standard bank. \n"
		text += "   \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__initialize_transactions in run: %s',  environment_directory + identifier + ".xml")

		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		#print bank
		state = State()
		state.successProbabilityFirms = 0.5             # we assign this values in order to check if the 
		state.firmLoanMaturity = 100.0                  # random function works 
		
		print bank
		bank.initialize_transactions(state)
		print bank


	#-------------------------------------------------------------------------
                
               
	#-------------------------------------------------------------------------
	# bank__get_initial_banking_capital
	#-------------------------------------------------------------------------
	def bank__get_initial_banking_capital(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		from state import State
		
		text = "This test checks bank.get_initial_banking_capital \n"
		text += "  This method is supposed to create a return value which will be used as a. \n"
		text += "  initial banking capital value. As the required capital ratio is 0.9 and  \n"
		text += "  our Investments are 200 the result should be 225.0 \n"
		text += "   \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__get_initial_banking_capital in run: %s',  environment_directory + identifier + ".xml")

		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		state = State()
		state.requiredCapitalRatio = 0.9
		required_capital_ratio = state.requiredCapitalRatio
		
		initial_banking_capital = 0.0
		print initial_banking_capital
		
		for type in ["I"]:                              # now apply the initial_banking_capital and print the new value
			initial_banking_capital += bank.get_initial_banking_capital(required_capital_ratio)			
			print initial_banking_capital


	#-------------------------------------------------------------------------

               
	#-------------------------------------------------------------------------
	# bank__get_account
	#-------------------------------------------------------------------------
	def bank__get_account(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory

		text = "This test checks bank.get_account \n"
		text += "  The purpose of this method is to establish an account for our bank which contains  \n"
		text += "  all kinds of assets and liabilities. The method simply adds all kinds of assets  \n"
		text += "  and stores them in one volume. As our Banks holds 300.0 assets (2* I = 100, E = 90, D = 250) \n"
		text += "  and 300 liabilites the total volume of our account should be 600.0 \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__get_account in run: %s',  environment_directory + identifier + ".xml")

		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
	
		account = 0.0                                           # counting all types in account together
		print bank                                              # and checking how much is the total
                                                                        # volume of the account
		for type in ["I",  "E",  "rD",  "BC",  "D",  "LC",  "L"]:     
                        if type == "I":                                      
                                account += bank.get_account(type)
                                print "I = " + str(account)
                        if type == "E":                                      
                                account += bank.get_account(type)
                                print "I+E = " + str(account)
                        if type == "rD":                                      
                                account += bank.get_account(type)
                                print "I+E+rD = " + str(account)
                        if type == "BC":                                      
                                account += bank.get_account(type)
                                print "I+E+rD+BC = " + str(account)
                        if type == "D":                                      
                                account += bank.get_account(type)
                                print "I+E+rD+BC+D = " + str(account)
                        if type == "LC":                                      
                                account += bank.get_account(type)
                                print "I+E+rD+BC+D+LC = " + str(account)
                        if type == "L":                                      
                                account += bank.get_account(type)
                                print "I+E+rD+BC+D+LC+L = " + str(account)         

			
 	#-------------------------------------------------------------------------
			
               
	#-------------------------------------------------------------------------
	# bank__get_account_num_transactions
	#-------------------------------------------------------------------------
	def bank__get_account_num_transactions(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory

		text = "This test checks bank.get_account_num_transactions \n"
		text += "  The purpose of this method is to count the numbers of transaction for   \n"
		text += "  accounts banks hold. Our standard bank has 7 transactions by default. \n"
		text += "  (2* I + E + rD + BC + D + LC). As long as our bank does not have e.g. \n"
		text += "  an L the number of transactions should be 7.0 \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__get_account_num_transactions in run: %s',  environment_directory + identifier + ".xml")

		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
	
		num_transactions = 0.0          # counting all types in account together
                                                # and checking if the number of transaction
                                                # is increasing by one 
		for type in ["I",  "E",  "rD",  "BC",  "D",  "LC",  "L"]:     
                        if type == "I":                                      
                                num_transactions += bank.get_account_num_transactions(type)
                                print "I = " + str(num_transactions)
                        if type == "E":                                      
                                num_transactions += bank.get_account_num_transactions(type)
                                print "I+E = " + str(num_transactions)
                        if type == "rD":                                      
                                num_transactions += bank.get_account_num_transactions(type)
                                print "I+E+rD = " + str(num_transactions)
                        if type == "BC":                                      
                                num_transactions += bank.get_account_num_transactions(type)
                                print "I+E+rD+BC = " + str(num_transactions)
                        if type == "D":                                      
                                num_transactions += bank.get_account_num_transactions(type)
                                print "I+E+rD+BC+D = " + str(num_transactions)
                        if type == "LC":                                      
                                num_transactions += bank.get_account_num_transactions(type)
                                print "I+E+rD+BC+D+LC = " + str(num_transactions)
                        if type == "L":                                      
                                num_transactions += bank.get_account_num_transactions(type)
                                print "I+E+rD+BC+D+LC+L = " + str(num_transactions)     
			
 	#-------------------------------------------------------------------------

               
	#-------------------------------------------------------------------------
	# bank__add_transaction
	#-------------------------------------------------------------------------
	def bank__add_transaction(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory

		text = "This test checks bank.add_transaction \n"
		text += "  The most simple way to test this function is to assign an new    \n"
		text += "  transaction to our bank. Therefore, lets just assign the following  \n"
		text += "  transaction and check whether it has been added: \n"
		text += '  (type = "D",  fromID = -1,  toID = bank.identifier,  value = 10,  \n'
		text += "   interest = 0.09, maturity = 0, timeOfDefault = -1) \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__add_transaction in run: %s',  environment_directory + identifier + ".xml")

		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		bank.add_transaction("D",  -1,  bank.identifier,  10,  0.09,  0, -1)
		print bank
	
			
 	#-------------------------------------------------------------------------

               
	#-------------------------------------------------------------------------
	# bank__purge_accounts
	#-------------------------------------------------------------------------
	def bank__purge_accounts(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory

		text = "This test checks bank.purge_accounts \n"
		text += "  The most simple way to test this function is to assign an new    \n"
		text += "  transaction to our bank. Therefore, lets just assign the following  \n"
		text += "  transaction and check whether it has been added: \n"
		text += '  (type = "D",  fromID = -1,  toID = bank.identifier,  value = 10,  \n'
		text += "   interest = 0.09, maturity = 0, timeOfDefault = -1) \n"
		self.print_info(text)		

		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__purge_accounts in run: %s',  environment_directory + identifier + ".xml")

		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		
		#
		# TEST CODE
		#
		account = 0.0
		
		for transaction in bank.accounts:
			if transaction.transactionType == "I":
				print account
				bank.purge_accounts()
				account += bank.accounts
				print account
                                
			
 	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__change_deposits
	#-------------------------------------------------------------------------
	
	def bank__change_deposits(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.change_deposits \n"
		text += "  suppose that the change in depostits = 10.0 \n"
		text += "  then the new deposits should be 260.0  \n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__change_deposits in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      

		#
		# TEST CODE
		#

		change = 10.0
		
		for transaction in bank.accounts:
			if (transaction.transactionType == "D"):
				print "Old Deposits = " + str(transaction.transactionValue)
				bank.change_deposits(change)
				print "New Deposits = " + str(transaction.transactionValue)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# bank__initialize_standard_bank
	#-------------------------------------------------------------------------
	
	def bank__initialize_standard_bank(self, args):
		import os
		from bank import Bank
		from environment import Environment # needed for the bankDirectory
		
		text = "This test checks bank.initialize_standard_bank() \n"
		text += "  It is successfull if a standart Bank with 2 asstets (I = 100),\n"
		text += "  E = 90, D = 250  and pReal = 0,9 etc. has been created.\n"
		text += "  See 'initialize_standard_bank' in bank.py for details.\n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__initialize_standard_bank in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct bank filename
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# get the bankDirectory from the environment
		bankDirectory = environment.parameters.bankDirectory
		# and loop over all banks in the directory
		listing = os.listdir(bankDirectory)
		bankFilename = bankDirectory + listing[0]
		
		#
		# TEST CODE
		#
		
		# generate the bank
		bank = Bank()
		bank.initialize_standard_bank()      
		print bank
	#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
#  TESTS FOR ENVIRONMENT.PY
#-------------------------------------------------------------------------
 
	#-------------------------------------------------------------------------
	# environment__initialize
	#-------------------------------------------------------------------------
	
	def environment__initialize(self, args):
		import os
                from bank import Bank
		from environment import Environment 
		
		text = "This test checks environment.initialize \n"
		text += "  It is successfull if a standart Bank with 2 asstets (I = 100),\n"
		text += "  E = 90, D = 250  and pReal = 0,9 etc. has been created.\n"
		text += "  See 'initialize_standard_bank' in bank.py for details.\n"
		self.print_info(text)
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test environment__initialize in run: %s',  environment_directory + identifier + ".xml")
		
		# Construct  environment 
		environment = Environment()
		
		#
		# TEST CODE
		#
		environment.initialize(environment_directory,  identifier)
		bankDirectory = environment.parameters.bankDirectory

		bank = Bank()
		account = 0.0                                           
            
		for type in ["I"]:     
                        if type == "I":                                      
                                account += bank.get_account(type)
                                print "I = " + str(account)
		
		

	#-------------------------------------------------------------------------

 	
	#-------------------------------------------------------------------------
	# environment__read_environment_file
	#-------------------------------------------------------------------------

	def environment__read_environment_file(self, args):
                text = "This test checks environment.read_environment_file \n"
		text += "  This is a function from the standard Python library \n"
		text += "  which does not really need to be tested therefore \n"
		self.print_info(text)
	
	#-------------------------------------------------------------------------

		
#-------------------------------------------------------------------------
#  TESTS FOR NETWORK.PY
#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# network__do_interbank_trades
	#-------------------------------------------------------------------------
	def network__do_interbank_trades(self, args):
		from environment import Environment
		from updater import Updater
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test network__do_interbank_trades in run: %s',  environment_directory + identifier + ".xml")
		
		#
		# TEST CODE
		#
		environment = Environment(environment_directory,  identifier)
		# create a test environment with standardised banks
		
		#print environment.banks[0]
		#print environment.banks[1]
		#print environment.banks[2]
		print environment.network
		environment.banks[0].Lp = 2.0
		environment.banks[1].Lp = -1.0
		environment.banks[2].Lp = -1.0
		environment.network.do_interbank_trades(environment.get_state(0))
		print environment.network
		environment.banks[0].Lp = 2.3
		environment.banks[1].Lp = -1.1
		environment.banks[2].Lp = -1.2
		environment.network.do_interbank_trades(environment.get_state(0))
		print environment.network
		
		#print environment.banks[0]
		#print environment.banks[1]
		#print environment.banks[2]
		
		#
		# MEASUREMENT AND LOGGING
		#
		logging.info('FINISHED logging for test updater__remove_inactive_bank in run: %s \n', environment_directory + identifier + ".xml")
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# network__remove_inactive_bank
	#-------------------------------------------------------------------------
	def network__remove_inactive_bank(self, args):
		from environment import Environment
		from updater import Updater
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test updater__remove_inactive_banks in run: %s',  environment_directory + identifier + ".xml")
		
		#
		# TEST CODE
		#
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# create a test environment with standardised banks
		
		#print environment.banks[0]
		#print environment.banks[1]
		#print environment.banks[2]
		environment.banks[0].Lp = 2.0
		environment.banks[1].Lp = -1.0
		environment.banks[2].Lp = -1.0
		environment.network.do_interbank_trades(environment.get_state(0))
		print environment.network
		
		updater = Updater(environment)
		
		#
		# execute the update code
		#
		environment.banks[0].reduce_banking_capital(2.0)
		environment.banks[0].check_solvency('info')
		environment.network.remove_inactive_bank(environment.banks[0])
		
		#print environment.banks[0]
		#print environment.banks[1]
		#print environment.banks[2]
		print environment.network
		
		#
		# MEASUREMENT AND LOGGING
		#
		logging.info('FINISHED logging for test updater__remove_inactive_bank in run: %s \n', environment_directory + identifier + ".xml")
	#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
#  TESTS FOR UPDATER.PY
#-------------------------------------------------------------------------

	#-------------------------------------------------------------------------
	# test_updater
	#-------------------------------------------------------------------------
	def updater__updater(self, args):
		from environment import Environment
		from updater import Updater
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test updater__updater2 in run: %s',  environment_directory + identifier + ".xml")
		
		#
		# TEST CODE
		#
		environment = Environment(environment_directory,  identifier)
		# create a test environment with standardised banks
		environment.banks[0].change_deposits(1.0)
		environment.banks[1].change_deposits(-1.0)
		
		updater = Updater(environment)
		
		#
		# execute the update code
		#
		updater.do_update(environment.get_state(0),  environment.network, environment.network.contracts.nodes(), 0, "info")
		
		#
		# MEASUREMENT AND LOGGING
		#
		logging.info('FINISHED logging for test updater__updater2 in run: %s \n', environment_directory + identifier + ".xml")
	#-------------------------------------------------------------------------
	

	#-------------------------------------------------------------------------
	# test_updater1
	#-------------------------------------------------------------------------
	def updater__updater1(self, args):
		from environment import Environment
		from updater import Updater
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test updater__updater1 in run: %s',  environment_directory + identifier + ".xml")
		
		#
		# TEST CODE
		#
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# create a test environment with standardised banks
		
		print environment.banks[0]
		print environment.banks[1]
		print environment.banks[2]
		
		updater = Updater(environment)
		
		#
		# execute the update code
		#
		updater.do_update_phase1(environment.get_state(0),  environment.network, environment.network.contracts.nodes(), 0, "info")
		
		print environment.banks[0]
		print environment.banks[1]
		print environment.banks[2]
		
		#
		# MEASUREMENT AND LOGGING
		#
		logging.info('FINISHED logging for test updater__updater1 in run: %s \n', environment_directory + identifier + ".xml")
	#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#  UNKNOWN TESTS
#-------------------------------------------------------------------------

	#-------------------------------------------------------------------------
	# test_fire_sales
	#-------------------------------------------------------------------------
	def test_fire_sales(self, args): # TODO not consistent with other test names
		import logging
		import networkx as nx
		
		from environment import Environment
		from runner import Runner
		from measurement import Measurement
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		measurement_directory = str(args[4])
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for run: %s',  environment_directory + identifier + ".xml")
		
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		runner = Runner()
		measurement = Measurement()
		
		#
		# UPDATE STEP
		#
		for i in range(environment.parameters.numSimulations):
			environment.initialize(environment_directory,  identifier)
			runner.initialize(environment)
			measurement.initialize() # clear the previous measurement
			
			# do the run
			runner.do_run(measurement, "info")
			
			# do the histograms, i.e. add the current measurement to the histogram
			measurement.do_histograms()
			logging.info('')
		
		#
		# MEASUREMENT AND LOGGING
		#
		measurement.write_histograms(measurement_directory,  environment)
		logging.info('FINISHED logging for run: %s \n', environment_directory + identifier + ".xml")
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# test_state
	#-------------------------------------------------------------------------
	def test_state(self, args):
		from environment import Environment
		from updater import Updater
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test updater__remove_inactive_banks in run: %s',  environment_directory + identifier + ".xml")
		
		#
		# TEST CODE
		#
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		# create a test environment with standardised banks
		
		#
		print environment.get_state(0)
		environment.banks[0].reduce_banking_capital(10.0)
		environment.banks[0].check_solvency(environment.get_state(0),  "info",  0)
		print environment.get_state(1)
		
		#
		# MEASUREMENT AND LOGGING
		#
		logging.info('FINISHED logging for test updater__remove_inactive_bank in run: %s \n', environment_directory + identifier + ".xml")
	#-------------------------------------------------------------------------


		

	#-------------------------------------------------------------------------
	# liquidate_assets
	#-------------------------------------------------------------------------
	def updater__liquidate_assets(self, args):
		from environment import Environment
		from updater import Updater
		
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test updater__liquidate_assets in run: %s',  environment_directory + identifier + ".xml")
		
		#
		# TEST CODE
		#
		environment = Environment(environment_directory,  identifier)
		# create a test environment with standardised banks
		
		print environment.banks[0]
		#print environment.banks[1]
		#print environment.banks[2]
		
		updater = Updater(environment)
		environment.banks[1].active=-1
		environment.banks[2].active=-1
		#
		# execute the update code
		#
		updater.do_update_phase1(environment, 0, "debug")
		updater.do_update_phase2(environment, 0, "info")
		
		print environment.banks[0]
		#print environment.banks[1]
		#print environment.banks[2]
		
		#
		# MEASUREMENT AND LOGGING
		#
		logging.info('FINISHED logging for test updater__liquidate_assets in run: %s \n', environment_directory + identifier + ".xml")
	#-------------------------------------------------------------------------





	#-------------------------------------------------------------------------
	# bank__test1
	#-------------------------------------------------------------------------
	def bank__test1(self, args):
		from environment import Environment

		text = "This test checks the environment.initializer \n"
		text += "  It is successfull if a bank has been generate and \n"
		text += "  if a network of 3 banks with 3 nodes and 6 edges \n"
		text += "  has been established.\n"
		self.print_info(text)
				
		#
		# INITIALIZATION
		#
		environment_directory = str(args[1])
		identifier = str(args[2])
		log_directory = str(args[3])
		
		
		# Configure logging parameters so we get output while the program runs
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename = log_directory + identifier + ".log", level=logging.INFO)
		logging.info('START logging for test bank__test1 in run: %s',  environment_directory + identifier + ".xml")
		
		#
		# TEST CODE
		#
		environment = Environment()
		environment.initialize(environment_directory,  identifier)
		
		#for bank in environment.banks:
		print environment.banks[2]
		print environment.network
		
		
		#
		# MEASUREMENT AND LOGGING
		#
		logging.info('FINISHED logging for test bank__test1 in run: %s \n', environment_directory + identifier + ".xml")
	#-------------------------------------------------------------------------



