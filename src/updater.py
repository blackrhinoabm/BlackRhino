#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
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
    model_parameters = {}
    agents = []
    interactions = None

    #
    #
    # METHODS
    #
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Updater, self).set_identifier(_value)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, _value):
        super(Updater, self).set_model_parameters(_value)

    def get_agents(self):
        return self.agents

    def set_agents(self, _value):
        super(Updater, self).set_agents(_value)

    def get_interactions(self):
        return self.interactions

    def set_interactions(self, _value):
        super(Updater, self).set_interactions(_value)

    def get_agent_by_id(self, _id):
        super(Updater, self).get_agent_by_id(_id)

    def check_agent_homogeneity(self):
        super(Updater, self).check_agent_homogeneity()

    def initialize_agents(self):
        super(Updater, self).initialize_agents()

    def __str__(self):
        return super(Updater, self).__str__()

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self,  environment):
        self.environment = environment
        self.model_parameters = environment.static_parameters
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self,  environment,  time,  debug):
        network = environment.network
        # state = environment.get_state(time)

        active_banks = self.find_active_banks(environment,  network,  time)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update_phase1
    # -------------------------------------------------------------------------
    def do_update_phase1(self,  environment,   active_banks,  time,  debug):
        self.agents = environment.banks

        #
        # loop over all banks and do update step
        #
        for bank in active_banks:
            # first, update all maturities
            bank.update_maturity()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update_phase2
    # -------------------------------------------------------------------------
    def do_update_phase2(self,  environment,  active_banks,  time,  debug):
        for bank in active_banks:
            # next, determine new deposit level
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update_phase3
    # -------------------------------------------------------------------------
    def do_update_phase3(self,  environment,  active_banks,  time,  debug):
        current_assets = 0.0  # the volume of all assets in the market, required to determine the price-drop of assets in a fire sale
        for bank in active_banks:  # find the current amount of assets in the market
    # -------------------------------------------------------------------------

#
# HELPER ROUTINES
#

    # -------------------------------------------------------------------------
    # find_active_banks()
    # -------------------------------------------------------------------------
    def find_active_banks(self,  environment,  network,  time):
        active_banks = []

        for bank in environment.banks:
            if bank.parameters["active"] > -1:
                active_banks.append(bank)
            else:
                network.remove_inactive_bank(bank,  time)

        return active_banks
    # -------------------------------------------------------------------------
