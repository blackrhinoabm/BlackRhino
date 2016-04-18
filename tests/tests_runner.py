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


class TestsRunner(object):
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
#  TESTS FOR RUNNER.PY >> TINA TO DO <<
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # runner__init
    # -------------------------------------------------------------------------
    def runner__init__(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the Directory
        from src.runner import Runner

        text = "This test checks runner.__init__ \n"
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
        logging.info('START logging for test runner__init__ in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory for testing purpose (just one bank)
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

        # making an instance of the Runner class
        runner = Runner(environment)
        #
        # TESTING
        #

        text = "Identifier: "
        text = text + runner.get_identifier()
        print(text)

        text = "Number of sweeps:"
        text = text + str(runner.num_sweeps)
        print(text)

        text = "Updater"
        text = text + str(runner.updater)
        print(text)


    # -------------------------------------------------------------------------
    # runner__get_identifier
    # -------------------------------------------------------------------------

    def runner__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the Directory
        from src.runner import Runner

        text = "This test checks runner.get_identifier \n"
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
        logging.info('START logging for test runner__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory for testing purpose (just one bank)
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

        # making an instance of the Runner class
        runner = Runner(environment)

        #
        # TESTING
        #

        text = "Identifier: "
        text = text + runner.get_identifier()
        print(text)

    # -------------------------------------------------------------------------
    # runner__set_identifier
    # -------------------------------------------------------------------------
    def runner__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the Directory
        from src.runner import Runner

        text = "This test checks runner.set_identifier \n"
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
        logging.info('START logging for test runner__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory for testing purpose (just one bank)
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

        # making an instance of the Runner class
        runner = Runner(environment)
        #
        # TESTING
        #

        text = "Identifier: "
        text = text + runner.get_identifier()
        print(text)

        runner.set_identifier("new_identifier")

        text = "Print new Identifier:"
        text = text + runner.get_identifier()
        print(text)

    # -------------------------------------------------------------------------
    # runner__get_num_sweeps
    # -------------------------------------------------------------------------
    def runner__get_num_sweeps(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the Directory
        from src.runner import Runner

        text = "This test checks runner.get_num_sweeps \n"
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
        logging.info('START logging for test runner_get_num_sweeps in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory for testing purpose (just one bank)
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

        # making an instance of the Runner class
        runner = Runner(environment)
        #
        # TESTING
        #
        text = "Number of sweeps: "
        text = text + str(runner.get_num_sweeps())
        print(text)
    # -------------------------------------------------------------------------
    # testing set_num_sweeps
    # -------------------------------------------------------------------------

    def runner__set_num_sweeps(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the Directory
        from src.runner import Runner

        text = "This test checks runner.set_num_sweeps \n"
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
        logging.info('START logging for test runner_set_num_sweeps in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory for testing purpose (just one bank)
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

        # making an instance of the Runner class
        runner = Runner(environment)
        #
        # TESTING
        #
        text = "Number of sweeps: "
        text = text + str(runner.get_num_sweeps())
        print(text)

        runner.set_num_sweeps(666)

        text = "New number of sweeps: "
        text = text + str(runner.get_num_sweeps())
        print(text)

    # -------------------------------------------------------------------------
    # do_run
    # -------------------------------------------------------------------------

    def runner__do_run(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment  # needed for the Directory
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks runner.do_run \n"
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
        logging.info('START logging for test runner_do_run in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct bank filename
        environment = Environment(environment_directory,  identifier)

        # get the bank_directory from the environment
        bank_directory = environment.bank_directory
        # and loop over all banks in the directory for testing purpose (just one bank)
        listing = os.listdir(bank_directory)
        bank_filename = bank_directory + listing[0]


        # making an instance of the Runner class
        runner = Runner(environment)

        #
        # TESTING
        #
        runner.do_run(environment)








