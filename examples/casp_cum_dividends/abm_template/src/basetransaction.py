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
import networkx as nx

__author__ = """Pawel Fiedor (pawel.fiedor@uct.ac.za)"""

# -------------------------------------------------------------------------
#
#  class Transaction
#
# -------------------------------------------------------------------------


class BaseTransaction(object):
    """
    Class variables: __metaclass__
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_identifier(self):
        return
    @abc.abstractmethod
    def set_identifier(self, _identifier, environment):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        if not isinstance(_identifier, str):
            raise TypeError
        else:
            environment.network.transactions.remove_edge(self.from_.identifier, self.to.identifier, key=self.identifier)
            self.identifier = _identifier
            environment.network.transactions.add_edge(self.from_.identifier, self.to.identifier, key=self.identifier, type_=self.type_, asset=self.asset, amount=self.amount, interest=self.interest, maturity=self.maturity, time_of_default=self.time_of_default)
        return
    identifier = abc.abstractproperty(get_identifier, set_identifier)
    # identifier of the specific environment used for distinguishing them / logging
    # identifier should be a string

    @abc.abstractmethod
    def get_type_(self):
        return
    @abc.abstractmethod
    def set_type_(self, _type, environment):
        """
        Class variables: type_
        Local variables: _type
        """
        if not isinstance(_type, str):
            raise TypeError
        else:
            self.type_ = _type
            nx.set_edge_attributes(environment.network.transactions, 'type_', {(self.from_.identifier, self.to.identifier, self.identifier): _type})
        return
    type_ = abc.abstractproperty(get_type_, set_type_)
    # type of transactions, e.g. "deposit"
    # trailing underscore to distinguish from python keyword

    @abc.abstractmethod
    def get_asset(self):
        return
    @abc.abstractmethod
    def set_asset(self, _asset, environment):
        """
        Class variables: transaction_asset
        Local variables: _asset
        """
        if not isinstance(_asset, str):
            raise TypeError
        else:
            self.asset = _asset
            nx.set_edge_attributes(environment.network.transactions, 'asset', {(self.from_.identifier, self.to.identifier, self.identifier): _asset})
        return
    asset = abc.abstractproperty(get_asset, set_asset)
    # type of asset, used for investment types

    @abc.abstractmethod
    def get_from_(self):
        return
    @abc.abstractmethod
    def set_from_(self, _from, environment):
        """
        Class variables: from_
        Local variables: _from
        """
        environment.network.transactions.remove_edge(self.from_.identifier, self.to.identifier, key=self.identifier)
        self.from_ = _from
        environment.network.transactions.add_edge(self.from_.identifier, self.to.identifier, key=self.identifier, type_=self.type_, asset=self.asset, amount=self.amount, interest=self.interest, maturity=self.maturity, time_of_default=self.time_of_default)
        return
    from_ = abc.abstractproperty(get_from_, set_from_)
    # agent being the originator of the transaction
    # trailing underscore to distinguish from python keyword

    @abc.abstractmethod
    def get_to(self):
        return
    @abc.abstractmethod
    def set_to(self, _to, environment):
        """
        Class variables: to
        Local variables: _to
        """
        environment.network.transactions.remove_edge(self.from_.identifier, self.to.identifier, key=self.identifier)
        self.to = _to
        environment.network.transactions.add_edge(self.from_.identifier, self.to.identifier, key=self.identifier, type_=self.type_, asset=self.asset, amount=self.amount, interest=self.interest, maturity=self.maturity, time_of_default=self.time_of_default)
        return
    to = abc.abstractproperty(get_to, set_to)
    # agent being the recipient of the transaction

    @abc.abstractmethod
    def get_amount(self):
        return
    @abc.abstractmethod
    def set_amount(self, _amount, environment):
        """
        Class variables: amount
        Local variables: _amount
        """
        if not (isinstance(_amount, float) or isinstance(_amount, int)):
            raise TypeError
        else:
            self.amount = float(_amount)
            # nx.set_edge_attributes(environment.network.transactions, 'amount', {(self.from_.identifier, self.to.identifier, self.identifier): float(_amount)})
        return
    amount = abc.abstractproperty(get_amount, set_amount)
    # amount of the transaction

    @abc.abstractmethod
    def get_interest(self):
        return
    @abc.abstractmethod
    def set_interest(self, _interest, environment):
        """
        Class variables: interest
        Local variables: _interest
        """
        if not (isinstance(_interest, float) or isinstance(_interest, int)):
            raise TypeError
        else:
            self.interest = float(_interest)
            nx.set_edge_attributes(environment.network.transactions, 'interest', {(self.from_.identifier, self.to.identifier, self.identifier): float(_interest)})
        return
    interest = abc.abstractproperty(get_interest, set_interest)
    # interest rate paid to the originator each time step

    @abc.abstractmethod
    def get_maturity(self):
        return
    @abc.abstractmethod
    def set_maturity(self, _maturity, environment):
        """
        Class variables: maturity
        Local variables: _maturity
        """
        if not (isinstance(_maturity, float) or isinstance(_maturity, int)):
            raise TypeError
        else:
            self.maturity = int(_maturity)
            nx.set_edge_attributes(environment.network.transactions, 'maturity', {(self.from_.identifier, self.to.identifier, self.identifier): int(_maturity)})
        return
    maturity = abc.abstractproperty(get_maturity, set_maturity)
    # time (in steps) to maturity

    @abc.abstractmethod
    def get_time_of_default(self):
        return
    @abc.abstractmethod
    def set_time_of_default(self, _time_of_default, environment):
        """
        Class variables: time_of_default
        Local variables: _time_of_default
        """
        if not (isinstance(_time_of_default, float) or isinstance(_time_of_default, int)):
            raise TypeError
        else:
            self.time_of_default = int(_time_of_default)
            nx.set_edge_attributes(environment.network.transactions, 'time_of_default', {(self.from_.identifier, self.to.identifier, self.identifier): int(_time_of_default)})
        return
    time_of_default = abc.abstractproperty(get_time_of_default, set_time_of_default)
    # control variable checking for defaulted transactions

    @abc.abstractmethod
    def __init__(self):
        import uuid
        self.identifier = str(uuid.uuid4())
    # a standard method for initialisation of a transaction
    # creates a unique identifier

    # makes sure to remove it from the appropriate agents' accounts
    @abc.abstractmethod
    def remove_transaction(self, environment):
        # we check if the from_ and to variables are agents
        # environment.network.transactions.remove_edge(self.from_.identifier, self.to.identifier, key=self.identifier)
        if hasattr(self.from_, "accounts"):  # and hasattr(self.to, "accounts"):
                # if from_ and to are the same agents we remove it once
                if self.from_ == self.to:
                    for tranx in self.from_.accounts:
                        if tranx.identifier == self.identifier:
                            # we remove the transaction from agent's accounts
                            # this way it is no longer linked in the model in any way
                            self.from_.accounts.remove(tranx)
                # if we have two separate agents we need to remove twice
                else:
                    for tranx in self.from_.accounts:
                        if tranx.identifier == self.identifier:
                            # we remove the transaction from agent's accounts
                            # this way it is no longer linked in the model in any way
                            self.from_.accounts.remove(tranx)
                    for tranx in self.to.accounts:
                        if tranx.identifier == self.identifier:
                            # we remove the transaction from agent's accounts
                            # this way it is no longer linked in the model in any way
                            self.to.accounts.remove(tranx)
    # a standard method for deleting a transaction
    # makes sure to remove it from the appropriate agents' accounts

    @abc.abstractmethod
    def print_transaction(self):
        print "        <transaction type='" + self.type_ + "'>"
        if self.asset != "":
            print "            <property type='asset' value='" + self.asset + "'>"
        if hasattr(self.from_, "identifier"):
            print "            <property type='from' value='" + str(self.from_.identifier) + "'></property>"
        else:
            print "            <property type='from' value='" + str(self.from_) + "'></property>"
        if hasattr(self.to, "identifier"):
            print "            <property type='to' value='" + str(self.to.identifier) + "'></property>"
        else:
            print "            <property type='to' value='" + str(self.to) + "'></property>"
        print "            <property type='amount' value='" + str(self.amount) + "'></property>"
        print "            <property type='interest' value='" + str(self.interest) + "'></property>"
        print "            <property type='maturity' value='" + str(self.maturity) + "'></property>"
        print "            <property type='time_of_default' value='" + str(self.time_of_default) + "'></property>"
        print "        </transaction>"
    # a standard function which prints the transaction and its properties

    @abc.abstractmethod
    def write_transaction(self):
        text = "        <transaction type='" + self.type_ + "'>\n"
        if self.asset != "":
            text = text + "            <property type='asset' value='" + self.asset + "'>\n"
        if hasattr(self.from_, "identifier"):
            text = text + "            <property type='from' value='" + str(self.from_.identifier) + "'></property>\n"
        else:
            text = text + "            <property type='from' value='" + str(self.from_) + "'></property>\n"
        if hasattr(self.to, "identifier"):
            text = text + "            <property type='to' value='" + str(self.to.identifier) + "'></property>\n"
        else:
            text = text + "            <property type='to' value='" + str(self.to) + "'></property>\n"
        text = text + "            <property type='amount' value='" + str(self.amount) + "'></property>\n"
        text = text + "            <property type='interest' value='" + str(self.interest) + "'></property>\n"
        text = text + "            <property type='maturity' value='" + str(self.maturity) + "'></property>\n"
        text = text + "            <property type='time_of_default' value='" + str(self.time_of_default) + "'></property>\n"
        text = text + "        </transaction>\n"

        return text
    # a standard function which returns a string with the transaction and its properties

    @abc.abstractmethod
    def add_transaction(self, type_, asset, from_, to, amount, interest, maturity, time_of_default, environment):
        self.type_ = type_
        self.asset = asset
        # the convention used is that amounts are positive
        if amount >= 0:
            self.from_ = from_
            self.to = to
        else:  # negative amounts reverse direction and delete sign
            self.from_ = to
            self.to = from_
            amount = abs(amount)
        self.amount = amount
        self.interest = interest
        self.maturity = maturity
        self.time_of_default = time_of_default
        # We attempt to add the transaction to the agents to which it belongs to
        # First we check whether from_ is a string, if it is we need to find the
        # actual agent object and link it to from_
        if isinstance(self.from_, str):
            self.from_ = environment.get_agent_by_id(self.from_)
        # We do the same thing with to agent
        if isinstance(self.to, str):
            self.to = environment.get_agent_by_id(self.to)
        # Then we check if both agents have accounts (ie are actual agents)
        # instead of something diffeerent than string but unrelated
        if hasattr(self.from_, "accounts") and hasattr(self.to, "accounts"):
            # And apend the from_ and to_ to accounts of the appropriate agents
            if self.from_ == self.to:
                self.from_.accounts.append(self)
            else:
                self.from_.accounts.append(self)
                self.to.accounts.append(self)
            environment.network.transactions.add_edge(self.from_.identifier, self.to.identifier, key=self.identifier, type_=self.type_, asset=self.asset, amount=self.amount, interest=self.interest, maturity=self.maturity, time_of_default=self.time_of_default)
        else:
            raise TypeError("Transaction's from or to is not an instance of an agent.")
    # a standard function which adds the transaction to the appropriate agents' accounts

    @abc.abstractmethod
    def clear_accounts(self, agent, environment):
        # This removes all transactions of the agent from its books
        while len(agent.accounts) > 0:
            agent.accounts[0].remove_transaction(environment)
    # a standard function which clears the accounts of a given agent
    # and deletes

    @abc.abstractmethod
    def purge_accounts(self, environment):
        # This removes all transactions with amount 0
        for agent in environment.agents_generator():
            new_accounts = []
            for transaction in agent.accounts:
                if transaction.amount > 0.0:
                    new_accounts.append(transaction)
                else:
                    # need to check since we're looping over all transactions, thus some will have been removed from the network on the other leg
                    if environment.network.transactions.has_edge(transaction.from_.identifier, transaction.to.identifier, key=transaction.identifier) is True:
                        # and remove from the network
                        environment.network.transactions.remove_edge(transaction.from_.identifier, transaction.to.identifier, key=transaction.identifier)
            agent.accounts = new_accounts
    # a standard method for purging accounts of all agents
