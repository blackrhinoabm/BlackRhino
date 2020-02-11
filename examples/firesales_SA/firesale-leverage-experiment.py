#!/usr/bin/env python
from __future__ import division
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

"""
This is a minimal example.

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
along with this program. If not, see <http://www.gnu.org/licenses/>

The development of this software has been supported by the ERA-Net
on Complexity through the grant RESINEE.


"""

# -------------------------------------------------------------------------
#
#  MAIN
#
# -------------------------------------------------------------------------
if __name__ == '__main__':
    from src.environment import Environment
    from src.runner import Runner
    import logging
    import pandas as pd
    import numpy as np
    import random
    from src.frange import frange
    import matplotlib.pyplot as plt
    import sys
    import decimal

    
# INITIALIZATION
#
    environment_directory = str("configs/environment/")
    identifier = str("firesales")

############
    environment = Environment(environment_directory, identifier)
    runner = Runner(environment)
   
############ 
    #Declare variables of interest for the simulation

    print("the illiquidity paramer is"), environment.static_parameters['illiquidity']  #is declared inside ENV config
    print("the num_simulations paramer is"), environment.static_parameters['num_simulations'] # is declared inside ENV config 

 
    

    # #LIST OF VARIABLES 
    shock_list = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2,  -0.1]
    
    #shock_list = [-0.1, -0.2, -0.5, -0.7, -0.9]
    #Make illiquiidty parameters in floating range
    #ill_list = list(frange(0.00000000000000714285714285714, 0.00000000714285714285714, 0.0000000001))
    delta_leverage = [0.8, 0.9, 1 , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5]

    number_shocks = len(shock_list)
    number_lev = len(delta_leverage)
    banks = len(environment.agents)

    output = []

    for index1, element1 in enumerate(delta_leverage):  

        for index2, element2 in enumerate(shock_list):

            print("**********START simulation %s") % (index2+1)
                
            environment.initialize(environment_directory, identifier)
            environment.shocks[0].asset_returns['m_14'] = element2
            environment.static_parameters['leverage_increase']  = element1 

            print environment.shocks[0].asset_returns['m_14']
            logging.info('  STARTED with run %s',  str(index2))
            runner.initialize(environment)
            # do the run
            runner.do_run(environment)
            df_system = runner.updater.env_var_par_df
        
            df_asset_class = pd.DataFrame({'asset_class': ['m_14']})
            df_shock = pd.DataFrame({'shock': [element2]})
            df_illiquidity = pd.DataFrame({'leverage': [element1]})

            df_all_fucking_variables = pd.concat((df_system , df_asset_class, df_shock, df_illiquidity), axis=1, ignore_index = False )
        
            output.append(df_all_fucking_variables)
        
            logging.info(' Run DONE')
            logging.info("***\nSimulation number %s had total number of %s sweeps", index2, str(runner.num_sweeps))
            logging.info("***\nSimulation number %s had total number of %s shocks", index2, str(number_shocks))

            logging.info("***\nThis run had the illiquidity coefficient %s " , environment.static_parameters['illiquidity'])

                 
        pd.concat(output, ignore_index = False).to_csv("LEVERAGE_list_" + str(number_lev) + "_" + str(number_shocks) + "_" + str(index1) + ".csv")

        print('Program DONE! Fire-sales happend!')
        logging.info('FINISHED Program logging for run: %s \n', environment_directory + identifier + ".xml")


    ##############
    ##############
    # QUICK RUN 
    ##############
    ##############

    # for i in range(int(environment.static_parameters['num_simulations'])):

    #     if i == 0:

    #         print("**********START simulation %s") % (i+1)
    #         environment.initialize(environment_directory, identifier)

    #         #specify shock for asset class 
    #         environment.shocks[0].asset_returns['m_14'] = -0.2

    #         #print environment.shocks[0].asset_returns['m_14']
    #         # print environment.shocks[0].asset_returns

    #         runner.initialize(environment)
    #         # # do the run

    #         environment.static_parameters['leverage_increase'] = 0.3
    #         print environment.static_parameters['leverage_increase']
    #         runner.do_run(environment)
    #         df1 = runner.updater.env_var_par_df  
    #         print(' Run DONE')
    #         print("***\nSimulation number %s had total number of %s sweeps", i, str(runner.num_sweeps))
    #         print("***\nThis run had the illiquidity coefficient %s " , environment.static_parameters['illiquidity'])
    #         df_all = pd.concat([df1], keys=[ '-0.2'], ignore_index = False).to_csv("output/leverage_" + str(environment.static_parameters['illiquidity'])  +"_"+ str(environment.num_agents) + "_" + str(environment.num_sweeps) + ".csv")
        

