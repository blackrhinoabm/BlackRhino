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
from xml.etree.ElementTree import Element, SubElement, tostring

sys.path.append('src/')


if __name__ == '__main__':

    if (len(sys.argv) != 3):
        sys.exit("Usage: ./generate_banks.py num_banks directory")

    num_banks = int(sys.argv[1])

    for i in range(num_banks):
        file_number = str(i).zfill(len(str(num_banks)))  # Add leading zeros
        filename = sys.argv[2] + "bank-" + file_number + ".xml"

        # Build xml
        root = ET.Element("root", identifier=str(i))
        ET.SubElement(root, "parameter", type="changing", name="pReal",
                      value="0.998", validity='0-1000')
        ET.SubElement(root, "parameter", type="changing", name="rhoReal",
                      value="0.02", validity='0-1000')
        ET.SubElement(root, "parameter", type="changing", name="pFinancial",
                      value="1.0", validity='0-1000')
        ET.SubElement(root, "parameter", type="changing", name="rhoFinancial",
                      value="0.0", validity='0-1000')
        ET.SubElement(root, "parameter", type="changing", name="thetaBank",
                      value="1.67", validity='0-1000')
        ET.SubElement(root, "parameter", type="changing", name="xiBank",
                      value="1.0", validity='0-1000')
        ET.SubElement(root, "parameter", type="changing", name="gammaBank",
                      value="2.0", validity='0-1000')

        # Save xml
        tree = ET.ElementTree(root)
        tree.write(filename)
