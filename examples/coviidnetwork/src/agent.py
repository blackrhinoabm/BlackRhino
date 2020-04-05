import logging
from xml.etree import ElementTree
import numpy as np


class Agent:
    def __init__(self, identifier, status, transmission_rate, prob_hospital, prob_death, prob_susceptible):
        # parameters
        self.identifier = identifier  # identifier of the specific agent
        self.transmission_rate = transmission_rate
        self.prob_hospital = prob_hospital
        self.prob_death = prob_death
        self.prob_susceptible = prob_susceptible

        # state_variables
        self.sick_days = 0
        self.incubation_days = 0
        self.critical_days = 0
        self.days_recovered = 0
        self.status = status

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
                name = subelement.attrib['name']
                value = subelement.attrib['value']

                if name == 'status':
                    self.status = value
                elif name == 'transmission_rate':
                    self.transmission_rate = float(value)

        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)

    def infect(self, neighours):
        for neighbour in neighours:
            # only infect neighbours that are susceptible
            random_draw = np.random.random()
            if neighbour.status == 's' and random_draw < self.transmission_rate:
                neighbour.status = 'i1'

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


