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
import networkx as nx
from src.helper import Helper

# -------------------------------------------------------------------------
#  class Tests
# -------------------------------------------------------------------------


class TestsNetwork(object):
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
#  TESTS FOR NETWORK.PY
# -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__init
    # -------------------------------------------------------------------------

    def network__init(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.init \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__init in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a network \n")
        network = Network("test")
        print("Network ID: ")
        print(network.identifier)

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__get_identifier
    # -------------------------------------------------------------------------

    def network__get_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.get_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__get_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a network \n")
        network = Network("test")
        print("Network ID: ")
        print(network.get_identifier())
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__set_identifier
    # -------------------------------------------------------------------------

    def network__set_identifier(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.set_identifier \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__set_identifier in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Creating a network \n")
        network = Network("test")
        print("Network ID: ")
        print(network.get_identifier())
        print("Changing network ID")
        network.set_identifier("test2")
        print("Network ID: ")
        print(network.get_identifier())
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__get_transactions
    # -------------------------------------------------------------------------

    def network__get_transactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.get_transactions \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__get_transactions in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print(nx.info(environment.network.get_transactions()))
        print("Adding a transaction")
        transaction = Transaction()
        transaction.add_transaction("type", "asset", "bank_test_config_id", "bank_test_config_id_two", 1,  2,  3, 4, environment)
        print(nx.info(environment.network.get_transactions()))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__set_transactions
    # -------------------------------------------------------------------------

    def network__set_transactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.set_transactions \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__set_transactions in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print(nx.info(environment.network.get_transactions()))
        print("Setting transactions to an empty graph")
        empty_graph = nx.MultiDiGraph()
        environment.network.set_transactions(empty_graph)
        print(nx.info(environment.network.get_transactions()))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__initialize_networks
    # -------------------------------------------------------------------------

    def network__initialize_networks(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.initialize_networks \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__initialize_networks in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        empty_graph = nx.MultiDiGraph()
        environment.network.set_transactions(empty_graph)
        print("Starting with an empty network")
        print(nx.info(environment.network.get_transactions()))
        print("Initializing transactions")
        environment.network.initialize_networks(environment)
        print(nx.info(environment.network.get_transactions()))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__str
    # -------------------------------------------------------------------------

    def network__str(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.str \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__str in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print(environment.network)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__write_network_of_transactions
    # -------------------------------------------------------------------------

    def network__write_network_of_transactions(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.write_network_of_transactions \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__write_network_of_transactions in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Writing the gexf file")
        environment.network.write_network_of_transactions("2")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__write_list_of_edges
    # -------------------------------------------------------------------------

    def network__write_list_of_edges(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.write_list_of_edges \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__write_list_of_edges in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Writing the edges file")
        environment.network.write_list_of_edges("2")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__subnetwork_by_type
    # -------------------------------------------------------------------------

    def network__subnetwork_by_type(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.subnetwork_by_type \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__subnetwork_by_type in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Properties of the full network:")
        print(nx.info(environment.network.transactions))
        print("Creating the subnetwork by type")
        G = environment.network.subnetwork_by_type("loans")
        print("Properties of the subnetwork:")
        print(nx.info(G))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__subnetwork_by_asset
    # -------------------------------------------------------------------------

    def network__subnetwork_by_asset(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.subnetwork_by_asset \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__subnetwork_by_asset in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Properties of the full network:")
        print(nx.info(environment.network.transactions))
        print("Creating the subnetwork by asset")
        G = environment.network.subnetwork_by_asset("")
        print("Properties of the subnetwork:")
        print(nx.info(G))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__subnetwork_by_amount
    # -------------------------------------------------------------------------

    def network__subnetwork_by_amount(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.subnetwork_by_amount \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__subnetwork_by_amount in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Properties of the full network:")
        print(nx.info(environment.network.transactions))
        print("Creating the subnetwork by amount")
        G = environment.network.subnetwork_by_amount(1, 1000)
        print("Properties of the subnetwork:")
        print(nx.info(G))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__subnetwork_by_interest
    # -------------------------------------------------------------------------

    def network__subnetwork_by_interest(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.subnetwork_by_interest \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__subnetwork_by_interest in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Properties of the full network:")
        print(nx.info(environment.network.transactions))
        print("Creating the subnetwork by interest")
        G = environment.network.subnetwork_by_interest(-1, 1)
        print("Properties of the subnetwork:")
        print(nx.info(G))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__subnetwork_by_maturity
    # -------------------------------------------------------------------------

    def network__subnetwork_by_maturity(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.subnetwork_by_maturity \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__subnetwork_by_maturity in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Properties of the full network:")
        print(nx.info(environment.network.transactions))
        print("Creating the subnetwork by maturity")
        G = environment.network.subnetwork_by_maturity(-1, 3)
        print("Properties of the subnetwork:")
        print(nx.info(G))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__subnetwork_by_time_of_default
    # -------------------------------------------------------------------------

    def network__subnetwork_by_time_of_default(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.subnetwork_by_time_of_default \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__subnetwork_by_time_of_default in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Properties of the full network:")
        print(nx.info(environment.network.transactions))
        print("Creating the subnetwork by time of default")
        G = environment.network.subnetwork_by_time_of_default(-2, 3)
        print("Properties of the subnetwork:")
        print(nx.info(G))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # network__update_network
    # -------------------------------------------------------------------------

    def network__update_network(self, args):
        import os
        from src.bank import Bank
        from src.household import Household
        from src.firm import Firm
        from src.environment import Environment
        from src.transaction import Transaction
        from src.network import Network

        text = "This test checks network.update_network \n"
        self.print_info(text)
        #
        # INITIALIZATION
        #
        environment_directory = str(args[0])
        identifier = str(args[1])
        log_directory = str(args[2])

        # Configure logging parameters so we get output while the program runs
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                            filename=log_directory + identifier + ".log", level=logging.INFO)
        logging.info('START logging for test network__update_network in run: %s',
                     environment_directory + identifier + ".xml")

        # Construct household filename
        environment = Environment(environment_directory,  identifier)

        #
        # TESTING
        #

        print("Original network:")
        print(environment.network)
        print("Changing some transactions manually:")
        for agent in environment.agents_generator():
            for transaction in agent.accounts:
                transaction.amount = 700.0
        print("Printing network:")
        print(environment.network)
        print("Updating network")
        environment.network.update_network(environment)
        print("Printing network:")
        print(environment.network)
    # -------------------------------------------------------------------------
