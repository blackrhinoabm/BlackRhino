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

# import random
import logging
from abm_template.src.basenetwork import BaseNetwork
import networkx as nx

# -------------------------------------------------------------------------
#  class Network
# -------------------------------------------------------------------------


class Network(BaseNetwork):
    #
    #
    # VARIABLES
    #
    #
    identifier = ""
    transactions = nx.MultiDiGraph()

    #
    #
    # METHODS
    #
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        super(Network, self).set_identifier(identifier)

    def get_transactions(self):
        return self.transactions

    def set_transactions(self, transactions):
        super(Network, self).set_transactions(transactions)

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, identifier):
        super(Network, self).__init__(identifier)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_networks
    # -------------------------------------------------------------------------
    def initialize_networks(self,  environment):
        super(Network, self).initialize_networks(environment)
    # -------------------------------------------------------------------------

#
# HELPER ROUTINES
#

    # -------------------------------------------------------------------------
    # __str()__
    # -------------------------------------------------------------------------
    def __str__(self):
        return super(Network, self).__str__()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_network_of_transactions
    # -------------------------------------------------------------------------
    def write_network_of_transactions(self, time):
        super(Network, self).write_network_of_transactions(time)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_list_of_edges
    # -------------------------------------------------------------------------
    def write_list_of_edges(self, time):
        super(Network, self).write_list_of_edges(time)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # update_network
    # TODO: think if this is necessary
    # This would loop through the transactions and update all the fields
    # in the network, but if properly applied this should be unnecessary
    # -------------------------------------------------------------------------
    def update_network(self, environment):
        super(Network, self).update_network(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # subnetwork_by_type
    # -------------------------------------------------------------------------
    def subnetwork_by_type(self, _type):
        return super(Network, self).subnetwork_by_type(_type)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # subnetwork_by_asset
    # -------------------------------------------------------------------------
    def subnetwork_by_asset(self, _asset):
        return super(Network, self).subnetwork_by_asset(_asset)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # subnetwork_by_amount
    # -------------------------------------------------------------------------
    def subnetwork_by_amount(self, lower_bound, upper_bound):
        return super(Network, self).subnetwork_by_amount(lower_bound, upper_bound)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # subnetwork_by_interest
    # -------------------------------------------------------------------------
    def subnetwork_by_interest(self, lower_bound, upper_bound):
        return super(Network, self).subnetwork_by_interest(lower_bound, upper_bound)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # subnetwork_by_maturity
    # -------------------------------------------------------------------------
    def subnetwork_by_maturity(self, lower_bound, upper_bound):
        return super(Network, self).subnetwork_by_maturity(lower_bound, upper_bound)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # subnetwork_by_time_of_default
    # -------------------------------------------------------------------------
    def subnetwork_by_time_of_default(self, lower_bound, upper_bound):
        return super(Network, self).subnetwork_by_time_of_default(lower_bound, upper_bound)
    # -------------------------------------------------------------------------
