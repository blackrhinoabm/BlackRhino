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
from src.measurement import reset_system_variables
from src.measurement import calc_new_system_variables

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

        "This is stuff needed to write as output"
        self.all_agents_result_dictionary_with_dataframes = {}

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, current_step):

        if current_step < 1:

            for agent in environment.agents:
                agent.initialize_total_assets()
                agent.initialize_cash_reserves()

                "Caluclate system variables before anything happens"
                environment.variable_parameters['system_equity']  += agent.state_variables['equity']
                environment.variable_parameters['system_equity_pre_shock']  += agent.state_variables['equity']
                environment.variable_parameters['system_cash_reserves'] += agent.state_variables['cash_reserves']
                environment.variable_parameters['system_assets'] += agent.state_variables['total_assets']
                environment.variable_parameters['system_debt'] += agent.state_variables['debt']
                environment.variable_parameters['system_equity_losses'] += agent.state_variables['total_assets'] * agent.state_variables['shock_for_agent']

                environment.variable_parameters['equity_to_pre_shock'] = environment.variable_parameters['system_equity'] / environment.variable_parameters['system_equity_pre_shock']
                environment.variable_parameters['cum_equity_losses'] = 1 - environment.variable_parameters['equity_to_pre_shock']
                environment.variable_parameters['rel_equity_losses'] = - environment.variable_parameters['system_equity_losses'] / environment.variable_parameters['system_equity_pre_shock']

                #When you add a new variable to measure stuff, add it several 
                # times in lines 112ff(to initialize), reset function and update function in measurement! 
                environment.variable_parameters['system_direct_shock'] = 0 

                agent.append_results_to_dataframe(current_step)
            
            self.plug_agents_and_system_results_together(environment, current_step)

            #############  #Initial Impact
            self.do_firstround_effects(environment, current_step)
            #############

        else:
            logging.info('2.**** UPDATER.PY*** SECOND ROUND EFFECTS:')

            #########  FEEDBACK effects
            self.do_secondround_effects(environment, current_step)
            ########


            "Uncomment the following if you want beginning and\
            end of the period (2 results per current_steps). Default leave out!)"
            # for agent in environment.agents:
            #     agent.update_results_to_dataframe(current_step)
            #     logging.info("Updated results of %s within agent class", agent.identifier)



#####################################################################
    def do_firstround_effects(self, environment, current_step):
        print "1.**** UPDATER.PY*** FIRST ROUND EFFECTS FOR THIS SIMULATION:"
            #First we intiliaze the shock, which
            #gets configured in the shock config file or as argument,
            #check out capital buffer,
            #calculate total asset purchases for
            #each individual agent and the direct losses
            #for each agent"""
            #Note: Use identifier to pick out one agent\
            #Alternatively, use environment.agents[0]"

        for agent in environment.agents:
            agent.initialize_shock(environment)

            "We need to check whether the agent can absorb the\
            shock with its cash buffer (then it won't fire-sale!)\
            In that case we have to calculate new total assets and weights\
            This is quite a pain but a nice simple extension to the existing model\
            Another nice feature would be to only sell marketable assets\
            but hey..time is short."

            agent.calc_equity_and_valuation_losses()
            
            agent.state_variables['cash_reserves'] = agent.check_losses_against_capital_bufffer(environment, current_step)
            agent.calc_new_equity_and_debt() 

            ########## METHOD FOR CASH LIQUIDITY BUFFER
            if agent.state_variables['cash_reserves'] >0:
                #no fire-sales
                agent.state_variables['total_asset_sales'] = 0
                new_assets = agent.state_variables['equity'] + agent.state_variables['debt']
                new_cash, cash_weight_to_reallocate = agent.new_cash_weight(new_assets)
                

                agent.update_asset_weights(new_cash, cash_weight_to_reallocate, environment, current_step)

            if agent.state_variables['cash_reserves']==0 and agent.state_variables['debt_paid_by_cash']==0:
                agent.calc_total_asset_sales(environment, current_step, new_assets, agent.state_variables['debt_paid_by_cash'])
                new_assets = agent.state_variables['equity'] + agent.state_variables['debt']
                if new_assets > 0:
                    new_cash, cash_weight_to_reallocate = agent.new_cash_weight(new_assets)
                    agent.update_asset_weights(new_cash, cash_weight_to_reallocate, environment, current_step)

            if agent.state_variables['cash_reserves']==0 and agent.state_variables['debt_paid_by_cash']>0:

                new_assets = agent.state_variables['equity'] + agent.state_variables['debt']
                agent.calc_total_asset_sales(environment, current_step, new_assets, agent.state_variables['debt_paid_by_cash'])

                new_cash, cash_weight_to_reallocate = agent.new_cash_weight(new_assets)
                agent.update_asset_weights(new_cash, cash_weight_to_reallocate, environment, current_step)
 
    
            else:
                pass


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
            environment.variable_parameters['system_TAS'] = environment.variable_parameters['system_TAS'] + self.asset_sales_across_banks_per_asset_class[i]
        
        #UNCOMMENT for checking
        #print "***Updater.py*** In Step:", (current_step+1) , "Total assets whiped out by shock:", environment.variable_parameters['system_TAS']

    def do_firstround_effects_one_bank(self, environment, current_step):
        print "1.**** UPDATER.PY*** FIRST ROUND EFFECTS FOR THIS SIMULATION:"
        for agent in environment.agents:
            "CHECK by printing:"
            if agent.identifier == "SBSA":
                print "**UPDATER.PY***TOTAL ASSETS OF ", agent.identifier, "are:", agent.state_variables['total_assets']

            """First we intiliaze the shock, which
            gets configured in the shock config file or main file,
            check out capital buffer,
            calculate total asset purchases for
            each individual agent and the direct losses
            for each agent"""
            "Note: Use identifier to pick out one agent\
            Alternatively, use environment.agents[0]"

        for agent in environment.agents:
            agent.initialize_shock(environment)

            "We need to check whether the agent can absorb the\
            shock with its cash buffer (then it won't fire-sale!)\
            In that case we have to calculate new total assets and weights\
            This is quite a pain but a nice simple extension to the existing model\
            Another nice feature would be to only sell marketable assets\
            but hey..time is short."

            agent.calc_equity_and_valuation_losses_leverage()
            
            agent.state_variables['cash_reserves'] = agent.check_losses_against_capital_bufffer(environment, current_step)
            agent.calc_new_equity_and_debt() 

             
            if agent.state_variables['cash_reserves'] >0:
                #no fire-sales
                agent.state_variables['total_asset_sales'] = 0
                new_assets = agent.state_variables['equity'] + agent.state_variables['debt']
                new_cash, cash_weight_to_reallocate = agent.new_cash_weight(new_assets)
                

                agent.update_asset_weights(new_cash, cash_weight_to_reallocate, environment, current_step)

            if agent.state_variables['cash_reserves']==0 and agent.state_variables['debt_paid_by_cash']>0:

                new_assets = agent.state_variables['equity'] + agent.state_variables['debt']
                agent.calc_total_asset_sales(environment, current_step, new_assets, agent.state_variables['debt_paid_by_cash'])

                new_cash, cash_weight_to_reallocate = agent.new_cash_weight(new_assets)
                agent.update_asset_weights(new_cash, cash_weight_to_reallocate, environment, current_step)
                break #exit the loop, so only SBSA get's the initial impact

            if agent.state_variables['cash_reserves']==0 and agent.state_variables['debt_paid_by_cash']==0:
                agent.calc_total_asset_sales(environment, current_step, new_assets, agent.state_variables['debt_paid_by_cash'])
                new_assets = agent.state_variables['equity'] + agent.state_variables['debt']
                if new_assets > 0:
                    new_cash, cash_weight_to_reallocate = agent.new_cash_weight(new_assets)
                    agent.update_asset_weights(new_cash, cash_weight_to_reallocate, environment, current_step)
                break

            else:
                pass

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
            environment.variable_parameters['system_TAS'] = environment.variable_parameters['system_TAS'] + self.asset_sales_across_banks_per_asset_class[i]
        
        #UNCOMMENT for checking
        #print "***Updater.py*** In Step:", (current_step+1) , "Total assets whiped out by shock:", environment.variable_parameters['system_TAS']


    def do_secondround_effects(self, environment, current_step):
        print "2.**** UPDATER.PY*** SECOND ROUND EFFECTS FOR THIS SIMULATION:"

        """We update the balance sheets from the first
        round effects. Each bank's new debt is equal to
        its initial debt less total asset purchases.
        The new equity equals the initial equity_t-1 less
        the product of (shock on assets * total assets)_t-1 """

        "reset the system values to not double count"
        reset_system_variables(environment, current_step) #in measurement.py
        calc_new_system_variables(environment, current_step) #in measurement.py
        self.plug_agents_and_system_results_together(environment, current_step)

        print "Now begins step %s" % (current_step +1)

        "This is to update the shock vector"
        for m in self.asset_sales_across_banks_per_asset_class:
            price_shock = self.asset_sales_across_banks_per_asset_class[m] * environment.static_parameters['illiquidity']

            for shock in environment.shocks:
                shock.asset_returns[m] = price_shock

        "The routine from first round effect but\
         with new shock vector and balance sheets"

        for agent in environment.agents:
            agent.initialize_shock(environment)

            agent.calc_equity_and_valuation_losses()
            

            ########## METHOD FOR CASH LIQUIDITY BUFFER
            agent.state_variables['cash_reserves'] = agent.check_losses_against_capital_bufffer(environment, current_step)
            agent.calc_new_equity_and_debt() 

            if agent.state_variables['cash_reserves'] >0:
                #no fire-sales
                agent.state_variables['total_asset_sales'] = 0
                new_assets = agent.state_variables['equity'] + agent.state_variables['debt']
                new_cash, cash_weight_to_reallocate = agent.new_cash_weight(new_assets)
            
                agent.update_asset_weights(new_cash, cash_weight_to_reallocate, environment, current_step)

            if agent.state_variables['cash_reserves']==0 and agent.state_variables['debt_paid_by_cash']>0:
                new_assets = agent.state_variables['equity'] + agent.state_variables['debt']
                agent.calc_total_asset_sales(environment, new_assets, current_step, agent.state_variables['debt_paid_by_cash'])


                new_cash, cash_weight_to_reallocate = agent.new_cash_weight(new_assets)
                agent.update_asset_weights(new_cash, cash_weight_to_reallocate, environment, current_step)

            if agent.state_variables['cash_reserves']==0 and agent.state_variables['debt_paid_by_cash']==0:
                new_assets = agent.state_variables['equity'] + agent.state_variables['debt']

                agent.calc_total_asset_sales(environment, new_assets , current_step, agent.state_variables['debt_paid_by_cash'])
                
                if new_assets > 0:
                    new_cash, cash_weight_to_reallocate = agent.new_cash_weight(new_assets)
                    agent.update_asset_weights(new_cash, cash_weight_to_reallocate, environment, current_step)

            else:
                pass

        #     # this adds up the sales of m1, m2, m3 etc  across the banks
        #     # but not across classes, so we get a dictionary with
        #     # total sales of m1:value ,total sales of m2: value, etc.

        self.add_sales_across_banks(environment)

##### CALCULATE SYSTEM TOTAL ASSET SALES
#####
        environment.variable_parameters['system_TAS'] = 0
        for i in self.asset_sales_across_banks_per_asset_class:
            environment.variable_parameters['system_TAS'] = environment.variable_parameters['system_TAS'] + self.asset_sales_across_banks_per_asset_class[i]
        print "***UPDATER.PY Assets whiped out by feedback effects:", environment.variable_parameters['system_TAS'], "in step:", (current_step+1)

        AV =0
        for agent in environment.agents:
            AV+= agent.calc_equity_losses_from_system_deleveraging(environment, current_step)

        for agent in environment.agents:
            agent.calc_systemicness(environment, current_step, AV)
          

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
            "LEVERAGE IS HARD CODED PAY ATTENTION!!!!!!"
            if key != 'leverage':
                self.asset_sales_across_banks_per_asset_class[key] = 0.0
                for agent in environment.agents:
                    self.asset_sales_across_banks_per_asset_class[key] += agent.parameters[key] * agent.state_variables['total_asset_sales']

                    "Uncomment for CHECK: This is the sale per asset class per bank (cumulative):"
                    #print self.asset_sales_across_banks_per_asset_class[key], "for asset class", key,  "after adding", agent.identifier
    # -----------------------------------------------------------------------

    def plug_agents_and_system_results_together(self, environment, current_step):
        import pandas as pd
        "The measurement of variables per update step turned\
        out be rather tricky. I use a couple of methods to do this.\
        First, all the system-wide variables which are\
        stored in the environment. We make one dataframe with\
        column headers with the keys of\
        environment.variable_parameters and values entries"

        results_env_variable_parameters = []
        results_env_variable_parameters_columns = []

        if current_step <1:

            for k, v in environment.variable_parameters.iteritems():
                results_env_variable_parameters.append(v)
                results_env_variable_parameters_columns.append(k)


            df_env_p = pd.DataFrame(columns=results_env_variable_parameters_columns)
            df_env_p= df_env_p.append(pd.Series(results_env_variable_parameters, index=results_env_variable_parameters_columns), ignore_index=True)

            df_timer = pd.DataFrame({'current_step':[current_step]})
            self.env_var_par_df = pd.concat([df_timer, df_env_p], axis=1)

        else:

            temp = []

            temp.append(current_step)
            for v in environment.variable_parameters:
                temp.append(environment.variable_parameters[v])

            x = []
            x.append(current_step)
            x = list(self.env_var_par_df.columns.values)

            dftemp = pd.DataFrame([temp], columns=x)
            self.env_var_par_df = pd.concat([self.env_var_par_df, dftemp], ignore_index=True)

        #print self.env_var_par_df
        "Second, all the results for the agents. That's a bit\
        harder. We make an xlist with\
         names which later become the keys in the dictionary\
         There are as many key, value pairs as agents\
         self.all_agents_result_dictionary_with_dataframes = {df_1 : SBSA_results, df_2: Absa_results}\
         "
        xlist = []
        for i in range(len(environment.agents)):
            x = "df_" + str(i)
            xlist.append(x)

        self.all_agents_result_dictionary_with_dataframes = dict((el,0) for el in xlist)
         
        #print self.all_agents_result_dictionary_with_dataframes
        "Adding all agent results"
        for key in self.all_agents_result_dictionary_with_dataframes:
            for agent in environment.agents:
                if agent.identifier in self.all_agents_result_dictionary_with_dataframes.values():
                    pass
                else:
                    self.all_agents_result_dictionary_with_dataframes.update({key:agent.identifier})
        #print self.all_agents_result_dictionary_with_dataframes
        for key in self.all_agents_result_dictionary_with_dataframes:
            for agent in environment.agents:
                try:
                    if self.all_agents_result_dictionary_with_dataframes[key] == agent.identifier:
                        self.all_agents_result_dictionary_with_dataframes.update({key:agent.results_df})
                except:
                    logging.info(" We are in the updater and adding results per agents (i.e. result dataframe)\
                                 so dictionary self.all_agents_result_dictionary_with_dataframes. We just added the results of %s !",  agent.identifier)

    def write_sweep_list_of_results_to_csv(self, current_step, environment):
        import numpy as np
        self.env_var_par_df.to_csv("output/results_system_sweeps.csv")

        resultagentlist = []

        for k, v in self.all_agents_result_dictionary_with_dataframes.iteritems():
            resultagentlist.append(self.all_agents_result_dictionary_with_dataframes[k])

        "To get column names, we need to work around a bit\
        The next code takes all the different agents' header names\
        and puts them in:"

        resultagents_columns = np.array([resultagentlist[i].columns.values for i in range(len(resultagentlist))])

        "However, resultagents_columns has a number of agents of sublists. We need to merge\
        them and put them all together in one list called total,\
        which we use to give our csv column names\
        This neat little code here does that (python can be really cool)"
        total = []
        for i in range(len((resultagents_columns))):
            for k in resultagents_columns[i]:
                total.append(k)


        "Finally we have a result dataframe we can write to csv!!"
        df_stacked = pd.concat([r for r in resultagentlist], axis=1,  ignore_index=True)
        df_stacked.columns = total
        df_stacked.to_csv("results_all_agents_sweeps.csv")

        #  OLD CODE THROUGH WHICH I SUFFERED A GREAT DEAL - here for memorial
        #for asset_class in environment.agents[0].state_variables:

        #     if asset_class != 'leverage' and asset_class != 'losses_from_system_deleveraging' and asset_class != 'equity_losses' and asset_class != 'shock_for_agent' and asset_class != 'total_assets' and asset_class != 'total_asset_sales' and :

        #         self.asset_sales_across_banks_per_asset_class[asset_class] = 0.0

        #         for agent in environment.agents:
        #             # print asset_class, agent.state_variables[asset_class], agent.identifier, agent.state_variables['total_asset_sales']

        #             self.asset_sales_across_banks_per_asset_class[asset_class] += agent.state_variables[asset_class] * agent.state_variables['total_asset_sales']

        #             if agent.identifier == "SBSA":
        #                 print asset_class, self.asset_sales_across_banks_per_asset_class[asset_class], agent.identifier
    def do_update_leverage(self, environment, current_step, param):
        if current_step < 1:

            for agent in environment.agents:

                agent.change_leverage(param) # THIS IS NEW
                agent.initialize_total_assets()
                agent.initialize_cash_reserves()



                "Caluclate system variables before anything happens"
                environment.variable_parameters['system_equity']  += agent.state_variables['equity']
                environment.variable_parameters['system_equity_pre_shock']  += agent.state_variables['equity']
                environment.variable_parameters['system_cash_reserves'] += agent.state_variables['cash_reserves']
                environment.variable_parameters['system_assets'] += agent.state_variables['total_assets']
                environment.variable_parameters['system_debt'] += agent.state_variables['debt']
                environment.variable_parameters['system_equity_losses'] += agent.state_variables['total_assets'] * agent.state_variables['shock_for_agent']

                environment.variable_parameters['equity_to_pre_shock'] = environment.variable_parameters['system_equity'] / environment.variable_parameters['system_equity_pre_shock']
                environment.variable_parameters['cum_equity_losses'] = 1 - environment.variable_parameters['equity_to_pre_shock']
                environment.variable_parameters['rel_equity_losses'] = - environment.variable_parameters['system_equity_losses'] / environment.variable_parameters['system_equity_pre_shock']

                #When you add a new variable to measure stuff, add it several 
                # times in lines 112ff(to initialize), reset function and update function in measurement! 
                environment.variable_parameters['system_direct_shock'] = 0 

                agent.append_results_to_dataframe(current_step)
            
            self.plug_agents_and_system_results_together(environment, current_step)

            #############  #Initial Impact
            self.do_firstround_effects(environment, current_step)
            #############

        else:
            logging.info('2.**** UPDATER.PY*** SECOND ROUND EFFECTS:')
            
            #########  FEEDBACK effects
            self.do_secondround_effects(environment, current_step)
            ########


            "Uncomment the following if you want beginning and\
            end of the period (2 results per current_steps). Default leave out!)"
            # for agent in environment.agents:
            #     agent.update_results_to_dataframe(current_step)
            #     logging.info("Updated results of %s within agent class", agent.identifier)

    