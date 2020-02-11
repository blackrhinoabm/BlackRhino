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

    args = ["configs/environments/", "test_degroot", "log/"]

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
