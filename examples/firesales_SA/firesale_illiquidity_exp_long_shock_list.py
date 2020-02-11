
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
    import decimal
    from src.frange import frange

    import matplotlib.pyplot as plt
    import sys

# We pass in the name of the script as args[1] here:
    print("The name of the script is"), sys.argv[0]
# This program varies shocks and illiquidity coefficient"
# pass in asset class of initial shock, e.g. m_14
	
# INITIALIZATION
#
    environment_directory = str("configs/environment/")
    identifier = str("firesales")
    log_directory = str("log/")

####### No logging because massive data is produced
 
############
    environment = Environment(environment_directory, identifier)
    runner = Runner(environment)

    #Make shocks in floating range
    shock_list = list(frange(-0.9, 0, 0.01))

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
    banks = len(environment.agents)

    output = []
        
    for index1, element1 in enumerate(rho_list):  

    	for index2, element2 in enumerate(shock_list):
            print("**********START simulation %s") % (index2+1)
            environment.initialize(environment_directory, identifier)
            if len(sys.argv)>1:
                environment.shocks[0].asset_returns[sys.argv[1]] = element2
    	        environment.static_parameters['illiquidity'] = element1 
                print environment.shocks[0].asset_returns[sys.argv[1]]
                logging.info('  STARTED with run %s',  str(index2))
                runner.initialize(environment)
                # do the run
                runner.do_run(environment)
                df_system = runner.updater.env_var_par_df
            
                df_asset_class = pd.DataFrame({'asset_class': [sys.argv[1]]})
                df_shock = pd.DataFrame({'shock': [element2]})
                df_illiquidity = pd.DataFrame({'illiquidity': [element1]})

                df_all_fucking_variables = pd.concat((df_system , df_asset_class, df_shock, df_illiquidity), axis=1, ignore_index = False )
            
                output.append(df_all_fucking_variables)
            else:
                print "Can't run :( \n Please pass in key of shocked asset (m_1, .... m_23) as sys.argv[1])"
                exit()
        pd.concat(output, ignore_index = False).to_csv("shock_list" + str(number_shocks) + "_" + str(banks) + "_" + str(index1) + ".csv")


	print('Program DONE! Fire-sales happend!')
 
