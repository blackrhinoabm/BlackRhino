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

# -------------------------------------------------------------------------
#  class Tests
# -------------------------------------------------------------------------


class TestsTransaction(object):
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
#  TESTS FOR TRANSACTION.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__init
    # -------------------------------------------------------------------------

    def transaction__init(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction
        from sample_agent import Agent

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction
        from sample_agent import Agent

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction
        from sample_agent import Agent

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

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
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

        agent_one = Agent("agent_one", {"test": "parameters"}, {"test": "variables"})
        agent_two = Agent("agent_two", {"test": "parameters"}, {"test": "variables"})

        config.agents = []
        config.agents.append(agent_one)
        config.agents.append(agent_two)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", agent_one, "agent_two", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(config)
        print("The transaction:")
        print(transaction)
        print("Agent one:")
        print(config.get_agent_by_id("agent_one"))
        print("Agent two:")
        print(config.get_agent_by_id("agent_two"))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__remove_transaction
    # -------------------------------------------------------------------------

    def transaction__remove_transaction(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

        agent_one = Agent("agent_one", {"test": "parameters"}, {"test": "variables"})
        agent_two = Agent("agent_two", {"test": "parameters"}, {"test": "variables"})

        config.agents = []
        config.agents.append(agent_one)
        config.agents.append(agent_two)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "agent_one", "agent_two", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(config)
        print("The transaction:")
        print(transaction)
        print("Agent one:")
        print(config.get_agent_by_id("agent_one"))
        print("Agent two:")
        print(config.get_agent_by_id("agent_two"))
        print("Removing the transaction")
        transaction.remove_transaction()
        print("The transaction:")
        print(transaction)
        print("Agent one:")
        print(config.get_agent_by_id("agent_one"))
        print("Agent two:")
        print(config.get_agent_by_id("agent_two"))
        print("Removing the transaction")

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__print_transaction
    # -------------------------------------------------------------------------

    def transaction__print_transaction(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

        agent_one = Agent("agent_one", {"test": "parameters"}, {"test": "variables"})
        agent_two = Agent("agent_two", {"test": "parameters"}, {"test": "variables"})

        config.agents = []
        config.agents.append(agent_one)
        config.agents.append(agent_two)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "agent_one", "agent_two", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(config)
        print("Printing transaction:")
        transaction.print_transaction()

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__str
    # -------------------------------------------------------------------------

    def transaction__str(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

        agent_one = Agent("agent_one", {"test": "parameters"}, {"test": "variables"})
        agent_two = Agent("agent_two", {"test": "parameters"}, {"test": "variables"})

        config.agents = []
        config.agents.append(agent_one)
        config.agents.append(agent_two)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "agent_one", "agent_two", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(config)
        print("Printing transaction:")
        print(transaction.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__write_transaction
    # -------------------------------------------------------------------------

    def transaction__write_transaction(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

        agent_one = Agent("agent_one", {"test": "parameters"}, {"test": "variables"})
        agent_two = Agent("agent_two", {"test": "parameters"}, {"test": "variables"})

        config.agents = []
        config.agents.append(agent_one)
        config.agents.append(agent_two)

        #
        # TESTING
        #

        print("Creating a transaction")
        transaction = Transaction()
        print("Assigning values")
        transaction.this_transaction("type", "asset", "agent_one", "agent_two", 1,  2,  3, 4)
        print("Adding the transaction to the books")
        transaction.add_transaction(config)
        print("Printing transaction:")
        print(transaction.write_transaction())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__clear_accounts
    # -------------------------------------------------------------------------

    def transaction__clear_accounts(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

        agent_one = Agent("agent_one", {"test": "parameters"}, {"test": "variables"})
        agent_two = Agent("agent_two", {"test": "parameters"}, {"test": "variables"})

        config.agents = []
        config.agents.append(agent_one)
        config.agents.append(agent_two)

        #
        # TESTING
        #

        transaction = Transaction()
        transaction.this_transaction("type", "asset", "agent_one", "agent_two", 1,  2,  3, 4)
        transaction.add_transaction(config)
        print("Before clearing one agent's accounts")
        for agent in config.agents:
            print(agent)
        config.get_agent_by_id("agent_one").clear_accounts()
        print("After clearing one agent's accounts")
        for agent in config.agents:
            print(agent)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # transaction__purge_accounts
    # -------------------------------------------------------------------------

    def transaction__purge_accounts(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config
        from sample_transaction import Transaction

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

        # Construct a config
        config = Config()

        agent_one = Agent("agent_one", {"test": "parameters"}, {"test": "variables"})
        agent_two = Agent("agent_two", {"test": "parameters"}, {"test": "variables"})

        config.agents = []
        config.agents.append(agent_one)
        config.agents.append(agent_two)

        #
        # TESTING
        #

        print("Before purging the accounts")
        transaction = Transaction()
        transaction.this_transaction("type", "asset", "agent_one", "agent_two", 0,  2,  3, 4)
        transaction.add_transaction(config)
        transaction = Transaction()
        transaction.this_transaction("type", "asset", "agent_one", "agent_two", 1,  2,  3, 4)
        transaction.add_transaction(config)
        print(config.get_agent_by_id("agent_one"))
        print(config.get_agent_by_id("agent_two"))
        print("After clearing one bank's accounts")
        transaction.purge_accounts(config)
        print(config.get_agent_by_id("agent_one"))
        print(config.get_agent_by_id("agent_two"))

    # -------------------------------------------------------------------------
