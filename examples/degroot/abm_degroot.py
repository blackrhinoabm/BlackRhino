from src.environment import Environment
from src.runner import Runner


args = ["configs/environments/", "test_degroot", "log/"]

# initialization
environment_directory = str(args[0])
identifier = str(args[1])
log_directory = str(args[2])

environment = Environment(environment_directory, identifier)
runner = Runner(environment)

# update step
for i in range(int(environment.static_parameters['num_simulations'])):
    environment.initialize(environment_directory, identifier)
    runner.initialize(environment)
    # do the run
    runner.do_run(environment)
