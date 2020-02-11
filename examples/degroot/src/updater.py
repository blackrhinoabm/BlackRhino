#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2016 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)
Pawel Fiedor (pawel@fiedor.eu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from abm_template.src.basemodel import BaseModel
from src.agent import Agent


# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------


class Updater(BaseModel):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""
    new_opinion = {}
    starting_opinion = {}

    model_parameters = {}

    #
    #
    # METHODS
    #

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

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, environment):
        self.environment = environment
        self.new_opinion = {}
        self.initial_opinion = {}
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment):

       self.degroot_modified(environment)
       #self.original_degroot(environment)


    # --------------------------------------------------------------------------
    def degroot_modified(self, environment):
        
        for agent in environment.agents:
            self.new_opinion[agent.identifier] = agent.create_temp_variable(environment) 
            self.initial_opinion[agent.identifier] = agent.initial_opinion
              
        for agent in environment.agents:
            agent.opinion = float(environment.static_parameters['lambda']) * float(self.new_opinion[agent.identifier])  + (1- float(environment.static_parameters['lambda']))*self.initial_opinion[agent.identifier] 

    def original_degroot(self, environment):

        for agent in environment.agents:
            self.new_opinion[agent.identifier] = agent.create_temp_variable(environment)

        for agent in environment.agents:
            agent.opinion = self.new_opinion[agent.identifier]
