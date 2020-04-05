import logging
import copy
from xml.etree import ElementTree
from examples.coviidnetwork.src.agent import Agent
import networkx as nx
import random
import numpy as np


class Environment:
    def __init__(self, environment_directory, identifier, seed=1):
        np.random.seed(seed)
        random.seed(seed)

        self.identifier = identifier
        self.static_parameters = {}

        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_xml_config_file(environment_filename)
        logging.info(" environment file read: %s", environment_filename)

        # then read in all the agents
        self.agent_parameters = {}
        self.initialize_agents_from_files(self.static_parameters['agent_directory'])

        # create network
        self.network = nx.erdos_renyi_graph(self.static_parameters["num_agents"], 0.01)
        self.agents = [Agent(x, 's', self.agent_parameters["transmission_rate"],
                             self.agent_parameters["probability_hospital"], self.agent_parameters["probability_to_die"],
                             self.agent_parameters["probability_susceptible"]
                             ) for x in range(len(self.network.nodes))]

        # add agent to the network structure
        for idx, agent in enumerate(self.agents):
            self.network.nodes[idx]['agent'] = agent

        self.health_overburdened_multi = 1.0
        self.infection_states = []

    def store_network(self):
        current_network = copy.deepcopy(self.network)
        return current_network

    def read_xml_config_file(self, env_filename):
        xmlText = open(env_filename).read()
        element = ElementTree.XML(xmlText)
        self.identifier = element.attrib['identifier']

        # set parameters using xml file
        for subelement in element:
            try:  # we see whether the value is a int
                value = int(subelement.attrib['value'])
                type_ = subelement.attrib['type']
                self.static_parameters[type_] = value

            except:  # if not, it is a string
                value = str(subelement.attrib['value'])
                type_ = subelement.attrib['type']
                self.static_parameters[type_] = value

    def initialize_agents_from_files(self, agent_directory):
        xmlText = open(agent_directory).read()
        element = ElementTree.XML(xmlText)

        for subelement in element:
            try:  # we see whether the value is a int
                value = int(subelement.attrib['value'])
                name = subelement.attrib['name']
                self.agent_parameters[name] = value

            except:  # if not, it is a string
                value = float(subelement.attrib['value'])
                name = subelement.attrib['name']
                self.agent_parameters[name] = value

    def __getattr__(self, attr):
        return super(Environment, self).__getattr__(attr)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Environment, self).set_identifier(value)

    def __str__(self):
        return super(Environment, self).__str__()

    def accrue_interests(self):
        super(Environment, self).accrue_interests()

    def add_shock(self, shock):
        super(Environment, self).add_shock()

    def add_static_parameter(self, params):
        super(Environment, self).add_static_parameters(params)

    def get_static_parameters(self):
        return self.static_parameters

    def set_static_parameters(self, params):
        super(Environment, self).set_static_parameters(params)

    def add_variable_parameter(self, params):
        super(Environment, self).add_static_parameters(params)

    def get_variable_parameters(self):
        return self.variable_parameters

    def set_variable_parameters(self, params):
        super(Environment, self).set_variable_parameters(params)

    def get_assets(self):
        return self.assets

    def set_assets(self, params):
        super(Environment, self).set_assets(params)

    def get_shocks(self):
        return self.shocks

    def set_shocks(self, params):
        super(Environment, self).set_shocks(params)

    def agents_generator(self):
        super(Environment, self).agents_generator()

    def get_agent_by_id(self, ident):
        super(Environment, self).get_agent_by_id(ident)

    def check_global_transaction_balance(self, _type):
        super(Environment, self).check_global_transaction_balance(_type)

    def write_environment_file(self, file_name):
        super(Environment, self).write_environment_file()

    def print_parameters(self):
        super(Environment, self).print_parameters()

    def update_asset_returns(self):
        super(Environment, self).update_asset_returns()




