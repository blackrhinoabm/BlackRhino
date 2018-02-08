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


class TestsUpdater(object):
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
#  TESTS FOR UPDATER.PY >> PAWEL TO DO <<
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__get_identifier
    # -------------------------------------------------------------------------

    def updater__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.get_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__get_identifier in run: %s',
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
        model = Updater(environment)
        model.identifier = "test_model_id"
        print("Model's ID:")
        print(model.get_identifier())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__set_identifier
    # -------------------------------------------------------------------------

    def updater__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.set_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__set_identifier in run: %s',
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
        model = Updater(environment)
        model.identifier = "test_model_id"
        print("Model's ID:")
        print(model.get_identifier())
        print("Changing model ID...")
        model.set_identifier("new_model_id")
        print("Model's ID:")
        print(model.get_identifier())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__get_model_parameters
    # -------------------------------------------------------------------------

    def updater__get_model_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.get_model_parameters \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__get_model_parameters in run: %s',
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
        model = Updater(environment)
        model.model_parameters = {"test": "model parameters"}
        print("Model's parameters:")
        print(model.get_model_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__set_model_parameters
    # -------------------------------------------------------------------------

    def updater__set_model_parameters(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.set_model_parameters \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__set_model_parameters in run: %s',
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
        model = Updater(environment)
        model.model_parameters = {"test": "model parameters"}
        print("Model's parameters:")
        print(model.get_model_parameters())
        print("Changing model's parameters:...")
        model.model_parameters = {"new": "model parameters"}
        print("Model's parameters:")
        print(model.get_model_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__get_interactions
    # -------------------------------------------------------------------------

    def updater__get_interactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.get_interactions \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__get_interactions in run: %s',
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
        model = Updater(environment)
        print("Model's interactions:")
        print(model.get_interactions())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__set_interactions
    # -------------------------------------------------------------------------

    def updater__set_interactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.set_interactions \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__set_interactions in run: %s',
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
        model = Updater(environment)
        print("Model's interactions:")
        print(model.get_interactions())
        print("Changing model's agents:...")
        model.set_interactions(["new", "interactions"])
        print("Model's interactions:")
        print(model.get_interactions())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__str
    # -------------------------------------------------------------------------

    def updater__str(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.str \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__str in run: %s',
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
        model = Updater(environment)
        model.identifier = "testing str"
        print(model.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__init
    # -------------------------------------------------------------------------

    def updater__init(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.init \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__init in run: %s',
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
        model = Updater(environment)
        model.__init__(environment)
        print(model.environment)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__accrue_interests
    # -------------------------------------------------------------------------

    def updater__accrue_interests(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.accrue_interests \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__accrue_interests in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        # generate a bank
        bank = Bank()
        bank.identifier = "test_bank"
        bank.interest_rate_deposits = 0.05
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
        model = Updater(environment)
        model.__init__(environment)
        environment.new_transaction("deposits", "",  environment.get_agent_by_id("test_household").identifier, environment.get_agent_by_id("test_bank"),
                                    10.0, environment.get_agent_by_id("test_bank").interest_rate_deposits,  0, -1)
        print(environment.get_agent_by_id("test_household"))
        print("Accruing interests\n")
        model.accrue_interests(environment, 0)
        print(environment.get_agent_by_id("test_household"))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__endow_labour
    # -------------------------------------------------------------------------

    def updater__endow_labour(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.endow_labour \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__endow_labour in run: %s',
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
        model = Updater(environment)
        environment.get_agent_by_id("test_household").sweep_labour = 0
        print(environment.get_agent_by_id("test_household").sweep_labour)
        print("Endowing labour")
        model.endow_labour(environment, 0)
        print(environment.get_agent_by_id("test_household").sweep_labour)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__sell_labour
    # -------------------------------------------------------------------------

    def updater__sell_labour(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.sell_labour \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__sell_labour in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        print(environment.households[0])
        print("Selling labour")
        model.sell_labour(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__consume_rationed
    # -------------------------------------------------------------------------

    def updater__consume_rationed(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.consume_rationed \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__consume_rationed in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        model.sell_labour(environment, 0)
        print(environment.households[0])
        print("Consuming the production")
        model.consume_rationed(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__net_loans_deposits
    # -------------------------------------------------------------------------

    def updater__net_loans_deposits(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.net_loans_deposits \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__net_loans_deposits in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        model.sell_labour(environment, 0)
        model.consume_rationed(environment, 0)
        print(environment.households[0])
        print("Netting loans and deposits")
        model.net_loans_deposits(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__net_labour_goods
    # -------------------------------------------------------------------------

    def updater__net_labour_goods(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.net_labour_goods \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__net_labour_goods in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        model.sell_labour(environment, 0)
        model.consume_rationed(environment, 0)
        model.net_loans_deposits(environment, 0)
        print(environment.households[0])
        print("Netting labour and goods")
        model.net_labour_goods(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # updater__do_update
    # -------------------------------------------------------------------------

    def updater__do_update(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.market import Market
        from src.updater import Updater

        text = "This test checks updater.do_update \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test updater__do_update in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #
        model = Updater(environment)
        print(environment.households[0])
        print("Doing update")
        model.do_update(environment, 0)
        print(environment.households[0])

    # -------------------------------------------------------------------------
