#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

# import logging
# import math
from src.baseagent import BaseAgent

# ============================================================================
#
# class Agent
#
# ============================================================================


class Agent(BaseAgent):

    identifier = ""
    parameters = {}
    state_variables = {}

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Agent, self).set_identifier(_value)

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, _value):
        super(Agent, self).set_parameters(_value)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _value):
        super(Agent, self).set_state_variables(_value)

    def __str__(self):
        super(Agent, self).__str__()

    def __init__(self, _identifier, _params, _variables):
        super(Agent, self).__init__(_identifier, _params, _variables)
