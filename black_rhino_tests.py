#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
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

    from tests.tests import Tests

    test = Tests()

    # Tests for Bank
    test.bank__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__get_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__set_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__get_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__set_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__get_parameters_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__check_consistency(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__get_account(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__get_account_num_transactions(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__initialize_standard_bank(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__get_transactions_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test.bank__getattr(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Firm
    test.firm__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__get_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__set_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__get_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__set_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__get_parameters_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__get_account(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__get_account_num_transactions(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__initialize_standard_firm(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__get_transactions_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test.firm__getattr(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Household
    test.household__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__get_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__set_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__get_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__set_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__get_parameters_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__get_account(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__get_account_num_transactions(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__initialize_standard_household(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__get_transactions_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test.household__getattr(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Environment
    test.environment__add_static_parameter(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__add_variable_parameter(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__get_static_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__set_static_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__get_variable_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__set_variable_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__print_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__write_environment_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__read_xml_config_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__initialize(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__initialize_banks_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__initialize_firms_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__initialize_households_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__get_agent_by_id(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__read_transactions_for_banks(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__read_transactions_for_firms(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__read_transactions_for_households(["tests/environments/", "test_all_methods", "tests/log/"])
    test.environment__check_global_transaction_balance(["tests/environments/", "test_all_methods", "tests/log/"])
