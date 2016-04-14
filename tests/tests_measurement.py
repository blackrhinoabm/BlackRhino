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


class TestsMeasurement(object):
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
#  TESTS FOR MEASUREMENT.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__get_identifier
    # -------------------------------------------------------------------------

    def measurement__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.get_identifier \n"
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
        logging.info('START logging for test measurement__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's ID:")
        print(measurement.get_identifier())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__set_identifier
    # -------------------------------------------------------------------------

    def measurement__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.set_identifier \n"
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
        logging.info('START logging for test measurement__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's ID:")
        print(measurement.get_identifier())
        measurement.set_identifier("new_measurement_id")
        print("Measurement's ID:")
        print(measurement.get_identifier())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__get_config
    # -------------------------------------------------------------------------

    def measurement__get_config(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.get_config \n"
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
        logging.info('START logging for test measurement__get_config in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's config:")
        print(measurement.get_config())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__set_config
    # -------------------------------------------------------------------------

    def measurement__set_config(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.set_config \n"
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
        logging.info('START logging for test measurement__set_config in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's config:")
        print(measurement.get_config())
        measurement.set_config({"test": ["config"]})
        print("Measurement's config:")
        print(measurement.get_config())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__get_environment
    # -------------------------------------------------------------------------

    def measurement__get_environment(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.get_environment \n"
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
        logging.info('START logging for test measurement__get_environment in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's environment:")
        print(measurement.get_environment())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__set_environment
    # -------------------------------------------------------------------------

    def measurement__set_environment(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.set_environment \n"
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
        logging.info('START logging for test measurement__set_environment in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's environment:")
        print(measurement.get_environment())
        measurement.set_environment(runner)
        print("Measurement's environment:")
        print(measurement.get_environment())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__get_runner
    # -------------------------------------------------------------------------

    def measurement__get_runner(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.get_runner \n"
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
        logging.info('START logging for test measurement__get_runner in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's runner:")
        print(measurement.get_runner())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__set_runner
    # -------------------------------------------------------------------------

    def measurement__set_runner(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.set_runner \n"
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
        logging.info('START logging for test measurement__set_runner in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's runner:")
        print(measurement.get_runner())
        measurement.set_runner(environment)
        print("Measurement's runner:")
        print(measurement.get_runner())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__get_filename
    # -------------------------------------------------------------------------

    def measurement__get_filename(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.get_filename \n"
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
        logging.info('START logging for test measurement__get_filename in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's filename:")
        print(measurement.get_filename())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__set_filename
    # -------------------------------------------------------------------------

    def measurement__set_filename(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.set_filename \n"
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
        logging.info('START logging for test measurement__set_filename in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's filename:")
        print(measurement.get_filename())
        measurement.set_filename("TestFilename.csv")
        print("Measurement's filename:")
        print(measurement.get_filename())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__get_file
    # -------------------------------------------------------------------------

    def measurement__get_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.get_file \n"
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
        logging.info('START logging for test measurement__get_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's file:")
        print(measurement.get_file())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__set_file
    # -------------------------------------------------------------------------

    def measurement__set_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.set_file \n"
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
        logging.info('START logging for test measurement__set_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        file_new = open("__init__.py", "r")
        measurement = Measurement(environment, runner)
        print("Measurement's file:")
        print(measurement.get_file())
        measurement.set_file(file_new)
        print("Measurement's file:")
        print(measurement.get_file())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__get_csv_writer
    # -------------------------------------------------------------------------

    def measurement__get_csv_writer(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.get_csv_writer \n"
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
        logging.info('START logging for test measurement__get_csv_writer in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print("Measurement's csv_writer:")
        print(measurement.get_csv_writer())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__set_csv_writer
    # -------------------------------------------------------------------------

    def measurement__set_csv_writer(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.set_csv_writer \n"
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
        logging.info('START logging for test measurement__set_csv_writer in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        import csv
        file_new = open("__init__.py", "r")
        csv_writer = csv.writer(file_new, lineterminator='\n')
        measurement = Measurement(environment, runner)
        print("Measurement's csv_writer:")
        print(measurement.get_csv_writer())
        measurement.set_csv_writer(csv_writer)
        print("Measurement's csv_writer:")
        print(measurement.get_csv_writer())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__init
    # -------------------------------------------------------------------------

    def measurement__init(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.init \n"
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
        logging.info('START logging for test measurement__init in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        print(measurement)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__open_file
    # -------------------------------------------------------------------------

    def measurement__open_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.open_file \n"
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
        logging.info('START logging for test measurement__open_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        measurement.open_file()
        print(measurement.get_file())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__write_to_file
    # -------------------------------------------------------------------------

    def measurement__write_to_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.write_to_file \n"
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
        logging.info('START logging for test measurement__write_to_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        measurement.open_file()
        print(measurement.get_file())
        print("The current size of the file: ")
        print(measurement.file.tell())
        measurement.write_to_file()
        print(measurement.get_file())
        print("The current size of the file: ")
        print(measurement.file.tell())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__close_file
    # -------------------------------------------------------------------------

    def measurement__close_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.close_file \n"
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
        logging.info('START logging for test measurement__close_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        measurement.open_file()
        print("Is the file closed?")
        print(measurement.file.closed)
        measurement.close_file()
        print("Is the file closed?")
        print(measurement.file.closed)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # measurement__read_xml_config_file
    # -------------------------------------------------------------------------

    def measurement__read_xml_config_file(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.runner import Runner
        from src.measurement import Measurement

        text = "This test checks measurement.read_xml_config_file \n"
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
        logging.info('START logging for test measurement__read_xml_config_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # Construct a runner
        runner = Runner(environment)

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
        measurement = Measurement(environment, runner)
        measurement.read_xml_config_file(environment.measurement_config)
        print("Identifier read from the config:")
        print(measurement.identifier)

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
