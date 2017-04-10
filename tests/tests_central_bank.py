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


class TestsCentralBank(object):
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
#  TESTS FOR CENTRAL_BANK.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__get_identifier
    # -------------------------------------------------------------------------

    def central_bank__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.get_identifier \n"
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
        logging.info('START logging for test central_bank__get_identifier in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        text = "Identifier: "
        text = text + cb.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__set_identifier
    # -------------------------------------------------------------------------

    def central_bank__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.set_identifier \n"
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
        logging.info('START logging for test central_bank__set_identifier in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        text = "Original identifier: "
        text = text + cb.get_identifier()
        print(text)
        cb.set_identifier("new_ident")
        text = "New identifier: "
        text = text + cb.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__get_parameters
    # -------------------------------------------------------------------------

    def central_bank__get_parameters(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.get_parameters \n"
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
        logging.info('START logging for test central_bank__get_parameters in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        text = "Parameters:"
        print(text)
        print(cb.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__set_parameters
    # -------------------------------------------------------------------------

    def central_bank__set_parameters(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.set_parameters \n"
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
        logging.info('START logging for test central_bank__set_parameters in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        text = "Original parameters:"
        print(text)
        print(cb.get_parameters())
        text = "New parameters:"
        print(text)
        cb.set_parameters({'rd': 0.44, 'rl': 0.55, 'active': 1})
        print(cb.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__get_state_variables
    # -------------------------------------------------------------------------

    def central_bank__get_state_variables(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.get_state_variables \n"
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
        logging.info('START logging for test central_bank__get_state_variables in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        text = "State variables:"
        print(text)
        print(cb.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__set_state_variables
    # -------------------------------------------------------------------------

    def central_bank__set_state_variables(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.set_state_variables \n"
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
        logging.info('START logging for test central_bank__set_state_variables in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        text = "Original state variables:"
        print(text)
        print(cb.get_state_variables())
        text = "New state variables:"
        print(text)
        cb.set_state_variables({'test': 0.66})
        print(cb.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__str
    # -------------------------------------------------------------------------

    def central_bank__str(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.str \n"
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
        logging.info('START logging for test central_bank__str in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        print(cb.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__get_parameters_from_file
    # -------------------------------------------------------------------------

    def central_bank__get_parameters_from_file(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.get_parameters_from_file \n"
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
        logging.info('START logging for test central_bank__get_parameters_from_file in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        # test whether the parameters are read properly
        text = "Identifier has been read as follows: \n"
        text = text + "Identifier: "
        text = text + cb.identifier
        text = text + "\n"
        self.print_info(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__check_consistency
    # -------------------------------------------------------------------------

    def central_bank__check_consistency(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.check_consitency \n"
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
        logging.info('START logging for test central_bank__check_consistency in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        print("Checking consistency of the central bank: ")
        print(cb.check_consistency())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__get_account
    # -------------------------------------------------------------------------

    def central_bank__get_account(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.get_account \n"
        text = text + "  The method simply adds all kinds of assets and stores  \n"
        text = text + "  them in one volume. The central banks holds 600 in assets. \n"
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
        logging.info('START logging for test central_bank__get_account in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        environment.new_transaction("deposits", "",  cb.identifier, "test_firm",
                                    100, 0.0,  0, -1)
        environment.new_transaction("cash", "",  cb.identifier, "test_firm",
                                    200, 0.0,  0, -1)
        environment.new_transaction("loans", "",  cb.identifier, "test_firm",
                                    300, 0.0,  0, -1)

        account = 0.0                                           # counting all types in account together
        print(cb)                                              # and checking how much is the total
        # volume of the account
        for type in ["deposits",  "cash",  "loans"]:
                        if type == "deposits":
                                account = account + cb.get_account(type)
                                print("D = " + str(account))
                        if type == "cash":
                                account = account + cb.get_account(type)
                                print("D+M = " + str(account))
                        if type == "loans":
                                account = account + cb.get_account(type)
                                print("D+M+L = " + str(account))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__get_account_num_transactions
    # -------------------------------------------------------------------------

    def central_bank__get_account_num_transactions(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.get_account_num_transactions \n"
        text = text + "  The purpose of this method is to count the numbers of transaction for   \n"
        text = text + "  accounts banks hold. Our central bank has 3 transactions by default. \n"
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
        logging.info('START logging for test central_bank__get_account_num_transactions in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        environment.new_transaction("deposits", "",  cb.identifier, "test_firm",
                                    100, 0.0,  0, -1)
        environment.new_transaction("cash", "",  cb.identifier, "test_firm",
                                    200, 0.0,  0, -1)
        environment.new_transaction("loans", "",  cb.identifier, "test_firm",
                                    300, 0.0,  0, -1)

        num_transactions = 0.0          # counting all types in account together
        print(cb)
        # and checking if the number of transaction
        # is increasing by one
        for type in ["deposits",  "cash",  "loans"]:
                        if type == "deposits":
                                num_transactions = num_transactions + cb.get_account_num_transactions(type)
                                print("D = " + str(num_transactions))
                        if type == "cash":
                                num_transactions = num_transactions + cb.get_account_num_transactions(type)
                                print("D+M = " + str(num_transactions))
                        if type == "loans":
                                num_transactions = num_transactions + cb.get_account_num_transactions(type)
                                print("D+M+L = " + str(num_transactions))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__add_transaction
    # -------------------------------------------------------------------------

    def central_bank__add_transaction(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.add_transaction \n"
        text = text + "  The most simple way to test this function is to assign an new    \n"
        text = text + "  transaction to central bank. Therefore, lets just assign the following  \n"
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
        logging.info('START logging for test central_bank__add_transaction in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        print(cb)
        print("Adding new transaction: \n")
        print(environment.get_agent_by_id(cb.identifier))
        cb.add_transaction("deposits", "", "test_household",
                           cb.identifier,  10,  0.09,  0, -1, environment)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down
        print(cb)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__clear_accounts
    # -------------------------------------------------------------------------

    def central_bank__clear_accounts(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.clear_accounts \n"
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
        logging.info('START logging for test central_bank__clear_accounts in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in cb.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        cb.add_transaction("deposits", "", "test_household",
                           cb.identifier, 0.0,  0.09,  0, -1, environment)
        cb.add_transaction("deposits", "", "test_household",
                           cb.identifier, 20.0,  0.09,  0, -1, environment)

        account = 0.0
        tranx = 0

        for transaction in cb.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        cb.clear_accounts(environment)

        account = 0.0
        tranx = 0

        for transaction in cb.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__purge_accounts
    # -------------------------------------------------------------------------

    def central_bank__purge_accounts(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.purge_accounts \n"
        text = text + "  Checking if after the purge_accounts the total amount    \n"
        text = text + "  of transactions in the central bank stays the same.  \n"
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
        logging.info('START logging for test central_bank__purge_accounts in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in cb.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        cb.add_transaction("deposits", "", "test_household",
                           cb.identifier, 0.0,  0.09,  0, -1, environment)
        cb.add_transaction("deposits", "", "test_household",
                           cb.identifier, 20.0,  0.09,  0, -1, environment)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down

        account = 0.0
        tranx = 0

        for transaction in cb.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        cb.accounts[0].purge_accounts(environment)

        account = 0.0
        tranx = 0

        for transaction in cb.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__get_transactions_from_file
    # -------------------------------------------------------------------------

    def central_bank__get_transactions_from_file(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.get_transactions_from_file \n"
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
        logging.info('START logging for test central_bank__get_transactions_from_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        central_bank_directory = environment.central_bank_directory
        # and loop over all banks in the directory
        listing = os.listdir(central_bank_directory)
        central_bank_filename = central_bank_directory + listing[0]

        # generate a household
        household = Household()
        household.identifier = "test_household"
        environment.households.append(household)

        # generate a firm
        firm = Firm()
        firm.identifier = "test_firm"
        environment.firms.append(firm)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        environment.central_bank[0].clear_accounts(environment)
        print("Printing central bank: \n")
        print(environment.central_bank[0])
        print("Reading transactions from the config file.\n")
        print("Printing bank: \n")
        cb.get_transactions_from_file(central_bank_directory + listing[0], environment)
        print(environment.central_bank[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # central_bank__getattr
    # -------------------------------------------------------------------------

    def central_bank__getattr(self, args):
        import os
        from src.bank import Bank
        from src.central_bank import CentralBank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the bankDirectory

        text = "This test checks central_bank.getattr \n"
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
        logging.info('START logging for test central_bank__getattr in run: %s',
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

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        environment.banks.append(bank)

        # generate a central bank
        cb = CentralBank()
        cb.identifier = "test_central_bank"
        environment.central_bank.append(cb)

        #
        # TESTING
        #

        print('Accessing rates through bank.parameters["interest_rate_cb_loans"] :')
        print(cb.parameters["interest_rate_cb_loans"])
        print("Accessing rates through bank.interest_rate_cb_loans:")
        print(cb.interest_rate_cb_loans)

    # -------------------------------------------------------------------------
