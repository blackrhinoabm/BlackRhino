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
import logging
import pandas as pd


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

        self.system_TAS = 0
        self.system_loss_equity_from_direct_effects = 0
        self.system_loss_equity_from_indirect_effects = 0
        self.system_loss_assets_from_indirect_effects = 0
        self.system_loss_assets = 0
        self.system_assets = 0

        self.system_vulnerability = 0
        self.prices = {}
        self.initialize_prices()

        "This is all stuff needed to write output"
        self.d = {}

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, current_step):

        if current_step < 1:

            for agent in environment.agents:
                agent.initialize_total_assets()
                agent.add_parameters_dealer(self)
                
                environment.variable_parameters['system_equity']  += agent.state_variables['equity']
                self.system_assets += agent.state_variables['total_assets']

            print "1.**** UPDATER.PY*** FIRST ROUND EFFECTS:"     
            self.do_firstround_effects(environment, current_step)
            
            for agent in environment.agents:
                agent.append_results_to_dataframe(current_step)
            
            self.plug_agents_and_system_results_together(environment, current_step)


        else:

            print "2.**** UPDATER.PY*** SECOND ROUND EFFECTS:"
            logging.info('2.**** UPDATER.PY*** SECOND ROUND EFFECTS:')

            self.do_secondround_effects(environment, current_step)

            for agent in environment.agents:
                agent.update_results_to_dataframe(current_step)
                logging.info("Updated results of %s within agent class", agent.identifier)
                print agent

            self.plug_agents_and_system_results_together(environment, current_step)

#####################################################################
    def do_firstround_effects(self, environment, current_step):

       
        for agent in environment.agents:

            "CHECK by printing:"
            if agent.identifier == "SBSA":
                print "**UPDATER.PY***TOTAL ASSETS OF ", agent.identifier, "are:", agent.state_variables['total_assets']

            """Now we intiliaze the shock, which 
            gets configured in the shock config file, 
            calculate total asset purchases for 
            each individual agent and the direct losses 
            for each agent"""

        for agent in environment.agents:
            agent.initialize_shock(environment)

            "CHECK:\
            Use identifier to pick out one agent\
            Alternatively, use environment.agents[0]"

            if agent.identifier == "SBSA":
                print "***AGENT.PY*** Shock for ", agent.identifier, "on its total asset is:", agent.state_variables['shock_for_agent'] *100, "%"

            agent.calc_total_asset_sales(environment, current_step)

            """Just printing first round effects to screen"""
            #print("TOTAL ASSET SALES BY: "), agent.identifier, agent.state_variables['total_asset_sales']
            agent.calc_direct_losses()
            #print ("Direct losses: "), agent.state_variables["direct_losses"], agent.identifier
            #print agent.identifier, "total asset sales", agent.state_variables['total_asset_sales'], current_step

            "The next method call is very important."
            "We loop over the m asset classes in"
            "our dictionary environment.agents[0].state_variables"
            "The methods returns a dictionary with"
            "asset class as keys and"
            "total asset sales of this class as values"
            "(across the whole system)"
        self.add_sales_across_banks(environment)

        "This is the cross-check that all sales per asset class sum up to the total loss of assets for the system"
        for i in self.asset_sales_across_banks_per_asset_class:
            self.system_TAS = self.system_TAS + self.asset_sales_across_banks_per_asset_class[i]


        for agent in environment.agents:
            self.system_loss_equity_from_direct_effects += (agent.state_variables['shock_for_agent'] * agent.state_variables['total_assets'])
            self.system_loss_assets += (agent.state_variables['shock_for_agent'] * agent.state_variables['total_assets'] * agent.parameters['leverage']) 

        print "***Updater.py*** In Step:", (current_step+1) , "Total assets whiped out by shock:", self.system_TAS



    def do_secondround_effects(self, environment, current_step): 

        """We update the balance sheets from the first
        round effects. Each bank's new debt is equal to
        its initial debt less total asset purchases.
        The new equity equals the initial equity_t-1 less
        the product of (shock on assets * total assets)_t-1 """

        for agent in environment.agents:
            agent.update_balance_sheet()

            "Uncomment for checking updated balance sheets:"
            print "***UPDATER.PY*** Check balance sheets after step", current_step, agent.state_variables['total_assets'], "total assets for", agent.identifier

        print "Now begins step %s" % (current_step +1)

            # This is to update the shock vector
        for m in self.asset_sales_across_banks_per_asset_class:

            price_shock = self.asset_sales_across_banks_per_asset_class[m] * environment.static_parameters['illiquidity']

            for shock in environment.shocks:
                shock.asset_returns[m] = price_shock

            'JUST CHECKING, uncomment for printing the updated shock vector with new price effects for all m:'
                # print shock.asset_returns[m], m
            # if m=="m_22":    
            #         print"***UPDATER.PY*** For asset class", m, "the updated price shock is", shock.asset_returns[m] * 100, "%"

        for agent in environment.agents:
            agent.initialize_shock(environment)

            agent.calc_total_asset_sales(environment, current_step)

            agent.calc_indirect_losses(environment.variable_parameters['system_equity'] , current_step)
        #     # this adds up the sales of m1, m2, m3 etc  across the banks
        #     # but not across classes, so we get a dictionary with
        #     # total sales of m1:value ,total sales of m2: value, etc.
            
        for agent in environment.agents:
            self.system_loss_equity_from_indirect_effects += (agent.state_variables['shock_for_agent'] * agent.state_variables['total_assets'])
            self.system_loss_assets_from_indirect_effects += (agent.state_variables['shock_for_agent'] * agent.state_variables['total_assets'] * agent.parameters['leverage'])


        self.calc_system_vulnerability(environment)

        self.add_sales_across_banks(environment)

                # agent.check_accounts()

                # print agent.state_variables['total_assets'], agent.identifier

        self.system_TAS = 0
        for i in self.asset_sales_across_banks_per_asset_class:
            self.system_TAS = self.system_TAS + self.asset_sales_across_banks_per_asset_class[i]

        print "***UPDATER.PY Assets whiped out by feedback effects:", self.system_TAS, "in step:", (current_step+1)


    def add_sales_across_banks(self, environment):

        "This method is crucial because"
        "it is summing up the sales per asset class"
        "across banks. We need the volume of"
        "sales to compute the second"
        "round price effect on our assets."
        "Because we have severeal"
        "keyes in agents.parameters, we need to"
        "exclude the values for the keyes we"
        "have to exclude, i.e. the values for leverage"
        "This is horribl code, but for time reasons I do it like this." 
        "To do:  nest asset class keyes in a dictionary"
        "inside paramters so there is no confusion"
        "pick out one agent:"

        for key in environment.agents[0].parameters:

            "VERY VERY IMPORTANT ! THIS COST ME A DAY TO TROUBLE SHOOT IN OXFORD!!"
            "LEVERAGE IS HARD CODED PAY ATTENTION!!!!!! ALSO TAKE OUT dealer and other"
            if key != 'leverage' and key !="dealer":
                self.asset_sales_across_banks_per_asset_class[key] = 0.0

                for agent in environment.agents:
                    self.asset_sales_across_banks_per_asset_class[key] += agent.parameters[key] * agent.state_variables['total_asset_sales']
                    
                    "Uncomment for CHECK: This is the sale per asset class per bank (cumulative):"
                    # print self.asset_sales_across_banks_per_asset_class[key], "for asset class", key,  "after adding", agent.identifier
                    
            "Uncomment for CHECK: This is the sale per asset class (cumulative):"
            # if key == 'm_22':
            #     print "***Updater.py***", key, "sales across the system are:", self.asset_sales_across_banks_per_asset_class


    def calc_system_vulnerability(self, environment):

        temp = 0

        for agent in environment.agents:
            temp += agent.state_variables['losses_from_system_deleveraging']

        self.system_vulnerability = (temp/environment.variable_parameters['system_equity'] )
        # print "Aggregate system_vulnerability is:", self.system_vulnerability * 100, "percent"

    def print_effect_to_screen(self, current_step, environment):
        self.assets_relative = (self.system_loss_assets /self.system_assets)*100
        print "Assets whiped out by shock:", self.assets_relative,\
                "percent in step %s for %s banks" % (current_step, environment.num_agents)

        self.equity_relative = (self.system_loss_equity_from_direct_effects /environment.variable_parameters['system_equity'] )*100
        print "Equity whiped out by shock:", self.equity_relative, "percent in step %s for %s banks" % (current_step, environment.num_agents)

    # -----------------------------------------------------------------------


    def initialize_prices(self):
        self.prices["risky_asset"] = 113.945


    def plug_agents_and_system_results_together(self, environment, current_step):
        import pandas as pd
        
        "This is for the agent stuff. We make an xlist with\
         names which later become the keys in the dictionary\
         There are as many key, value pairs as agents\
         self.d = {df_1 : SBSA_results, df_2: Absa_results}\
         "
        xlist = []  
        for i in range(len(environment.agents)):
            x = "df_" + str(i) 
            xlist.append(x)
             
        self.d = dict((el,0) for el in xlist)

        "Adding all agent results"
        for key in self.d:
            for agent in environment.agents:
                if agent.identifier in self.d.values():
                    pass
                else:
                    self.d.update({key:agent.identifier})

        for key in self.d:
            for agent in environment.agents:
                try: 
                    if self.d[key] == agent.identifier:
                        self.d.update({key:agent.results_df})
                except TypeError:
                    logging.info(" We are in the updater and adding results per agents (i.e. result dataframe)\
                                 so dictionary self.d. We just added the results of %s !",  agent.identifier)

        "Now the same procedure as every year..\
        the rest of the variables of interest."

        plist = []  
        for i in range(len(environment.variable_parameters)):
            p = "df_" + str(i) 
            plist.append(p) 
             

    def write_list_of_results(self, current_step, environment):
        import numpy as np
        resultlist = []
        result_columns = []
        for k, v in self.d.iteritems():
            resultlist.append(self.d[k])

        "To get column names, we need to work around a bit\
        The next code takes all the different agents' header names\
        and puts them in a list called x"
        for i in range(len(resultlist)):
            result_columns.append(resultlist[i].columns.values)
            x = np.array([[result_columns[i-1]],[result_columns[i]]]).tolist()

        "However, x has a number of agents of sublists. We need to merge\
        them and put them all together in one list called total,\
        which we use to give our csv column names\
        This neat little code here does that (python can be really cool)"
        total = []
        for i in range(len(x)):
            for k in x[i]:
                total += k        
        "Finally we have a result dataframe we can write to csv!!"
        df_stacked = pd.concat([r for r in resultlist], axis=1,  ignore_index=True)
        df_stacked.columns = total
        df_stacked.to_csv("results_all.csv")        

        #  OLD CODE THROUGH WHICH I SUFFERED A GREAT DEAL - here for memorial
        #for asset_class in environment.agents[0].state_variables:

        #     if asset_class != 'leverage' and asset_class != 'losses_from_system_deleveraging' and asset_class != 'direct_losses' and asset_class != 'shock_for_agent' and asset_class != 'total_assets' and asset_class != 'total_asset_sales' and :

        #         self.asset_sales_across_banks_per_asset_class[asset_class] = 0.0

        #         for agent in environment.agents:
        #             # print asset_class, agent.state_variables[asset_class], agent.identifier, agent.state_variables['total_asset_sales']

        #             self.asset_sales_across_banks_per_asset_class[asset_class] += agent.state_variables[asset_class] * agent.state_variables['total_asset_sales']
                    
        #             if agent.identifier == "SBSA":
        #                 print asset_class, self.asset_sales_across_banks_per_asset_class[asset_class], agent.identifier                    
