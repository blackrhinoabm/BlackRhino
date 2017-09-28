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
        # self.static_parameters["cbank_directory"] = ""

        self.exogenous_parameters = {}
        self.agents = []
        self.cbanks = []
        self.dealers = []
        self.investmentfunds = []
        self.mmf = []
        self.pensionfunds = []
        self.insurancecompanies = []
        self.hedgefunds = []

        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_xml_config_file(environment_filename)


        # then read in all the agents
        self.initialize_cbanks_from_files(self.static_parameters['cbank_directory'])
        self.initialize_dealers_from_files(self.static_parameters['dealer_directory'])
        self.initialize_pf_from_files(self.static_parameters['pf_directory'])
        self.initialize_ic_from_files(self.static_parameters['ic_directory'])
        self.initialize_mmf_from_files(self.static_parameters['mmf_directory'])
        self.initialize_if_from_files(self.static_parameters['if_directory'])
        self.initialize_hf_from_files(self.static_parameters['hf_directory'])


        # add agents to the list of all agents
        self.agents = [self.cbanks, self.dealers, self.investmentfunds,\
        self.mmf, self.pensionfunds, self.insurancecompanies, self.hedgefunds]





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
##-----------------------------------
  ###------------------------------------------------------------------

    def initialize_cbanks_from_files(self, cbank_directory):
        from src.cbank_class.cbank import Cbank
        agent_files = os.listdir(cbank_directory)

        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                cbank = Cbank()
                agent_filename = cbank_directory + each_agent_file
                cbank.get_parameters_from_file(agent_filename, self)
                self.cbanks.append(cbank)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    def initialize_dealers_from_files(self, dealer_directory):
        from src.dealer_class.dealer import Dealer
        agent_files = os.listdir(dealer_directory)
        for each_agent_file in agent_files:
            if '.xml' in each_agent_file:
                dealer = Dealer()
                agent_filename = dealer_directory + each_agent_file
                dealer.get_parameters_from_file(agent_filename, self)
                self.dealers.append(dealer)

    def initialize_pf_from_files(self, pf_directory):
        from src.pf_class.pf import PF

        agent_files = os.listdir(pf_directory)

        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                pf = PF()
                agent_filename = pf_directory + each_agent_file
                pf.get_parameters_from_file(agent_filename, self)
                self.pensionfunds.append(pf)

    def initialize_ic_from_files(self, ic_directory):
        from src.ic_class.ic import IC
        agent_files = os.listdir(ic_directory)

        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                ic = IC()
                agent_filename = ic_directory + each_agent_file
                ic.get_parameters_from_file(agent_filename, self)
                self.insurancecompanies.append(ic)

    def initialize_mmf_from_files(self, mmf_directory):
        from src.mmf_class.mmf import MMF

        agent_files = os.listdir(mmf_directory)

        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                mmf = MMF()
                agent_filename = mmf_directory + each_agent_file
                mmf.get_parameters_from_file(agent_filename, self)
                self.mmf.append(mmf)

    def initialize_if_from_files(self, if_directory):
        from src.invfund_class.invfund import IF

        agent_files = os.listdir(if_directory)
        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                invfund = IF()
                agent_filename = if_directory + each_agent_file
                invfund.get_parameters_from_file(agent_filename, self)
                self.investmentfunds.append(invfund)

    def initialize_hf_from_files(self, hf_directory):
        from src.hf_class.hf import HF

        agent_files = os.listdir(hf_directory)

        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                hf = HF()
                agent_filename = hf_directory + each_agent_file
                hf.get_parameters_from_file(agent_filename, self)
                self.hedgefunds.append(hf)

    # -------------------------------------------------------------------------
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
