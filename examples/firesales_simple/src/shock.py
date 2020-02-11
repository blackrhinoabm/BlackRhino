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

# from abm_template.src.baseshock import BaseShock
import logging

# -------------------------------------------------------------------------
#  class Shock
# -------------------------------------------------------------------------


class Shock():
    #
    #
    # VARIABLES
    #
    #
    identifier = ""

    asset_returns = {}
    #
    #
    # METHODS
    #
    #

    # -------------------------------------------------------------------------
    # do_shock(environment, time, step)
    # This is the main wrapper function for the shocks
    # Here we specify what shocks are doing to the environment at the
    # beginning and the end (step) of the affected sweeps
    # Shocks are distinguished by the shock_type saved in the environment's
    # variables, these are strings for our purposes.
    # -------------------------------------------------------------------------

    def get_identifier(self):
        return self.identifier

    def __init__(self, environment, runner):

        self.asset_returns = {}

        self.environment = environment

        self.runner = runner

    def read_xml_config_file(self, config_file):
        from xml.etree import ElementTree

        try:
            xmlText = open(config_file).read()
            element = ElementTree.XML(xmlText)
            # we get the identifier
            self.identifier = element.attrib['identifier']

            # and then we're only interested in <parameter> fields
            element = element.findall('parameter')

            # loop over all <parameter> entries in the xml file
            for subelement in element:

                if subelement.attrib['type'] == 'asset':
                    name = str(subelement.attrib['name'])
                    value = float(subelement.attrib['value'])
                    self.asset_returns[name] = value

        except:
            logging.error("    ERROR: %s could not be parsed", config_file)


    # -------------------------------------------------------------------------
