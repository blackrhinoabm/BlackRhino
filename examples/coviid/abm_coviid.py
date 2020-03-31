from src.environment import Environment
from src.runner import Runner


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
