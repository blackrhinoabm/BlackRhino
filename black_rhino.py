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
    import logging

    from src.environment import Environment
    from src.runner import Runner

    args = ['./black_rhino.py',  "tests/environments/", "test_all_methods",  "tests/log/"]
    # args = sys.argv

    if len(args) != 4:
        print("Usage: ./black_rhino environment_directory/ environment_identifier log_directory/")
        sys.exit()


#
# INITIALIZATION
#
    environment_directory = str(args[1])
    identifier = str(args[2])
    log_directory = str(args[3])

    # Configure logging parameters so we get output while the program runs
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                        filename=log_directory + identifier + ".log", level=logging.INFO)
    logging.info('START logging for run: %s',  environment_directory + identifier + ".xml")

    environment = Environment(environment_directory,  identifier)
    runner = Runner(environment)

#
# UPDATE STEP
#
    for i in range(int(environment.num_simulations)):
        logging.info('  STARTED with run %s',  str(i))
        environment.initialize(environment_directory,  identifier)
        runner.initialize(environment)
        # do the run
        runner.do_run(environment)
        logging.info('  DONE')

#
# MEASUREMENT AND LOGGING
#
    logging.info('FINISHED logging for run: %s \n', environment_directory + identifier + ".xml")
