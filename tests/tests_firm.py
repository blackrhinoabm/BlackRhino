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


class TestsFirm(object):
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

        firm.clear_accounts(environment)

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

        environment.firms[0].clear_accounts(environment)
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
