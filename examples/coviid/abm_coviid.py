from examples.coviid.src.environment import Environment
from examples.coviid.src.runner import Runner
import json


args = ["configs/environments/", "config_coviid", "log/", 1]

# initialization
environment_directory = str(args[0])
identifier = str(args[1])
log_directory = str(args[2])
runs = args[3]

# Monte Carlo Simulations
for i in range(runs):
    # initialize environment and runner from files
    environment = Environment(environment_directory, identifier)
    runner = Runner(environment)
    # do the run
    runner.do_run(environment)

    # store grid
    with open('grids.json', 'w') as F:
        F.write(json.dumps(environment.infection_states))
