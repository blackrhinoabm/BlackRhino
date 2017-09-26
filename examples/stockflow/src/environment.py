#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-


import os
import numpy as np
from xml.etree import ElementTree

# -------------------------------------------------------------------------
#
#  class Environment
#
# -------------------------------------------------------------------------


class Environment():
    #
    #
    #
    # CODE
    #
    def __init__(self, environment_directory, identifier):
        self.initialize(environment_directory, identifier)

    # ------------------------------------------------------------------------
    # the next function
    # initializes the environment, initializing all the exogenouss
    # reading the env_config file from supplied environment_directory and
    # identifier, and initializes all agents from the directories
    # supplied in the main config file
    # -------------------------------------------------------------------------
    def initialize(self, environment_directory, identifier):
        self.identifier = identifier

        self.static_parameters = {}
        self.exogenous_parameters = {}
        self.agents = []

        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_xml_config_file(environment_filename)
        # then read in all the agents
        self.initialize_agents_from_files(self.static_parameters['agent_directory'])


    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    # read_xml_config_file(self, config_file_name)
    # reads an xml file with config and sets identifier and parameters
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def read_xml_config_file(self, env_filename):

        xmlText = open(env_filename).read()
        element = ElementTree.XML(xmlText)  # we tell python it's an xml
        self.identifier = element.attrib['identifier']

        # loop over all entries in the xml file
        for subelement in element:
            name = subelement.attrib['name']

            if subelement.attrib['type'] == 'static':
                try:  # we see whether the value is a str
                    value = float(subelement.attrib['value'])
                except:
                    value = str(subelement.attrib['value'])
                self.static_parameters[name] = value

            if subelement.attrib['type'] == 'exogenous':
                try:
                    value = float(subelement.attrib['value'])
                except:  # if not, it is a string
                    value = str(subelement.attrib['value'])
                self.exogenous_parameters[name] = value

    def initialize_agents_from_files(self, agent_directory):

        from src.agent import Agent
        agent_files = os.listdir(agent_directory)

        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                agent = Agent()
                agent_filename = agent_directory + each_agent_file
                agent.get_parameters_from_file(agent_filename, self)
                self.agents.append(agent)

    # -------------------------------------------------------------------------

    def __getattr__(self, attr):
        if (attr in self.static_parameters) and (attr in self.exogenous_parameters):
            raise AttributeError('The same name exists in both static and exogenous parameters.')
        else:
            try:
                return self.static_parameters[attr]
            except:
                try:
                    return self.exogenous_parameters[attr]
                except:
                    raise AttributeError('Environment has no attribute "%s".' % attr)

        # a standard method for returning attributes from the dectionaries as attributes

    def __str__(self):
        """
        Class exogenouss: identifier, static_parameters, exogenous_parameters
        Local exogenouss: out_str, entry, value, from_value, to_value
        """
        out_str = "<config identifier='" + self.identifier + "'>\n"
        for entry in self.static_parameters:
            value = self.static_parameters[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                out_str = out_str + "  <parameter type='static' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
            else:
                raise TypeError
        for entry in self.exogenous_parameters:
            if isinstance(self.exogenous_parameters[entry], list):
                from_value = self.exogenous_parameters[entry][0]
                to_value = self.exogenous_parameters[entry][1]
                out_str = out_str + "  <parameter type='exogenous' name='" + entry + "' range='" + str(from_value) + "-" + \
                    str(to_value) + "'></parameter>\n"
            else:
                raise TypeError
        out_str = out_str + "</config>"

        return out_str
