#!/usr/bin/env python
# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------
if __name__ == '__main__':
	import sys
	sys.path.append('src/')
	import random

	if (len(sys.argv) != 3):
			print "Usage: ./generate_funds.py num_funds directory"
			sys.exit()

	num_funds = int(sys.argv[1])

	for i in range(num_funds):
		fileName = sys.argv[2] + "fund-"
		# the following code ensures leading zeros so filenames will be in the right order
		# for python to read in. Also, bank names are sorted properly in activeBanks of madfimas
		# this code is ugly, but works...
		if (num_funds <= 9):
			fileName += "%01d" % (i,)
		if (num_funds > 9):
			fileName += "%02d" % (i,)
		if (num_funds > 99):
			fileName += "%03d" % (i,)
		if (num_funds > 999):
			fileName += "%04d" % (i,)
		fileName += ".xml"
		outFile = open(fileName,  'w')

		if (i < 20):

			value_theta = random.uniform(3,10)

			text = "<fund identifier='" + str(i) + "'>\n"
			text = text + "    <parameter type='parameters' name='domicile' value='" + "0" + "'></parameter>\n"
			text = text + "    <parameter type='state_variables' name='theta' value='" + str(value_theta) + "' validity='0-1000'></parameter>\n"
			text = text + "</fund>\n"

		else:
			value_theta = random.uniform(0, 5)

			text = "<fund identifier='" + str(i) + "'>\n"
			text = text + "    <parameter type='parameters' name='domicile' value='" + "1" + "' validity='0-1000'></parameter>\n"
			text = text + "    <parameter type='state_variables' name='theta' value='" + str(value_theta) + "' validity='0-1000'></parameter>\n"
			text = text + "</fund>\n"


		outFile.write(text)
		outFile.close()
