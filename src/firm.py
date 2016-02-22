#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
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
from abm_template.src.baseagent import BaseAgent

# ============================================================================
#
# class Firm
#
# ============================================================================


class Firm(BaseAgent):
    #
    #
    # VARIABLES
    #
    #
    identifier = ""
    parameters = {}
    state_variables = {}
    accounts = []  # all accounts of a bank

    parameters["productivity"] = 0.0  # how many units of goods do we get from 1 unit of labour
    parameters["active"] = 0

    #
    #
    # CODE
    #
    #

    # -------------------------------------------------------------------------
    # functions for setting/changing id, parameters, and state variables
    # -------------------------------------------------------------------------
    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Firm, self).set_identifier(value)

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, value):
        super(Firm, self).set_parameters(value)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, value):
        super(Firm, self).set_state_variables(value)

    def append_parameters(self, value):
        super(Firm, self).append_parameters(value)

    def append_state_variables(self, value):
        super(Firm, self).append_state_variables(value)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # functions needed to make Firm() hashable
    # -------------------------------------------------------------------------
    def __key__(self):
        return self.identifier

    def __eq__(self, other):
        return self.__key__() == other.__key__()

    def __hash__(self):
        return hash(self.__key__())
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self):
        self.accounts = []  # clear transactions when firm is initialized
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __del__
    # -------------------------------------------------------------------------
    def __del__(self):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __str__
    # -------------------------------------------------------------------------
    def __str__(self):
        firm_string = super(Firm, self).__str__()
        firm_string = firm_string.replace("\n", "\n    <type value='firm''>\n", 1)
        text = "\n"
        for transaction in self.accounts:
            text += transaction.write_transaction()
        text += "  </agent>"
        return firm_string.replace("\n  </agent>", text, 1)
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_parameters_from_file
    # -------------------------------------------------------------------------
    def get_parameters_from_file(self,  firm_filename, environment):
        super(Firm, self).get_parameters_from_file(firm_filename, environment)
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_new_investments
    # -------------------------------------------------------------------------
    def get_new_investments(self, low, high):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # check_consistency
    # -------------------------------------------------------------------------
    def check_consistency(self):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account
    # -------------------------------------------------------------------------
    def get_account(self,  type_):
        return super(Firm, self).get_account(type_)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account_num_transactions
    # -------------------------------------------------------------------------
    def get_account_num_transactions(self,  type_):  # returns the number of transactions in a given account
        return super(Firm, self).get_account_num_transactions(type_)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # add_transaction
    # -------------------------------------------------------------------------
    def add_transaction(self,  type_, asset, from_id,  to_id,  value,  interest,  maturity, time_of_default):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction(type_, asset, from_id,  to_id,  value,  interest,  maturity,  time_of_default)
        self.accounts.append(transaction)
        del transaction
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # clear_accounts
    # -------------------------------------------------------------------------
    def clear_accounts(self):
        super(Firm, self).clear_accounts()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # purge_accounts
    # -------------------------------------------------------------------------
    def purge_accounts(self):
        super(Firm, self).purge_accounts()
    # -------------------------------------------------------------------------
