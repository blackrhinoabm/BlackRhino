#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

import math
import random

from src.basemodel import BaseModel

from sample_config import Config
from sample_agent import Agent


class Model(BaseModel):
    """
    Class variables: identifier, model_parameters, agents, interactions, steps_per_state_variable, par_keys, par_lower, par_upper, par_current, par_step, precision
    """
    identifier = ""
    model_parameters = {}
    agents = []
    interactions = None

    def __init__(self, model_config):
        super(Model, self).__init__(model_config)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        super(Model, self).set_identifier(_value)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, _value):
        """
        Class variables: model_parameters
        Local variables: _params
        """
        super(Model, self).set_model_parameters(_value)

    def get_agents(self):
        return self.agents

    def set_agents(self, _value):
        """
        Class variables: agents
        Local variables: _agents
        """
        super(Model, self).set_agents(_value)

    def get_interactions(self):
        return self.interactions

    def set_interactions(self, _value):
        """
        Class variables: interactions
        Local variables: _interactions
        """
        super(Model, self).set_interactions(_value)

    def __str__(self):
        return super(Model, self).__str__()

    def initialize_agents(self):
        for agent_iterator in range(0, int(self.model_parameters['num_agents'])):
            temp_agent = Agent(str(agent_iterator), {}, {})
            self.agents.append(temp_agent)

    def get_agent_by_id(self, _id):
        """
        Class variables: agents
        Local variables: _id, agent_iterator
        """
        for agent_iterator in self.agents:
            if agent_iterator.identifier == _id:
                return agent_iterator

    def check_agent_homogeneity(self):
        """
        Class variables: agents
        Local variables: parameter_iterator, temp_parameter, agent_iterator, temp_state_variable
        """
        for parameter_iterator in self.agents[0].parameters:
            temp_parameter = self.agents[0].parameters[parameter_iterator]
            for agent_iterator in self.agents:
                if agent_iterator.parameters[parameter_iterator] != temp_parameter:
                    return False
                temp_parameter = agent_iterator.parameters[parameter_iterator]
        for parameter_iterator in self.agents[0].state_variables:
            temp_state_variable = self.agents[0].state_variables[parameter_iterator]
            for agent_iterator in self.agents:
                if agent_iterator.state_variables[parameter_iterator] != temp_state_variable:
                    return False
                temp_state_variable == agent_iterator.state_variables[parameter_iterator]
        return True


    # TODO this code is fairly general and should be generalized further and then moved to the BaseAgent class
    def check_fixed_point(self, agentA, agentB):

        actions = [0, 1]
        agentA.parameters['action'] = random.randint(min(actions), max(actions))
        agentB.parameters['action'] = random.randint(min(actions), max(actions))
        for iterator in range(0, int(self.model_parameters['num_sweeps'])):
            originalactionA = agentA.parameters['action']
            originalactionB = agentB.parameters['action']
            # then get the best response of B given the current portfolio choice of A
            print self.get_best_response(agentA.parameters['action'])
            agentB.parameters['action'] = self.get_best_response(agentA.parameters['action'])

            # and then get the best response of A given the best response of B
            print self.get_best_response(agentB.parameters['action'])
            agentA.parameters['action'] = self.get_best_response(agentB.parameters['action'])

            # check if we have a fixed point
            if (iterator != 0 and originalactionA == agentA.parameters['action'] and originalactionB == agentB.parameters['action']):
                # here we have to write out the results
                print "Found equilibrium!"
                self.model_parameters['equilibrium'] = "yes"
                return
        print "No equilibrium found!"
        self.model_parameters['equilibrium'] = "no"

    def get_best_response(self, reaction):
        if self.payout_from_game(1, reaction) > self.payout_from_game(0, reaction):
            return 1
        else:
            return 0

    def do_update(self):
        # equilibrium is found by iterating over all possible variable choices for agent A, communicating them to
        # agent B, obtaining B's best response by iterating over all possible variable choices for B, communicating
        # B's best response back to A, and computing A's best response. Any fixed point of this procedure is an
        # equilibrium
        agentA = self.agents[0]
        agentB = self.agents[1]
        self.check_fixed_point(agentA, agentB)
        if self.model_parameters['equilibrium'] == "no":
            pass
        else:
            return [agentA.parameters['action'], agentB.parameters['action']]

    def payout_from_game(self, action, reaction):
        if action == 1:
            if reaction == 1:
                return 1-float(self.model_parameters['theta'])
            elif reaction == 0:
                return -float(self.model_parameters['theta'])
            else:
                print "Wrong action, check the code!"
        elif action == 0:
            if reaction == 1:
                return 0
            elif reaction == 0:
                return 0
            else:
                print "Wrong action, check the code!"
        else:
            print "Wrong action, check the code!"
