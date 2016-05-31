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

import logging
import os

# ============================================================================
#
# class Bank
#
# ============================================================================


class Agent(object):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""  # identifier of the specific bank
    opinion = 0.0   # initial 'opinion' of the agent
    transition_probabilities= {}  # weights of the opinions

    #
    #
    # CODE
    #
    #

    # -------------------------------------------------------------------------
    # functions for setting/changing id, parameters, and state variables
    # these either return or set specific value to the above variables
    # with the exception of append (2 last ones) which append the dictionaries
    #
    # -------------------------------------------------------------------------
    # functions needed to make Agent() hashable
    # -------------------------------------------------------------------------

    def __key__(self):
        return self.identifier

    def __eq__(self, other):
        return self.__key__() == other.__key__()

    def __hash__(self):
        return hash(self.__key__())


    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self):
        self.identifier = ""  # identifier of the specific agent... e.g. it will be read from the config file
        self.opinion = 0.0  # parameters of the opinion of the specific agent
        self.transition_probabilities= {}  # transision probabilities of the specific bank

        # DO NOT EVER ASSIGN PARAMETERS BY HAND AS DONE BELOW IN PRODUCTION CODE
        # ALWAYS READ THE PARAMETERS FROM CONFIG FILES
        # OR USE THE FUNCTIONS FOR SETTING / CHANGING VARIABLES
        # CONVERSELY, IF YOU WANT TO READ THE VALUE, DON'T USE THE FULL NAMES
        # INSTEAD USE __getattr__ POWER TO CHANGE THE COMMAND FROM
        # instance.static_parameters["xyz"] TO instance.xyz - THE LATTER IS PREFERRED

    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # get_parameters_from_file
    # reads the specified config file given the environment
    # and sets parameters to the ones found in the config file
    # the config file should be an xml file that looks like the below:
    # <agent identifier='string'>
    #     <parameter name='string' value='string'></parameter>
    # </agent>
    # -------------------------------------------------------------------------


    def get_parameters_from_file(self, agent_filename, environment):
        from xml.etree import ElementTree

        try:
            xmlText = open(agent_filename).read()
            element = ElementTree.XML(xmlText)
            # we get the identifier
            self.identifier = element.attrib['identifier']
            # and then we're only interested in <parameter> fields
            element = element.findall('parameter')

            # loop over all <parameter> entries in the xml file
            for subelement in element:
                name = subelement.attrib['name']
                value = subelement.attrib['value']

            # take 'starting opinion' from static type
                if subelement.attrib['type']=='static':
                    return value=float(value)

            # take weights from transition type and add them to transition probabilities list
                if subelement.attrib['type']=='transition':
                    self.transition_probabilities[name]=float(value)

        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)
    # a standard function reading parameters of the agents from
    # an xml file, looking somewhat like the below
    # <agent identifier='string'>
    #     <parameter name='string' value='string'></parameter>
    # </agent>

    def create_temporary_variable(self, )
        tempv =

    def multiply_matrices

 return 