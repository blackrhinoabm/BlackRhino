
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

	
# INITIALIZATION
#
    environment_directory = str("configs/environment/")
    identifier = str("firesales")
    log_directory = str("log/")

####### Logging Configuration!!!
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                        filename=log_directory + identifier + ".log", level=logging.INFO)
    logging.info('The program starts! Logging enabled.')
############
    environment = Environment(environment_directory, identifier)
    runner = Runner(environment)

    #Make shocks in floating range
    shock_list = [-0.9, -0.7, -0.5, -0.3,  -0.1]
 
 	#Make illiquiidty parameters in floating range
    #ill_list = list(frange(0.00000000000000714285714285714, 0.00000000714285714285714, 0.0000000001))
    rho_list = [ 2.00E-15 ,2.50E-15 ,3.00E-15 , 3.50E-15 ,4.00E-15,
4.50E-15,
5.00E-15,
6.50E-15,
7.00E-15,
7.50E-15,
8.00E-15,
8.50E-15,
9.00E-15,
9.50E-15,
1.00E-14,
1.50E-14,
2.00E-14,
2.50E-14,
3.00E-14,
3.50E-14,
4.00E-14,
4.50E-14,
5.00E-14,
5.50E-14,
6.00E-14,
6.50E-14,
7.00E-14,
7.50E-14,
8.00E-14,
8.50E-14,
9.00E-14,
1.00E-13,
1.50E-13,
2.00E-13,
2.50E-13,
3.00E-13,
3.50E-13,
4.00E-13,
4.50E-13,
5.00E-13,
5.50E-13,
6.00E-13,
6.50E-13,
7.00E-13,
7.50E-13,
8.00E-13,
8.50E-13,
9.00E-13,
9.10E-13,
9.20E-13,
9.30E-13,
9.40E-13,
9.50E-13,
9.60E-13,
9.70E-13,
9.80E-13,
9.90E-13,
1.00E-12,
2.00E-12,
7.00E-12,
8.00E-12,
9.00E-12,
9.00E-11,
 ]
 
# #
# # UPDATE STEP
# #
 
    # #declare number of shocks
    number_shocks = len(shock_list)
    banks = len(environment.agents)

    output = []
    # mu, sigma = 3., 0.6 # mean and standard deviation
    # mylist = np.random.lognormal(mu, sigma, number_shocks).tolist()
    
    
    # illiquidity_coefficient  = random.uniform(0.00000000000000714285714285714, 0.000000000001)
    # environment.static_parameters['illiquidity'] = illiquidity_coefficient 
    
    for index1, element1 in enumerate(rho_list):  

    	for index2, element2 in enumerate(shock_list):
	    
 	        print("**********START simulation %s") % (index2+1)
	    
	        environment.initialize(environment_directory, identifier)
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
	    
	        logging.info(' Run DONE')
	        logging.info("***\nSimulation number %s had total number of %s sweeps", index2, str(runner.num_sweeps))
	        logging.info("***\nSimulation number %s had total number of %s shocks", index2, str(number_shocks))

	        logging.info("***\nThis run had the illiquidity coefficient %s " , environment.static_parameters['illiquidity'])

	     
		pd.concat(output, ignore_index = False).to_csv("shock_list" + str(number_shocks) + "_" + str(banks) + "_" + str(index1) + ".csv")

	print('Program DONE! Fire-sales happend!')
	logging.info('FINISHED Program logging for run: %s \n', environment_directory + identifier + ".xml")

