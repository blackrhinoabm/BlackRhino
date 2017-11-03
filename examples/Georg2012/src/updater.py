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
#  class Updater
#-------------------------------------------------------------------------
class Updater(object):
#	from environment import Environment

	#
	# VARIABLES
	#

	# 
	# METHODS
	#
	#-------------------------------------------------------------------------
	# __init__
	#-------------------------------------------------------------------------
	def __init__(self,  environment):
		self.environment = environment
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# do_update
	#-------------------------------------------------------------------------
	def do_update(self,  environment,  time,  debug):
		network = environment.network
		state = environment.get_state(time)
		
		active_banks = self.find_active_banks(environment,  network,  time)
		self.do_update_phase1(environment,  active_banks,  time,  debug)
		
		active_banks = self.find_active_banks(environment,  network,  time)
		self.do_update_phase2(environment,  active_banks, time,  debug)
		network.do_interbank_trades(state)
		
		active_banks = self.find_active_banks(environment,  network,  time)
		self.do_update_phase3(environment,  active_banks,  time,  debug)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# do_update_phase1
	#-------------------------------------------------------------------------
	def do_update_phase1(self,  environment,   active_banks,  time,  debug):
		state = environment.get_state(time)
		network = environment.network
		banks = environment.banks
		
		#
		# loop over all banks and do update step
		#
		for bank in active_banks:
			# first, update all maturities
			bank.update_maturity()
			
			# then, update the risk-aversion parameter of banks to incorporate information contagion
			bank.update_risk_aversion(environment.get_state(time), time)
			
			# re-calculate the (constraint) optimal portfolio decision of the bank
			
			
			# initialize bank liquidity
			bank.Q = 0.0
			bank.Q = bank.Q + bank.get_interest("D")
			bank.Q = bank.Q + bank.get_interest("rD")
			bank.Q = bank.Q + bank.get_interest("E")
			bank.Q = bank.Q + bank.get_interest("I") # here a loss on the banking capital might occur
			bank.Q = bank.Q + bank.get_interest("L")
			bank.Q = bank.Q + bank.get_interest("LC")
			
			# first, get all required reserves
			bank.Q = bank.Q + bank.liquidate_due_transactions("rD")
			# then, get all excess reserves
			bank.Q = bank.Q + bank.liquidate_due_transactions("E")
			# then, get payments from firms (interest, due loans)
			bank.Q = bank.Q + bank.liquidate_due_transactions("I")
			# now, settle interbank claims
			# remove the claim from the network of exposures
			network.liquidate_due_transactions(bank)
			# and liquidate it
			bank.Q = bank.Q + bank.liquidate_due_transactions("L")
			# and central bank claims
			bank.Q = bank.Q + bank.liquidate_due_transactions("LC")
			# transfer required reserves to the central bank
			bank.Q = bank.Q + bank.transfer_required_deposits()
			
			# check the solvency, the bank might be insolvent due to a loss on the risky assets
			bank.check_solvency(state,  debug,  time)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# do_update_phase2
	#-------------------------------------------------------------------------
	def do_update_phase2(self,  environment,  active_banks,  time,  debug):
		for bank in active_banks:
			# next, determine new deposit level
			new_deposit_level = bank.get_new_deposits(self.environment.get_state(time).scaleFactorHouseholds)
			bank.Q = bank.Q + new_deposit_level
			# and calculate the liquidity demand
			bank.calculate_liquidity_demand()
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# do_update_phase3
	#-------------------------------------------------------------------------
	def do_update_phase3(self,  environment,  active_banks,  time,  debug):
		current_assets = 0.0 # the volume of all assets in the market, required to determine the price-drop of assets in a fire sale
		for bank in active_banks: # find the current amount of assets in the market
			current_assets += bank.get_account("I")
		
		state = environment.get_state(time)
		network = environment.network
		banks = environment.banks
		
		#
		# then do the update code
		#
		for bank in active_banks:
			# transfer to/from standing facilitiesget_parameters_from_file
			bank.get_central_bank_liquidity(state)
			
			# check for the bank's liquidity
			bank.liquidate_assets(environment.initial_assets,  current_assets,  state,  debug,  time)
			
			# transfer investments to firms
			bank.Q = bank.Lp # transfer available liquidity to Q
			bank.Lp = 0.0
			bank.transfer_investments(state) # state is needed to determine the probability that a loan defaults
			bank.transfer_excess_reserves()
		
		if (debug == "debug"):
			network.write_network_of_exposures(time)
	#-------------------------------------------------------------------------


#
# HELPER ROUTINES
#
	#-------------------------------------------------------------------------
	# find_active_banks()
	#-------------------------------------------------------------------------
	def find_active_banks(self,  environment,  network,  time):
		active_banks = []
		
		for bank in environment.banks:
			if bank.active > -1:
				active_banks.append(bank)
			else:
				network.remove_inactive_bank(bank,  time)
		
		return active_banks
	#-------------------------------------------------------------------------
