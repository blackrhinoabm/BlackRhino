#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import logging
from xml.etree import ElementTree
from abm_template.src.baseconfig import BaseConfig

# -------------------------------------------------------------------------
#
#  class Environment
#
# -------------------------------------------------------------------------


class Environment2(BaseConfig):
    #
    #
    # VARIABLES
    #
    #
    identifier = ""  # identifier of the environment
    static_parameters = {}  # a dictionary containing all environmenet parameters
    agents = []

    static_parameters["num_simulations"] = 0  # number of simulations
    static_parameters["num_sweeps"] = 0  # numbers of runs in a single simulation
    static_parameters["num_agents"] = 0  # number of agents in a simulation
    static_parameters["agent_directory"] = ""  # directory containing agent xmls
    static_parameters["shock_config"] = ""  # directory containing agent xmls
    static_parameters["illiquidity"] = ""
    
    saveparams = {} 


    variable_parameters = {}
    assets = {}

    shocks = []
    #
    # CODE
    #

    def __getattr__(self, attr):
        return super(Environment2, self).__getattr__(attr)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Environment2, self).set_identifier(value)

    def __str__(self):
        return super(Environment2, self).__str__()

    def accrue_interests(self):
        super(Environment2, self).accrue_interests()

    def add_shock(self, shock):
        super(Environment2, self).add_shock()

    def add_static_parameter(self, params):
        super(Environment2, self).add_static_parameters(params)

    def get_static_parameters(self):
        return self.static_parameters

    def set_static_parameters(self, params):
        super(Environment2, self).set_static_parameters(params)

    def add_variable_parameter(self, params):
        super(Environment2, self).add_static_parameters(params)

    def get_variable_parameters(self):
        return self.variable_parameters

    def set_variable_parameters(self, params):
        super(Environment2, self).set_variable_parameters(params)

    def get_assets(self):
        return self.assets

    def set_assets(self, params):
        super(Environment, self).set_assets(params)

    def get_shocks(self):
        return self.shocks

    def set_shocks(self, params):
        super(Environment2, self).set_shocks(params)

    def agents_generator(self):
        super(Environment2, self).agents_generator()

    def get_agent_by_id(self, ident):
        super(Environment2, self).get_agent_by_id(ident)

    def check_global_transaction_balance(self, _type):
        super(Environment2, self).check_global_transaction_balance(_type)

    def write_environment_file(self, file_name):
        super(Environment2, self).write_environment_file()

    def print_parameters(self):
        super(Environment2, self).print_parameters()

    def update_asset_returns(self):
        super(Environment2, self).update_asset_returns()

    def __init__(self, environment_directory, identifier, agent_config_dir):
        self.initialize(environment_directory, identifier, agent_config_dir)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # read_xml_config_file(self, config_file_name)
    # reads an xml file with config and sets identifier and parameters
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    def read_xml_config_file(self, env_filename):

        try:
            xmlText = open(env_filename).read()
            element = ElementTree.XML(xmlText)  # we tell python it's an xml
            self.identifier = element.attrib['identifier']

            # loop over all entries in the xml file
            for subelement in element:

                try:  # we see whether the value is a int
                    if subelement.attrib['type'] == 'illiquidity':
                        value = float(subelement.attrib['value'])
                        type_ = subelement.attrib['type']
                        self.static_parameters[type_] = value

                    else:
                        value = int(subelement.attrib['value'])
                        type_ = subelement.attrib['type']
                        self.static_parameters[type_] = value

                except:  # if not, it is a string
                    value = str(subelement.attrib['value'])
                    type_ = subelement.attrib['type']
                    self.static_parameters[type_] = value

        except:
            logging.error("    ERROR: %s could not be parsed", env_filename)
    # -------------------------------------------------------------------------
    # the next function
    # initializes the environment, initializing all the variables
    # reading the env_config file from supplied environment_directory and
    # identifier, and initializes all agents from the directories
    # supplied in the main config file
    # -------------------------------------------------------------------------

    def initialize(self, environment_directory, identifier, agent_config_dir):
        self.identifier = identifier

        self.static_parameters = {}
        self.static_parameters["num_simulations"] = 0
        self.static_parameters["num_sweeps"] = 0
        self.static_parameters["num_agents"] = 0
        self.static_parameters["agent_directory"] = ""
        self.static_parameters["shock_config"] = ""
        self.static_parameters["illiquidity"] = ""

        self.static_parameters['leverage_increase']=0
        self.agents = []
        self.shocks = []
        self.shock_measure = (0,0)

        #variables interesting for simulation and measurement
        self.variable_parameters['system_TAS'] = 0
        self.variable_parameters['system_assets'] = 0
        self.variable_parameters['system_equity'] = 0
        self.variable_parameters['system_equity_pre_shock'] = 0
        self.variable_parameters['system_debt'] = 0
        self.variable_parameters['cum_equity_losses'] = 0
        self.variable_parameters['rel_equity_losses'] = 0


        self.variable_parameters['system_equity_losses'] = 0
        self.variable_parameters['system_cash_reserves'] = 0

        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_xml_config_file(environment_filename)
        # logging.info("We read the environment file from: %s", environment_filename)

        self.static_parameters['agent_directory'] = agent_config_dir
        # then read in all the agents
        self.initialize_agents_from_files(self.static_parameters['agent_directory'])

        self.initialize_shock(self.static_parameters['shock_config'])



    # -------------------------------------------------------------------------
    def initialize_agents_from_files(self, agent_directory):

        from src.agent import Agent
        agent_files = os.listdir(agent_directory)

        for each_agent_file in agent_files:

            if '.xml' in each_agent_file:
                agent = Agent()
                agent_filename = agent_directory + each_agent_file
                agent.get_parameters_from_file(agent_filename, self)
                self.agents.append(agent)
                agent.initialize_total_assets()

    def initialize_shock(self, shock_config):
        from src.runner import Runner
        runner = Runner(self)

        from src.shock import Shock
        shock = Shock(self, runner)
        shock.read_xml_config_file(shock_config)
        self.shocks.append(shock)

        shock.measure_intitial_shock(self)
        for k, v in shock.legend.iteritems():
            if shock.legend[k] != 0:
                self.shock_measure = (k, v)
                # df_shock = pd.DataFrame[]

       # you can use this code below to see if the function of reading the shock worked
        for key in shock.asset_returns:
            if shock.asset_returns[key]!= 0.0:
                # print "0. ***ENV.PY*** When shock is initialised:  The asset class", key, "is shocked by", shock.asset_returns[key] * 100, "%"
                pass
            #print shock.asset_returns.items()
