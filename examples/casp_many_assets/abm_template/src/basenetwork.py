#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-

"""
abm_template is a multi-agent simulator template for financial  analysis
Copyright (C) 2016 Co-Pierre Georg (co-pierre.georg@uct.ac.za)
Pawel Fiedor (pawel.fiedor@uct.ac.za)

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

import abc
import logging
import networkx as nx

__author__ = """Pawel Fiedor (pawel.fiedor@uct.ac.za)"""

# -------------------------------------------------------------------------
#
#  class Network
#
# -------------------------------------------------------------------------


class BaseNetwork(object):
    """
    Class variables: __metaclass__
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_identifier(self):
        return
    @abc.abstractmethod
    def set_identifier(self, _identifier):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        if not isinstance(_identifier, str):
            raise TypeError
        else:
            self.identifier = _identifier
        return
    identifier = abc.abstractproperty(get_identifier, set_identifier)
    # identifier of the specific environment used for distinguishing them / logging
    # identifier should be a string

    @abc.abstractmethod
    def get_transactions(self):
        return
    @abc.abstractmethod
    def set_transactions(self, _transactions):
        """
        Class variables: transactions
        Local variables: _transactions
        """
        if not isinstance(_transactions, nx.classes.multidigraph.MultiDiGraph):
            raise TypeError
        else:
            self.transactions = _transactions
        return
    identifier = abc.abstractproperty(get_transactions, set_transactions)
    # networkx object (MultiDiGraph)

    @abc.abstractmethod
    def __init__(self, _identifier):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        self.identifier = _identifier
    # an abstract method for initialising the network

    @abc.abstractmethod
    def initialize_networks(self, _environment):
        """
        Class variables: transactions
        Local variables: _environment
        """
        self.transactions = nx.MultiDiGraph()

        # first ensure that all nodes are in self.transactions
        for agent in _environment.agents_generator():
            self.transactions.add_node(agent.identifier)

        # after we are done, give a short message to the log
        logging.info("  created the network of transactions with %s nodes",  str(len(list(self.transactions.nodes()))))
    # an abstract method for initialising the actual graph

    @abc.abstractmethod
    def __str__(self):
        """
        Class variables:
        Local variables: _identifier
        """
        text = "<network type='transactions' identifier='" + self.identifier + "'>\n"
        for node in self.transactions.nodes():
            text += "  <node id='" + node + "'>\n"
        for edge in self.transactions.edges(keys=True, data=True):
            text += "  <edge from='" + edge[0] + "' to='" + edge[1] + "' id='" + str(edge[2]) + "' type='" + edge[3]['type_'] + "' asset='" + edge[3]['asset'] + "' amount='" + str(edge[3]['amount']) + "' interest='" + str(edge[3]['interest']) + "' maturity='" + str(edge[3]['maturity']) + "' time_of_default='" + str(edge[3]['time_of_default']) + "'>\n"
        text += "</network>\n"

        return text
    # an abstract method for printing the network

    @abc.abstractmethod
    def write_network_of_transactions(self, _time):
        """
        Class variables: identifier, transactions
        Local variables: _time
        """
        nx.write_graphml(self.transactions.to_directed(), "transactions-" + self.identifier + "-" + str(_time) + ".graphml")
    # an abstract method for saving the network as gexf file

    @abc.abstractmethod
    def write_list_of_edges(self, _time):
        """
        Class variables: identifier, transactions
        Local variables: _time
        """
        nx.write_edgelist(self.transactions.to_directed(), "transactions-" + self.identifier + "-" + str(_time) + ".list")
    # an abstract method for saving list of edges

    @abc.abstractmethod
    def subnetwork_by_type(self, _type):
        """
        Class variables: identifier, transactions
        Local variables: _type
        """
        G = nx.MultiDiGraph(((source, target, key, attr) for source, target, key, attr in self.transactions.edges(data=True, keys=True) if attr['type_'] == _type))
        return G
    # an abstract method for getting a subnetwork confined by type of transaction

    @abc.abstractmethod
    def subnetwork_by_asset(self, _asset):
        """
        Class variables: identifier, transactions
        Local variables: _asset
        """
        G = nx.MultiDiGraph(((source, target, key, attr) for source, target, key, attr in self.transactions.edges(data=True, keys=True) if attr['asset'] == _asset))
        return G
    # an abstract method for getting a subnetwork confined by asset of transaction

    @abc.abstractmethod
    def subnetwork_by_amount(self, lower_bound, upper_bound):
        """
        Class variables: identifier, transactions
        Local variables: lower_bound, upper_bound
        """
        G = nx.MultiDiGraph(((source, target, key, attr) for source, target, key, attr in self.transactions.edges(data=True, keys=True) if (attr['amount'] > lower_bound and attr['amount'] < upper_bound)))
        return G
    # an abstract method for getting a subnetwork confined by amount of transaction

    @abc.abstractmethod
    def subnetwork_by_interest(self, lower_bound, upper_bound):
        """
        Class variables: identifier, transactions
        Local variables: lower_bound, upper_bound
        """
        G = nx.MultiDiGraph(((source, target, key, attr) for source, target, key, attr in self.transactions.edges(data=True, keys=True) if (attr['interest'] > lower_bound and attr['interest'] < upper_bound)))
        return G
    # an abstract method for getting a subnetwork confined by interest on transaction

    @abc.abstractmethod
    def subnetwork_by_maturity(self, lower_bound, upper_bound):
        """
        Class variables: identifier, transactions
        Local variables: lower_bound, upper_bound
        """
        G = nx.MultiDiGraph(((source, target, key, attr) for source, target, key, attr in self.transactions.edges(data=True, keys=True) if (attr['maturity'] > lower_bound and attr['maturity'] < upper_bound)))
        return G
    # an abstract method for getting a subnetwork confined by maturity of transaction

    @abc.abstractmethod
    def subnetwork_by_time_of_default(self, lower_bound, upper_bound):
        """
        Class variables: identifier, transactions
        Local variables: lower_bound, upper_bound
        """
        G = nx.MultiDiGraph(((source, target, key, attr) for source, target, key, attr in self.transactions.edges(data=True, keys=True) if (attr['time_of_default'] > lower_bound and attr['time_of_default'] < upper_bound)))
        return G
    # an abstract method for getting a subnetwork confined by time of default of transaction

    @abc.abstractmethod
    def update_network(self, environment):
        for agent in environment.agents_generator():
            for transaction in agent.accounts:
                # here we update all fields
                transaction.set_type_(transaction.type_, environment)
                transaction.set_asset(transaction.asset, environment)
                transaction.set_from_(transaction.from_, environment)
                transaction.set_to(transaction.to, environment)
                transaction.set_amount(transaction.amount, environment)
                transaction.set_interest(transaction.interest, environment)
                transaction.set_maturity(transaction.maturity, environment)
                transaction.set_time_of_default(transaction.time_of_default, environment)
    # an abstract method for updating all attributes in the network
