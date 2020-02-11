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

import networkx as nx
import logging

#-------------------------------------------------------------------------
#
# class Network
#
#-------------------------------------------------------------------------
class Network(object):
	#
	# VARIABLES
	#
	identifier = ""
	contracts = nx.DiGraph()
	exposures = nx.DiGraph()
	
	#
	# METHODS
	#
	#-------------------------------------------------------------------------
	# __init__
	#-------------------------------------------------------------------------
	def __init__(self,  identifier):
		self.identifier = identifier
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# initialize_networks
	#-------------------------------------------------------------------------    
	def initialize_networks(self,  environment):
		# TODO: I thought this line should just be contracts = nx.DiGraph()
		# but without the self., no interbank trades happen in the simulations.
		# beats me, why...
		self.contracts = nx.DiGraph()
		
		#
		# read in the network structure
		# 
		if (environment.parameters.graphType == "list"):
		# networks that are read from files
			try:
				# the network of contracts is directed, as the willingness to lend is not necessarily mutual
				contracts = nx.read_weighted_edgelist(str(environment.parameters.contractsNetworkFile) + ".list").to_directed()
				logging.info("  read network of contracts: %s",  environment.parameters.contractsNetworkFile)
			except:
				logging.error("    ERROR: no .list contractsNetworkFile found: %s",  environment.parameters.contractsNetworkFile)
				logging.error("    ERROR: check your %s.xml file.",  environment.parameters.identifier)
			
		if (environment.parameters.graphType == "gexf"):
		# networks that are read from files
			try:
				# the network of contracts is directed, as the willingness to lend is not neccessarily mutual
				contracts = nx.read_gexf(str(environment.parameters.contractsNetworkFile) + ".gexf").to_directed()
				logging.info("  read network of contracts: %s",  environment.parameters.contractsNetworkFile)
			except:
				logging.error("    ERROR: no .gexf contractsNetworkFile found: %s",  environment.parameters.contractsNetworkFile)
				logging.error("    ERROR: check your %s.xml file.", environment.parameters.identifier)
		
		# first ensure that all nodes are in self.contracts and self.exposures
		for bank in environment.banks:
			self.contracts.add_node(bank)
			self.exposures.add_node(bank)
		
		# create the network of contracts by looping over all edges in contracts
		# find the node with the appropriate identifier in self.contracts and add the 
		# edge to the network
		for u, v, edata in contracts.edges(data=True):
			try:
				link_weight = edata['weight']
			except:
				link_weight = 1.0
			for node in self.contracts:
				if (node.identifier == str(u)):
					from_node = node
				if (node.identifier == str(v)):
					to_node = node
			try: # if the edge cannot be added, the from or to node is missing and something funny is going on
				self.contracts.add_edge(from_node,  to_node,  weight=link_weight)
			except: # if that happens, debug which node is the problem
				try:
					_from = from_node.identifier
				except:
					_from = "nan"
				try:
					_to = to_node.identifier
				except:
					_to = "nan"
				# and do some logging
				logging.error("    ERROR: add_edge failed, from_node=%s, to_node=%s",  str(_from),  str(_to))
		
		# after we are done, give a short message to the log
		logging.info("  created the network of contracts with %s nodes and %s links",  str(len(self.contracts.nodes())), str(len(self.contracts.edges())))
		logging.info("  created the network of exposures with %s nodes",  str(len(self.exposures.nodes())) )
	#-------------------------------------------------------------------------    


#
# INTERBANK ROUTINES  
#

	#-------------------------------------------------------------------------
	# do_interbank_trades
	#-------------------------------------------------------------------------
	def do_interbank_trades(self,  state):
		from random import shuffle
		activeBanks = []
		neighbors = []
		
		# we are doing interbank trades, so the interest rate is fixed, as is the timeOfDefault and maturity
		interest = state.rb
		maturity = state.interbankLoanMaturity
		timeOfDefault = -1
		
		# we want to loop randomly over all nodes in order to avoid effects originating in the ordering of banks
		banks = self.contracts.nodes() # shuffle cannot deal with the return from a function
		shuffle(banks)
		for bank in banks: # loop over all banks in the list of shuffled banks
			#print str(bank.identifier) + " " + str(bank.Lp)
			neighbors = self.contracts.neighbors(bank) # we also want to loop over the neighbors in a random ordering
			shuffle(neighbors)
			for neighbor in neighbors:
				# now check if we have a match
				if (bank.Lp * neighbor.Lp < 0.0) and (bank.active > -1) and (neighbor.active > -1):
					#this harmless line implies that there is rationing in the model
					value = min(abs(bank.Lp),  abs(neighbor.Lp))
					
					if bank.Lp > 0.0: # bank has excess liquidity
						# add transactions
						bank.add_transaction("L", int(bank.identifier),  int(neighbor.identifier),  value,  interest,  maturity,  timeOfDefault)
						neighbor.add_transaction("L", int(bank.identifier),  int(neighbor.identifier),  value,  interest,  maturity,  timeOfDefault)
						# update network of exposures
						self.update_network_of_exposures(bank,  neighbor,  value)
						# and change Lp accordingly
						bank.Lp -= value
						neighbor.Lp += value
					if neighbor.Lp > 0.0: # neighbor has excess liquidity
						# add transactions
						bank.add_transaction("L", int(neighbor.identifier),  int(bank.identifier), value,  interest,  maturity,  timeOfDefault)
						neighbor.add_transaction("L", int(neighbor.identifier),  int(bank.identifier), value,  interest,  maturity,  timeOfDefault)
						# update network of exposures
						self.update_network_of_exposures(neighbor,  bank,  value)
						# and change Lp accordingly
						neighbor.Lp -= value
						bank.Lp += value
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# update_network_of_exposures
	#-------------------------------------------------------------------------
	def update_network_of_exposures(self,  nodeFrom,  nodeTo,  weight):
		# add_weighted_edges_from overwrites the currently set weight
		# hence, the weight has to be recalculated before setting it
		current_weight = 0.0
		try:
			current_weight = self.exposures[nodeFrom][nodeTo]['weight']
		except:
			current_weight  = 0.0
		
		new_weight = current_weight + weight
		self.exposures.add_weighted_edges_from([(nodeFrom,nodeTo,  float(new_weight))])
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# remove_inactive_bank()
	#-------------------------------------------------------------------------
	def remove_inactive_bank(self,  bank,  time):
		try:
			# this removes the bank from the network of contracts and makes it impossible to trade with 
			# in the next update step
			self.contracts.remove_node(bank)
		except: # if the bank has been removed in the current update step, remove_node(bank) throws an exception
			pass 
		
		try:
			self.remove_defaulted_loans(bank,  time)
		except: # if the bank has been removed in the current update step, remove_node(bank) throws an exception
			pass 
		
		try:
			self.exposures.remove_node(bank)
		except:
			pass
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# def remove_defaulted_loans(bank):
	#-------------------------------------------------------------------------
	def remove_defaulted_loans(self, bank,  time):
		try:
			num_neighbors = len(self.exposures[bank])
		except:
			num_neighbors = 0
		
		if num_neighbors > 0:
			logging.info("      time: %s: contagion originating from bank %s to %s neighbors", time, bank.identifier,  num_neighbors)
		
		# if remove_node does not throw an exception, also remove the bank from the network of exposures
		for neighbor in self.exposures[bank]:
			loss = self.exposures[bank][neighbor]['weight']
			neighbor.reduce_banking_capital(loss)
			neighbor.check_solvency("info")
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# liquidate_due_transactions
	#-------------------------------------------------------------------------
	def liquidate_due_transactions(self,  bank):
		# the cheap and easy way to remove all links to a given node 
		# is to remove the node itself.
		# TODO: this method does not work for interbank loans of longer maturities
		try:
			self.exposures.remove_node(bank)
		except:
			pass
	#-------------------------------------------------------------------------


#
# HELPER ROUTINES
#
	#-------------------------------------------------------------------------
	# __str()__
	#-------------------------------------------------------------------------
	def __str__(self):
		text = "<network type='contracts' identifier='" + self.identifier + "'>\n"
		for node in self.contracts.nodes():
			text += "  <node id='" + node.identifier + "'>\n"
		for edge in self.contracts.edges():
			text += "  <edge from='" + edge[0].identifier+ "' to='" + edge[1].identifier+ "'>\n"
		text += "</network>\n"
		
		text += "<network type='exposures' identifier='" + self.identifier + "'>\n"
		for node in self.exposures.nodes():
			text += "  <node id='" + node.identifier + "'>\n"
		for fromID,  toID,  edata in self.exposures.edges(data=True):
			text += "  <edge from='" + fromID.identifier + "' to='" + toID.identifier + "' weight='" + str(edata['weight']) + "'>\n"
		text += "</network>\n"
		
		return text
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# write_network_of_exposures
	#-------------------------------------------------------------------------
	def write_network_of_exposures(self, time):
		nx.write_edgelist(self.exposures.to_directed(), "exposures-" + self.identifier + "-" + str(time) + ".list")
	#-------------------------------------------------------------------------
