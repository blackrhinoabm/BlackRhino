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

	if (len(sys.argv) != 3):
			print "Usage: ./generate_banks.py numBanks directory"
			sys.exit()

	numBanks = int(sys.argv[1])
	
	for i in range(numBanks):
		fileName = sys.argv[2] + "bank-"
		# the following code ensures leading zeros so filenames will be in the right order
		# for python to read in. Also, bank names are sorted properly in activeBanks of madfimas
		# this code is ugly, but works...
		if (numBanks <= 9):
			fileName += "%01d" % (i,)
		if (numBanks > 9):
			fileName += "%02d" % (i,)
		if (numBanks > 99):
			fileName += "%03d" % (i,)
		if (numBanks > 999):
			fileName += "%04d" % (i,)
		fileName += ".xml"
		outFile = open(fileName,  'w')
		
		text = "<bank identifier='" + str(i) + "'>\n"
		text = text + "    <parameter type='changing' name='pReal' value='" + "0.998" + "' validity='0-1000'></parameter>\n"
		text = text + "    <parameter type='changing' name='rhoReal' value='" + "0.02" + "' validity='0-1000'></parameter>\n"
		text = text + "    <parameter type='changing' name='pFinancial' value='" + "1.0" + "' validity='0-1000'></parameter>\n"
		text = text + "    <parameter type='changing' name='rhoFinancial' value='" + "0.0" + "' validity='0-1000'></parameter>\n"
		text = text + "    <parameter type='changing' name='thetaBank' value='" + "1.67" + "' validity='0-1000'></parameter>\n"
		text = text + "    <parameter type='changing' name='xiBank' value='" + "1.0" + "' validity='0-1000'></parameter>\n"
		text = text + "    <parameter type='changing' name='gammaBank' value='2.0' validity='0-1000'></parameter>\n"
		text = text + "</bank>\n"
		outFile.write(text)
		outFile.close()
