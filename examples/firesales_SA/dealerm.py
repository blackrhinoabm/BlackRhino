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

# We pass in the name of the environment xml as args[1] here:

    args = ["configs/environment/", "firesales", "log/"]

#
# INITIALIZATION
#
    environment_directory = str(args[0])
    identifier = str(args[1])
    log_directory = str(args[2])


####### Logging Configuration!!!
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                        filename=log_directory + identifier + ".log", level=logging.INFO)
    logging.info('The program starts! Logging enabled.')
############


    environment = Environment(environment_directory, identifier)
    runner = Runner(environment)

#
# UPDATE STEP
#

    sim_result_list = []

    for i in range(int(environment.static_parameters['num_simulations'])):
        if i == 0:

            print("**********START simulation %s") % (i+1)
            environment.initialize(environment_directory, identifier)
            environment.shocks[0].asset_returns['m_14'] = -0.1
            runner.initialize(environment)
                    # do the run
            runner.do_run(environment)
            sim_result_list.append(runner.sweep_result_list)

            print("***\nSimulation number %s had total number of %s sweeps" ) % (i+1, runner.num_sweeps)
            print("***\nThis run had the illiquidity coefficient %s " ) % (environment.static_parameters['illiquidity'])

        if i == 1:
            print("**********START simulation %s") % (i+1)
            environment.initialize(environment_directory, identifier)
            environment.shocks[0].asset_returns['m_14'] = -0.2

            runner.initialize(environment)
            # do the run
            runner.do_run(environment)

            sim_result_list.append(runner.sweep_result_list)
            print("***\nSimulation number %s had total number of %s sweeps" ) % (i+1, runner.num_sweeps)
            print("***\nThis run had the illiquidity coefficient %s " ) % (environment.static_parameters['illiquidity'])

        # print sim_result_list

        logging.info('  STARTED with run %s',  str(i))
        runner.initialize(environment)
        # do the run
        runner.do_run(environment)

        logging.info(' Run DONE')

    print('Program DONE! Fire-sales happend!')
    logging.info('FINISHED Program logging for run: %s \n', environment_directory + identifier + ".xml")
