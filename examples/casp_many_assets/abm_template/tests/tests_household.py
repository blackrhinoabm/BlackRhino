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
from src.helper import Helper

# -------------------------------------------------------------------------
#  class Tests
# -------------------------------------------------------------------------


class TestsHousehold(object):
    #
    # VARIABLES
    #

    #
    # METHODS
    #

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # print_info(text)
    # -------------------------------------------------------------------------
    def print_info(self, text):
        print('##############################################################################\n')
        print(text)
        print('##############################################################################\n')
    # -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR HOUSEHOLD.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__get_identifier
    # -------------------------------------------------------------------------

    def household__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.get_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)
        #
        # TESTING
        #

        text = "Identifier: "
        text = text + household.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__set_identifier
    # -------------------------------------------------------------------------

    def household__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.set_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        text = "Original identifier: "
        text = text + household.get_identifier()
        print(text)
        household.set_identifier("new_ident")
        text = "New identifier: "
        text = text + household.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__get_parameters
    # -------------------------------------------------------------------------

    def household__get_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.get_parameters \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__get_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        text = "Parameters:"
        print(text)
        print(household.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__set_parameters
    # -------------------------------------------------------------------------

    def household__set_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.set_parameters \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__set_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        text = "Original parameters:"
        print(text)
        print(household.get_parameters())
        text = "New parameters:"
        print(text)
        household.set_parameters({'ps': 1.55, 'active': 1, 'labour': 8})
        print(household.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__get_state_variables
    # -------------------------------------------------------------------------

    def household__get_state_variables(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.get_state_variables \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__get_state_variables in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        text = "State variables:"
        print(text)
        print(household.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__set_state_variables
    # -------------------------------------------------------------------------

    def household__set_state_variables(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.set_state_variables \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__set_state_variables in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #
        text = "Original state variables:"
        print(text)
        print(household.get_state_variables())
        text = "New state variables:"
        print(text)
        household.set_state_variables({'test': 0.66})
        print(household.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__str
    # -------------------------------------------------------------------------

    def household__str(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.str \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__str in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        print(household.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__get_parameters_from_file
    # -------------------------------------------------------------------------

    def household__get_parameters_from_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.get_parameters_from_file \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__get_parameters_from_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the household_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        household.get_parameters_from_file(householdFilename, environment)

        #
        # TESTING
        #

        # test whether the parameters are read properly
        text = "Identifier has been read as follows: \n"
        text = text + "Identifier: "
        text = text + household.identifier
        text = text + "\n"
        text = text + "Amount of labour: "
        text = text + str(household.parameters["labour"])
        text = text + "\n"
        text = text + "Propensity to save: "
        text = text + str(household.parameters["propensity_to_save"])
        self.print_info(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__get_account
    # -------------------------------------------------------------------------

    def household__get_account(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.get_account \n"
        text = text + "  The purpose of this method is to establish an account for our household which contains  \n"
        text = text + "  all kinds of assets and liabilities. The method simply adds all kinds of assets  \n"
        text = text + "  and stores them in one volume. As our household holds 250.0 assets \n"
        text = text + "  and 250 liabilites the total volume of our account should be 500.0 \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__get_account in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        account = 0.0                                           # counting all types in account together
        print(household)                                             # and checking how much is the total
        # volume of the account
        for type in ["deposits",  "cash",  "manhours"]:
                        if type == "deposits":
                                account = account + household.get_account(type)
                                print("D = " + str(account))
                        if type == "cash":
                                account = account + household.get_account(type)
                                print("D+M = " + str(account))
                        if type == "manhours":
                                account = account + household.get_account(type)
                                print("D+M+H = " + str(account))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__get_account_num_transactions
    # -------------------------------------------------------------------------

    def household__get_account_num_transactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.get_account_num_transactions \n"
        text = text + "  The purpose of this method is to count the numbers of transaction for   \n"
        text = text + "  accounts households hold. Our standard frm has 3 transactions by default. \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__get_account_num_transactions in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        num_transactions = 0.0          # counting all types in account together
        print(household)
        # and checking if the number of transaction
        # is increasing by one
        for type in ["deposits",  "cash",  "manhours"]:
                        if type == "deposits":
                                num_transactions = num_transactions + household.get_account_num_transactions(type)
                                print("D = " + str(num_transactions))
                        if type == "cash":
                                num_transactions = num_transactions + household.get_account_num_transactions(type)
                                print("D+M = " + str(num_transactions))
                        if type == "manhours":
                                num_transactions = num_transactions + household.get_account_num_transactions(type)
                                print("D+M+H = " + str(num_transactions))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__add_transaction
    # -------------------------------------------------------------------------

    def household__add_transaction(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.add_transaction \n"
        text = text + "  The most simple way to test this function is to assign an new    \n"
        text = text + "  transaction to our household. Therefore, lets just assign the following  \n"
        text = text + "  transaction and check whether it has been added: \n"
        text = text + '  (type = "deposits",  fromID = -1,  toID = household.identifier,  amount = 10,  \n'
        text = text + "   interest = 0.09, maturity = 0, timeOfDefault = -1) \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__add_transaction in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        print(household)
        print("Adding new transaction: \n")
        household.add_transaction("deposits", "", environment.banks[0:1][0],
                                  household.identifier,  10,  0.09,  0, -1, environment)
        # environment.banks[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first bank in environment, but if there are no
        # banks (which happens in testing) it doesn't break down
        print(household)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__clear_accounts
    # -------------------------------------------------------------------------

    def household__clear_accounts(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.clear_accounts \n"
        text = text + "  Checking if after the clear_accounts the total amount    \n"
        text = text + "  of transactions in zero.  \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__clear_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in household.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        household.add_transaction("deposits", "", environment.banks[0:1][0],
                                  household.identifier, 0.0,  0.09,  0, -1, environment)
        # environment.banks[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first bank in environment, but if there are no
        # banks (which happens in testing) it doesn't break down

        account = 0.0
        tranx = 0

        for transaction in household.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        household.clear_accounts()

        account = 0.0
        tranx = 0

        for transaction in household.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__purge_accounts
    # -------------------------------------------------------------------------

    def household__purge_accounts(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.purge_accounts \n"
        text = text + "  Checking if after the purge_accounts the total amount    \n"
        text = text + "  of transactions in the household stays the same.  \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__purge_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in household.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        household.add_transaction("deposits", "", environment.banks[0:1][0],
                                  household.identifier, 0.0,  0.09,  0, -1, environment)
        # environment.banks[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first bank in environment, but if there are no
        # banks (which happens in testing) it doesn't break down

        account = 0.0
        tranx = 0

        for transaction in household.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        household.accounts[0].purge_accounts(environment)

        account = 0.0
        tranx = 0

        for transaction in household.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__initialize_standard_household
    # -------------------------------------------------------------------------

    def household__initialize_standard_household(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.initialize_standard_household \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__initialize_standard_household in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        print(household)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__get_transactions_from_file
    # -------------------------------------------------------------------------

    def household__get_transactions_from_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.get_transactions_from_file \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__get_transactions_from_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)

        #
        # TESTING
        #

        environment.households[0].clear_accounts()
        print("Printing household:\n")
        print(environment.households[0])
        print("Reading transactions from the config file.\n")
        print("Printing household: \n")
        household.get_transactions_from_file(household_directory + listing[0], environment)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # household__getattr
    # -------------------------------------------------------------------------

    def household__getattr(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks household.getattr \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test household__getattr in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        household_directory = environment.household_directory
        # and loop over all firms in the directory
        listing = os.listdir(household_directory)
        householdFilename = household_directory + listing[0]

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        environment.households.append(household)
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        print('Accessing rates through household.parameters["propensity_to_save"] :')
        print(household.parameters["propensity_to_save"])
        print("Accessing rates through household.propensity_to_save:")
        print(household.propensity_to_save)

    # -------------------------------------------------------------------------
