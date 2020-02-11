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
        self.legend= {}
        self.environment = environment
        self.runner = runner



    def make_legend(self):
        alist = [("m_1 Cash and gold reserves", 0.0),\
                 ("m_2 SA Interbank deposits, loans and advances", 0.0),\
                 ("m_3 Rand Deposits with and loans to foreign banks", 0.0),\
                 ("m_4 Loans granted under repo agreement", 0.0),\
                 ("m_5 Foreign currency loans and advances", 0.0),\
                 ("m_6 Redeemable preference shares", 0.0),\
                 ("m_7 Corporate instalment credit", 0.0),\
                 ("m_8 Household instalment credit", 0.0),\
                 ("m_9 Corporate mortgage", 0.0),\
                 ("m_10 Household mortgage", 0.0),\
                 ("m_11 Unsecured lending corporate", 0.0),\
                 ("m_12 Unsecured lending households", 0.0),\
                 ("m_13 Other credit (credit card + leasing + Overdarft + factoring debt", 0.0),\
                 ("m_14 Central and provincial government bonds", 0.0),\
                 ("m_15 Other public-sector bonds", 0.0),\
                 ("m_16 Private sector bonds", 0.0),\
                 ("m_17 Equity holdings in subsidiaries and joint ventures", 0.0),\
                 ("m_18 Listed and unlisted equities", 0.0),\
                 ("m_19 Securitisation/ asset-backed securities", 0.0),\
                 ("m_20 Derivative instruments", 0.0),\
                 ("m_21 Treasury bills, SA Reserve Bank bills,  Land Bank bills", 0.0),\
                 ("m_22 Other investments", 0.0),\
                 ("m_23 Non financial assets", 0.0)]

        self.legend = dict(alist)

    def measure_intitial_shock(self, environment):
        self.make_legend()
        for i in self.asset_returns:
            try:
                if self.asset_returns[i] != 0 :
                    print "We have a shock for: %s" %i

                    for k, v in self.legend.iteritems():
                        if i in k:
                            self.legend[k]= self.asset_returns[i]

            except:
                raise TypeError

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


    def __getattr__(self, attr):
        if (attr in self.asset_returns) and (attr in self.legend):
            raise AttributeError('The same name exists in both legend and asset_returns.')
        else:
            try:
                return self.legend[attr]
            except:
                try:
                    return self.asset_returns[attr]
                except:
                    raise AttributeError('Agent %s has no attribute "%s".' % self.identifier, attr)
    # -------------------------------------------------------------------------
