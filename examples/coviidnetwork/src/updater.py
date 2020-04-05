import random
import numpy as np


class Updater:
    def __init__(self, environment):
        self.environment = environment
        self.new_opinion = {}
        self.initial_opinion = {}

    def do_update(self, environment, seed=1):
        # set monte carlo seed
        np.random.seed(seed)  # TODO necessary to do twice?
        random.seed(seed)

        # some agents are the infected
        sick_with_symptoms = []
        sick_without_symptoms = []

        # some agents are in the hospital
        critical = []
        # some agents are recovered
        recovered = []

        #TODO DEBUG THIS some agents are dead
        dead = []

        for idx, agent in enumerate(environment.agents):
            if agent.status == 'd':
                dead.append(agent)

            if agent.status == 'i1':
                sick_without_symptoms.append(agent)
                agent.incubation_days += 1

                # some agents get symptoms
                if agent.incubation_days > environment.agent_parameters['days_incubation']:
                    agent.status = 'i2'
                    sick_without_symptoms.remove(agent)

            if agent.status == 'i2':
                sick_with_symptoms.append(agent)
                agent.sick_days += 1
                # some agents recover
                if agent.sick_days > environment.agent_parameters['days_incubation']:
                    if np.random.random() < agent.prob_hospital:
                        agent.status = 'c'
                        sick_with_symptoms.remove(agent)
                    else:
                        agent.status = 'r'
                        sick_with_symptoms.remove(agent)

            if agent.status == 'c':
                critical.append(agent)
                agent.critical_days += 1
                # some agents in critical status will die, the rest will recover
                if agent.critical_days > environment.agent_parameters['days_critical']:
                    if np.random.random() < (agent.prob_death * environment.health_overburdened_multi):
                        agent.status = 'd'
                        critical.remove(agent)
                    else:
                        agent.status = 'r'
                        critical.remove(agent)

            if agent.status == 'r':
                recovered.append(agent)
                agent.days_recovered += 1
                if np.random.random() < (agent.prob_susceptible * agent.days_recovered):
                    recovered.remove(agent)
                    agent.status = 's'

        # if the health system is overburdened the multiplier for the death rate is higher than otherwise
        if len(critical) / len(environment.agents) > float(environment.static_parameters["health_system_capacity"]):
            environment.health_overburdened_multi = float(environment.static_parameters["health_overburdened_multiplier"])
        else:
            environment.health_overburdened_multi = 1.0

        for agent in sick_without_symptoms + sick_with_symptoms:
            # find indices from neighbour agents
            neighbours_from_graph = [x for x in environment.network.neighbors(agent.identifier)]
            # find the corresponding agents
            neighbours_to_infect = [environment.agents[idx] for idx in neighbours_from_graph]
            agent.infect(neighbours_to_infect)

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
