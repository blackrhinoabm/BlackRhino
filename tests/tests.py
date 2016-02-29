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


class Tests(object):
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
#  TESTS FOR BANK.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__get_identifier
    # -------------------------------------------------------------------------

    def bank__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.get_identifier \n"
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
        logging.info('START logging for test bank__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        text = "Identifier: "
        text += bank.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__set_identifier
    # -------------------------------------------------------------------------

    def bank__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.set_identifier \n"
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
        logging.info('START logging for test bank__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        text = "Original identifier: "
        text += bank.get_identifier()
        print(text)
        bank.set_identifier("new_ident")
        text = "New identifier: "
        text += bank.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__get_parameters
    # -------------------------------------------------------------------------

    def bank__get_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.get_parameters \n"
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
        logging.info('START logging for test bank__get_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)
        bank.get_parameters_from_file(bank_filename, environment)

        #
        # TESTING
        #

        text = "Parameters:"
        print(text)
        print(bank.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__set_parameters
    # -------------------------------------------------------------------------

    def bank__set_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.set_parameters \n"
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
        logging.info('START logging for test bank__set_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        text = "Original parameters:"
        print(text)
        print(bank.get_parameters())
        text = "New parameters:"
        print(text)
        bank.set_parameters({'rd': 0.44, 'rl': 0.55, 'active': 1})
        print(bank.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__get_state_variables
    # -------------------------------------------------------------------------

    def bank__get_state_variables(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.get_state_variables \n"
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
        logging.info('START logging for test bank__get_state_variables in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        text = "State variables:"
        print(text)
        print(bank.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__set_state_variables
    # -------------------------------------------------------------------------

    def bank__set_state_variables(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.set_state_variables \n"
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
        logging.info('START logging for test bank__set_state_variables in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        text = "Original state variables:"
        print(text)
        print(bank.get_state_variables())
        text = "New state variables:"
        print(text)
        bank.set_state_variables({'test': 0.66})
        print(bank.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__str
    # -------------------------------------------------------------------------

    def bank__str(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.str \n"
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
        logging.info('START logging for test bank__str in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        print(bank.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__get_parameters_from_file
    # -------------------------------------------------------------------------

    def bank__get_parameters_from_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.get_parameters_from_file \n"
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
        logging.info('START logging for test bank__get_parameters_from_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        bank.get_parameters_from_file(bank_filename, environment)

        #
        # TESTING
        #

        # test whether the parameters are read properly
        text = "Identifier has been read as follows: \n"
        text += "Identifier: "
        text += bank.identifier
        text += "\n"
        self.print_info(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__check_consistency
    # -------------------------------------------------------------------------

    def bank__check_consistency(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.check_consitency \n"
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
        logging.info('START logging for test bank__check_consistency in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        print("Checking consistency of the standard bank: ")
        print(bank.check_consistency())
        print("Adding additional deposits without adding appropriate cash/loans.")
        bank.add_transaction("deposits", "", environment.households[0:1][0],
                             bank.identifier, 150, bank.interest_rate_deposits, 0, -1)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down
        print("Checking consistency of the standard bank: ")
        print(bank.check_consistency())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__get_account
    # -------------------------------------------------------------------------

    def bank__get_account(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.get_account \n"
        text += "  The purpose of this method is to establish an account for our bank which contains  \n"
        text += "  all kinds of assets and liabilities. The method simply adds all kinds of assets  \n"
        text += "  and stores them in one volume. As our Banks holds 250.0 assets \n"
        text += "  and 250 liabilites the total volume of our account should be 500.0 \n"
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
        logging.info('START logging for test bank__get_account in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        account = 0.0                                           # counting all types in account together
        print(bank)                                              # and checking how much is the total
        # volume of the account
        for type in ["deposits",  "cash",  "loans"]:
                        if type == "deposits":
                                account += bank.get_account(type)
                                print("D = " + str(account))
                        if type == "cash":
                                account += bank.get_account(type)
                                print("D+M = " + str(account))
                        if type == "loans":
                                account += bank.get_account(type)
                                print("D+M+L = " + str(account))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__get_account_num_transactions
    # -------------------------------------------------------------------------

    def bank__get_account_num_transactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.get_account_num_transactions \n"
        text += "  The purpose of this method is to count the numbers of transaction for   \n"
        text += "  accounts banks hold. Our standard bank has 3 transactions by default. \n"
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
        logging.info('START logging for test bank__get_account_num_transactions in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        num_transactions = 0.0          # counting all types in account together
        print(bank)
        # and checking if the number of transaction
        # is increasing by one
        for type in ["deposits",  "cash",  "loans"]:
                        if type == "deposits":
                                num_transactions += bank.get_account_num_transactions(type)
                                print("D = " + str(num_transactions))
                        if type == "cash":
                                num_transactions += bank.get_account_num_transactions(type)
                                print("D+M = " + str(num_transactions))
                        if type == "loans":
                                num_transactions += bank.get_account_num_transactions(type)
                                print("D+M+L = " + str(num_transactions))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__add_transaction
    # -------------------------------------------------------------------------

    def bank__add_transaction(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.add_transaction \n"
        text += "  The most simple way to test this function is to assign an new    \n"
        text += "  transaction to our bank. Therefore, lets just assign the following  \n"
        text += "  transaction and check whether it has been added: \n"
        text += '  (type = "deposits",  fromID = -1,  toID = bank.identifier,  amount = 10,  \n'
        text += "   interest = 0.09, maturity = 0, timeOfDefault = -1) \n"
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
        logging.info('START logging for test bank__add_transaction in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        print(bank)
        print("Adding new transaction: \n")
        bank.add_transaction("deposits", "", environment.households[0:1][0],
                             bank.identifier,  10,  0.09,  0, -1)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down
        print(bank)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__clear_accounts
    # -------------------------------------------------------------------------

    def bank__clear_accounts(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.clear_accounts \n"
        text += "  Checking if after the clear_accounts the total amount    \n"
        text += "  of transactions in zero.  \n"
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
        logging.info('START logging for test bank__clear_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        bank.add_transaction("deposits", "", environment.households[0:1][0],
                             bank.identifier, 0.0,  0.09,  0, -1)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        bank.clear_accounts()

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__purge_accounts
    # -------------------------------------------------------------------------

    def bank__purge_accounts(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.purge_accounts \n"
        text += "  Checking if after the purge_accounts the total amount    \n"
        text += "  of transactions in the bank stays the same.  \n"
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
        logging.info('START logging for test bank__purge_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        bank.add_transaction("deposits", "", environment.households[0:1][0],
                             bank.identifier, 0.0,  0.09,  0, -1)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        bank.purge_accounts()

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__initialize_standard_bank
    # -------------------------------------------------------------------------

    def bank__initialize_standard_bank(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.initialize_standard_bank \n"
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
        logging.info('START logging for test bank__initialize_standard_bank in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        print(bank)

    # -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR FIRM.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__get_identifier
    # -------------------------------------------------------------------------

    def firm__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.get_identifier \n"
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
        logging.info('START logging for test firm__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        text = "Identifier: "
        text += firm.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__set_identifier
    # -------------------------------------------------------------------------

    def firm__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.set_identifier \n"
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
        logging.info('START logging for test firm__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        text = "Original identifier: "
        text += firm.get_identifier()
        print(text)
        firm.set_identifier("new_ident")
        text = "New identifier: "
        text += firm.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__get_parameters
    # -------------------------------------------------------------------------

    def firm__get_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.get_parameters \n"
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
        logging.info('START logging for test firm__get_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        text = "Parameters:"
        print(text)
        print(firm.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__set_parameters
    # -------------------------------------------------------------------------

    def firm__set_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.set_parameters \n"
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
        logging.info('START logging for test firm__set_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        text = "Original parameters:"
        print(text)
        print(firm.get_parameters())
        text = "New parameters:"
        print(text)
        firm.set_parameters({'productivity': 1.55, 'active': 1})
        print(firm.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__get_state_variables
    # -------------------------------------------------------------------------

    def firm__get_state_variables(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.get_state_variables \n"
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
        logging.info('START logging for test firm__get_state_variables in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        text = "State variables:"
        print(text)
        print(firm.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__set_state_variables
    # -------------------------------------------------------------------------

    def firm__set_state_variables(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.set_state_variables \n"
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
        logging.info('START logging for test firm__set_state_variables in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        #
        # TESTING
        #

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        text = "Original state variables:"
        print(text)
        print(firm.get_state_variables())
        text = "New state variables:"
        print(text)
        firm.set_state_variables({'test': 0.66})
        print(firm.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__str
    # -------------------------------------------------------------------------

    def firm__str(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.str \n"
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
        logging.info('START logging for test firm__str in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        print(firm.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__get_parameters_from_file
    # -------------------------------------------------------------------------

    def firm__get_parameters_from_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.get_parameters_from_file \n"
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
        logging.info('START logging for test firm__get_parameters_from_file in run: %s', 
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)
        firm.get_parameters_from_file(firmFilename, environment)

        #
        # TESTING
        #

        # test whether the parameters are read properly
        text = "Identifier has been read as follows: \n"
        text += "Identifier: "
        text += firm.identifier
        text += "\n"
        text += "Productivity: "
        text += str(firm.parameters["productivity"])
        self.print_info(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__get_account
    # -------------------------------------------------------------------------

    def firm__get_account(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.get_account \n"
        text += "  The purpose of this method is to establish an account for our firm which contains  \n"
        text += "  all kinds of assets and liabilities. The method simply adds all kinds of assets  \n"
        text += "  and stores them in one volume. As our firms holds 250.0 assets \n"
        text += "  and 250 liabilites the total volume of our account should be 500.0 \n"
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
        logging.info('START logging for test firm__get_account in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        account = 0.0                                           # counting all types in account together
        print(firm)                                             # and checking how much is the total
        # volume of the account
        for type in ["loans",  "cash",  "goods"]:
                        if type == "loans":
                                account += firm.get_account(type)
                                print("L = " + str(account))
                        if type == "cash":
                                account += firm.get_account(type)
                                print("L+M = " + str(account))
                        if type == "goods":
                                account += firm.get_account(type)
                                print("L+M+G = " + str(account))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__get_account_num_transactions
    # -------------------------------------------------------------------------

    def firm__get_account_num_transactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.get_account_num_transactions \n"
        text += "  The purpose of this method is to count the numbers of transaction for   \n"
        text += "  accounts firms hold. Our standard frm has 3 transactions by default. \n"
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
        logging.info('START logging for test firm__get_account_num_transactions in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        num_transactions = 0.0          # counting all types in account together
        print(firm)
        # and checking if the number of transaction
        # is increasing by one
        for type in ["loans",  "cash",  "goods"]:
                        if type == "loans":
                                num_transactions += firm.get_account_num_transactions(type)
                                print("L = " + str(num_transactions))
                        if type == "cash":
                                num_transactions += firm.get_account_num_transactions(type)
                                print("L+M = " + str(num_transactions))
                        if type == "goods":
                                num_transactions += firm.get_account_num_transactions(type)
                                print("L+M+G = " + str(num_transactions))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__add_transaction
    # -------------------------------------------------------------------------

    def firm__add_transaction(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.add_transaction \n"
        text += "  The most simple way to test this function is to assign an new    \n"
        text += "  transaction to our firm. Therefore, lets just assign the following  \n"
        text += "  transaction and check whether it has been added: \n"
        text += '  (type = "deposits",  fromID = -1,  toID = firm.identifier,  amount = 10,  \n'
        text += "   interest = 0.09, maturity = 0, timeOfDefault = -1) \n"
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
        logging.info('START logging for test firm__add_transaction in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        print(firm)
        print("Adding new transaction: \n")
        firm.add_transaction("deposits", "", environment.households[0:1][0],
                             firm.identifier,  10,  0.09,  0, -1)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down
        print(firm)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__clear_accounts
    # -------------------------------------------------------------------------

    def firm__clear_accounts(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.clear_accounts \n"
        text += "  Checking if after the clear_accounts the total amount    \n"
        text += "  of transactions in zero.  \n"
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
        logging.info('START logging for test firm__clear_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in firm.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        firm.add_transaction("deposits", "", environment.households[0:1][0],
                             firm.identifier, 0.0,  0.09,  0, -1)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down

        account = 0.0
        tranx = 0

        for transaction in firm.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        firm.clear_accounts()

        account = 0.0
        tranx = 0

        for transaction in firm.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__purge_accounts
    # -------------------------------------------------------------------------

    def firm__purge_accounts(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.purge_accounts \n"
        text += "  Checking if after the purge_accounts the total amount    \n"
        text += "  of transactions in the firm stays the same.  \n"
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
        logging.info('START logging for test firm__purge_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in firm.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        firm.add_transaction("deposits", "", environment.households[0:1][0],
                             firm.identifier, 0.0,  0.09,  0, -1)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down

        account = 0.0
        tranx = 0

        for transaction in firm.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        firm.purge_accounts()

        account = 0.0
        tranx = 0

        for transaction in firm.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__initialize_standard_firm
    # -------------------------------------------------------------------------

    def firm__initialize_standard_firm(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.initialize_standard_firm \n"
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
        logging.info('START logging for test firm__initialize_standard_bank in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        environment = Environment(environment_directory,  identifier)

        # get the firm_directory from the environment
        firm_directory = environment.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        print(firm)

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
        helper = Helper()
        helper.initialize_standard_household(household, environment)
        #
        # TESTING
        #

        text = "Identifier: "
        text += household.get_identifier()
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
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        text = "Original identifier: "
        text += household.get_identifier()
        print(text)
        household.set_identifier("new_ident")
        text = "New identifier: "
        text += household.get_identifier()
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
        household.get_parameters_from_file(householdFilename, environment)

        #
        # TESTING
        #

        # test whether the parameters are read properly
        text = "Identifier has been read as follows: \n"
        text += "Identifier: "
        text += household.identifier
        text += "\n"
        text += "Amount of labour: "
        text += str(household.parameters["labour"])
        text += "\n"
        text += "Propensity to save: "
        text += str(household.parameters["propensity_to_save"])
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
        text += "  The purpose of this method is to establish an account for our household which contains  \n"
        text += "  all kinds of assets and liabilities. The method simply adds all kinds of assets  \n"
        text += "  and stores them in one volume. As our household holds 250.0 assets \n"
        text += "  and 250 liabilites the total volume of our account should be 500.0 \n"
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
                                account += household.get_account(type)
                                print("D = " + str(account))
                        if type == "cash":
                                account += household.get_account(type)
                                print("D+M = " + str(account))
                        if type == "manhours":
                                account += household.get_account(type)
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
        text += "  The purpose of this method is to count the numbers of transaction for   \n"
        text += "  accounts households hold. Our standard frm has 3 transactions by default. \n"
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
                                num_transactions += household.get_account_num_transactions(type)
                                print("D = " + str(num_transactions))
                        if type == "cash":
                                num_transactions += household.get_account_num_transactions(type)
                                print("D+M = " + str(num_transactions))
                        if type == "manhours":
                                num_transactions += household.get_account_num_transactions(type)
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
        text += "  The most simple way to test this function is to assign an new    \n"
        text += "  transaction to our household. Therefore, lets just assign the following  \n"
        text += "  transaction and check whether it has been added: \n"
        text += '  (type = "deposits",  fromID = -1,  toID = household.identifier,  amount = 10,  \n'
        text += "   interest = 0.09, maturity = 0, timeOfDefault = -1) \n"
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
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        print(household)
        print("Adding new transaction: \n")
        household.add_transaction("deposits", "", environment.banks[0:1][0],
                                  household.identifier,  10,  0.09,  0, -1)
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
        text += "  Checking if after the clear_accounts the total amount    \n"
        text += "  of transactions in zero.  \n"
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
                                  household.identifier, 0.0,  0.09,  0, -1)
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
        text += "  Checking if after the purge_accounts the total amount    \n"
        text += "  of transactions in the household stays the same.  \n"
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
                                  household.identifier, 0.0,  0.09,  0, -1)
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

        household.purge_accounts()

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
        helper = Helper()
        helper.initialize_standard_household(household, environment)

        #
        # TESTING
        #

        print(household)

    # -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR ENVIRONMENT.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__add_static_parameter
    # -------------------------------------------------------------------------

    def environment__add_static_parameter(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.add_static_parameter \n"
        text = "Should add 'test':0.66 to static parameters \n"
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
        logging.info('START logging for test environment__add_static_parameter in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print(environment.static_parameters)
        print("Adding 'test':0.66")
        environment.add_static_parameter("test", 0.66)
        print(environment.static_parameters)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__add_variable_parameter
    # -------------------------------------------------------------------------

    def environment__add_variable_parameter(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.add_variable_parameter \n"
        text = "Should add 'test':0.66-0.77 to the parameters \n"
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
        logging.info('START logging for test environment__add_variable_parameter in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print(environment.variable_parameters)
        print("Adding 'test':0.66-0.77")
        environment.add_variable_parameter("test", 0.66, 0.77)
        print(environment.variable_parameters)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__get_identifier
    # -------------------------------------------------------------------------

    def environment__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.get_identifier \n"
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
        logging.info('START logging for test environment__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        text = "Identifier: "
        text += environment.identifier
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__set_identifier
    # -------------------------------------------------------------------------

    def environment__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.set_identifier \n"
        text = "and sets the identifier to XYZ \n"
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
        logging.info('START logging for test environment__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        text = "Identifier: "
        text += environment.identifier
        print(text)
        print("Changing identifier to XYZ")
        environment.set_identifier("XYZ")
        text = "Identifier: "
        text += environment.identifier
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__get_static_parameters
    # -------------------------------------------------------------------------

    def environment__get_static_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.get_static_parameters \n"
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
        logging.info('START logging for test environment__get_static_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print "Static parameters:"
        print(environment.get_static_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__set_static_parameters
    # -------------------------------------------------------------------------

    def environment__set_static_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.set_static_parameters \n"
        text = "and sets them to 'test':0.55 \n"
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
        logging.info('START logging for test environment__set_static_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Static parameters:")
        print(environment.get_static_parameters())
        print("Changing static parameters to 'test':0.55")
        environment.set_static_parameters({'test': 0.55})
        print("Static parameters:")
        print(environment.get_static_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__get_variable_parameters
    # -------------------------------------------------------------------------

    def environment__get_variable_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.get_variable_parameters \n"
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
        logging.info('START logging for test environment__get_variable_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print "Variable parameters:"
        print(environment.get_variable_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__set_variable_parameters
    # -------------------------------------------------------------------------

    def environment__set_variable_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.set_variable_parameters \n"
        text = "and sets them to 'test': 0.55-0.66 \n"
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
        logging.info('START logging for test environment__set_variable_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Variable parameters:")
        print(environment.get_variable_parameters())
        print("Changing variable parameters to 'test': 0.55-0.66")
        environment.set_variable_parameters({'test': [0.55, 0.66]})
        print("Variable parameters:")
        print(environment.get_variable_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__str
    # -------------------------------------------------------------------------

    def environment__str(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.__str__ \n"
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
        logging.info('START logging for test environment__str__ in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print(environment.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__print_parameters
    # -------------------------------------------------------------------------

    def environment__print_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.print_parameters \n"
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
        logging.info('START logging for test environment__print_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print("Parameters of the environment: ")
        environment.print_parameters()

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__write_environment_file
    # -------------------------------------------------------------------------

    def environment__write_environment_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.write_environment_file \n"
        text = "and writes a mirror of the config file \n"
        text = "in the directory from which it was called \n"
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
        logging.info('START logging for test environment__write_environment_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print("Writing the environment file")
        environment.write_environment_file(identifier)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__read_xml_config_file
    # -------------------------------------------------------------------------

    def environment__read_xml_config_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.read_xml_config_file \n"
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
        logging.info('START logging for test environment__read_xml_config_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print("Read the environment config file")
        print(environment.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__initialize
    # -------------------------------------------------------------------------

    def environment__initialize(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.initialize \n"
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
        logging.info('START logging for test environment__initialize in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print("Initialized the environment")
        print(environment.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__initialize_banks_from_files
    # -------------------------------------------------------------------------

    def environment__initialize_banks_from_files(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.initialize_banks_from_files \n"
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
        logging.info('START logging for test environment__initialize_banks_from_files in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print("Initialized the banks")
        text = "num_banks parameter: "
        text += str(environment.num_banks)
        print(text)
        text = "Number of banks read: "
        text += str(len(environment.banks))
        print(text)
        print("The banks read: ")
        for i in range(0, int(environment.num_banks)):
            print(environment.banks[i].__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__initialize_firms_from_files
    # -------------------------------------------------------------------------

    def environment__initialize_firms_from_files(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.initialize_firms_from_files \n"
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
        logging.info('START logging for test environment__initialize_firms_from_files in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print("Initialized the firms")
        text = "num_firms parameter: "
        text += str(environment.num_firms)
        print(text)
        text = "Number of firms read: "
        text += str(len(environment.firms))
        print(text)
        print("The firms read: ")
        for i in range(0, int(environment.num_firms)):
            print(environment.firms[i].__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__initialize_households_from_files
    # -------------------------------------------------------------------------

    def environment__initialize_households_from_files(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.initialize_households_from_files \n"
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
        logging.info('START logging for test environment__initialize_households_from_files in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print("Initialized the households")
        text = "num_households parameter: "
        text += str(environment.num_households)
        print(text)
        text = "Number of households read: "
        text += str(len(environment.households))
        print(text)
        print("The households read: ")
        for i in range(0, int(environment.num_households)):
            print(environment.households[i].__str__())

    # -------------------------------------------------------------------------

# BELOW IT'S THE OLD STUFF

# -------------------------------------------------------------------------
#  TESTS FOR UPDATER.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # test_updater
    # -------------------------------------------------------------------------
    def updater__updater(self, args):
        from src.environment import Environment
        from src.updater import Updater

        #
        # INITIALIZATION
        #
        environment_directory = str(args[1])
        identifier = str(args[2])
        log_directory = str(args[3])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__updater2 in run: %s',
                     environment_directory + identifier + ".xml")

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
        updater.do_update(environment, 0, "info")

        #
        # MEASUREMENT AND LOGGING
        #
        logging.info('FINISHED logging for test updater__updater2 in run: %s \n', environment_directory + identifier + ".xml")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # test_updater1
    # -------------------------------------------------------------------------
    def updater__updater1(self, args):
        from src.environment import Environment
        from src.updater import Updater

        #
        # INITIALIZATION
        #
        environment_directory = str(args[1])
        identifier = str(args[2])
        log_directory = str(args[3])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__updater1 in run: %s',  environment_directory + identifier + ".xml")

        #
        # TEST CODE
        #
        environment = Environment(environment_directory,  identifier)
        # environment.initialize(environment_directory,  identifier)
        # create a test environment with standardised banks

        print environment.banks[0]
        print environment.banks[1]
        print environment.banks[2]

        updater = Updater(environment)

        #
        # execute the update code
        #
        updater.do_update_phase1(environment,  environment.network.contracts.nodes(), 0, "info")

        print environment.banks[0]
        print environment.banks[1]
        print environment.banks[2]

        #
        # MEASUREMENT AND LOGGING
        #
        logging.info('FINISHED logging for test updater__updater1 in run: %s \n', environment_directory + identifier + ".xml")
    # -------------------------------------------------------------------------
