#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
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
        print '##############################################################################\n'
        print text
        print '##############################################################################\n'
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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__get_identifier in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__set_identifier in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__get_parameters in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__set_parameters in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__get_state_variables in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__set_state_variables in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__str in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__get_parameters_from_file in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

        # generate a household
        household = Household()
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        environment.firms.append(firm)

        # generate the bank
        bank = Bank()
        bank.get_parameters_from_file(bankFilename, environment)

        # test whether the parameters are read properly
        text = "Identifier, interest rate on deposits and loans have been read as follows: \n"
        text += "Identifier: "
        text += bank.identifier
        text += "\n"
        text += "Rate on loans: "
        text += str(bank.parameters["rl"])
        text += "\n"
        text += "Rate on deposits: "
        text += str(bank.parameters["rd"])
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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__check_consistency in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

        print("Checking consistency of the standard bank: ")
        print(bank.check_consistency())
        print("Adding additional deposits without adding appropriate cash/loans.")
        bank.add_transaction("D",  environment.households[0:1][0],  bank.identifier,  150,  bank.parameters["rd"],  0, -1)
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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__get_account in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

        account = 0.0                                           # counting all types in account together
        print bank                                              # and checking how much is the total
        # volume of the account
        for type in ["D",  "M",  "L"]:
                        if type == "D":
                                account += bank.get_account(type)
                                print "D = " + str(account)
                        if type == "M":
                                account += bank.get_account(type)
                                print "D+M = " + str(account)
                        if type == "L":
                                account += bank.get_account(type)
                                print "D+M+L = " + str(account)

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__get_account_num_transactions in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

        num_transactions = 0.0          # counting all types in account together
        print(bank)
        # and checking if the number of transaction
        # is increasing by one
        for type in ["D",  "M",  "L"]:
                        if type == "D":
                                num_transactions += bank.get_account_num_transactions(type)
                                print "D = " + str(num_transactions)
                        if type == "M":
                                num_transactions += bank.get_account_num_transactions(type)
                                print "D+M = " + str(num_transactions)
                        if type == "L":
                                num_transactions += bank.get_account_num_transactions(type)
                                print "D+M+L = " + str(num_transactions)

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
        text += '  (type = "D",  fromID = -1,  toID = bank.identifier,  value = 10,  \n'
        text += "   interest = 0.09, maturity = 0, timeOfDefault = -1) \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__add_transaction in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

        print(bank)
        print("Adding new transaction: \n")
        bank.add_transaction("D",  environment.households[0:1][0],  bank.identifier,  10,  0.09,  0, -1)
        print bank

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__clear_accounts in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.transactionValue
            tranx = tranx + 1

        print tranx
        print account

        bank.add_transaction("D", environment.households[0:1][0],  bank.identifier, 0.0,  0.09,  0, -1)

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.transactionValue
            tranx = tranx + 1

        print tranx
        print account

        bank.clear_accounts()

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.transactionValue
            tranx = tranx + 1

        print tranx
        print account

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__purge_accounts in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.transactionValue
            tranx = tranx + 1

        print tranx
        print account

        bank.add_transaction("D", environment.households[0:1][0],  bank.identifier, 0.0,  0.09,  0, -1)

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.transactionValue
            tranx = tranx + 1

        print tranx
        print account

        bank.purge_accounts()

        account = 0.0
        tranx = 0

        for transaction in bank.accounts:
            account = account + transaction.transactionValue
            tranx = tranx + 1

        print tranx
        print account

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__initialize_standard_bank in run: %s',  environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bankDirectory from the environment
        bankDirectory = environment.static_parameters["bankDirectory"]
        # and loop over all banks in the directory
        listing = os.listdir(bankDirectory)
        bankFilename = bankDirectory + listing[0]

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
        bank.initialize_standard_bank(environment)

        print(bank)

    # -------------------------------------------------------------------------

# BELOW IT'S THE OLD STUFF

# -------------------------------------------------------------------------
#  TESTS FOR ENVIRONMENT.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__initialize
    # -------------------------------------------------------------------------

    def environment__initialize(self, args):
        import os
        from src.bank import Bank
        from src.environment import Environment

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test environment__initialize in run: %s',  environment_directory + identifier + ".xml")

        # Construct  environment
        environment = Environment(environment_directory,  identifier)

        #
        # TEST CODE
        #
        # environment.initialize(environment_directory,  identifier)
        bankDirectory = environment.static_parameters["bankDirectory"]

        bank = Bank()
        account = 0.0

        for type in ["I"]:
                        if type == "I":
                                account += bank.get_account(type)
                                print "I = " + str(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__read_environment_file
    # -------------------------------------------------------------------------

    def environment__read_environment_file(self, args):
        text = "This test checks environment.read_environment_file \n"
        text += "  This is a function from the standard Python library \n"
        text += "  which does not really need to be tested therefore \n"
        self.print_info(text)

    # -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#  TESTS FOR NETWORK.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__do_interbank_trades
    # -------------------------------------------------------------------------
    def network__do_interbank_trades(self, args):
        from src.environment import Environment
        from src.updater import Updater

        #
        # INITIALIZATION
        #
        environment_directory = str(args[1])
        identifier = str(args[2])
        log_directory = str(args[3])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__do_interbank_trades in run: %s',  environment_directory + identifier + ".xml")

        #
        # TEST CODE
        #
        environment = Environment(environment_directory,  identifier)
        # create a test environment with standardised banks

        # print environment.banks[0]
        # print environment.banks[1]
        # print environment.banks[2]
        print environment.network
        environment.banks[0].parameters["Lp"] = 2.0
        environment.banks[1].parameters["Lp"] = -1.0
        environment.banks[2].parameters["Lp"] = -1.0
        environment.network.do_interbank_trades(environment.get_state(0))
        print environment.network
        environment.banks[0].parameters["Lp"] = 2.3
        environment.banks[1].parameters["Lp"] = -1.1
        environment.banks[2].parameters["Lp"] = -1.2
        environment.network.do_interbank_trades(environment.get_state(0))
        print environment.network

        # print environment.banks[0]
        # print environment.banks[1]
        # print environment.banks[2]

        #
        # MEASUREMENT AND LOGGING
        #
        logging.info('FINISHED logging for test updater__remove_inactive_bank in run: %s \n', environment_directory + identifier + ".xml")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__remove_inactive_bank
    # -------------------------------------------------------------------------
    def network__remove_inactive_bank(self, args):
        from src.environment import Environment
        from src.updater import Updater

        #
        # INITIALIZATION
        #
        environment_directory = str(args[1])
        identifier = str(args[2])
        log_directory = str(args[3])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__remove_inactive_banks in run: %s',  environment_directory + identifier + ".xml")

        #
        # TEST CODE
        #
        environment = Environment(environment_directory,  identifier)
        # environment.initialize(environment_directory,  identifier)
        # create a test environment with standardised banks

        # print environment.banks[0]
        # print environment.banks[1]
        # print environment.banks[2]
        environment.banks[0].parameters["Lp"] = 2.0
        environment.banks[1].parameters["Lp"] = -1.0
        environment.banks[2].parameters["Lp"] = -1.0
        environment.network.do_interbank_trades(environment.get_state(0))
        print environment.network

        updater = Updater(environment)

        #
        # execute the update code
        #
        environment.banks[0].reduce_banking_capital(2.0)
        environment.banks[0].check_solvency(environment, 'info', 0)
        environment.network.remove_inactive_bank(environment.banks[0], 0)

        # print environment.banks[0]
        # print environment.banks[1]
        # print environment.banks[2]
        print environment.network

        #
        # MEASUREMENT AND LOGGING
        #
        logging.info('FINISHED logging for test updater__remove_inactive_bank in run: %s \n', environment_directory + identifier + ".xml")
    # -------------------------------------------------------------------------

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
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

# -------------------------------------------------------------------------
#  UNKNOWN TESTS
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # test_fire_sales
    # -------------------------------------------------------------------------
    def test_fire_sales(self, args):  # TODO not consistent with other test names
        import logging
        import networkx as nx

        from src.environment import Environment
        from src.runner import Runner
        from src.measurement import Measurement

        #
        # INITIALIZATION
        #
        environment_directory = str(args[1])
        identifier = str(args[2])
        log_directory = str(args[3])
        measurement_directory = str(args[4])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for run: %s',  environment_directory + identifier + ".xml")

        environment = Environment(environment_directory,  identifier)
        # environment.initialize(environment_directory,  identifier)
        runner = Runner()
        measurement = Measurement()

        #
        # UPDATE STEP
        #
        for i in range(environment.static_parameters["numSimulations"]):
            environment.initialize(environment_directory,  identifier)
            runner.initialize(environment)
            measurement.initialize()  # clear the previous measurement

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
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # test_state
    # -------------------------------------------------------------------------
    def test_state(self, args):
        from src.environment import Environment
        from src.updater import Updater

        #
        # INITIALIZATION
        #
        environment_directory = str(args[1])
        identifier = str(args[2])
        log_directory = str(args[3])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__remove_inactive_banks in run: %s',  environment_directory + identifier + ".xml")

        #
        # TEST CODE
        #
        environment = Environment(environment_directory,  identifier)
        # environment.initialize(environment_directory,  identifier)
        # create a test environment with standardised banks

        #
        print environment.get_state(0)
        environment.banks[0].reduce_banking_capital(10.0)
        environment.banks[0].check_solvency(environment.get_state(0),  "info", 0)
        print environment.get_state(1)

        #
        # MEASUREMENT AND LOGGING
        #
        logging.info('FINISHED logging for test updater__remove_inactive_bank in run: %s \n', environment_directory + identifier + ".xml")
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # liquidate_assets
    # -------------------------------------------------------------------------
    def updater__liquidate_assets(self, args):
        from src.environment import Environment
        from src.updater import Updater

        #
        # INITIALIZATION
        #
        environment_directory = str(args[1])
        identifier = str(args[2])
        log_directory = str(args[3])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__liquidate_assets in run: %s',  environment_directory + identifier + ".xml")

        #
        # TEST CODE
        #
        environment = Environment(environment_directory,  identifier)
        # create a test environment with standardised banks

        print environment.banks[0]
        # print environment.banks[1]
        # print environment.banks[2]

        updater = Updater(environment)
        environment.banks[1].parameters["active"] = -1
        environment.banks[2].parameters["active"] = -1
        #
        # execute the update code
        #
        updater.do_update_phase1(environment, 0, "debug")
        updater.do_update_phase2(environment, 0, "info")

        print environment.banks[0]
        # print environment.banks[1]
        # print environment.banks[2]

        #
        # MEASUREMENT AND LOGGING
        #
        logging.info('FINISHED logging for test updater__liquidate_assets in run: %s \n', environment_directory + identifier + ".xml")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # bank__test1
    # -------------------------------------------------------------------------
    def bank__test1(self, args):
        from src.environment import Environment

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
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',  filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test bank__test1 in run: %s',  environment_directory + identifier + ".xml")

        #
        # TEST CODE
        #
        environment = Environment(environment_directory,  identifier)
        # environment.initialize(environment_directory,  identifier)

        # for bank in environment.banks:
        print environment.banks[2]
        print environment.network

        #
        # MEASUREMENT AND LOGGING
        #
        logging.info('FINISHED logging for test bank__test1 in run: %s \n', environment_directory + identifier + ".xml")
    # -------------------------------------------------------------------------
