#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-
 

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


 
#
# INITIALIZATION
#
    environment_directory = str("/Users/admin/git_repos/BlackRhino/examples/firesale2020/configs/environment/")
    identifier = str("firesales")
    log_directory = str("log/")

    years=[ 2015]
    months = [12]


    print("The time period is {} {} ".format(years,months))
    results=[]
    for year in years:
        for month in months:
            agent_config_dir = "/Users/admin/git_repos/BlackRhino/examples/firesale2020/experiments/single_bank/bank_configs/"+str(year)+"-"+str(month)+"/"

    ####### Logging Configuration!!!

    ############
            environment = Environment2(environment_directory, identifier, agent_config_dir)
            runner = Runner(environment)

            for i in range(int(environment.static_parameters['num_simulations'])):

                print("**********START simulation %s") % (i+1)
                environment.initialize(environment_directory, identifier, agent_config_dir)
                # environment.shocks[0].asset_returns[sys.argv[2]] = float(sys.argv[1])

                environment.static_parameters["scenario"] = 'single_bank'

                identifier = "STANDARD"  #maybe pass in as sys.argv??

                print("The scenario is {}, {}".format(environment.static_parameters["scenario"], identifier))

                #     print(environment.shocks[0].asset_returns[sys.argv[2]])
                #     print(environment.shocks[0].asset_returns)


                runner.initialize(environment) #honestly this is a bit stupid - I blame Pawel! ;)
                # # do the run
                # runner.do_run(environment)
                # df1 = runner.updater.env_var_par_df 

                # results_varnames = []
                # for i in runner.sweep_result_list[0]:
                #     results_varnames.append(i)


# Comment out below
                #write results
                # helper={}
                # p = "./output/"+str(year)+"-"+str(month)+"/single_shock_" + str(environment.static_parameters['illiquidity'])  +"_"+ str(environment.num_agents) + "_" + str(environment.num_sweeps) +str(sys.argv[2])+str(sys.argv[1])+".csv"


                # if not os.path.exists("./output/"+str(year)+"-"+str(month)+"/"):
                #     os.makedirs('./output/'+str(year)+"-"+str(month)+"/")
                
                # df_all = pd.concat([df1], keys=[ float(sys.argv[1])], ignore_index = False)\
                # .to_csv(p)
         
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






