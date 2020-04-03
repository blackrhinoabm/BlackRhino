from examples.coviid.src.abm_template.basemodel import BaseModel
from examples.coviid.src.agent import Agent


class Updater:
    def __init__(self, environment):
        self.environment = environment
        self.new_opinion = {}
        self.initial_opinion = {}

    def do_update(self, environment):
        # some agents are the infected
        sick_with_symptoms = []
        sick_without_symptoms = []
        for row, agent_set in enumerate(environment.agents):
            for col, agent in enumerate(agent_set): #TODO replace this: for neighbour in nx.neighbours_of_network_agent
                if agent.status == 'i1':
                    sick_without_symptoms.append(agent)
                    agent.incubation_days += 1

                    # some agents get symptoms
                    if agent.incubation_days > environment.agent_parameters['days_incubation']:
                        agent.status = 'i2'
                        sick_without_symptoms.remove(agent)

                elif agent.status == 'i2':
                    sick_with_symptoms.append(agent)
                    agent.sick_days += 1
                    # some agents recover
                    if agent.sick_days > environment.agent_parameters['days_with_symptoms']:
                        agent.status = 'r'
                        sick_with_symptoms.remove(agent)
        for agent in sick_without_symptoms + sick_with_symptoms:
            agent.infect()

        environment.infection_states.append(environment.store_network())

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Updater, self).set_identifier(value)

    def __str__(self):
        super(Updater, self).__str__(self)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, values):
        super(Updater, self).set_model_parameters(values)

    def get_interactions(self):
        return self.interactions

    def interactions(self):
        super(Updater, self).interactions(self)

    def set_interactions(self, values):
        super(Updater, self).set_interactions(values)
