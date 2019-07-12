#!/usr/bin/env python
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


    environment.static_parameters['leverage_increase'] = (1/3)
    print environment.static_parameters['leverage_increase']
    for i in range(int(environment.static_parameters['num_simulations'])):

        if i == 0:

            print("**********START simulation %s") % (i+1)
            environment.initialize(environment_directory, identifier)

            #specify shock for asset class 
            environment.shocks[0].asset_returns['m_14'] = -0.2

            #print environment.shocks[0].asset_returns['m_14']
            # print environment.shocks[0].asset_returns

            runner.initialize(environment)
            # # do the run
            runner.do_run(environment, )
            df1 = runner.updater.env_var_par_df  
            print(' Run DONE')
            print("***\nSimulation number %s had total number of %s sweeps", i, str(runner.num_sweeps))
            print("***\nThis run had the illiquidity coefficient %s " , environment.static_parameters['illiquidity'])
            df_all = pd.concat([df1], keys=[ '-0.2'], ignore_index = False).to_csv("output/leverage_" + str(environment.static_parameters['illiquidity'])  +"_"+ str(environment.num_agents) + "_" + str(environment.num_sweeps) + ".csv")
        
        if i==1:
            

            pass