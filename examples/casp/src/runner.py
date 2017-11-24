#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2016 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)
Pawel Fiedor (pawel@fiedor.eu)

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

from updater import Updater


#-------------------------------------------------------------------------
#
# class Runner
#
#-------------------------------------------------------------------------
class Runner(object):
#	from environment import Environment

	#
	# VARIABLES
	#

	#
	# METHODS
	#
	#-------------------------------------------------------------------------
	# __init__
	#-------------------------------------------------------------------------
	def __init__(self, environment):
		pass
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# initialize()
	#-------------------------------------------------------------------------
	def initialize(self,  environment):
		self.environment = environment
		self.updater = Updater(self.environment)
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# do_run
	#-------------------------------------------------------------------------
	def do_run(self, measurement,  debug):
		# loop over all time steps and do the updating
		for i in range(self.environment.parameters.num_sweeps):
			# the update step
			self.updater.do_update(self.environment, i, debug)

			# do the measurement
			# measurement.do_measurement(self.environment.banks)
	#------------------------------------------------------------------------
