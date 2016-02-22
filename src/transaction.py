#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2012 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)

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
    # VARIABLES
    #

    transaction_type = ""
    transaction_asset = ""
    transaction_from = 0
    transaction_to = 0
    transaction_value = 0.0
    transaction_interest = 0.0
    transaction_maturity = 0
    # this is used only for loans I, and will be > 0 for defaulting loans. with each update step, it is reduced by 1
    # if timeOfDefault == 0: loan defaults
    transaction_time_of_default = -1

    #
    # METHODS
    #

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self):
        pass
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # functions for setting/changing variables
    # -------------------------------------------------------------------------
    def get_transaction_type(self):
        return self.transaction_type

    def set_transaction_type(self, type):
        super(Transaction, self).set_transaction_type(type)

    def get_transaction_asset(self):
        return self.transaction_asset

    def set_transaction_asset(self, asset):
        super(Transaction, self).set_transaction_asset(asset)

    def get_transaction_from(self):
        return self.transaction_from

    def set_transaction_from(self, from_):
        super(Transaction, self).set_transaction_from(from_)

    def get_transaction_to(self):
        return self.transaction_to

    def set_transaction_to(self, to):
        super(Transaction, self).set_transaction_to(to)

    def get_transaction_value(self):
        return self.transaction_value

    def set_transaction_value(self, value):
        super(Transaction, self).set_transaction_value(value)

    def get_transaction_interest(self):
        return self.transaction_interest

    def set_transaction_interest(self, interest):
        super(Transaction, self).set_transaction_interest(interest)

    def get_transaction_maturity(self):
        return self.transaction_maturity

    def set_transaction_maturity(self, maturity):
        super(Transaction, self).set_transaction_maturity(maturity)

    def get_transaction_time_of_default(self):
        return self.transaction_time_of_default

    def set_transaction_time_of_default(self, time_of_default):
        super(Transaction, self).set_transaction_time_of_default(time_of_default)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # this_transaction(transaction_type,
    #                  transaction_asset,
    #                  transaction_from,
    #                  transaction_to,
    #                  transaction_value,
    #                  transaction_interest,
    #                  transaction_maturity,
    #                  transaction_time_of_default)
    # -------------------------------------------------------------------------
    def this_transaction(self, transaction_type, transaction_asset, transaction_from, transaction_to, transaction_value,  transaction_interest,  transaction_maturity, transaction_time_of_default):
        super(Transaction, self).this_transaction(transaction_type, transaction_asset, transaction_from, transaction_to, transaction_value,  transaction_interest,  transaction_maturity, transaction_time_of_default)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # print_transaction()
    # -------------------------------------------------------------------------
    def print_transaction(self):
        super(Transaction, self).print_transaction()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_transaction()
    # -------------------------------------------------------------------------
    def write_transaction(self):
        return super(Transaction, self).write_transaction()
    # -------------------------------------------------------------------------
