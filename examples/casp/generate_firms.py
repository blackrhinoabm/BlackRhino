#!/usr/bin/env python
# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------
if __name__ == '__main__':
	import sys
	# sys.path.append('src/')
	import random

	if (len(sys.argv) != 3):
			print "Usage: ./generate_firms.py num_firms directory"
			sys.exit()

	num_firms = int(sys.argv[1])

	for i in range(num_firms):
		fileName = sys.argv[2] + "firm-"
		# the following code ensures leading zeros so filenames will be in the right order
		# for python to read in. Also, bank names are sorted properly in activeBanks of madfimas
		# this code is ugly, but works...
		if (num_firms <= 9):
			fileName += "%01d" % (i,)
		if (num_firms > 9):
			fileName += "%02d" % (i,)
		if (num_firms > 99):
			fileName += "%03d" % (i,)
		if (num_firms > 999):
			fileName += "%04d" % (i,)
		fileName += ".xml"
		outFile = open(fileName,  'w')

		if (i < 1):

			# value_theta = random.uniform(3,10)

			text = "<firm identifier='firm-" + str(i) + "'>\n"
			text = text + "    <parameter type='parameters' name='domicile' value='" + "0" + "'></parameter>\n"
			text = text + "    <parameter type='state_variables' name='dividend_firm' value='" + "6" + "' validity='0-1000'></parameter>\n"
			text = text + "    <parameter type='state_variables' name='success_probability_firm' value='" + "0.9" + "' validity='0-1000'></parameter>\n"
			text = text + "</firm>\n"

		else:
			# value_theta = random.uniform(3, 10)

			text = "<firm identifier='firm-" + str(i) + "'>\n"
			text = text + "    <parameter type='parameters' name='domicile' value='" + "1" + "' validity='0-1000'></parameter>\n"
			text = text + "    <parameter type='state_variables' name='dividend_firm' value='" + "8" + "' validity='0-1000'></parameter>\n"
			text = text + "    <parameter type='state_variables' name='success_probability_firm' value='" + "0.8" + "' validity='0-1000'></parameter>\n"
			text = text + "</firm>\n"


		outFile.write(text)
		outFile.close()
