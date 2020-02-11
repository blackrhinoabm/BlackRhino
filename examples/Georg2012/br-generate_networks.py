#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


#-------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------
if __name__ == '__main__':
	import sys
	sys.path.append('src/')
	import networkx as nx

	if (len(sys.argv) != 5):
		print "Usage: ./generate_networks.py numNodes [random/ba] networkParameter1 networkParameter2"
		sys.exit()

	# check which network type was given
	if (sys.argv[2] == "random"):
		# generate a random network
		G = nx.DiGraph()
		G = nx.gnp_random_graph(int(sys.argv[1]), float(sys.argv[3]),  directed=True)
		fileName = "network-" + str(sys.argv[2]) + "-" + str(sys.argv[1]) + "-" + str(sys.argv[3])
		nx.write_gexf(G,  fileName + ".gexf")
	if (sys.argv[2] == "ba"):
		# generate a random network
		G = nx.DiGraph()
		G = nx.barabasi_albert_graph(int(sys.argv[1]), int(sys.argv[3]))
		fileName = "network-" + str(sys.argv[2]) + "-" + str(sys.argv[1]) + "-" + str(sys.argv[3])
		nx.write_gexf(G,  fileName + ".gexf")
