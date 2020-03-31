import os
import logging
import numpy as np

from xml.etree import ElementTree
from abm_template.src.baseconfig import BaseConfig
from src.agent import Agent


class Environment(BaseConfig):
    identifier = ""  # identifier of the environment
    static_parameters = {}  # a dictionary containing all environmenet parameters
    agents = []
    static_parameters["lambda"] = 0  # number of simulations

    static_parameters["num_simulations"] = 0  # number of simulations
    static_parameters["num_sweeps"] = 0  # numbers of runs in a single simulation
    static_parameters["num_agents"] = 0  # number of agents in a simulation
    static_parameters["agent_directory"] = ""  # directory containing agent xmls

    variable_parameters = {}
    assets = {}

    shocks = []

    def __init__(self, environment_directory, identifier):
        self.identifier = identifier
        self.static_parameters = {"num_simulations": 0, "num_sweeps": 0, "num_agents": 0,
                                  "transmission_rate": 0, "days_incubation": 0, "days_with_symptoms": 0,
                                  "agent_directory": "", "measurement_config": ""}

        self.agents = []

        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_xml_config_file(environment_filename)
        logging.info(" environment file read: %s", environment_filename)

        # then read in all the agents
        self.initialize_agents_from_files(self.static_parameters['agent_directory'])

        # create the grid structure
        self.rows, self.columns = int(np.sqrt(self.static_parameters["num_agents"]))
        self.agents = []
        for c in range(self.columns):
            row = []
            for r in range(self.rows):
                row.append(Agent(str([r, c]), 's', (c, r), self.static_parameters["transmission_rate"]))
            self.agents.append(row)
        # determine neighbours after the grid is complete
        for row, agent_set in enumerate(self.agents):
            for col, agent in enumerate(agent_set):
                agent.neighbours = []
                # add horizontal neighbours
                for n in [col - 1, col + 1]:
                    if n in range(self.columns):  # check if on grid
                        agent.neighbours.append(self.agents[row][n])
                # add vertical neighbours
                for n in [row - 1, row + 1]:
                    if n in range(self.columns):  # check if on grid
                        agent.neighbours.append(self.agents[n][col])
        self.infection_states = []

    def read_xml_config_file(self, env_filename):
        xmlText = open(env_filename).read()
        element = ElementTree.XML(xmlText)
        self.identifier = element.attrib['identifier']

        # loop over all entries in the xml file
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
        agent_files = os.listdir(agent_directory)

        for each_agent_file in agent_files:
            if '.xml' in each_agent_file:
                agent = Agent()
                agent_filename = agent_directory + each_agent_file
                agent.get_parameters_from_file(agent_filename, self)
                self.agents.append(agent)

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




