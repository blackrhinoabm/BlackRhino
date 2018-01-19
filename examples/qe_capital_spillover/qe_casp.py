#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
#
#  MAIN
#
# -------------------------------------------------------------------------
if __name__ == '__main__':
    import logging
    from src.environment import Environment
    from src.runner import Runner

    args = ["configs/environment/", "qe_casp", "log/"]

#
# INITIALIZATION
#
    environment_directory = str(args[0])
    identifier = str(args[1])
    log_directory = str(args[2])

    # Configure logging parameters so we get output while the program runs
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                        filename=log_directory + identifier + ".log", level=logging.INFO)
    logging.info("START logging")

    logging.info('Instantiate environment object to find environment.static_parameters["num_simulations"]')
    environment = Environment(environment_directory, identifier)
    logging.info('Instantiate runner object')
    runner = Runner(environment)

#
# UPDATE STEP
#
    logging.info('Iterating over %s number of simulations ', environment.static_parameters['num_simulations'] )
    for i in range(int(environment.static_parameters['num_simulations'])):
        # environment.initialize(environment_directory, identifier)  Turns out I don't need to call this as already initialized environment?? Crazy
        # logging.info('Call runner.initialize to get num_sweeps and pass into runner')

        runner.initialize(environment)
    #     # do the run
        runner.do_run(environment, i)
