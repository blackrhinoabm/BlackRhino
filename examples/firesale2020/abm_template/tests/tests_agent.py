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


class TestsAgent(object):
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
#  TESTS FOR BASEAGENT.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__get_identifier
    # -------------------------------------------------------------------------

    def agent__get_identifier(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.get_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        text = "Identifier: "
        text = text + agent.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__set_identifier
    # -------------------------------------------------------------------------

    def agent__set_identifier(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.set_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        text = "Original identifier: "
        text = text + agent.get_identifier()
        print(text)
        agent.set_identifier("new_ident")
        text = "New identifier: "
        text = text + agent.get_identifier()
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__get_parameters
    # -------------------------------------------------------------------------

    def agent__get_parameters(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.get_parameters \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        text = "Parameters:"
        print(text)
        print(agent.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__set_parameters
    # -------------------------------------------------------------------------

    def agent__set_parameters(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.set_parameters \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__set_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        text = "Original parameters:"
        print(text)
        print(agent.get_parameters())
        text = "New parameters:"
        print(text)
        agent.set_parameters({'productivity': 1.55, 'active': 1})
        print(agent.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__append_parameters
    # -------------------------------------------------------------------------

    def agent__append_parameters(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.append_parameters \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__append_parameters in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        text = "Original parameters:"
        print(text)
        agent.set_parameters({'productivity': 1.55, 'active': 1})
        print(agent.get_parameters())
        text = "New parameters:"
        print(text)
        agent.append_parameters({'new': 2.34})
        print(agent.get_parameters())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__get_state_variables
    # -------------------------------------------------------------------------

    def agent__get_state_variables(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.get_state_variables \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__get_state_variables in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        text = "State variables:"
        print(text)
        print(agent.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__set_state_variables
    # -------------------------------------------------------------------------

    def agent__set_state_variables(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.set_state_variables \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__set_state_variables in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        text = "Original state variables:"
        print(text)
        print(agent.get_state_variables())
        text = "New state variables:"
        print(text)
        agent.set_state_variables({'test': 0.66})
        print(agent.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__append_state_variables
    # -------------------------------------------------------------------------

    def agent__append_state_variables(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.append_state_variables \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__append_state_variables in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        text = "Original state variables:"
        print(text)
        agent.set_state_variables({'test': 0.66})
        print(agent.get_state_variables())
        text = "New state variables:"
        print(text)
        agent.append_state_variables({'new': 0.77})
        print(agent.get_state_variables())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__str
    # -------------------------------------------------------------------------

    def agent__str(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.str \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__str in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        print(agent.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__init
    # -------------------------------------------------------------------------

    def agent__init(self, args):
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.init \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__init in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)

        #
        # TESTING
        #

        print(agent.__str__())

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__get_parameters_from_file
    # -------------------------------------------------------------------------

    def agent__get_parameters_from_file(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.get_parameters_from_file \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__get_parameters_from_file in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()
        list_env = os.listdir(environment_directory)
        config.read_xml_config_file(environment_directory + list_env[0])
        # get the firm_directory from the environment
        firm_directory = config.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents.append(agent)
        agent.get_parameters_from_file(firmFilename, config)

        #
        # TESTING
        #

        # test whether the parameters are read properly
        text = "Identifier has been read as follows: \n"
        text = text + "Identifier: "
        text = text + agent.identifier
        text = text + "\n"
        text = text + "Productivity: "
        text = text + str(agent.parameters["productivity"])
        print(text)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__get_account
    # -------------------------------------------------------------------------

    def agent__get_account(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.get_account \n"
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
        logging.info('START logging for test agent__get_account in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()
        list_env = os.listdir(environment_directory)
        config.read_xml_config_file(environment_directory + list_env[0])
        # get the firm_directory from the environment
        firm_directory = config.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents = []
        config.agents.append(agent)
        agent.get_parameters_from_file(firmFilename, config)

        agent_helper = Agent("helperagent id", {"test": "parameters"}, {"test": "variables"})
        agent_helper.identifier = "helper_agent"
        config.agents.append(agent_helper)

        from sample_transaction import Transaction
        amount = 150.0
        transaction = Transaction()
        transaction.this_transaction("loans", "", agent.identifier, agent_helper.identifier,
                                     amount,  0.0,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        amount = 100.0
        transaction = Transaction()
        transaction.this_transaction("cash", "", agent.identifier, agent_helper.identifier,
                                     amount,  0.0,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        amount = 250.0
        transaction = Transaction()
        transaction.this_transaction("goods", "", agent.identifier, agent_helper.identifier,
                                     amount,  0.0,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)

        #
        # TESTING
        #
        print(agent.accounts)
        account = 0.0                                           # counting all types in account together
        print(agent.__str__())                                             # and checking how much is the total
        # volume of the account
        for type in ["loans",  "cash",  "goods"]:
                        if type == "loans":
                                account = account + agent.get_account(type)
                                print("L = " + str(account))
                        if type == "cash":
                                account = account + agent.get_account(type)
                                print("L+M = " + str(account))
                        if type == "goods":
                                account = account + agent.get_account(type)
                                print("L+M+G = " + str(account))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__get_account_num_transactions
    # -------------------------------------------------------------------------

    def agent__get_account_num_transactions(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.get_account_num_transactions \n"
        text = text + "  The purpose of this method is to count the numbers of transaction for   \n"
        text = text + "  accounts firms hold. Our standard frm has 3 transactions by default. \n"
        text = text + "  But we double count as we have only one agent, so you should see 6. \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__get_account_num_transactions in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()
        list_env = os.listdir(environment_directory)
        config.read_xml_config_file(environment_directory + list_env[0])
        # get the firm_directory from the environment
        firm_directory = config.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents = []
        config.agents.append(agent)
        agent.get_parameters_from_file(firmFilename, config)

        from sample_transaction import Transaction
        amount = 150.0
        transaction = Transaction()
        transaction.this_transaction("loans", "", agent.identifier, agent.identifier,
                                     amount,  0.0,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        amount = 150.0
        transaction = Transaction()
        transaction.this_transaction("cash", "", agent.identifier, agent.identifier,
                                     amount,  0.0,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        amount = 200.0
        transaction = Transaction()
        transaction.this_transaction("goods", "", agent.identifier, agent.identifier,
                                     amount,  0.0,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        #
        # TESTING
        #

        num_transactions = 0.0          # counting all types in account together
        print(agent)
        # and checking if the number of transaction
        # is increasing by one
        for type in ["loans",  "cash",  "goods"]:
                        if type == "loans":
                                num_transactions = num_transactions + agent.get_account_num_transactions(type)
                                print("L = " + str(num_transactions))
                        if type == "cash":
                                num_transactions = num_transactions + agent.get_account_num_transactions(type)
                                print("L+M = " + str(num_transactions))
                        if type == "goods":
                                num_transactions = num_transactions + agent.get_account_num_transactions(type)
                                print("L+M+G = " + str(num_transactions))

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__clear_accounts
    # -------------------------------------------------------------------------

    def agent__clear_accounts(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.clear_accounts \n"
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
        logging.info('START logging for test agent__clear_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()
        list_env = os.listdir(environment_directory)
        config.read_xml_config_file(environment_directory + list_env[0])
        # get the firm_directory from the environment
        firm_directory = config.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents = []
        config.agents.append(agent)
        agent.get_parameters_from_file(firmFilename, config)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in agent.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        from sample_transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction("deposits", "", agent.identifier,
                                     agent.identifier, 10.0,  0.09,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down

        account = 0.0
        tranx = 0

        for transaction in agent.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        agent.clear_accounts()

        account = 0.0
        tranx = 0

        for transaction in agent.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__purge_accounts
    # -------------------------------------------------------------------------

    def agent__purge_accounts(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.purge_accounts \n"
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
        logging.info('START logging for test agent__purge_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()
        list_env = os.listdir(environment_directory)
        config.read_xml_config_file(environment_directory + list_env[0])
        # get the firm_directory from the environment
        firm_directory = config.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents = []
        config.agents.append(agent)
        agent.get_parameters_from_file(firmFilename, config)

        #
        # TESTING
        #

        account = 0.0
        tranx = 0

        for transaction in agent.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        from sample_transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction("deposits", "", agent.identifier,
                                     agent.identifier, 0.0,  0.09,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        # environment.households[0:1][0] is only for testing purposes DO NOT USE IN PRODUCTION
        # what it does is is takes the first household in environment, but if there are no
        # households (which happens in testing) it doesn't break down

        account = 0.0
        tranx = 0

        for transaction in agent.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

        agent.accounts[0].purge_accounts(config)

        account = 0.0
        tranx = 0

        for transaction in agent.accounts:
            account = account + transaction.amount
            tranx = tranx + 1

        print(tranx)
        print(account)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__get_transactions_from_file
    # -------------------------------------------------------------------------

    def agent__get_transactions_from_file(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.get_transactions_from_file \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__clear_accounts in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()
        list_env = os.listdir(environment_directory)
        config.read_xml_config_file(environment_directory + list_env[0])
        # get the firm_directory from the environment
        firm_directory = config.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "firm_test_config_id"
        config.agents = []
        config.agents.append(agent)
        #config.agent.get_parameters_from_file(firmFilename, config)

        #
        # TESTING
        #

        config.agents[0].accounts = []
        print("Printing agent:\n")
        print(config.agents[0])
        print("Reading transactions from the config file.\n")
        print("Printing agent: \n")
        config.agents[0].get_transactions_from_file(firm_directory + listing[0], config)
        print(config.agents[0])

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__getattr
    # -------------------------------------------------------------------------

    def agent__getattr(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.getattr \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__getattr in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()
        list_env = os.listdir(environment_directory)
        config.read_xml_config_file(environment_directory + list_env[0])
        # get the firm_directory from the environment
        firm_directory = config.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents = []
        config.agents.append(agent)
        agent.get_parameters_from_file(firmFilename, config)

        #
        # TESTING
        #

        print('Accessing rates through firm.parameters["productivity"] :')
        print(agent.parameters["productivity"])
        print("Accessing rates through firm.productivity:")
        print(agent.productivity)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # agent__check_consistency
    # -------------------------------------------------------------------------

    def agent__check_consistency(self, args):
        import os
        from sample_agent import Agent
        from sample_config import Config  # needed for the bankDirectory

        text = "This test checks agent.check_consistency \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test agent__check_consistency in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct firm filename
        config = Config()
        list_env = os.listdir(environment_directory)
        config.read_xml_config_file(environment_directory + list_env[0])
        # get the firm_directory from the environment
        firm_directory = config.firm_directory
        # and loop over all firms in the directory
        listing = os.listdir(firm_directory)
        firmFilename = firm_directory + listing[0]

        # generate an agent
        agent = Agent("baseagent id", {"test": "parameters"}, {"test": "variables"})
        agent.identifier = "test_agent"
        config.agents = []
        config.agents.append(agent)
        agent.get_parameters_from_file(firmFilename, config)

        from sample_transaction import Transaction
        amount = 150.0
        transaction = Transaction()
        transaction.this_transaction("loans", "", agent.identifier, agent.identifier,
                                     amount,  0.0,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        amount = 150.0
        transaction = Transaction()
        transaction.this_transaction("cash", "", agent.identifier, agent.identifier,
                                     amount,  0.0,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        amount = 200.0
        transaction = Transaction()
        transaction.this_transaction("goods", "", agent.identifier, agent.identifier,
                                     amount,  0.0,  0, -1)
        # environment.firms[0] is only for testing purposes DO NOT USE IN PRODUCTION
        transaction.add_transaction(config)
        #
        # TESTING
        #

        print(agent.check_consistency())

    # -------------------------------------------------------------------------
