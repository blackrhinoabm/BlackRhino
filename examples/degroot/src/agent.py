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

# This script contains the Agent class which is later called in the Environment
# script. In the degroot learning algorithm a group of individuals observe
# each other's opinions and adapt their subjective propability distribution
# of an unknown value of a parameter theta
# The model (which is executed in the updater script) describes how the group
# forms a collective subjective propability distrbution by revealing their
# individual distribution to each other and pooling their opnion

# Implementation: Every agent has an opinion variable and weights/probabilities
# describing how much it'cares' for the opinion of the other. These weights are
# stored in a dictionary called transition_probabilities

import logging

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

    identifier = ""  # identifier of the specific agent
    opinion = 0.0   # initial 'opinion' of the agent
    transition_probabilities = {}  # weights of the opinions

    #
    #
    # CODE
    #
    #

    # -----------------------------------------------------------------------
    # __init__  used to automatically instantiate an agent as an object when
    # the agent class is called
    # ------------------------------------------------------------------------

    def __init__(self):
        self.identifier = ""  # identifier of the specific agent
        self.opinion = 0.0  # opinion of the specific agent
        self.transition_probabilities = {}  # dictionary with weights

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
                if subelement.attrib['type'] == 'static':
                    name = subelement.attrib['name']
                    value = subelement.attrib['value']

                    if name == 'starting opinion':
                        self.opinion = float(value)

                if subelement.attrib['type'] == 'transition':
                    name = subelement.attrib['name']
                    value = subelement.attrib['value']
                    self.transition_probabilities[name] = float(value)

        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)

    # -------------------------------------------------------------------------
    # The next function creates a temporary variable tempv (which needs some
    # kind of starting value, here 0.0),
    # then we go through every agent in the list agents which is defined in the
    # environment class (in the environment script), take its opinion variable,
    # multiply it with the weight stored in the transition_probabilities
    # dictionary. We also need the key agent.identifier to tell python
    # which weight to multiply with which opinion
    # return is needed to pass the tempv variable back to the updater script
    # -------------------------------------------------------------------------
    def create_temp_variable(self, environment):
        tempv = 0.0

        for agent in environment.agents:
            tempv = tempv + agent.opinion * self.transition_probabilities[agent.identifier]

        return tempv
