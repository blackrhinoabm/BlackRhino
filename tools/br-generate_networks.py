#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]

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
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import sys

import networkx as nx

sys.path.append('src/')


if __name__ == '__main__':

    if (len(sys.argv) != 5):
        sys.exit("Usage: ./generate_networks.py numNodes [random/ba]"
                 "networkParameter1 networkParameter2")

    n = int(sys.argv[1])
    network = sys.argv[2]
    p = float(sys.argv[3])
    filename = "network-" + "-".join(network, n, p)

    # check which network type was given
    if (network == "random"):
        G = nx.gnp_random_graph(n, p, directed=True)
        nx.write_gexf(G, filename + ".gexf")
    elif (network == "ba"):
        G = nx.barabasi_albert_graph(n, p)
        nx.write_gexf(G, filename + ".gexf")
    else:
        raise NameError("Unidentified network type given.")
