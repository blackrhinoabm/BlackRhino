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
        environment.banks.append(bank)
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        text = "Identifier: "
        text = text + bank.get_identifier()
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
        environment.banks.append(bank)
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        text = "Original identifier: "
        text = text + bank.get_identifier()
        print(text)
        bank.set_identifier("new_ident")
        text = "New identifier: "
        text = text + bank.get_identifier()
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
        environment.banks.append(bank)
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
        environment.banks.append(bank)
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
        environment.banks.append(bank)
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
        environment.banks.append(bank)
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
        environment.banks.append(bank)
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
        environment.banks.append(bank)
        bank.get_parameters_from_file(bank_filename, environment)

        #
        # TESTING
        #

        # test whether the parameters are read properly
        text = "Identifier has been read as follows: \n"
        text = text + "Identifier: "
        text = text + bank.identifier
        text = text + "\n"
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
        environment.banks.append(bank)
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        print("Checking consistency of the standard bank: ")
        print(bank.check_consistency())
        print("Adding additional deposits without adding appropriate cash/loans.")
        bank.add_transaction("deposits", "", environment.get_agent_by_id("test_household"),
                             bank, 150, bank.interest_rate_deposits, 0, -1, environment)
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
        text = text + "  The purpose of this method is to establish an account for our bank which contains  \n"
        text = text + "  all kinds of assets and liabilities. The method simply adds all kinds of assets  \n"
        text = text + "  and stores them in one volume. As our Banks holds 250.0 assets \n"
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
        environment.banks.append(bank)
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
                                account = account + bank.get_account(type)
                                print("D = " + str(account))
                        if type == "cash":
                                account = account + bank.get_account(type)
                                print("D+M = " + str(account))
                        if type == "loans":
                                account = account + bank.get_account(type)
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
        text = text + "  The purpose of this method is to count the numbers of transaction for   \n"
        text = text + "  accounts banks hold. Our standard bank has 3 transactions by default. \n"
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
        environment.banks.append(bank)
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
                                num_transactions = num_transactions + bank.get_account_num_transactions(type)
                                print("D = " + str(num_transactions))
                        if type == "cash":
                                num_transactions = num_transactions + bank.get_account_num_transactions(type)
                                print("D+M = " + str(num_transactions))
                        if type == "loans":
                                num_transactions = num_transactions + bank.get_account_num_transactions(type)
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
        text = text + "  The most simple way to test this function is to assign an new    \n"
        text = text + "  transaction to our bank. Therefore, lets just assign the following  \n"
        text = text + "  transaction and check whether it has been added: \n"
        text = text + '  (type = "deposits",  fromID = -1,  toID = bank.identifier,  amount = 10,  \n'
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
        environment.banks.append(bank)
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        print(bank)
        print("Adding new transaction: \n")
        print(environment.get_agent_by_id(bank.identifier))
        bank.add_transaction("deposits", "", "test_household",
                             bank.identifier,  10,  0.09,  0, -1, environment)
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
        environment.banks.append(bank)
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

        bank.add_transaction("deposits", "", "test_household",
                             bank.identifier, 0.0,  0.09,  0, -1, environment)

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        for bank in environment.banks:
            print(bank)
        for firm in environment.firms:
            print(firm)
        for household in environment.households:
            print(household)
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
        text = text + "  Checking if after the purge_accounts the total amount    \n"
        text = text + "  of transactions in the bank stays the same.  \n"
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
        environment.banks.append(bank)
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

        bank.add_transaction("deposits", "", "test_household",
                             bank.identifier, 0.0,  0.09,  0, -1, environment)
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

        bank.accounts[0].purge_accounts(environment)

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
        environment.banks.append(bank)
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        print(bank)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__get_transactions_from_file
    # -------------------------------------------------------------------------

    def bank__get_transactions_from_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.get_transactions_from_file \n"
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
        logging.info('START logging for test bank__get_transactions_from_file in run: %s',
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

        #
        # TESTING
        #

        environment.banks[0].clear_accounts()
        print("Printing bank: \n")
        print(environment.banks[0])
        print("Reading transactions from the config file.\n")
        print("Printing bank: \n")
        bank.get_transactions_from_file(bank_directory + listing[0], environment)
        print(environment.banks[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__getattr
    # -------------------------------------------------------------------------

    def bank__getattr(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks bank.getattr \n"
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
        logging.info('START logging for test bank__getattr in run: %s',
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
        environment.banks.append(bank)
        helper = Helper()
        helper.initialize_standard_bank(bank, environment)

        #
        # TESTING
        #

        print('Accessing rates through bank.parameters["interest_rate_loans"] :')
        print(bank.parameters["interest_rate_loans"])
        print("Accessing rates through bank.interest_rate_loans:")
        print(bank.interest_rate_loans)

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
        environment.firms.append(firm)
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        text = "Identifier: "
        text = text + firm.get_identifier()
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
        environment.firms.append(firm)
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        text = "Original identifier: "
        text = text + firm.get_identifier()
        print(text)
        firm.set_identifier("new_ident")
        text = "New identifier: "
        text = text + firm.get_identifier()
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
        environment.firms.append(firm)
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
        environment.firms.append(firm)
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
        environment.firms.append(firm)
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
        environment.firms.append(firm)
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
        environment.firms.append(firm)
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
        environment.firms.append(firm)
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)
        firm.get_parameters_from_file(firmFilename, environment)

        #
        # TESTING
        #

        # test whether the parameters are read properly
        text = "Identifier has been read as follows: \n"
        text = text + "Identifier: "
        text = text + firm.identifier
        text = text + "\n"
        text = text + "Productivity: "
        text = text + str(firm.parameters["productivity"])
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
        text = text + "  The purpose of this method is to establish an account for our firm which contains  \n"
        text = text + "  all kinds of assets and liabilities. The method simply adds all kinds of assets  \n"
        text = text + "  and stores them in one volume. As our firms holds 250.0 assets \n"
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
        environment.firms.append(firm)
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
                                account = account + firm.get_account(type)
                                print("L = " + str(account))
                        if type == "cash":
                                account = account + firm.get_account(type)
                                print("L+M = " + str(account))
                        if type == "goods":
                                account = account + firm.get_account(type)
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
        text = text + "  The purpose of this method is to count the numbers of transaction for   \n"
        text = text + "  accounts firms hold. Our standard frm has 3 transactions by default. \n"
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
        environment.firms.append(firm)
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
                                num_transactions = num_transactions + firm.get_account_num_transactions(type)
                                print("L = " + str(num_transactions))
                        if type == "cash":
                                num_transactions = num_transactions + firm.get_account_num_transactions(type)
                                print("L+M = " + str(num_transactions))
                        if type == "goods":
                                num_transactions = num_transactions + firm.get_account_num_transactions(type)
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
        text = text + "  The most simple way to test this function is to assign an new    \n"
        text = text + "  transaction to our firm. Therefore, lets just assign the following  \n"
        text = text + "  transaction and check whether it has been added: \n"
        text = text + '  (type = "deposits",  fromID = -1,  toID = firm.identifier,  amount = 10,  \n'
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
        environment.firms.append(firm)
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        print(firm)
        print("Adding new transaction: \n")
        firm.add_transaction("deposits", "", environment.households[0:1][0],
                             firm.identifier,  10,  0.09,  0, -1, environment)
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
        environment.firms.append(firm)
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
                             firm.identifier, 0.0,  0.09,  0, -1, environment)
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
        text = text + "  Checking if after the purge_accounts the total amount    \n"
        text = text + "  of transactions in the firm stays the same.  \n"
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
        environment.firms.append(firm)
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
                             firm.identifier, 0.0,  0.09,  0, -1, environment)
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

        firm.accounts[0].purge_accounts(environment)

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
        environment.firms.append(firm)
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        print(firm)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__get_transactions_from_file
    # -------------------------------------------------------------------------

    def firm__get_transactions_from_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.get_transactions_from_file \n"
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
        logging.info('START logging for test firm__get_transactions_from_file in run: %s',
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
        environment.firms.append(firm)

        #
        # TESTING
        #

        environment.firms[0].clear_accounts()
        print("Printing firm:\n")
        print(environment.firms[0])
        print("Reading transactions from the config file.\n")
        print("Printing firm: \n")
        firm.get_transactions_from_file(firm_directory + listing[0], environment)
        print(environment.firms[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # firm__getattr
    # -------------------------------------------------------------------------

    def firm__getattr(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks firm.getattr \n"
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
        logging.info('START logging for test firm__getattr in run: %s',
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
        environment.firms.append(firm)
        helper = Helper()
        helper.initialize_standard_firm(firm, environment)

        #
        # TESTING
        #

        print('Accessing rates through firm.parameters["productivity"] :')
        print(firm.parameters["productivity"])
        print("Accessing rates through firm.productivity:")
        print(firm.productivity)

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
        text = text + environment.identifier
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
        text = text + environment.identifier
        print(text)
        print("Changing identifier to XYZ")
        environment.set_identifier("XYZ")
        text = "Identifier: "
        text = text + environment.identifier
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
        text = text + str(environment.num_banks)
        print(text)
        text = "Number of banks read: "
        text = text + str(len(environment.banks))
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
        text = text + str(environment.num_firms)
        print(text)
        text = "Number of firms read: "
        text = text + str(len(environment.firms))
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
        text = text + str(environment.num_households)
        print(text)
        text = "Number of households read: "
        text = text + str(len(environment.households))
        print(text)
        print("The households read: ")
        for i in range(0, int(environment.num_households)):
            print(environment.households[i].__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__get_agent_by_id
    # -------------------------------------------------------------------------

    def environment__get_agent_by_id(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.get_agent_by_id \n"
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
        logging.info('START logging for test environment__get_agent_by_id in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print("Getting a bank with id: bank_test_config_id")
        print(environment.get_agent_by_id("bank_test_config_id"))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__read_transactions_for_banks
    # -------------------------------------------------------------------------

    def environment__read_transactions_for_banks(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.read_transactions_for_banks \n"
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
        logging.info('START logging for test environment__read_transactions_for_banks in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Clearing accounts of the bank:")
        environment.banks[0].clear_accounts()  # let's use the first bank
        print(environment.banks[0])
        print("Reading transactions: ")
        environment.read_transactions_for_banks(environment.bank_directory)
        print(environment.banks[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__read_transactions_for_firms
    # -------------------------------------------------------------------------

    def environment__read_transactions_for_firms(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.read_transactions_for_firms \n"
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
        logging.info('START logging for test environment__read_transactions_for_firms in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Clearing accounts of the firm:")
        environment.firms[0].clear_accounts()  # let's use the first bank
        print(environment.firms[0])
        print("Reading transactions: ")
        environment.read_transactions_for_firms(environment.firm_directory)
        print(environment.firms[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__read_transactions_for_households
    # -------------------------------------------------------------------------

    def environment__read_transactions_for_households(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.read_transactions_for_households \n"
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
        logging.info('START logging for test environment__read_transactions_for_households in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Clearing accounts of the household:")
        environment.households[0].clear_accounts()  # let's use the first bank
        print(environment.households[0])
        print("Reading transactions: ")
        environment.read_transactions_for_banks(environment.bank_directory)  # deposits are saved in bank config files only
        # environment.read_transactions_for_households(environment.household_directory)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__check_global_transaction_balance
    # -------------------------------------------------------------------------

    def environment__check_global_transaction_balance(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.check_global_transaction_balance \n"
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
        logging.info('START logging for test environment__check_global_transaction_balance in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Checking global consistency of deposits:")
        if environment.check_global_transaction_balance("deposits") == True:
            print("Consistent")
        else:
            print("Not consistent")
        # environment.banks[0].add_transaction("deposits", "", environment.households[0:1][0],
        #                                      environment.banks[0].identifier, 150, environment.banks[0].interest_rate_deposits, 0, -1)
        # print("Checking global consistency of deposits:")
        # if environment.check_global_transaction_balance("deposits") == True:
        #     print("Consistent")
        # else:
        #     print("Not consistent")

    # -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR TRANSACTION.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__init
    # -------------------------------------------------------------------------

    def transaction__init(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.init \n"
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
        logging.info('START logging for test transaction__init in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction \n")
        transaction = Transaction()
        print("Transaction ID: ")
        print(transaction.identifier)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__del
    # -------------------------------------------------------------------------

    def transaction__del(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.del \n"
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
        logging.info('START logging for test transaction__del in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Transaction exists? ")
        print("transaction" in locals())
        print("Deleting the transaction")
        del transaction
        print("Transaction exists? ")
        print("transaction" in locals())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__get_type_
    # -------------------------------------------------------------------------

    def transaction__get_type_(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.get_type_ \n"
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
        logging.info('START logging for test transaction__get_type_ in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.type_ = "test_type"
        print("Type: ")
        print(transaction.get_type_())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__set_type_
    # -------------------------------------------------------------------------

    def transaction__set_type_(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.set_type_ \n"
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
        logging.info('START logging for test transaction__set_type_ in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.type_ = "test_type"
        print("Type: ")
        print(transaction.get_type_())
        print("Setting type")
        transaction.set_type_("new_type")
        print("Type: ")
        print(transaction.get_type_())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__get_asset
    # -------------------------------------------------------------------------

    def transaction__get_asset(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.get_asset \n"
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
        logging.info('START logging for test transaction__get_asset in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.asset = "test_asset"
        print("Asset: ")
        print(transaction.get_asset())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__set_asset
    # -------------------------------------------------------------------------

    def transaction__set_asset(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.set_asset \n"
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
        logging.info('START logging for test transaction__set_asset in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.asset = "test_asset"
        print("Asset: ")
        print(transaction.get_asset())
        print("Setting asset")
        transaction.set_asset("new_asset")
        print("Asset: ")
        print(transaction.get_asset())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__get_from_
    # -------------------------------------------------------------------------

    def transaction__get_from_(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.get_from_ \n"
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
        logging.info('START logging for test transaction__get_from_ in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.from_ = "test_from"
        print("From: ")
        print(transaction.get_from_())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__set_from_
    # -------------------------------------------------------------------------

    def transaction__set_from_(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.set_from_ \n"
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
        logging.info('START logging for test transaction__set_from_ in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.from_ = "test_from"
        print("From: ")
        print(transaction.get_from_())
        print("Setting from")
        transaction.set_from_("new_from")
        print("From: ")
        print(transaction.get_from_())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__get_to
    # -------------------------------------------------------------------------

    def transaction__get_to(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.get_to \n"
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
        logging.info('START logging for test transaction__get_to in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.to = "test_to"
        print("To: ")
        print(transaction.get_to())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__set_to
    # -------------------------------------------------------------------------

    def transaction__set_to(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.set_to \n"
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
        logging.info('START logging for test transaction__set_to in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.to = "test_to"
        print("To: ")
        print(transaction.get_to())
        print("Setting to")
        transaction.set_to("new_to")
        print("To: ")
        print(transaction.get_to())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__get_amount
    # -------------------------------------------------------------------------

    def transaction__get_amount(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.get_amount \n"
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
        logging.info('START logging for test transaction__get_amount in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.amount = 15.0
        print("Amount: ")
        print(transaction.get_amount())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__set_amount
    # -------------------------------------------------------------------------

    def transaction__set_amount(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.set_amount \n"
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
        logging.info('START logging for test transaction__set_amount in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.amount = 15.0
        print("Amount: ")
        print(transaction.get_amount())
        print("Setting amount")
        transaction.set_amount(25.0)
        print("Amount: ")
        print(transaction.get_amount())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__get_interest
    # -------------------------------------------------------------------------

    def transaction__get_interest(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.get_interest \n"
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
        logging.info('START logging for test transaction__get_interest in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.interest = 0.01
        print("Interest: ")
        print(transaction.get_interest())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__set_amount
    # -------------------------------------------------------------------------

    def transaction__set_interest(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.set_interest \n"
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
        logging.info('START logging for test transaction__set_interest in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.interest = 0.01
        print("Interest: ")
        print(transaction.get_interest())
        print("Setting interest")
        transaction.set_interest(0.02)
        print("Interest: ")
        print(transaction.get_interest())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__get_maturity
    # -------------------------------------------------------------------------

    def transaction__get_maturity(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.get_maturity \n"
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
        logging.info('START logging for test transaction__get_maturity in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.maturity = 1
        print("Maturity: ")
        print(transaction.get_maturity())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__set_maturity
    # -------------------------------------------------------------------------

    def transaction__set_maturity(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.set_maturity \n"
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
        logging.info('START logging for test transaction__set_maturity in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.maturity = 1
        print("Maturity: ")
        print(transaction.get_maturity())
        print("Setting maturity")
        transaction.set_maturity(2)
        print("Maturity: ")
        print(transaction.get_maturity())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__get_time_of_default
    # -------------------------------------------------------------------------

    def transaction__get_time_of_default(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.get_time_of_default \n"
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
        logging.info('START logging for test transaction__get_time_of_default in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.time_of_default = 1
        print("Time of default: ")
        print(transaction.get_time_of_default())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__set_time_of_default
    # -------------------------------------------------------------------------

    def transaction__set_time_of_default(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.set_time_of_default \n"
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
        logging.info('START logging for test transaction__set_time_of_default in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        transaction.time_of_default = 1
        print("Time of default: ")
        print(transaction.get_time_of_default())
        print("Setting time of default")
        transaction.set_time_of_default(2)
        print("Time of default: ")
        print(transaction.get_time_of_default())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__this_transaction
    # -------------------------------------------------------------------------

    def transaction__this_transaction(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.this_transaction \n"
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
        logging.info('START logging for test transaction__this_transaction in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "from", "to", 1,  2,  3, 4)
        print("The transaction:")
        print(transaction)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__add_transaction
    # -------------------------------------------------------------------------

    def transaction__add_transaction(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.add_transaction \n"
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
        logging.info('START logging for test transaction__add_transaction in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "test_household", "test_firm", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(environment)
        print("The transaction:")
        print(transaction)
        print("The firm:")
        print(environment.get_agent_by_id("test_firm"))
        print("The household:")
        print(environment.get_agent_by_id("test_household"))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__remove_transaction
    # -------------------------------------------------------------------------

    def transaction__remove_transaction(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.remove_transaction \n"
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
        logging.info('START logging for test transaction__remove_transaction in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "test_household", "test_firm", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(environment)
        print("The transaction:")
        print(transaction)
        print("The firm:")
        print(environment.get_agent_by_id("test_firm"))
        print("The household:")
        print(environment.get_agent_by_id("test_household"))
        print("Removing the transaction")
        transaction.remove_transaction()
        print("The transaction:")
        print(transaction)
        print("The firm:")
        print(environment.get_agent_by_id("test_firm"))
        print("The household:")
        print(environment.get_agent_by_id("test_household"))
        print("Removing the transaction")

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__print_transaction
    # -------------------------------------------------------------------------

    def transaction__print_transaction(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.print_transaction \n"
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
        logging.info('START logging for test transaction__print_transaction in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "test_household", "test_firm", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(environment)
        print("Printing transaction:")
        transaction.print_transaction()

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__str
    # -------------------------------------------------------------------------

    def transaction__str(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.str \n"
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
        logging.info('START logging for test transaction__str in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "test_household", "test_firm", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(environment)
        print("Printing transaction:")
        print(transaction.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__write_transaction
    # -------------------------------------------------------------------------

    def transaction__write_transaction(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.write_transaction \n"
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
        logging.info('START logging for test transaction__write_transaction in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "test_household", "test_firm", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(environment)
        print("Printing transaction:")
        print(transaction.write_transaction())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__clear_accounts
    # -------------------------------------------------------------------------

    def transaction__clear_accounts(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.clear_accounts \n"
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
        logging.info('START logging for test transaction__clear_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        # bank = Bank()
        # bank.identifier = "test_bank"
        # environment.banks.append(bank)

        # generate a firm
        # firm = Firm()
        # firm.identifier = "test_firm"
        # environment.firms.append(firm)

        # generate a household
        # household = Household()
        # household.identifier = "test_household"
        # environment.households.append(household)

        #
        # TESTING
        #

        print("Before clearing one bank's accounts")
        for bank in environment.banks:
            print(bank)
        for household in environment.households:
            print(household)
        environment.get_agent_by_id("bank_test_config_id").clear_accounts()
        print("After clearing one bank's accounts")
        for bank in environment.banks:
            print(bank)
        for household in environment.households:
            print(household)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__purge_accounts
    # -------------------------------------------------------------------------

    def transaction__purge_accounts(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction

        text = "This test checks transaction.purge_accounts \n"
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
        logging.info('START logging for test transaction__purge_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        print("Before purging the accounts")
        transaction = Transaction()
        transaction.this_transaction("type", "asset", "test_household", "test_firm", 0,  2,  3, 4)
        transaction.add_transaction(environment)
        print(environment.get_agent_by_id("test_household"))
        print(environment.get_agent_by_id("test_firm"))
        print("After clearing one bank's accounts")
        transaction.purge_accounts(environment)
        print(environment.get_agent_by_id("test_household"))
        print(environment.get_agent_by_id("test_firm"))

    # -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR UPDATER.PY >> PAWEL TO DO <<
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR MARKET.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__get_identifier
    # -------------------------------------------------------------------------

    def market__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.get_identifier \n"
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
        logging.info('START logging for test market__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market_id")
        print("Market's ID:")
        print(market.get_identifier())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__set_identifier
    # -------------------------------------------------------------------------

    def market__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.set_identifier \n"
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
        logging.info('START logging for test market__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market_id")
        print("Market's ID:")
        print(market.get_identifier())
        print("Changing ID")
        market.set_identifier("new_market_id")
        print("Market's ID:")
        print(market.get_identifier())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__get_tolerance
    # -------------------------------------------------------------------------

    def market__get_tolerance(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.get_tolerance \n"
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
        logging.info('START logging for test market__get_tolerance in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market_id")
        print("Market's tolerance:")
        print(market.get_tolerance())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__set_tolerance
    # -------------------------------------------------------------------------

    def market__set_tolerance(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.set_tolerance \n"
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
        logging.info('START logging for test market__set_tolerance in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market_id")
        print("Market's tolerance:")
        print(market.get_tolerance())
        print("Changing tolerance")
        market.set_tolerance(0.55)
        print("Market's tolerance:")
        print(market.get_tolerance())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__get_resolution
    # -------------------------------------------------------------------------

    def market__get_resolution(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.get_resolution \n"
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
        logging.info('START logging for test market__get_resolution in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market_id")
        print("Market's resolution:")
        print(market.get_resolution())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__set_resolution
    # -------------------------------------------------------------------------

    def market__set_resolution(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.set_resolution \n"
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
        logging.info('START logging for test market__set_resolution in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market_id")
        print("Market's resolution:")
        print(market.get_resolution())
        print("Changing resolution")
        market.set_resolution(0.55)
        print("Market's resolution:")
        print(market.get_resolution())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__get_amplification
    # -------------------------------------------------------------------------

    def market__get_amplification(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.get_amplification \n"
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
        logging.info('START logging for test market__get_amplification in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market_id")
        print("Market's amplification:")
        print(market.get_amplification())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__set_amplification
    # -------------------------------------------------------------------------

    def market__set_amplification(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.set_amplification \n"
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
        logging.info('START logging for test market__set_amplification in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market_id")
        print("Market's amplification:")
        print(market.get_amplification())
        print("Changing amplification")
        market.set_amplification(0.55)
        print("Market's amplification:")
        print(market.get_amplification())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__tatonnement
    # -------------------------------------------------------------------------

    def market__tatonnement(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.tatonnement \n"
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
        logging.info('START logging for test market__tatonnement in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        sellers = []
        for agent in environment.households:
            sellers.append([agent, agent.supply_of_labour])
        buyers = []
        for agent in environment.firms:
            buyers.append([agent, agent.demand_for_labour])
        starting_price = 0.0
        price = 0.0
        market = Market("market")
        price = market.tatonnement(sellers, buyers, starting_price, 0.00000001, 0.01, 1.1)
        print("Price found through tatonnement:")
        print(price)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__rationing
    # -------------------------------------------------------------------------

    def market__rationing(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.rationing \n"
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
        logging.info('START logging for test market__rationing in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market")
        rationed = market.rationing([["agent1", 5], ["agent2", 7], ["agent3", -3], ["agent4", -4]])
        print("Pairs found through rationing:")
        print(rationed)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__rationing_proportional
    # -------------------------------------------------------------------------

    def market__rationing_proportional(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.rationing_proportional \n"
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
        logging.info('START logging for test market__rationing_proportional in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #
        market = Market("market")
        rationed = market.rationing_proportional([["agent1", 5], ["agent2", 7], ["agent3", -3], ["agent4", -4]])
        print("Pairs found through proportional rationing:")
        print(rationed)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # market__rationing_abstract
    # -------------------------------------------------------------------------

    def market__rationing_abstract(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market

        text = "This test checks market.rationing_abstract \n"
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
        logging.info('START logging for test market__rationing_abstract in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        def matching_agents_basic(agent_one, agent_two):
            import difflib
            seq = difflib.SequenceMatcher(a=agent_one.lower(), b=agent_two.lower())
            return seq.ratio()

        def matching_agents_basic_inv(agent_one, agent_two):
            import difflib
            seq = difflib.SequenceMatcher(a=agent_one.lower(), b=agent_two.lower())
            return 1-seq.quick_ratio()

        def allow_match_basic(agent_one, agent_two):
            return True

            def allow_match_basic(agent_one, agent_two):
                if ((agent_one == 'aaaaaa' and agent_two == 'aaaabb') or (agent_one == 'aaaabb' and agent_two == 'aaaaaa')):
                    return False
                else:
                    return True

        market = Market("market")
        rationed = market.rationing_abstract([["aaaaaa", 5], ["bbbbbb", 7], ["aaaabb", -3], ["aabbbb", -4]], matching_agents_basic, allow_match_basic)
        print("Pairs found through abstract rationing prioritising similar names:")
        print(rationed)
        rationed = market.rationing_abstract([["aaaaaa", 5], ["bbbbbb", 7], ["aaaabb", -3], ["aabbbb", -4]], matching_agents_basic_inv, allow_match_basic)
        print("Pairs found through abstract rationing prioritising dissimilar names:")
        print(rationed)
        rationed = market.rationing_abstract([["aaaaaa", 5], ["bbbbbb", 7], ["aaaabb", -3], ["aabbbb", -4]], matching_agents_basic_inv, allow_match_basic)
        print("Pairs found through abstract rationing prioritising similar names with 'aaaaaa'>'aaaabb' not allowed:")
        print(rationed)

    # -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR RUNNER.PY >> TINA TO DO <<
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR MEASUREMENT.PY >> PAWEL TO DO <<
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR HELPER.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # helper__initialize_standard_bank
    # -------------------------------------------------------------------------

    def helper__initialize_standard_bank(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.helper import Helper

        text = "This test checks helper.initialize_standard_bank \n"
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
        logging.info('START logging for test helper__initialize_standard_bank in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        # bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        helper = Helper()
        helper.initialize_standard_bank(bank, environment)
        print("Initialized standard bank")
        print(bank)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # helper__initialize_standard_firm
    # -------------------------------------------------------------------------

    def helper__initialize_standard_firm(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.helper import Helper

        text = "This test checks helper.initialize_standard_firm \n"
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
        logging.info('START logging for test helper__initialize_standard_firm in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a firm
        firm = Firm()
        # firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        helper = Helper()
        helper.initialize_standard_firm(firm, environment)
        print("Initialized standard firm")
        print(firm)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # helper__initialize_standard_household
    # -------------------------------------------------------------------------

    def helper__initialize_standard_household(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.helper import Helper

        text = "This test checks helper.initialize_standard_household \n"
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
        logging.info('START logging for test helper__initialize_standard_household in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

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
        # household.identifier = "test_household"
        environment.households.append(household)

        #
        # TESTING
        #

        helper = Helper()
        helper.initialize_standard_household(household, environment)
        print("Initialized standard household")
        print(household)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # helper__cobb_douglas
    # -------------------------------------------------------------------------

    def helper__cobb_douglas(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.helper import Helper

        text = "This test checks helper.cobb_douglas \n"
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
        logging.info('START logging for test helper__cobb_douglas in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        helper = Helper()
        production = helper.cobb_douglas(3, 2, 1.2, 0.5, 0.5)
        print("Calculating production in Cobb-Douglas:")
        print(production)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # helper__leontief
    # -------------------------------------------------------------------------

    def helper__leontief(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.helper import Helper

        text = "This test checks helper.leontief \n"
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
        logging.info('START logging for test helper__leontief in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        helper = Helper()
        production = helper.leontief([3, 2], [1.2, 0.5])
        print("Calculating production in Leontief:")
        print(production)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # helper__ces
    # -------------------------------------------------------------------------

    def helper__ces(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.helper import Helper

        text = "This test checks helper.ces \n"
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
        logging.info('START logging for test helper__ces in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        helper = Helper()
        production = helper.ces(3, 2, 0.5, 0.7)
        print("Calculating production in CES:")
        print(production)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # helper__translog
    # -------------------------------------------------------------------------

    def helper__translog(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.helper import Helper

        text = "This test checks helper.translog \n"
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
        logging.info('START logging for test helper__translog in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        helper = Helper()
        production = helper.translog(3, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5)
        print("Calculating production in translog:")
        print(production)

    # -------------------------------------------------------------------------
