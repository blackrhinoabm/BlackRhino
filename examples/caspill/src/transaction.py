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
#
# class Transaction
#
#-------------------------------------------------------------------------
class Transaction(object):
	#
	# VARIABLES
	#
	transactionType = ""
	transactionFrom = 0
	transactionTo = 0
	transactionValue = 0.0
	transactionInterest = 0.0
	transactionMaturity = 0
	# this is used only for loans I, and will be > 0 for defaulting loans. with each update step, it is reduced by 1
	# if timeOfDefault == 0: loan defaults
	transactionTimeOfDefault = -1 


	#
	# METHODS
	#
	#-------------------------------------------------------------------------
	# __init__
	#-------------------------------------------------------------------------
	def __init__(self):
		pass
	#------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# this_transaction(transactionType, 
	#                  transactionFrom, 
	#                  transactionTo, 
	#                  transactionValue, 
	#                  transactionInterest, 
	#                  transactionMaturity, 
	#                  transactionTimeOfDefault)
	#-------------------------------------------------------------------------
	def this_transaction(self,  transactionType,  transactionFrom,  transactionTo,  transactionValue,  transactionInterest ,  transactionMaturity, transactionTimeOfDefault):
		self.transactionType = transactionType
		# the convention used is that values are positive
		if transactionValue >= 0:
			self.transactionFrom = transactionFrom
			self.transactionTo = transactionTo
		else: # negative values reverse direction and delete sign
			self.transactionFrom = transactionTo
			self.transactionTo = transactionFrom
			transactionValue = abs(transactionValue)
		self.transactionValue = transactionValue
		self.transactionInterest = transactionInterest
		self.transactionMaturity = transactionMaturity
		self.transactionTimeOfDefault = transactionTimeOfDefault
	#------------------------------------------------------------------------- 


	#-------------------------------------------------------------------------
	# print_transaction()
	#-------------------------------------------------------------------------
	def print_transaction(self):
		print "        <transaction type='" + self.transactionType + "'>"
		print "            <property type='from' value='" + str(self.transactionFrom) + "'></property>"
		print "            <property type='to' value='" + str(self.transactionTo) + "'></property>"
		print "            <property type='value' value='" + str(self.transactionValue) + "'></property>"
		print "            <property type='interest' value='" + str(self.transactionInterest) + "'></property>"
		print "            <property type='maturity' value='" + str(self.transactionMaturity) + "'></property>"
		print "            <property type='timeOfDefault' value='" + str(self.transactionTimeOfDefault) + "'></property>"
		print "        </transaction>"
	#-------------------------------------------------------------------------


	#-------------------------------------------------------------------------
	# write_transaction()
	#-------------------------------------------------------------------------
	def write_transaction(self):
		text =  "        <transaction type='" + self.transactionType + "'>\n"
		text += "            <property type='from' value='" + str(self.transactionFrom) + "'></property>\n"
		text += "            <property type='to' value='" + str(self.transactionTo) + "'></property>\n"
		text += "            <property type='value' value='" + str(self.transactionValue) + "'></property>\n"
		text += "            <property type='interest' value='" + str(self.transactionInterest) + "'></property>\n"
		text += "            <property type='maturity' value='" + str(self.transactionMaturity) + "'></property>\n"
		text += "            <property type='timeOfDefault' value='" + str(self.transactionTimeOfDefault) + "'></property>\n"
		text += "        </transaction>\n"
		
		return text
	#-------------------------------------------------------------------------
