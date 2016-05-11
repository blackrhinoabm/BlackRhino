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
from src.baserunner import BaseRunner

from sample_config import Config
from sample_model import Model

# ============================================================================
#
# class Runner
#
# ============================================================================


class Runner(BaseRunner):

    identifier = ""
    num_simulations = 0

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Runner, self).set_identifier(_value)

    def get_num_simulations(self):
        return self.model_parameters

    def set_num_simulations(self, _value):
        super(Runner, self).set_num_simulations(_value)

    def __init__(self, config):
        self.identifier = config.identifier
        self.num_simulations = int(config.static_parameters['num_simulations'])

        self.model_config = Config()
        model_config_file_name = config.get_static_parameters()['model_config_file_name']
        self.model_config.read_xml_config_file(model_config_file_name)

        self.results = []
        self.output_file_name = config.static_parameters['output_file_name']

    def write_results(self, model):
        out_text = ""
        # loop over all results
        for result in self.results:  # each result is a list (of lists) itself
            for entry in result:
                out_text += str(entry) + ";"
            out_text += "\n"

        out_file_name = self.output_file_name
        out_file = open(out_file_name, 'w')
        out_file.write(out_text)
        out_file.close()

    def do_run(self):
        for i in range(0, self.num_simulations):

            model = Model(self.model_config)
            model.initialize_agents()
            result = model.do_update()

            self.results.append(result)
            self.write_results(model)
