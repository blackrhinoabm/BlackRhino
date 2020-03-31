import logging
from xml.etree import ElementTree
import numpy as np

from abm_template.src.baseagent import BaseAgent


class Agent(BaseAgent):
    identifier = ""  # identifier of the specific agent
    opinion = 0.0   # 'opinion' of the agent
    initial_opinion = 0.0   # initial  'opinion' of the agent

    state_variables = {}
    parameters = {}

    ''' Accounts is not used in our example, but it's in the BaseAgent
    parent class'''
    accounts = []

    '''The below is from an older version, where weights were stored in
    a dictionary We are using network graphs now, so its no needed anymore
    transition_probabilities = {}   '''

    def __getattr__(self, attr):
        super(Agent, self).__getattr__(attr)

    def __str__(self):
        ret_str = "  <agent identifier='" + self.identifier + "'>\n "

        ret_str = ret_str + " <parameter type='static' name=opinion value=" + str(self.opinion) + "></parameter>\n"

        for each_agent in self.transition_probabilities:
            weight = self.transition_probabilities[each_agent]
            if isinstance(weight, int) or isinstance(weight, float) or isinstance(weight, str):
                ret_str = ret_str + "    <parameter type='transition' + 'name='" + each_agent + "' value='" + str(weight) + "'></parameter>\n"
            else:
                raise TypeError

        ret_str = ret_str + "</agent>\n"

        return ret_str

    def get_parameters(self):
        return self.parameters

    def append_parameters(self, values):
        super(Agent, self).append_parameters(values)

    def set_parameters(self, values):
        super(Agent, self).append_parameters(values)

    def append_state_variables(self, values):
        super(Agent, self).append_state_variables(values)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _variables):
        super(Agent, self).set_state_variables(_variables)

    def check_consistency(self, assets, liabilities):
        super(Agent, self).check_consistency(assets,liabilities)

    def clear_accounts(self):
        super(Agent, self).clear_accounts()

    def get_account(self, _type):
        super(Agent, self).get_account(_type)

    def purge_accounts(self, environment):
        super(Agent, self).purge_accounts(environment)

    def get_account_num_transactions(self, _type):
        super(Agent, self).get_account_num_transactions(_type)

    def get_transactions_from_file(self, filename, environment):
        super(Agent, self).get_transactions_from_file(filename, environment)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Agent, self).set_identifier(value)

    def update_maturity(self):
        super(Agent, self).update_maturity()

    # -----------------------------------------------------------------------
    # __init__  used to automatically instantiate an agent as an object when
    # the agent class is called
    # ------------------------------------------------------------------------

    def __init__(self):
        self.identifier = ""  # identifier of the specific agent
        self.opinion = 0.0  # opinion of the specific agent
        self.initial_opinion = 0

    def infect(self):
        for neighbour in self.neighbours:
            # only infect neighbours that are susceptible
            if neighbour.status == 's' and np.random.random() > self.transmission_rate:
                neighbour.status = 'i1'

    def get_parameters_from_file(self, agent_filename, environment):
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

                    if name == 'starting_opinion':
                        self.opinion = float(value)
                        self.initial_opinion = float(value)

        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)

