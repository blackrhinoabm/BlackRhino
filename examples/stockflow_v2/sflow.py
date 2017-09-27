#!/usr/bin/env python -W ignore::DeprecationWarning
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
#
#  MAIN
#
# -------------------------------------------------------------------------
if __name__ == '__main__':

    from src.environment import Environment
    from src.runner import Runner
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning) 
# We have to pass in the name of the environment xml as args[1] here:
# the path of the environment xml as args[0]
# and the scenario name as args[2] here:

    args = ["configs/environment/", "environment_config", "benchmark"]

#
# INITIALIZATION
#
    environment_directory = str(args[0])
    identifier = str(args[1])
    scenario = str(args[2])
    environment = Environment(environment_directory, identifier)
    runner = Runner(environment, scenario)

#
# UPDATE STEP
#
    for i in range(int(environment.static_parameters['num_simulations'])):
        environment.initialize(environment_directory, identifier)
        runner.initialize(environment, scenario)
        # do the run
        runner.do_run(environment, scenario)
