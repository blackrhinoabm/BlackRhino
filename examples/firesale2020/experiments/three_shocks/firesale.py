#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
#
#  MAIN  - what are loan book assets?
#
# -------------------------------------------------------------------------
if __name__ == '__main__':
    import time
    start = time.time()
    import sys, os
    import os.path as path
    gotoroot =  path.abspath(path.join(__file__ ,"../../../")) #this was more difficult than expected  - import module from two directories up
    sys.path.append(gotoroot)
    from src.environment2 import Environment2
    from src.runner import Runner
    import logging
    import pandas as pd
    import numpy as np
    import random
    from src.frange import frange
    import matplotlib.pyplot as plt
    import decimal

    #
    # INITIALIZATION
    home = os.getcwd()
    environment_directory=gotoroot +  "/configs/environment/"
    years=[ 2020]
    months = [2]
 
    assets = ['m_18']

    # shocks=np.linspace(-0.04, -0.4, num=10).tolist() 
    # impacts=[round(num,2) for num in shocks]   #    impacts = [ -0.5,  -0.2,-0.1]
    impacts =[  -0.1, -0.2, -0.3, -0.4, -0.5, ]

    print("The time period is {} {} ".format(years,months))
    results_system_impacts = []
    results_agents_impacts = []
    assets_agt = []
    assets_sys = []

    #THIS WORKS FOR ONE MOMENT IN TIME!!!! 

    for year in years:
        for month in months:

            for asset in assets:
                #yeah that's a lot of loops.....
                for impact in impacts: 
                    agent_config_dir =  os.path.join(home,'bank_configs/',str(year)+"-"+str(month)+"/")

                    print(agent_config_dir)

            # ############
                    identifier = str("firesales")
                    environment = Environment2(environment_directory, identifier, agent_config_dir)
                    runner = Runner(environment)

                    # environment.static_parameters['leverage_increase']=1 #Default is 1 -> no change to leverage 


                    print("**********START simulation ")
                    environment.initialize(environment_directory, identifier, agent_config_dir)

                    runner.initialize(environment) #honestly this is a bit stupid - I blame Pawel! ;)
                    # # do the run
                    environment.shocks[0].asset_returns[asset] = float(impact)

                    environment.saveparams['shock']=str(impact)
                    environment.saveparams['asset']=asset
                    environment.saveparams['initial_shock_bank']='all'
                    environment.saveparams['outputpath']= "./output/" +str(year)+"-"+str(month)+"/"+ asset+ '/'
                    environment.saveparams['time']=str(year)+"-"+str(month)
                    environment.saveparams['illiquidity'] = environment.static_parameters["illiquidity"] 
                    print("The shock is {}".format(environment.shocks[0].asset_returns))
                    ##########
                    #DO THE STRESS-TEST #######
                    runner.do_run(environment) #important - check what is called here!
                    ############ !!!!
                    ##########
                    df_system = runner.updater.env_var_par_df 
                    df_agents = runner.updater.df_stacked 
                    results_system_impacts.append(df_system)
                    results_agents_impacts.append(df_agents)

                    results_varnames = []
                    for i in runner.sweep_result_list[0]:
                        results_varnames.append(i)

                #write results all shocks per asset - but it's not really needed because I write all to disk in the next loop 
                output_system_shocks_one_time_impacts=pd.concat(results_system_impacts)
                # output_system_shocks_one_time_impacts.drop_duplicates().to_csv(environment.saveparams['outputpath']+'all_shocks_SYSTEM_oneasset.csv')
                output_agents_shocks_one_time_impacts=pd.concat(results_agents_impacts)
                # output_agents_shocks_one_time_impacts.drop_duplicates().to_csv(environment.saveparams['outputpath']+'all_shocks_AGENTS_oneasset.csv')

                assets_sys.append(output_system_shocks_one_time_impacts)
                assets_agt.append(output_agents_shocks_one_time_impacts)

            environment.saveparams['outputpath']= "./output/"+str(year)+"-"+str(month)+"/"

            pd.concat(assets_sys).drop_duplicates().to_csv(environment.saveparams['outputpath']+'all_SYSTEM.csv')
            pd.concat(assets_agt).drop_duplicates().to_csv(environment.saveparams['outputpath']+'all_AGENTS.csv')
            break # Only one time point!!! 
# Comment out below
                #write results
                # helper={}
                # p = "./output/"+str(year)+"-"+str(month)+"/single_shock_" + str(environment.static_parameters['illiquidity'])  +"_"+ str(environment.num_agents) + "_" + str(environment.num_sweeps) +str(sys.argv[2])+str(sys.argv[1])+".csv"


                # if not os.path.exists("./output/"+str(year)+"-"+str(month)+"/"):
                #     os.makedirs('./output/'+str(year)+"-"+str(month)+"/")
                
                # df_all = pd.concat([df1], keys=[ float(sys.argv[1])], ignore_index = False)\
                # .to_csv(p)

                #get agent result location!
         
                # d=pd.read_csv('results_all_agents_sweeps.csv')
                # e=d.filter(like='systemicness') 
                # e.to_csv( "./output/"+str(year)+"-"+str(month)+'/systemicness_'+str(sys.argv[2])+str(sys.argv[1])+'_all_banks.csv')
                
                # t=pd.read_csv(p)
                # print("{} {} {}, Asset valuation lost through amplification: {} %".format( str(sys.argv[2]),str(sys.argv[1]),agent_config_dir[-8:-1], round((t['system_TAS'][2:].sum())/t['system_assets'][0] *-1 *100,)))

                # helper['asset class'] = str(sys.argv[2])
                # helper['shock'] =  str(sys.argv[1]) 
                # helper['time'] = agent_config_dir[-8:-1]
                # helper['asset_sales_from_deleveraging']=t['system_TAS'][2:].sum()
                # helper['asset_sales_from_direct_impact'] =t['system_TAS'][:1].sum()
                # helper['asset_sales_TOTAL'] = t['system_TAS'].sum()
                # helper['deleveraging_losses_relative_to_direct_impact']=t['system_TAS'][2:].sum()/t['system_assets'][0] *-1 *100
                # results.append(pd.DataFrame(helper, index=[agent_config_dir[-8:-1]]))
    # pd.concat(results).to_csv('t.csv')

    end = time.time()
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("Done. Run time {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))







