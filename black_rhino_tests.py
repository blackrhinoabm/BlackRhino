#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

"""
This is a minimal example.

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
along with this program. If not, see <http://www.gnu.org/licenses/>

The development of this software has been supported by the ERA-Net
on Complexity through the grant RESINEE.
"""

# -------------------------------------------------------------------------
#
#  MAIN
#
# -------------------------------------------------------------------------
if __name__ == '__main__':
    import pdb  # python debugger, for debugging purposes only

    import sys
    # sys.path.append('src/')
    import logging

    from src.tests import Tests

    test = Tests()

    # Tests for Bank
    test.bank__get_identifier(["environments/", "test_all_methods", "log/"])
    test.bank__set_identifier(["environments/", "test_all_methods", "log/"])
    test.bank__get_parameters(["environments/", "test_all_methods", "log/"])
    test.bank__set_parameters(["environments/", "test_all_methods", "log/"])
    test.bank__get_state_variables(["environments/", "test_all_methods", "log/"])
    test.bank__set_state_variables(["environments/", "test_all_methods", "log/"])
    test.bank__str(["environments/", "test_all_methods", "log/"])
    test.bank__get_parameters_from_file(["environments/", "test_all_methods", "log/"])
    test.bank__check_consistency(["environments/", "test_all_methods", "log/"])
    test.bank__get_account(["environments/", "test_all_methods", "log/"])
    test.bank__get_account_num_transactions(["environments/", "test_all_methods", "log/"])
    test.bank__add_transaction(["environments/", "test_all_methods", "log/"])
    test.bank__clear_accounts(["environments/", "test_all_methods", "log/"])
    test.bank__purge_accounts(["environments/", "test_all_methods", "log/"])
    test.bank__initialize_standard_bank(["environments/", "test_all_methods", "log/"])

    # Tests for Firm
    test.firm__get_identifier(["environments/", "test_all_methods", "log/"])
    test.firm__set_identifier(["environments/", "test_all_methods", "log/"])
    test.firm__get_parameters(["environments/", "test_all_methods", "log/"])
    test.firm__set_parameters(["environments/", "test_all_methods", "log/"])
    test.firm__get_state_variables(["environments/", "test_all_methods", "log/"])
    test.firm__set_state_variables(["environments/", "test_all_methods", "log/"])
    test.firm__str(["environments/", "test_all_methods", "log/"])
    test.firm__get_parameters_from_file(["environments/", "test_all_methods", "log/"])
    test.firm__get_account(["environments/", "test_all_methods", "log/"])
    test.firm__get_account_num_transactions(["environments/", "test_all_methods", "log/"])
    test.firm__add_transaction(["environments/", "test_all_methods", "log/"])
    test.firm__clear_accounts(["environments/", "test_all_methods", "log/"])
    test.firm__purge_accounts(["environments/", "test_all_methods", "log/"])
    test.firm__initialize_standard_firm(["environments/", "test_all_methods", "log/"])

    # Tests for Household
    test.household__get_identifier(["environments/", "test_all_methods", "log/"])
    test.household__set_identifier(["environments/", "test_all_methods", "log/"])
    test.household__get_parameters(["environments/", "test_all_methods", "log/"])
    test.household__set_parameters(["environments/", "test_all_methods", "log/"])
    test.household__get_state_variables(["environments/", "test_all_methods", "log/"])
    test.household__set_state_variables(["environments/", "test_all_methods", "log/"])
    test.household__str(["environments/", "test_all_methods", "log/"])
    test.household__get_parameters_from_file(["environments/", "test_all_methods", "log/"])
    test.household__get_account(["environments/", "test_all_methods", "log/"])
    test.household__get_account_num_transactions(["environments/", "test_all_methods", "log/"])
    test.household__add_transaction(["environments/", "test_all_methods", "log/"])
    test.household__clear_accounts(["environments/", "test_all_methods", "log/"])
    test.household__purge_accounts(["environments/", "test_all_methods", "log/"])
    test.household__initialize_standard_firm(["environments/", "test_all_methods", "log/"])
