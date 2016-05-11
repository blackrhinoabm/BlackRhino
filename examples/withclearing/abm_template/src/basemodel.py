#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = """Co-Pierre Georg (co-pierre.georg@uct.ac.za)"""

import abc

# -------------------------------------------------------------------------
#
#  class Model
#
# -------------------------------------------------------------------------
class BaseModel(object):
    """
    Class variables: __metaclass__, identifier, model_parameters, agents, interactions
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_identifier(self):
        return
    @abc.abstractmethod
    def set_identifier(self, _identifier):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        if not isinstance(_identifier, str):
            raise TypeError
        else:
            self.identifier = _identifier
        return
    identifier = abc.abstractproperty(get_identifier, set_identifier)

    @abc.abstractmethod
    def get_model_parameters(self):
        return
    @abc.abstractmethod
    def set_model_parameters(self, _params):
        """
        Class variables: model_parameters
        Local variables: _params
        """
        if not isinstance(_params, dict):
            raise TypeError
        else:
            self.model_parameters = _params
        return
    model_parameters = abc.abstractproperty(get_model_parameters, set_model_parameters)

    @abc.abstractmethod
    def get_agents(self):
        return
    @abc.abstractmethod
    def set_agents(self, _agents):
        """
        Class variables: agents
        Local variables: _agents
        """
        if not isinstance(_agents, list):
            raise TypeError
        else:
            self.agents = _agents
        return
    agents = abc.abstractproperty(get_agents, set_agents)

    @abc.abstractmethod
    def get_interactions(self):
        return
    @abc.abstractmethod
    def set_interactions(self, _interactions):
        """
        Class variables: interactions
        Local variables: _interactions
        """
        self.interactions = _interactions
        return
    interactions = abc.abstractproperty(get_interactions, set_interactions)


    @abc.abstractmethod
    def __str__(self):
        """
        Class variables: identifier, model_parameters, agents, interactions
        Local variables: ret_str, entry, value, agent
        """
        ret_str = "<model identifier='" + self.identifier + "'>\n"
        for entry in self.model_parameters:
            value = self.model_parameters[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                ret_str = ret_str + "  <parameter type='model' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
            else:
                raise TypeError
        for agent in self.agents:
            ret_str = ret_str + agent.__str__()
        if self.interactions:  # if interactions = None, don't print anything
            ret_str = ret_str + self.interactions.__str__()
        ret_str = ret_str + "</model>"

        return ret_str


    @abc.abstractmethod
    def __init__(self, model_config):
        """
        Class variables:
        Local variables: _params, model_config
        """
        _params = model_config.static_parameters

        self.set_identifier(model_config.identifier)
        # reset the agents, interactions, and parameters
        self.set_agents([])
        self.set_interactions(None)
        self.set_model_parameters({})

        if not "num_sweeps" in _params.keys():
            raise TypeError("num_sweeps needs to be implemented ")
        if not "num_agents" in _params.keys():
            raise TypeError("num_agents needs to be implemented ")

        self.set_model_parameters(_params)

    @abc.abstractmethod
    def initialize_agents(self):
        pass

    @abc.abstractmethod
    def do_update(self):
        pass

    @abc.abstractmethod
    def get_agent_by_id(self, _id):
        """
        Class variables:
        Local variables: _id
        """
        pass

    @abc.abstractmethod
    def check_agent_homogeneity(self):
        pass
