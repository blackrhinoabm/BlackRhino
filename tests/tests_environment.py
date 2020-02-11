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


class TestsEnvironment(object):
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
    # environment__get_assets
    # -------------------------------------------------------------------------

    def environment__get_assets(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.get_assets \n"
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
        logging.info('START logging for test environment__get_assets in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print "Assets:"
        print(environment.get_assets())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__set_assets
    # -------------------------------------------------------------------------

    def environment__set_assets(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.set_assets \n"
        text = "and sets them to 'test': [0.05, 0.04, 0.03]\n"
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
        logging.info('START logging for test environment__set_assets in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Assets:")
        print(environment.get_assets())
        print("Changing assets to 'test': [0.05, 0.04, 0.03]")
        environment.set_assets({'test': [0.05, 0.04, 0.03]})
        print("Assets:")
        print(environment.get_assets())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__get_shocks
    # -------------------------------------------------------------------------

    def environment__get_shocks(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.get_shocks \n"
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
        logging.info('START logging for test environment__get_shocks in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print "Shocks:"
        print(environment.get_shocks())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__set_shocks
    # -------------------------------------------------------------------------

    def environment__set_shocks(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.set_shocks \n"
        text = text + "and sets them to [1, 2, 'test']\n"
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
        logging.info('START logging for test environment__set_shocks in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Shocks:")
        print(environment.get_shocks())
        print("Changing shocks to [1, 2, 'test']")
        environment.set_shocks([1, 2, "test"])
        print("Assets:")
        print(environment.get_shocks())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__add_shock
    # -------------------------------------------------------------------------

    def environment__add_shock(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.add_shock \n"
        text = text + "and adds to them [3, 4, 'test']\n"
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
        logging.info('START logging for test environment__add_shock in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Shocks:")
        print(environment.get_shocks())
        print("Adding shock [3, 4, 'test']")
        environment.add_shock([3, 4, "test"])
        print("Shocks:")
        print(environment.get_shocks())

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
    # environment__initialize_central_bank_from_files
    # -------------------------------------------------------------------------

    def environment__initialize_central_bank_from_files(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.initialize_central_bank_from_files \n"
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
        logging.info('START logging for test environment__initialize_central_bank_from_files in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        print("Initialized the central bank")
        text = "Number of central banks read: "
        text = text + str(len(environment.central_bank))
        print(text)
        print("The central bank read: ")
        for i in range(0, int(len(environment.central_bank))):
            print(environment.central_bank[i].__str__())

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
        environment.banks[0].clear_accounts(environment)  # let's use the first bank
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
        environment.firms[0].clear_accounts(environment)  # let's use the first bank
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
        environment.households[0].clear_accounts(environment)  # let's use the first bank
        print(environment.households[0])
        print("Reading transactions: ")
        environment.read_transactions_for_banks(environment.bank_directory)  # deposits are saved in bank config files only
        # environment.read_transactions_for_households(environment.household_directory)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__read_transactions_for_central_bank
    # -------------------------------------------------------------------------

    def environment__read_transactions_for_central_bank(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.read_transactions_for_central_bank \n"
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
        logging.info('START logging for test environment__read_transactions_for_central_bank in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Clearing accounts of the central_bank:")
        environment.central_bank[0].clear_accounts(environment)  # let's use the first bank
        print(environment.central_bank[0])
        print("Reading transactions: ")
        environment.read_transactions_for_central_bank(environment.central_bank_directory)  # deposits are saved in bank config files only
        # environment.read_transactions_for_households(environment.household_directory)
        print(environment.central_bank[0])

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
    # environment__check_agent_homogeneity
    # -------------------------------------------------------------------------

    def environment__check_agent_homogeneity(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.check_agent_homogeneity \n"
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
        logging.info('START logging for test environment__check_agent_homogeneity in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        bank = Bank()
        bank.identifier = "new bank"
        environment.banks.append(bank)
        environment.agents = [environment.banks, environment.firms, environment.households]

        print("Are banks homogeneous?")
        print(environment.check_agent_homogeneity("banks"))
        print("Changing one of the banks...")
        environment.get_agent_by_id("new bank").parameters["active"] = 4
        print("Are banks homogeneous?")
        print(environment.check_agent_homogeneity("banks"))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # environment__update_asset_returns
    # -------------------------------------------------------------------------

    def environment__update_asset_returns(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment

        text = "This test checks environment.update_asset_returns \n"
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
        logging.info('START logging for test environment__update_asset_returns in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Assets:")
        print(environment.get_assets())
        print("Updating asset returns")
        environment.update_asset_returns()
        print("Assets:")
        print(environment.get_assets())

    # -------------------------------------------------------------------------
