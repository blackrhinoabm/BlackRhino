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
    log_directory = str("log/")

# THIS FIRESALE MODEL NEEDS 4 ARGUMENTS: 3 SHOCKS AND ONE ASSET CLASS THAT WILL BE SHOCKED

####### Logging Configuration!!!
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                        filename=log_directory + identifier + ".log", level=logging.INFO)
    logging.info('The program starts! Logging enabled.')
############
    environment = Environment(environment_directory, identifier)
    runner = Runner(environment)
   
    print("the illiquidity paramer is"), environment.static_parameters['illiquidity']
    for i in range(int(environment.static_parameters['num_simulations'])):

        if i == 0:

            print("**********START simulation %s") % (i+1)
            environment.initialize(environment_directory, identifier)
            environment.shocks[0].asset_returns[sys.argv[4]] = float(sys.argv[1])

            print environment.shocks[0].asset_returns[sys.argv[4]]
            print environment.shocks[0].asset_returns

            logging.info('  STARTED with run %s',  str(i))
            runner.initialize(environment)
            # do the run
            runner.do_run(environment)
            df1 = runner.updater.env_var_par_df  
            logging.info(' Run DONE')
            logging.info("***\nSimulation number %s had total number of %s sweeps", i, str(runner.num_sweeps))
            logging.info("***\nThis run had the illiquidity coefficient %s " , environment.static_parameters['illiquidity'])

        if i == 1:
            print("**********START simulation %s") % (i+1)
            environment.initialize(environment_directory, identifier)
            environment.shocks[0].asset_returns[sys.argv[4]] = float(sys.argv[2])

            logging.info('  STARTED with run %s',  str(i))
            runner.initialize(environment)
            # do the run
            runner.do_run(environment)
            df2 = runner.updater.env_var_par_df  
            logging.info(' Run DONE')
            logging.info("***\nSimulation number %s had total number of %s sweeps", (i+1), str(runner.num_sweeps))
            logging.info("***\nThis run had the illiquidity coefficient %s ", environment.static_parameters['illiquidity'])

        if i == 2:
            print("**********START simulation %s") % (i+1)
            environment.initialize(environment_directory, identifier)
            environment.shocks[0].asset_returns[sys.argv[4]] = float(sys.argv[3])
            logging.info('  STARTED with run %s',  str(i))
            runner.initialize(environment)
            # do the run
            runner.do_run(environment)
            df3 = runner.updater.env_var_par_df

            logging.info(' Run DONE')
            logging.info("***\nSimulation number %s had total number of %s sweeps", (i+1), str(runner.num_sweeps))
            logging.info("***\nThis run had the illiquidity coefficient %s ", environment.static_parameters['illiquidity'])
            results_varnames = []
            for i in runner.sweep_result_list[0]:
                results_varnames.append(i)

            df_all = pd.concat([df1, df2, df3], keys=[ float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])], ignore_index = False).to_csv("output/single_shocks_" + str(environment.static_parameters['illiquidity'])  +"_"+ str(environment.num_agents) + "_" + str(environment.num_sweeps) + ".csv")
    print environment.static_parameters['illiquidity']

    print('Program DONE! Fire-sales happend!')
    logging.info('FINISHED Program logging for run: %s \n', environment_directory + identifier + ".xml")
