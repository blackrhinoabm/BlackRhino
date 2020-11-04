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
    import sys
    sys.path.append('/Users/admin/git_repos/BlackRhino/examples/firesale2020/') #change path to your project path

    from src.environment2 import Environment2
    from src.runner import Runner
    import logging
    import pandas as pd
    import numpy as np
    import random
    from src.frange import frange
    import matplotlib.pyplot as plt
    import os
    import decimal
# We pass in the name of the environment xml as args[1] here:
    print("The name of the script is"), sys.argv[0]
 
#
# INITIALIZATION
#
    environment_directory = str("/Users/admin/git_repos/BlackRhino/examples/firesale2020/configs/environment/")
    identifier = str("firesales")
    log_directory = str("log/")

    years=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    months = [12,11,10,9,8,7,6,5,4,3,2,1]


    results=[]
    for year in years:
        for month in months:
            agent_config_dir = "/Users/admin/git_repos/BlackRhino/examples/firesale2020/experiments/single_shock_timeseries/bank_configs/"+str(year)+"-"+str(month)+"/"

    ####### Logging Configuration!!!

    ############
            environment = Environment2(environment_directory, identifier, agent_config_dir)
            runner = Runner(environment)

            for i in range(int(environment.static_parameters['num_simulations'])):

                print("**********START simulation %s") % (i+1)
                environment.initialize(environment_directory, identifier, agent_config_dir)
                environment.shocks[0].asset_returns[sys.argv[2]] = float(sys.argv[1])

                # this must be added because of the new leverage experiment  
                environment.static_parameters['leverage_increase']=1 #Default is 1 -> no change to leverage 

                if 'm_' in sys.argv[2]:
                    print(environment.shocks[0].asset_returns[sys.argv[2]])
                    print(environment.shocks[0].asset_returns)

                else: 
                    print("Check asset class argument - m_? \n Aborting.")
                    sys.exit()

                logging.info('  STARTED with run %s',  str(i))
                runner.initialize(environment)
                # do the run
                runner.do_run(environment)
                df1 = runner.updater.env_var_par_df 

                results_varnames = []
                for i in runner.sweep_result_list[0]:
                    results_varnames.append(i)

                #write results
                helper={}
                p = "./output/"+str(year)+"-"+str(month)+"/single_shock_" + str(environment.static_parameters['illiquidity'])  +"_"+ str(environment.num_agents) + "_" + str(environment.num_sweeps) +str(sys.argv[2])+str(sys.argv[1])+".csv"


                if not os.path.exists("./output/"+str(year)+"-"+str(month)+"/"):
                    os.makedirs('./output/'+str(year)+"-"+str(month)+"/")
                
                df_all = pd.concat([df1], keys=[ float(sys.argv[1])], ignore_index = False)\
                .to_csv(p)
         
                d=pd.read_csv('results_all_agents_sweeps.csv')
                e=d.filter(like='systemicness') 
                e.to_csv( "./output/"+str(year)+"-"+str(month)+'/systemicness_'+str(sys.argv[2])+str(sys.argv[1])+'_all_banks.csv')
                
                t=pd.read_csv(p)
                print("{} {} {}, Asset valuation lost through amplification: {} %".format( str(sys.argv[2]),str(sys.argv[1]),agent_config_dir[-8:-1], round((t['system_TAS'][2:].sum())/t['system_assets'][0] *-1 *100,)))

                helper['asset class'] = str(sys.argv[2])
                helper['shock'] =  str(sys.argv[1]) 
                helper['time'] = agent_config_dir[-8:-1]
                helper['asset_sales_from_deleveraging']=t['system_TAS'][2:].sum()
                helper['asset_sales_from_direct_impact'] =t['system_TAS'][:1].sum()
                helper['asset_sales_TOTAL'] = t['system_TAS'].sum()
                helper['deleveraging_losses_relative_to_direct_impact']=t['system_TAS'][2:].sum()/t['system_assets'][0] *-1 *100
                results.append(pd.DataFrame(helper, index=[agent_config_dir[-8:-1]]))
    pd.concat(results).to_csv('t.csv')






