#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Robustness check for Agent-Based Models
(conceivably other models as well)
across the whole of the multidimensional
parameter space.

Author: Pawel Fiedor (pawel@fiedor.eu)
        Co-Pierre Georg (cogeorg@gmail.com)

Version: 0.2

Date of last update: 19-11-2015 (Cape Town)

"""

# Libraries
#import sys
#import random
#import subprocess
#import importlib
#import operator
import math
import csv
import time
import glob
import os

# ---------------------------------------------------------------------------
#
# CLASS Goodness
#
# ---------------------------------------------------------------------------


class Goodness(object):
    __version__ = 0.2

    # Output type, minima, maxima, column in the input files,
    # hypothesis value (H0: x = x0), and values received from the appropriate computations
    # One element in a list for every parameter tested
    out_type = []
    out_low = []
    out_high = []
    out_column = []
    out_target = []
    out_gotten = []
    # Distance type to be used - either Euclidean ('euclid') or squared Euclidean ('squared'):
    # https://en.wikipedia.org/wiki/Euclidean_distance
    dist_type = ""
    # Folder in which the input .csv files are saved (WE USE ALL CSV IN THAT FOLDER)
    folder_name = ""
    # Whether there are headers in the files to read
    headers = ""

    # This reads the config file with the setup
    def read_config(self, FileName):
        """
        Reads config file (xml)

        Example of a config file below:

        <config identifier="test">
            <parameter type="output" kind="float" column="2" low="0.0" high="4.0" target="2.0"></parameter>
            <parameter type="output" kind="float" column="1" low="0.0" high="4.0" target="2.0"></parameter>
            <parameter type="output" kind="comp" column="3-2" low="0.0" high="4.0" target="0.0"></parameter>
            <parameter type="distance" kind="euclid"></parameter>
            <parameter type="folder" name="samples\\goodness" headers="yes"></parameter>
        </config>

        type output is the parameter space, kind can be integer or float, followed by column in the csv files
        minima, maxima, and the hypothesis value

        If minima and maxima are to be read from samples, then put "-inf" for low parameter and "inf" for high

        !!!
        Other hypothesis different than x0=a we may also check if x0>=x1 (one output is bigger than other)
        To do that use output with kind "comp", in column put "a-b" where a and b are integers representing
        column numbers for a hypothesis a>=b, always keep low="0.0" and target="0.0" for this hypothesis
        For high use any positive real number, if there is only this one hypothesis this is irrelevant
        If there are other hypothesis being tested this constitutes the weight with retards to other
        hypotheses, where weights of others are proportional to the max{(high-target),(target-low)} values.
        !!!

        """

        # Make the variables global, as we use them outside the function
        global out_type
        global out_low
        global out_high
        global out_column
        global out_target
        global dist_type
        global folder_name
        global headers

        # Align the variables with the class variables
        out_type = self.out_type
        out_low = self.out_low
        out_high = self.out_high
        out_column = self.out_column
        out_target = self.out_target
        dist_type = self.dist_type
        folder_name = self.folder_name
        headers = self.headers

        # Open the file
        from xml.etree import ElementTree
        xmlText = open(FileName).read()

        element = ElementTree.XML(xmlText)

        # Loop over all entries in the xml file, getting all the required values
        for subelement in element:
            if (subelement.attrib['type'] == 'folder'):
                folder_name = subelement.attrib['name']
                headers = subelement.attrib['heads']
            elif (subelement.attrib['type'] == 'output'):
                if (subelement.attrib['kind'] == 'integer'):
                    out_type.append("int")
                    out_column.append(int(subelement.attrib['column']))
                    if subelement.attrib['low'] == "-inf":
                        out_low.append("-inf")
                    else:
                        out_low.append(int(subelement.attrib['low']))
                    if subelement.attrib['high'] == "inf":
                        out_high.append("inf")
                    else:
                        out_high.append(int(subelement.attrib['high']))
                    out_target.append(int(subelement.attrib['target']))
                elif (subelement.attrib['kind'] == 'float'):
                    out_type.append("float")
                    out_column.append(int(subelement.attrib['column']))
                    if subelement.attrib['low'] == "-inf":
                        out_low.append("-inf")
                    else:
                        out_low.append(float(subelement.attrib['low']))
                    if subelement.attrib['high'] == "inf":
                        out_high.append("inf")
                    else:
                        out_high.append(float(subelement.attrib['high']))
                    out_target.append(float(subelement.attrib['target']))
                elif (subelement.attrib['kind'] == 'comp'):
                    out_type.append("comp")
                    out_column.append(subelement.attrib['column'])
                    out_low.append(float(subelement.attrib['low']))
                    out_high.append(float(subelement.attrib['high']))
                    out_target.append(float(subelement.attrib['target']))
                else:
                    print("Error reading config file.")
            elif (subelement.attrib['type'] == 'distance'):
                dist_type = subelement.attrib['kind']
            else:
                print("Error reading config file.")

    # Writes CSV file with the data needed to collate results from parallel runs [case for single output]
    def write_output_one(self, FileName, inter, leng, goood):
        with open(FileName, 'w') as f:
            csvWriter = csv.writer(f, lineterminator='\n')
            csvWriter.writerow(['Aggregate sample difference', "Sample size", "Goodness"])
            out_row = []
            out_row.append(inter)
            out_row.append(leng)
            out_row.append(goood)
            csvWriter.writerow(out_row)

    # Writes CSV file with the data needed to collate results from parallel runs [case for multiple outputs]
    def write_output_mult(self, FileName, inter, max_e, leng, goood):
        with open(FileName, 'w') as f:
            csvWriter = csv.writer(f, lineterminator='\n')
            csvWriter.writerow(['Aggregate sample difference', 'Max Euclidean difference', "Sample size", "Goodness"])
            out_row = []
            out_row.append(inter)
            out_row.append(max_e)
            out_row.append(leng)
            out_row.append(goood)
            csvWriter.writerow(out_row)

    # Gets the config of the csv file
    def getDialect(self, aFile):

        #import csv
        csvDialect = csv.Sniffer().sniff(aFile.readline())

        return csvDialect

    # Reads the CSV file into needed data
    def read_output_mult(self, FileName):
        with open(FileName, 'r') as f:
            csvDialect = self.getDialect(f)
            f.seek(0)
            csvReader = csv.reader(f, dialect=csvDialect)
            if headers == "yes":
                next(csvReader, None)
            outp = []
            for row in csvReader:
                outp.append(row)
            return outp

    # Reads all files in the specified directory, and reads the samples
    def read_directory(self):
        temp_folder = os.getcwd()  # This is to get working directory in order at the end of the function
        os.chdir(folder_name)
        for filez in glob.glob("*.csv"):
            temp_out = self.read_output_mult(filez)
            for row in temp_out:
                temp_out_two = []
                for iterator in out_column:
                    temp_column = 0
                    if type(iterator) == str:
                        temp_three = 0.0
                        if (float(row[int(iterator.split("-")[0])-1]) - float(row[int(iterator.split("-")[1])-1])) >= 0:
                            temp_three = 0.0
                        else:
                            temp_three = self.out_high[out_column.index(iterator)]
                        temp_out_two.append(temp_three)
                    elif type(iterator) == int:
                        try:
                            temp_column = self.out_column.index(iterator)
                            if self.out_type[temp_column] == "int":
                                temp_out_two.append(int(row[iterator-1]))
                            else:
                                temp_out_two.append(float(row[iterator-1]))
                        except:
                            temp_out_two.append(float(row[iterator-1]))
                self.out_gotten.append(temp_out_two)
        os.chdir(temp_folder)  # This is to get working directory in order at the end of the function

    # Check if maxima and minima are to be read from the config or from data
    def check_min_max(self):
        for x in range(0, len(out_low)):
            if self.out_low[x] == "-inf":
                self.out_low[x] = min([sublist[x] for sublist in self.out_gotten])
        for y in range(0, len(out_high)):
            if self.out_high[y] == "inf":
                self.out_high[y] = max([sublist[y] for sublist in self.out_gotten])

    # Main loop, reads config, reads the samples, and calculates the goodness
    def do_run(self, config_name):
        self.read_config(str(config_name))
        self.read_directory()
        self.check_min_max()
        self.calculate_goodness()

    def calculate_goodness(self):
        # Here we calculate the goodness of the model using either Euclidean
        # or squared Euclidean distance from the hypothesis
        if dist_type == "euclid":

            if len(out_type) == 1:
                # Calculating goodness for one output
                # First, calculate the maximum possible difference for normalisation
                max_diff = 0
                if (out_high[0] - out_target[0]) >= (out_target[0] - out_low[0]):
                    max_diff = abs(out_high[0] - out_target[0])
                else:
                    max_diff = abs(out_target[0] - out_low[0])
                # Then, calculate the sum of normalised differences between target in the hypothesis and the
                # obtained results
                intermediate=0
                for x in range(0, len(self.out_gotten)):
                    intermediate += abs(float(self.out_gotten[x][0]) - out_target[0]) / max_diff
                # Finally, we average the results (with respect to sample length)
                # and get the goodness of the model, which is printed out and saved in the decomposed form
                goodness = 0
                goodness = 1 - ( intermediate / float(len(self.out_gotten)) )
                # We write the output to .csv file for collating in case of parallel runs, the filename is unique
                # based on system time
                self.write_output_one('goodness_' + "".join(i for i in str(time.time()) if not ord(i)==46) + '.csv', intermediate, len(self.out_gotten), goodness)
            else:
                # Calculating goodness for multiple outputs
                # First, calculate the maximum possible difference for normalisation [multidimensional]
                max_diff = []
                for x in range(0, len(out_type)):
                    if (out_high[x] - out_target[x]) >= (out_target[x] - out_low[x]):
                        max_diff.append(abs(out_high[x] - out_target[x]))
                    else:
                        max_diff.append(abs(out_target[x] - out_low[x]))
                # Then, calculate the sum of normalised differences between target in the hypothesis and the obtained results [multidimensional]
                intermediate=0
                for x in range(0, len(self.out_gotten)):
                    anotherinter = 0
                    for y in range(0, len(self.out_gotten[x])):
                        anotherinter += (float(self.out_gotten[x][y]) - out_target[y]) ** 2
                    intermediate += math.sqrt(anotherinter)
                goodness = 0
                # Calculate the Euclidean maximum for normalisation
                max_euclid = 0
                for x in range(0, len(out_type)):
                    max_euclid += max_diff[x] ** 2
                max_euclid = math.sqrt(max_euclid)
                # Finally, calculate goodness
                goodness = 1 - ( intermediate / ( max_euclid * float(len(self.out_gotten) ) ) )
                # We write the output to .csv file for collating in case of parallel runs, the filename is unique based on system time
                self.write_output_mult('goodness_' + "".join(i for i in str(time.time()) if not ord(i)==46) + '.csv', intermediate, max_euclid, len(self.out_gotten), goodness)

        elif dist_type == "squared":  # NOT A METRIC!

            if len(out_type) == 1:
                # Calculating goodness for one output
                # First, calculate the maximum possible (squared) difference for normalisation
                max_diff = 0
                if (out_high[0] - out_target[0]) >= (out_target[0] - out_low[0]):
                    max_diff = abs(out_high[0] - out_target[0]) ** 2
                else:
                    max_diff = abs(out_target[0] - out_low[0]) ** 2
                #  Then, calculate the sum of normalised (squared) differences between target in the hypothesis and the obtained results
                intermediate=0
                for x in range(0, len(self.out_gotten)):
                    intermediate += (abs(float(self.out_gotten[x][0]) - out_target[0]) ** 2) / max_diff
                # Finally, we average the results (with respect to sample length) and get the goodness of the model, which is printed out and saved in the decomposed form
                goodness = 0
                goodness = 1 - ( intermediate / float(len(self.out_gotten) ) )
                # We write the output to .csv file for collating in case of parallel runs, the filename is unique based on system time
                self.write_output_one('goodness_' + "".join(i for i in str(time.time()) if not ord(i)==46) + '.csv', intermediate, len(self.out_gotten), goodness)
            else:
                # Calculating goodness for multiple outputs
                # First, calculate the maximum possible difference for normalisation [multidimensional]
                max_diff = []
                for x in range(0, len(out_type)):
                    if (out_high[x] - out_target[x]) >= (out_target[x] - out_low[x]):
                        max_diff.append((abs(out_high[x] - out_target[x]))**2)
                    else:
                        max_diff.append((abs(out_target[x] - out_low[x]))**2)
                # Then, calculate the sum of (squared) differences between target in the hypothesis and the obtained results [multidimensional]
                intermediate=0
                for x in range(0, len(self.out_gotten)):
                    anotherinter = 0
                    for y in range(0, len(self.out_gotten[x])):
                        anotherinter += (float(self.out_gotten[x][y]) - out_target[y]) ** 2
                    intermediate += anotherinter
                goodness = 0
                # Calculate the Euclidean maximum for normalisation
                max_euclid = 0
                for x in range(0, len(out_type)):
                    max_euclid += max_diff[x]
                # Finally, calculate goodness
                goodness = 1 - ( intermediate / ( max_euclid * float(len(self.out_gotten) ) ) )
                # We write the output to .csv file for collating in case of parallel runs, the filename is unique based on system time
                self.write_output_mult('goodness_' + "".join(i for i in str(time.time()) if not ord(i)==46) + '.csv', intermediate, max_euclid, len(self.out_gotten), goodness)
        else:
            print("Wrong distance type entered (should be euclid for Euclidean or squared for squared Euclidean).")
