#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

"""
fin_deepening is a multi-agent computational model extending
the Kitoyaki/Moore financial deeepening theta-phi model.
Copyright (C) 2015 Pawel Fiedor (Pawel.F.Fiedor@IEEE.org)

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

# import logging
# import math
from src.baseconfig import BaseConfig

# ============================================================================
#
# class Config
#
# ============================================================================


class Config(BaseConfig):

    identifier = ""
    static_parameters = {}
    variable_parameters = {}

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Config, self).set_identifier(_value)

    def get_static_parameters(self):
        return self.static_parameters

    def set_static_parameters(self, _value):
        super(Config, self).set_static_parameters(_value)

    def get_variable_parameters(self):
        return self.variable_parameters

    def set_variable_parameters(self, _value):
        super(Config, self).set_variable_parameters(_value)

    def __str__(self):
        super(Config, self).__str__()

    def __init__(self):
        super(Config, self).__init__()

    def read_xml_config_file(self, config_file_name):
        super(Config, self).read_xml_config_file(config_file_name)
