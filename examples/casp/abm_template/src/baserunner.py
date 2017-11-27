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

__author__ = """Pawel Fiedor (pawel.fiedor@uct.ac.za)"""

# -------------------------------------------------------------------------
#
#  class Runner
#
# -------------------------------------------------------------------------


class BaseRunner(object):
    """
    Class variables: __metaclass__, identifier, num_sweeps
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

    @abc.abstractmethod
    def get_num_sweeps(self):
        return
    @abc.abstractmethod
    def set_num_sweeps(self, _num_sweeps):
        """
        Class variables: num_sweeps
        Local variables: _num_sweeps
        """
        if not isinstance(_num_sweeps, int):
            raise TypeError
        else:
            self.num_sweeps = _num_sweeps
        return
    num_sweeps = abc.abstractproperty(get_num_sweeps, set_num_sweeps)

    @abc.abstractmethod
    def __init__(self, model_config):
        """
        Class variables:
        Local variables: _params, model_config
        """
        _num_sweeps = model_config.get_model_parameters()['num_sweeps']

        self.set_identifier(model_config.identifier)
        self.set_num_sweeps(_num_sweeps)

    @abc.abstractmethod
    def do_run(self):
        # This is the wrapper for the main run loop
        # In concrete implementations this will run the updater for each sweep
        # But also handle measurement class writing
        # And calling the shocks (through Shock class)
        pass
