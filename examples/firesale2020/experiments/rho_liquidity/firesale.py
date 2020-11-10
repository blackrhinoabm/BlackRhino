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
    year= 2015
    month = 12
 
    asset = 'm_18'

    shocks=np.linspace(-0.04, -0.4, num=10).tolist() 
    impacts=[round(num,2) for num in shocks]   #    impacts = [ -0.5,  -0.2,-0.1]
    # impacts =[  -0.1, -0.2, -0.3, -0.4, -0.5]


    #THIS WORKS FOR ONE MOMENT IN TIME!!!! 

    shock_list = impacts
    rho_list = [ 0.00000000000009, 0.000000000000085,
    0.00000000000008,
    0.000000000000075,
    0.00000000000007,
    0.000000000000065,
    0.00000000000006,
    0.000000000000055,
    0.00000000000005,
    0.000000000000045,
    0.00000000000004,
    0.000000000000035,
    0.00000000000003,
    0.000000000000025,
    0.00000000000002,
    0.000000000000015,
    0.00000000000001,
    0.00000000000099,
    0.00000000000098,
    0.00000000000097,
    0.00000000000096,
    0.00000000000095,
    0.00000000000094,
    0.00000000000093,
    0.00000000000092,
    0.00000000000091,
    0.0000000000009,
    0.00000000000085,
    0.0000000000008,
    0.00000000000075,
    0.0000000000007,
    0.00000000000065,
    0.0000000000006,
    0.00000000000055,
    0.0000000000005,
    0.00000000000045,
    0.0000000000004,
    0.00000000000035,
    0.0000000000003,
    0.00000000000025,
    0.0000000000002,
    0.00000000000015,
    0.0000000000001,
    0.000000000009,
    0.000000000008,
    0.000000000007,
    0.000000000002,
    0.000000000001,
    0.00000000009]

# #
# # UPDATE STEP
# #
    ######################!!!!!!!!!!!!!
    #choose random illiquidity parameter in interval 
    # ######################!!!!!!!!!!!!!!!!!!!!!!
    # #declare number of shocks
    number_shocks = len(shock_list)

    output = []
        
    for index1, element1 in enumerate(rho_list):  

        for index2, element2 in enumerate(shock_list):

            agent_config_dir =  os.path.join(home,'bank_configs/',str(year)+"-"+str(month)+"/")

            identifier = str("firesales")
            environment = Environment2(environment_directory, identifier, agent_config_dir)
            runner = Runner(environment)
            print("**********START simulation %s") % (index2+1)
            environment.initialize(environment_directory, identifier,agent_config_dir)
            banks = len(environment.agents)

            environment.shocks[0].asset_returns[asset] = element2
            environment.static_parameters['illiquidity'] = element1 

            environment.saveparams['shock']=str(element2)
            environment.saveparams['asset']=asset
            environment.saveparams['initial_shock_bank']='all_banks'
            environment.saveparams['outputpath']= "./output/" +str(year)+"-"+str(month)+"/"+ asset+ '/'
            environment.saveparams['time']=str(year)+"-"+str(month)
            environment.saveparams['illiquidity'] = environment.static_parameters["illiquidity"] 

            runner.initialize(environment)
            # do the run
            runner.do_run(environment)
            df_system = runner.updater.env_var_par_df
        
            df_asset_class = pd.DataFrame({'asset_class': [asset]})
            df_shock = pd.DataFrame({'shock': [element2]})
            df_illiquidity = pd.DataFrame({'illiquidity': [element1]})

            df_all_fucking_variables = pd.concat((df_system , df_asset_class, df_shock, df_illiquidity), axis=1, ignore_index = False )
        
            output.append(df_all_fucking_variables)

        pd.concat(output, ignore_index = False).to_csv("shock_list" + str(number_shocks) + "_" + str(banks) + "_" + str(index1) + ".csv")


    print('Program DONE! Fire-sales happend!')
 
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







