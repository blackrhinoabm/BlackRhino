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

from abm_template.src.basetransaction import BaseTransaction

# -------------------------------------------------------------------------
#
# class Transaction
#
# -------------------------------------------------------------------------


class Transaction(BaseTransaction):

    #
    #
    # VARIABLES
    #
    #

    identifier = None  # unique identifier of the transaction, may be useful for iterators
    type_ = ""  # type of transactions, e.g. "deposit"
    asset = ""  # type of asset, used for investment types
    from_ = 0.0  # agent being the originator of the transaction
    to = 0.0  # agent being the recipient of the transaction
    amount = 0.0  # amount of the transaction
    interest = 0.0  # interest rate paid to the originator each time step
    maturity = 0  # time (in steps) to maturity
    # this is used only for loans I, and will be > 0 for defaulting loans. with each update step, it is reduced by 1
    # if timeOfDefault == 0: loan defaults
    time_of_default = -1  # control variable checking for defaulted transactions

    #
    #
    # METHODS
    #
    #

    # -------------------------------------------------------------------------
    # __init__
    # Generate a unique identifier of the transaction
    # This may be useful for looping over various agent's accounts
    # -------------------------------------------------------------------------
    def __init__(self):
        import uuid
        self.identifier = uuid.uuid4()
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __del__()
    # removes the transaction from appropriate accounts and deletes the instance
    # if transaction hasn't been properly added there is no need to change accounts
    # -------------------------------------------------------------------------
    def __del__(self):
        if hasattr(self.from_, "accounts"):  # and hasattr(self.to, "accounts"):
                if self.from_ == self.to:
                    self.from_.accounts.remove(self)
                else:
                    self.from_.accounts.remove(self)
                    self.to.accounts.remove(self)
                del self
        else:
            del self
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # functions for setting/changing variables
    # these either return or set specific value to the above variables
    # -------------------------------------------------------------------------
    def get_type_(self):
        return self.type_

    def set_type_(self, type_):
        super(Transaction, self).set_type_(type_)

    def get_asset(self):
        return self.asset

    def set_asset(self, asset):
        super(Transaction, self).set_asset(asset)

    def get_from_(self):
        return self.from_

    def set_from_(self, from_):
        super(Transaction, self).set_from_(from_)

    def get_to(self):
        return self.to

    def set_to(self, to):
        super(Transaction, self).set_to(to)

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        super(Transaction, self).set_amount(amount)

    def get_interest(self):
        return self.interest

    def set_interest(self, interest):
        super(Transaction, self).set_interest(interest)

    def get_maturity(self):
        return self.maturity

    def set_maturity(self, maturity):
        super(Transaction, self).set_maturity(maturity)

    def get_time_of_default(self):
        return self.time_of_default

    def set_time_of_default(self, time_of_default):
        super(Transaction, self).set_time_of_default(time_of_default)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # this_transaction(type_,
    #                  asset,
    #                  from_,
    #                  to,
    #                  amount,
    #                  interest,
    #                  maturity,
    #                  time_of_default)
    # sets the variables of the transaction to the given amounts
    # -------------------------------------------------------------------------
    def this_transaction(self, type_, asset, from_, to, amount,  interest,  maturity, time_of_default):
        super(Transaction, self).this_transaction(type_, asset, from_, to, amount, interest, maturity, time_of_default)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # add_transaction
    # adds the transaction to appropriate agents' accounts
    # TODO: we need to make sure we don't do it twice when we iterate over
    # transactions in the accounts of agents (this may be tricky)
    # -------------------------------------------------------------------------
    def add_transaction(self, environment):
        super(Transaction, self).add_transaction(environment)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # print_transaction()
    # prints the transaction and its properties
    # -------------------------------------------------------------------------
    def print_transaction(self):
        super(Transaction, self).print_transaction()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __str__()
    # prints the transaction and its properties
    # -------------------------------------------------------------------------
    def __str__(self):
        return super(Transaction, self).write_transaction()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_transaction()
    # returns a string with the transaction and its properties
    # -------------------------------------------------------------------------
    def write_transaction(self):
        return super(Transaction, self).write_transaction()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # clear_accounts()
    # deletes all transactions of a given agent
    # this should be used very sparingly, as this does not account
    # for the economics of the process
    # -------------------------------------------------------------------------
    def clear_accounts(self, agent):
        for tranx in agent.accounts:
            tranx.__del__()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # purge_accounts()
    # removes all transactions of all agents with amount of zero
    # -------------------------------------------------------------------------
    def purge_accounts(self, environment):
        for bank in environment.banks:
            new_accounts = []

            for transaction in bank.accounts:
                if transaction.amount > 0.0:
                    new_accounts.append(transaction)

            bank.accounts = new_accounts
        for firm in environment.firms:
            new_accounts = []

            for transaction in firm.accounts:
                if transaction.amount > 0.0:
                    new_accounts.append(transaction)

            firm.accounts = new_accounts
        for household in environment.households:
            new_accounts = []

            for transaction in household.accounts:
                if transaction.amount > 0.0:
                    new_accounts.append(transaction)

            household.accounts = new_accounts
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # purge_accounts()
    # removes all transactions of a given agent with amount of zero
    # -------------------------------------------------------------------------
    def purge_accounts_agent(self, agent):
        new_accounts = []
        for transaction in agent.accounts:
            if transaction.amount > 0.0:
                new_accounts.append(transaction)

        agent.accounts = new_accounts
    # -------------------------------------------------------------------------
