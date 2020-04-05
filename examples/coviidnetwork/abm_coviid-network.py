from examples.coviidnetwork.src.environment import Environment
from examples.coviidnetwork.src.runner import Runner
import networkx as nx


args = ["configs/environments/", "config_coviid", "log/", 1]

# initialization
environment_directory = str(args[0])
identifier = str(args[1])
log_directory = str(args[2])
runs = args[3]

# Monte Carlo Simulations
for i in range(runs):
    # initialize environment and runner from files
    environment = Environment(environment_directory, identifier, seed=i)
    runner = Runner(environment)
    # do the run
    runner.do_run(environment, seed=i)

    # save network
    for idx, network in enumerate(environment.infection_states):
        for idx2, node in enumerate(network.nodes):
            network.nodes[idx2]['agent'] = network.nodes[idx2]['agent'].status

        nx.write_graphml_lxml(network, "measurements/{}-network_time{}.graphml".format(i, idx))
