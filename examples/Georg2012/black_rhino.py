#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
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
#-------------------------------------------------------------------------
#
#  MAIN
#
#-------------------------------------------------------------------------
if __name__ == '__main__':
    import pdb # python debugger, for debugging purposes only
    
    import sys
    sys.path.append('src/')
    import logging
    import networkx as nx
    
    from src.environment import Environment
    from src.runner import Runner
    from src.measurement import Measurement
    
    args = ['./black_rhino.py',  "environments/", "test1",  "log/",  "measurements/"]
    #args = sys.argv
    
    if len(args) != 5:
        print("Usage: ./black_rhino environment_directory/ environment_identifier log_directory/ measurement_directory/")
        sys.exit()

#
# INITIALIZATION
#
    environment_directory = str(args[1])
    identifier = str(args[2])
    log_directory = str(args[3])
    measurement_directory = str(args[4])
    
    # Configure logging parameters so we get output while the program runs
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                        filename=log_directory + identifier + ".log",
                        level=logging.INFO)
    logging.info('START logging for run: %s',  environment_directory + identifier + ".xml")
    
    environment = Environment()
    environment.initialize(environment_directory,  identifier)
    runner = Runner()
    measurement = Measurement()

#
# UPDATE STEP
#
    for i in range(environment.parameters.numSimulations):
        logging.info('  STARTED with run %s',  str(i))
        environment.initialize(environment_directory,  identifier)
        # check that environment file has been read correctly
        #environment.write_environment_file(identifier)
        runner.initialize(environment)
        measurement.initialize() # clear the previous measurement
        
        # do the run
        runner.do_run(measurement,  "info")
        # do the histograms, i.e. add the current measurement to the histogram
        measurement.do_histograms()
        logging.info('  DONE')

    #
    # MEASUREMENT AND LOGGING
    #
    measurement.write_histograms(measurement_directory,  environment)
    logging.info('FINISHED logging for run: %s \n', environment_directory + identifier + ".xml")

