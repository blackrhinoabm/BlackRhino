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

    sum = 0
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
        self.sum = 0
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, current_step):

        if current_step < 1:

            self.asset_sales_across_banks_per_asset_class = {}

            for agent in environment.agents:

                
                agent.start_shock(environment)


                agent.calc_total_asset_sales(environment, current_step)
                print agent.identifier, agent.TAS


            # the code below is to calculate total asset sales across all banks
            # It returns a dictionary with asset class as keys and
            # total asset sales of this class as values(across the wholesystem)
            self.add_sales_across_banks(environment)

            for agent in environment.agents:
                agent.update_balance_sheet()
                # print agent.identifier
                # agent.check_accounts()

                # now we need to add up all the sales for one asset class
                # and assign it to a variable so we have one number for all
                # asset sales across the whole system for all asset classes
                # I use the ABSA if clause to just use one agent (all agent
                # have this dictionary}

            for i in self.asset_sales_across_banks_per_asset_class:
                self.sum = self.sum + self.asset_sales_across_banks_per_asset_class[i]

            print "Total assets whiped out by shock:", self.sum, "in step:", (current_step+1)

        else:
            print "Now begins step %s" % (current_step +1)

            # This next code is to update the shock vector
            for m in self.asset_sales_across_banks_per_asset_class:
                price_shock = self.asset_sales_across_banks_per_asset_class[m] * environment.static_parameters['illiquidity']

                for shock in environment.shocks:
                    shock.asset_returns[m] = price_shock

            for agent in environment.agents:
                agent.start_shock(environment)

                agent.calc_total_asset_sales(environment, current_step)
                # print ("Bank %s sold %s assets") % (agent.identifier, agent.TAS)

        #     # this adds up the sales of m1, m2, m3 etc  across the banks
        #     # but not across classes, so we get a dictionary with
        #     # total sales of m1:value ,total sales of m2: value, etc.
            self.add_sales_across_banks(environment)

            for agent in environment.agents:
                agent.update_balance_sheet()
                # agent.check_accounts()

                # print agent.total_assets, agent.identifier

            # Now we need to sum up sales across classes to get a 'globas TAS' (total asset sales)
            # so total sales of m1+m2+m3 etc. Before, it was summed up "across
            #  banks per class",so total sales of asset class m1 of bank1 plus
            # total sales of m1 of bank2 plus total sales of m1 of bank 3 etc.
            # we set self sum 0 again to get the global TAS of this current step
            # alone
            self.sum = 0
            for i in self.asset_sales_across_banks_per_asset_class:
                self.sum = self.sum + self.asset_sales_across_banks_per_asset_class[i]

            print "Assets whiped out by feedback effects:", self.sum, "in step:", (current_step+1)

    def add_sales_across_banks(self, environment):
        for asset_class in environment.agents[0].state_variables:

            if asset_class != 'leverage':

                self.asset_sales_across_banks_per_asset_class[asset_class] = 0.0

                for agent in environment.agents:
                    self.asset_sales_across_banks_per_asset_class[asset_class] += agent.state_variables[asset_class] * agent.TAS

    # -----------------------------------------------------------------------
