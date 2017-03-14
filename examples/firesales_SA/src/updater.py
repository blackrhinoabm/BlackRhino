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
from src.shock import Shock


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

    asset_sales_across_banks_per_asset_class = {}

    model_parameters = {}

    system_TAS = 0
    system_loss_equity_from_direct_effects = 0
    system_loss_equity_from_indirect_effects = 0
    system_loss_assets_from_indirect_effects = 0
    system_loss_assets = 0
    system_equity = 0
    system_assets = 0
    system_vulnerability = 0

    pre_shock_system_assets = 0
    pre_shock_system_equity = 0

    temp = 0

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
        self.asset_sales_across_banks_per_asset_class = {}
        self.pre_shock_system_assets = 0
        self.pre_shock_system_equity = 0


        self.system_TAS = 0
        self.system_loss_equity_from_direct_effects = 0
        self.system_loss_equity_from_indirect_effects = 0
        self.system_loss_assets_from_indirect_effects = 0
        self.system_loss_assets = 0
        self.system_equity = 0
        self.system_assets = 0

        self.system_vulnerability = 0
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, current_step):

        if current_step < 1:

            for agent in environment.agents:
                self.system_equity += agent.parameters['equity']
                self.system_assets += agent.state_variables['total_assets']
                agent.initialize_total_assets

            self.pre_shock_system_equity = self.system_equity
            self.pre_shock_system_assets = self.system_assets

            for agent in environment.agents:
                agent.initialize_shock(environment)
                agent.calc_total_asset_sales(environment, current_step)
                print("TOTAL ASSET SALES BY: "), agent.identifier, agent.state_variables['total_asset_sales']
                agent.calc_direct_losses()
                print ("Direct losses: "), agent.state_variables["direct_losses"], agent.identifier

            # the code below is to calculate total asset sales across all banks
            # It returns a dictionary with asset class as keys and
            # total asset sales of this class as values(across the wholesystem)
            self.add_sales_across_banks(environment)

                # now we need to add up all the sales for one asset class
                # and assign it to a variable so we have one number for all
                # asset sales across the whole system for all asset classes
                # I use the ABSA if clause to just use one agent (all agent
                # have this dictionary}

            for i in self.asset_sales_across_banks_per_asset_class:
                self.system_TAS = self.system_TAS + self.asset_sales_across_banks_per_asset_class[i]

            for agent in environment.agents:
                self.system_loss_equity_from_direct_effects += (agent.state_variables['shock_for_agent'] * agent.state_variables['total_assets'])
                self.system_loss_assets += (agent.state_variables['shock_for_agent'] * agent.state_variables['total_assets'] * agent.state_variables['leverage']) 

            # print "Total assets whiped out by shock:", self.system_TAS, "in step:", (current_step+1)


        else:
            for agent in environment.agents:
                agent.update_balance_sheet()


            print "Now begins step %s" % (current_step +1)

            # This next code is to update the shock vector
            for m in self.asset_sales_across_banks_per_asset_class:
                price_shock = self.asset_sales_across_banks_per_asset_class[m] * environment.static_parameters['illiquidity']

                for shock in environment.shocks:
                    shock.asset_returns[m] = price_shock

            for agent in environment.agents:
                agent.initialize_shock(environment)

                agent.calc_total_asset_sales(environment, current_step)
                print agent.identifier, agent.state_variables['total_asset_sales'], current_step

                agent.calc_indirect_losses(self.pre_shock_system_equity, current_step)
        #     # this adds up the sales of m1, m2, m3 etc  across the banks
        #     # but not across classes, so we get a dictionary with
        #     # total sales of m1:value ,total sales of m2: value, etc.
            
            for agent in environment.agents:
                self.system_loss_equity_from_indirect_effects += (agent.state_variables['shock_for_agent'] * agent.state_variables['total_assets'])
                self.system_loss_assets_from_indirect_effects += (agent.state_variables['shock_for_agent'] * agent.state_variables['total_assets'] * agent.state_variables['leverage'])


            self.calc_system_vulnerability(environment)

            self.add_sales_across_banks(environment)

                # agent.check_accounts()

                # print agent.state_variables['total_assets'], agent.identifier

            # Now we need to sum up sales across classes to get a 'globas TAS' (total asset sales)
            # so total sales of m1+m2+m3 etc. Before, it was summed up "across
            #  banks per class",so total sales of asset class m1 of bank1 plus
            # total sales of m1 of bank2 plus total sales of m1 of bank 3 etc.
            # we set self sum 0 again to get the global TAS of this current step
            # alone
            self.system_TAS = 0
            for i in self.asset_sales_across_banks_per_asset_class:
                self.system_TAS = self.system_TAS + self.asset_sales_across_banks_per_asset_class[i]

            print "Assets whiped out by feedback effects:", self.system_TAS, "in step:", (current_step+1)


    def add_sales_across_banks(self, environment):
        for asset_class in environment.agents[0].state_variables:

            if asset_class != 'leverage' and asset_class != 'losses_from_system_deleveraging' and asset_class != 'direct_losses' and asset_class != 'shock_for_agent' and asset_class != 'total_assets' and asset_class != 'total_asset_sales':

                self.asset_sales_across_banks_per_asset_class[asset_class] = 0.0

                for agent in environment.agents:
                    self.asset_sales_across_banks_per_asset_class[asset_class] += agent.state_variables[asset_class] * agent.state_variables['total_asset_sales']

    def calc_system_vulnerability(self, environment):

        print "Aggregate system_vulnerability is:"

        temp = 0

        for agent in environment.agents:
            temp += agent.state_variables['losses_from_system_deleveraging']

        self.system_vulnerability = (temp/self.pre_shock_system_equity)
        # print self.system_vulnerability * 100, "percent"

    def print_effect_to_screen(self, current_step, environment):
        self.assets_relative = (self.system_loss_assets /self.pre_shock_system_assets)*100
        print "Assets whiped out by shock:", self.assets_relative , "percent in step %s for %s banks" % (current_step, environment.num_agents)

        self.equity_relative = (self.system_loss_equity_from_direct_effects /self.pre_shock_system_equity)*100
        print "Equity whiped out by shock:", self.equity_relative, "percent in step %s for %s banks" % (current_step, environment.num_agents)

    # -----------------------------------------------------------------------


    # -----------------------------------------------------------------------
