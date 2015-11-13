#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = """Co-Pierre Georg (co-pierre.georg@uct.ac.za)"""

import abc

# -------------------------------------------------------------------------
#
#  class Agent
#
# -------------------------------------------------------------------------
class BaseAgent(object):
    """
    Class variables: __metaclass__, identifier, parameters, state_variables
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
    def get_parameters(self):
        return
    @abc.abstractmethod
    def set_parameters(self, _params):
        """
        Class variables: parameters
        Local variables: _params
        """
        if not isinstance(_params, dict):
            raise TypeError
        else:
            self.parameters = _params
        return
    parameters = abc.abstractproperty(get_parameters, set_parameters)

    @abc.abstractmethod
    def get_state_variables(self):
        return
    @abc.abstractmethod
    def set_state_variables(self, _variables):
        """
        Class variables: state_variables
        Local variables: _variables
        """
        if not isinstance(_variables, dict):
            raise TypeError
        else:
            self.state_variables = _variables
        return
    state_variables = abc.abstractproperty(get_state_variables, set_state_variables)


    @abc.abstractmethod
    def __init__(self, _identifier, _params, _variables):
        """
        Class variables: parameters, state_variables
        Local variables: _identifier, _params, _variables
        """
        self.set_identifier(_identifier)
        self.parameters = _params
        self.state_variables = _variables

    @abc.abstractmethod
    def __str__(self):
        """
        Class variables: identifier, parameters, state_variables
        Local variables: ret_str, entry, value
        """
        ret_str = "  <agent identifier='" + self.identifier + "'>\n"
        for entry in self.parameters:
            value = self.parameters[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                ret_str += "    <parameter type='agent' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
            else:
                raise TypeError
        for entry in self.state_variables:
            value = self.state_variables[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                ret_str += "    <variable name='" + entry + "' value='" + str(value) + "'></variable>\n"
            elif isinstance(value, list):
                ret_str += "    <variable name='" + entry + "' value='[" + str(value[0]) + "," + str(value[1]) + \
                           "]'></variable>\n"
            else:
                raise TypeError
        ret_str += "  </agent>\n"

        return ret_str

    #@abc.abstractmethod
    #def get_best_response(self, opponent_strategy):
    #    pass