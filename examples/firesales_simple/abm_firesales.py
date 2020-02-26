#!/usr/bin/env python
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

    args = ["configs/environment/", "environment_config", "log/"]

#
# INITIALIZATION
#
    environment_directory = str(args[0])
    identifier = str(args[1])
    log_directory = str(args[2])

    environment = Environment(environment_directory, identifier)
    runner = Runner(environment)

#
# UPDATE STEP
#
    for i in range(int(environment.static_parameters['num_simulations'])):
        environment.initialize(environment_directory, identifier)
        runner.initialize(environment)
        # do the run
        runner.do_run(environment)
