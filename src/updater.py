#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2012 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)

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
    # from environment import Environment

    identifier = ""
    model_parameters = {}
    agents = []
    interactions = None

    #
    # VARIABLES
    #

    #
    # METHODS
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        super(Updater, self).set_identifier(_value)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, _value):
        """
        Class variables: model_parameters
        Local variables: _params
        """
        super(Updater, self).set_model_parameters(_value)

    def get_agents(self):
        return self.agents

    def set_agents(self, _value):
        """
        Class variables: agents
        Local variables: _agents
        """
        super(Updater, self).set_agents(_value)

    def get_interactions(self):
        return self.interactions

    def set_interactions(self, _value):
        """
        Class variables: interactions
        Local variables: _interactions
        """
        super(Updater, self).set_interactions(_value)

    def get_agent_by_id(self, _id):
        """
        Class variables:
        Local variables: _id
        """
        super(Updater, self).get_agent_by_id(_id)

    def check_agent_homogeneity(self):
        super(Updater, self).check_agent_homogeneity()

    def initialize_agents(self):
        super(Updater, self).initialize_agents()

    def __str__(self):
        """
        Class variables: identifier, model_parameters, agents, interactions
        Local variables: ret_str, entry, value, agent
        """
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
        self.do_update_phase1(environment,  active_banks,  time,  debug)

        active_banks = self.find_active_banks(environment,  network,  time)
        self.do_update_phase2(environment,  active_banks, time,  debug)
        network.do_interbank_trades(environment)

        active_banks = self.find_active_banks(environment,  network,  time)
        self.do_update_phase3(environment,  active_banks,  time,  debug)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update_phase1
    # -------------------------------------------------------------------------
    def do_update_phase1(self,  environment,   active_banks,  time,  debug):
        # state = environment.get_state(time)
        network = environment.network
        self.agents = environment.banks

        #
        # loop over all banks and do update step
        #
        for bank in active_banks:
            # first, update all maturities
            bank.update_maturity()

            # then, update the risk-aversion parameter of banks to incorporate information contagion
            bank.update_risk_aversion(environment.get_state(time), time)

            # re-calculate the (constraint) optimal portfolio decision of the bank

            # initialize bank liquidity
            bank.parameters["Q"] = 0.0
            bank.parameters["Q"] = bank.parameters["Q"] + bank.get_interest("D")
            bank.parameters["Q"] = bank.parameters["Q"] + bank.get_interest("rD")
            bank.parameters["Q"] = bank.parameters["Q"] + bank.get_interest("E")
            bank.parameters["Q"] = bank.parameters["Q"] + bank.get_interest("I")  # here a loss on the banking capital might occur
            bank.parameters["Q"] = bank.parameters["Q"] + bank.get_interest("L")
            bank.parameters["Q"] = bank.parameters["Q"] + bank.get_interest("LC")

            # first, get all required reserves
            bank.parameters["Q"] = bank.parameters["Q"] + bank.liquidate_due_transactions("rD")
            # then, get all excess reserves
            bank.parameters["Q"] = bank.parameters["Q"] + bank.liquidate_due_transactions("E")
            # then, get payments from firms (interest, due loans)
            bank.parameters["Q"] = bank.parameters["Q"] + bank.liquidate_due_transactions("I")
            # now, settle interbank claims
            # remove the claim from the network of exposures
            network.liquidate_due_transactions(bank)
            # and liquidate it
            bank.parameters["Q"] = bank.parameters["Q"] + bank.liquidate_due_transactions("L")
            # and central bank claims
            bank.parameters["Q"] = bank.parameters["Q"] + bank.liquidate_due_transactions("LC")
            # transfer required reserves to the central bank
            bank.parameters["Q"] = bank.parameters["Q"] + bank.transfer_required_deposits()

            # check the solvency, the bank might be insolvent due to a loss on the risky assets
            bank.check_solvency(environment,  debug,  time)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update_phase2
    # -------------------------------------------------------------------------
    def do_update_phase2(self,  environment,  active_banks,  time,  debug):
        for bank in active_banks:
            # next, determine new deposit level
            new_deposit_level = bank.get_new_deposits(self.environment.get_state(time).static_parameters["scaleFactorHouseholds"])
            bank.parameters["Q"] = bank.parameters["Q"] + new_deposit_level
            # and calculate the liquidity demand
            bank.calculate_liquidity_demand()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update_phase3
    # -------------------------------------------------------------------------
    def do_update_phase3(self,  environment,  active_banks,  time,  debug):
        current_assets = 0.0  # the volume of all assets in the market, required to determine the price-drop of assets in a fire sale
        for bank in active_banks:  # find the current amount of assets in the market
            current_assets += bank.get_account("I")

        # state = environment.get_state(time)
        network = environment.network
        self.agents = environment.banks

        #
        # then do the update code
        #
        for bank in active_banks:
            # transfer to/from standing facilitiesget_parameters_from_file
            bank.get_central_bank_liquidity(environment.get_state(time))

            # check for the bank's liquidity
            bank.liquidate_assets(environment.initial_assets,  current_assets, environment.get_state(time),  debug,  time)

            # transfer investments to firms
            bank.parameters["Q"] = bank.parameters["Lp"]  # transfer available liquidity to Q
            bank.parameters["Lp"] = 0.0
            bank.transfer_investments(environment.get_state(time))  # state is needed to determine the probability that a loan defaults
            bank.transfer_excess_reserves()

        if (debug == "debug"):
            network.write_network_of_exposures(time)
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
