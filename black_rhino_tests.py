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

    t = Tests()

    # Tests for Bank
    t.bank__get_identifier(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__set_identifier(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__get_parameters(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__set_parameters(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__get_state_variables(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__set_state_variables(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__str(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__get_parameters_from_file(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__check_consistency(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__get_account(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__get_account_num_transactions(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__add_transaction(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__clear_accounts(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__purge_accounts(["src\\environments\\", "test3", "src\\log\\"])
    t.bank__initialize_standard_bank(["src\\environments\\", "test3", "src\\log\\"])
