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
# MAIN
#-------------------------------------------------------------------------
if __name__ == '__main__':
	import sys
	sys.path.append('src/')
	from tests import Tests
	
	#
	# VARIABLES
	#
	tests = Tests()
	
	#
	# CODE
	#
	# for each appropriate chunk of the original code we need one test to ensure it is working
	args=['./br-make_tests.py',  "environments/", "test3",  "log/",  "measurements/"]
	#args = sys.argv

	#tests.bank__get_parameters_from_file(args)             #tricky one, havent tried yet
	#tests.bank__apply_sifi_surcharge(args)                 #tricky one, havent tried yet
	#tests.bank__update_maturity(args)
	#tests.bank__update_risk_aversion(args)                 #tricky one, doesnt work yet, havent changed anything 
	#tests.bank__get_interest(args)
	#tests.bank__liquidate_due_transactions(args)
	#tests.bank__get_new_deposits(args)
	#tests.bank__transfer_required_deposits(args)
	#tests.bank__reduce_banking_capital(args)
	#tests.bank__check_solvency(args)                
	#tests.bank__check_liquidity(args)
	#tests.bank__calculate_liquidity_demand(args)
	#tests.bank__get_central_bank_liquidity(args)           # works but maybe bug? --> see faq
	#tests.bank__liquidate_assets(args)                     # works but potential bug? --> see faq
	#tests.bank__transfer_investments(args)                 # several unclear things, leave open first
	#tests.bank__transfer_excess_reserves(args)
	#tests.bank__calculate_optimal_investment_volume(args)  # works but maybe bug? --> see faq
	#tests.bank__initialize_transactions(args)
	#tests.bank__get_initial_banking_capital(args)
	#tests.bank__get_account(args)
	#tests.bank__get_account_num_transactions(args)
	#tests.bank__add_transaction(args)
	#tests.bank__purge_accounts(args)                        # I cannot add a list, I cannot print it. How to test this???
	#tests.bank__change_deposits(args)
	#tests.bank__initialize_standard_bank(args)

	tests.environment__initialize(args)
	#tests.environment__read_environment_file(args)
	
	#tests.network__do_interbank_trades(args)
	#tests.network__remove_inactive_bank(args)
		
	#tests.updater__updater(args)
	#tests.updater__updater1(args)


	#UNKNOWN TESTS:
	#tests.test_fire_sales(args)
	#tests.test_state(args)
	#tests.updater__liquidate_assets(args)
	#tests.bank__test1(args)
	
