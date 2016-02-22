#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
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

import logging
import os
from abm_template.src.baseconfig import BaseConfig


# -------------------------------------------------------------------------
#
#  class Environment
#
# -------------------------------------------------------------------------
class Environment(BaseConfig):
    # from state import State
    # from parameters import Parameters

    #
    # VARIABLES
    #
    identifier = ""

    # parameters = Parameters()
    # state = State()
    banks = []
    households = []
    firms = []
    # assets = []

    static_parameters = {}
    static_parameters["num_simulations"] = 0
    static_parameters["num_sweeps"] = 0
    static_parameters["num_banks"] = 0
    static_parameters["bank_directory"] = ""
    static_parameters["firm_directory"] = ""
    static_parameters["household_directory"] = ""
    # parameters for the networks
    static_parameters["graphType"] = ""
    static_parameters["graphParameter1"] = 0.0
    static_parameters["graphParameter2"] = 0.0
    static_parameters["contractsNetworkFile"] = ""
    # the array of parameters that changes during the simulation
    # parameters = []
    variable_parameters = {}

    # state _ variables
    #
    # VARIABLES
    #
    # parameters determining the cash flow of banks
    static_parameters["interest_rate_loans"] = 0.0  # interest rate on loans
    static_parameters["interest_rate_deposits"] = 0.0  # interest rate on deposits
    # parameters for the central bank
    static_parameters["collateralQuality"] = 0.0  # the fraction of a bank's portfolio that the central bank accepts as collateral
    # firm parameters
    static_parameters["successProbabilityFirms"] = 0.0  # probability of successful credit
    static_parameters["positiveReturnFirms"] = 0.0  # return for a successful credit
    static_parameters["firmLoanMaturity"] = 0.0  # maturity of loans to firms
    # household parameters
    static_parameters["scaleFactorHouseholds"] = 0.0  # scaling factor for deposit fluctuations
    # bank parameters
    static_parameters["dividendLevel"] = 0.0  # dividend level as paid out by banks
    static_parameters["pBank"] = 0.0  # bank's assumed credit success probability
    static_parameters["rhoBank"] = 0.0  # expected return of banks
    static_parameters["pFinancial"] = 0.0  # bank's assumed credit success probability
    static_parameters["rhoFinancial"] = 0.0  # expected return of banks
    static_parameters["thetaBank"] = 0.0  # bank's risk aversion parameter
    static_parameters["xiBank"] = 0.0  # scaling factor for CRRA
    static_parameters["gammaBank"] = 0.0  # fraction of interbank lending in overall balance sheet
    static_parameters["assetNumber"] = 0  # number of assets in the economy
    static_parameters["interbankLoanMaturity"] = 0.0  # the maturity of interbank loans
    # simulation specific parameters
    static_parameters["shockType"] = 0  # type of shock that hits the system in the current state
    static_parameters["liquidationDiscountFactor"] = 0.0  # the discount factor delta in exp(-delta x) when liquidating assets
    static_parameters["riskAversionDiscountFactor"] = 0.0  # the risk aversion discount when there was no default in the previous period
    static_parameters["riskAversionAmplificationFactor"] = 0.0  # the risk aversion amplification when there *was* a default in the previous or current period
    # regulation specific parameters
    static_parameters["r"] = 0.0  # minimum required deposit rate
    static_parameters["sifiSurchargeFactor"] = 1.0  # the surcharge on banking capital that SIFIs have to hold
    static_parameters["liquidityCoverageRatio"] = 0.0  # the fraction of assets that must have a high liquidation value
    static_parameters["netStableFundingRatio"] = 0.0  # the fraction of deposits that must have low volatility
    static_parameters["leverageRatio"] = 0.0  # the minimal ratio of banking capital to total assets
    static_parameters["requiredCapitalRatio"] = 0.08  # the required capital ratio for banks

    # bookkeeping parameters
    static_parameters["insolvencyHistory"] = []  # [num, time] the number of bank insolvencies and when they occured

    # -------------------------------------------------------------------------
    # print_parameters(self)
    # -------------------------------------------------------------------------
    def print_parameters(self):
        print "identifier: " + self.identifier
        print "numSweeps: " + str(self.static_parameters["numSweeps"])
        print "numSimulations: " + str(self.static_parameters["numSimulations"])
        print "numBanks: " + str(self.static_parameters["numBanks"])
        print "graphType: " + str(self.static_parameters["graphType"])
        for key in self.variable_parameters:
            print str(key) + " ; " + str(self.variable_parameters[key]['value']) + " ; " + str(self.variable_parameters[key]['validity'][0]) + "-" + str(self.variable_parameters[key]['validity'][1])
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # add_parameter(self, type, value, validFrom, validTo)
    # -------------------------------------------------------------------------
    def add_parameter(self,  name,  value,  validFrom,  validTo):
        # add the parameter to the stack of parameters
        self.variable_parameters[name] = {'value': value, 'validity': [validFrom, validTo]}
    # -------------------------------------------------------------------------

    def __init__(self,  environment_directory,  identifier):
        self.initialize(environment_directory,  identifier)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        super(Environment, self).set_identifier(_value)

    def get_static_parameters(self):
        return self.static_parameters

    def set_static_parameters(self, _value):
        """
        Class variables: static_parameters
        Local variables: _params
        """
        super(Environment, self).set_static_parameters(_value)

    def get_variable_parameters(self):
        return self.variable_parameters

    def set_variable_parameters(self, _value):
        """
        Class variables: variable_parameters
        Local variables: _params
        """
        super(Environment, self).set_variable_parameters(_value)

    # -------------------------------------------------------------------------
    # __str__
    # -------------------------------------------------------------------------
    def __str__(self):
        text = "<state>\n"
        text += "  <!-- parameters determining the payment flow of banks -->\n"
        text += "  <parameter type='changing' name='rb' value='" + str(self.static_parameters["rb"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='rd' value='" + str(self.static_parameters["interest_rate_deposits"]) + "'></parameter>\n"
        text += "  <!-- parameters for the central bank -->\n"
        text += "  <parameter type='changing' name='collateralQuality' value='" + str(self.static_parameters["collateralQuality"]) + "'></parameter>\n"
        text += "  <!-- firm parameters-->\n"
        text += "  <parameter type='changing' name='successProbabilityFirms' value='" + str(self.static_parameters["successProbabilityFirms"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='positiveReturnFirms' value='" + str(self.static_parameters["positiveReturnFirms"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='firmLoanMaturity' value='" + str(self.static_parameters["firmLoanMaturity"]) + "'></parameter>\n"
        text += "  <!-- household parameters -->\n"
        text += "  <parameter type='changing' name='scaleFactorHouseholds' value='" + str(self.static_parameters["scaleFactorHouseholds"]) + "'></parameter>\n"
        text += "  <!-- bank parameters -->\n"
        text += "  <parameter type='changing' name='dividendLevel' value='" + str(self.static_parameters["dividendLevel"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='pBank' value='" + str(self.static_parameters["pBank"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='rhoBank' value='" + str(self.static_parameters["rhoBank"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='pFinancial' value='" + str(self.static_parameters["pFinancial"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='rhoFinancial' value='" + str(self.static_parameters["rhoFinancial"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='thetaBank' value='" + str(self.static_parameters["thetaBank"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='xiBank' value='" + str(self.static_parameters["xiBank"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='gammaBank' value='" + str(self.static_parameters["gammaBank"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='assetNumber' value='" + str(self.static_parameters["assetNumber"]) + "'></parameter>\n"
        text += "  <!-- simulation specific parameters -->\n"
        text += "  <parameter type='changing' name='shockType' value='" + str(self.static_parameters["shockType"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='liquidationDiscountFactor' value='" + str(self.static_parameters["liquidationDiscountFactor"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='riskAversionDiscountFactor' value='" + str(self.static_parameters["riskAversionDiscountFactor"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='riskAversionAmplificationFactor' value='" + str(self.static_parameters["riskAversionAmplificationFactor"]) + "'></parameter>\n"
        text += "  <!-- regulation specific parameters -->\n"
        text += "  <parameter type='changing' name='r' value='" + str(self.static_parameters["r"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='sifiSurchargeFactor' value='" + str(self.static_parameters["sifiSurchargeFactor"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='liquidityCoverageRatio' value='" + str(self.static_parameters["liquidityCoverageRatio"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='netStableFundingRatio' value='" + str(self.static_parameters["netStableFundingRatio"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='leverageRatio' value='" + str(self.static_parameters["leverageRatio"]) + "'></parameter>\n"
        text += "  <parameter type='changing' name='requiredCapitalRatio' value='" + str(self.static_parameters["requiredCapitalRatio"]) + "'></parameter>\n"
        text += "  <!-- bookkeeping parameters -->\n"
        # find the number of total insolvencies
        numberInsolvencies = 0
        for entry in self.static_parameters["insolvencyHistory"]:
            numberInsolvencies += entry[0]
        text += "  <variable name='numberInsolvencies' value='" + str(numberInsolvencies) + "'></variable>\n"
        text += "</state>\n"

        return text
    # ------------------------------------------------------------------------

    def read_xml_config_file(self, _config_file_name):
        """
        Class variables: identifier, static_parameters, variable_parameters
        Local variables: xmlText, config_file_name, element, subelement, name, value, format_correct, range_from, range_to
        """
        self.read_environment_file(_config_file_name)
        # super(Environment, self).read_xml_config_file(_config_file_name)

    #
    # METHODS
    #

    # -------------------------------------------------------------------------
    # initialize
    # -------------------------------------------------------------------------
    def initialize(self,  environment_directory,  identifier):
        self.identifier = identifier

        self.static_parameters = {}
        self.static_parameters["num_simulations"] = 0
        self.static_parameters["num_sweeps"] = 0
        self.static_parameters["num_banks"] = 0
        self.static_parameters["bank_directory"] = ""
        self.static_parameters["firm_directory"] = ""
        self.static_parameters["household_directory"] = ""
        # parameters for the networks
        self.static_parameters["graphType"] = ""
        self.static_parameters["graphParameter1"] = 0.0
        self.static_parameters["graphParameter2"] = 0.0
        self.static_parameters["contractsNetworkFile"] = ""
        # the array of parameters that changes during the simulation
        # parameters = []
        self.variable_parameters = {}

        # state _ variables
        #
        # VARIABLES
        #
        # parameters determining the cash flow of banks
        self.static_parameters["interest_rate_loans"] = 0.05  # interbank interest rate
        self.static_parameters["interest_rate_deposits"] = 0.01  # interest rate on deposits
        # first, read in the environment file
        environment_filename = environment_directory + identifier + ".xml"
        self.read_environment_file(environment_filename)
        logging.info("  environment file read: %s",  environment_filename)

        # then read in all the banks
        # if (self.static_parameters["bankDirectory"] != ""):
        #    if (self.static_parameters["bankDirectory"] != "none"):  # none is used for tests only
        #        self.initialize_banks_from_files(self.static_parameters["bankDirectory"],  self.get_state(0), 0)
        #        logging.info("  banks read from directory: %s",  self.static_parameters["bankDirectory"])
        # else:
        #    logging.error("ERROR: no bankDirectory given in %s\n",  environment_filename)

        self.initial_assets = 0.0  # the initial assets are needed to determine the fire-sale price in bank.liquidate_assets
        for bank in self.banks:
            self.initial_assets += bank.get_account("I")

        # finally, create the network
        # note: this has to be done after creating the banks, as they are
        # passed to the network as node objects
        #self.network.identifier = self.identifier
        #self.network.initialize_networks(self)

        # when there is a SIFI surcharge, implement it now on the banking capital
        #self.apply_sifi_surcharge()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # read_environment_file
    # -------------------------------------------------------------------------
    def read_environment_file(self,  environmentFilename):
        from xml.etree import ElementTree
        xmlText = open(environmentFilename).read()

        element = ElementTree.XML(xmlText)
        self.identifier = element.attrib['title']

        # self.parameters.identifier = self.identifier

        # loop over all entries in the xml file
        for subelement in element:
            # the first set of parameters will be valid for the whole simulation
            if (subelement.attrib['type'] == 'num_sweeps'):
                self.static_parameters["num_sweeps"] = int(subelement.attrib['value'])
            if (subelement.attrib['type'] == 'num_simulations'):
                self.static_parameters["num_simulations"] = int(subelement.attrib['value'])
            if (subelement.attrib['type'] == 'num_banks'):
                self.static_parameters["num_banks"] = int(subelement.attrib['value'])
            if (subelement.attrib['type'] == 'bank_directory'):
                self.static_parameters["bank_directory"] = str(subelement.attrib['value'])
            if (subelement.attrib['type'] == 'firm_directory'):
                self.static_parameters["firm_directory"] = str(subelement.attrib['value'])
            if (subelement.attrib['type'] == 'household_directory'):
                self.static_parameters["household_directory"] = str(subelement.attrib['value'])
            if (subelement.attrib['type'] == 'graphType'):
                self.static_parameters["graphType"] = str(subelement.attrib['value'])
            if (subelement.attrib['type'] == 'rd'):
                self.static_parameters["interest_rate_deposits"] = float(subelement.attrib['value'])
            if (subelement.attrib['type'] == 'rl'):
                self.static_parameters["interest_rate_loans"] = float(subelement.attrib['value'])
            if (subelement.attrib['type'] == 'contractsNetworkFile'):
                self.static_parameters["contractsNetworkFile"] = str(subelement.attrib['value'])
            # now also read in the parameters that can change during the simulation
            if (subelement.attrib['type'] == 'changing'):
                name = subelement.attrib['name']
                value = float(subelement.attrib['value'])
                validFrom = subelement.attrib['validity'].rsplit("-")[0]
                validTo = subelement.attrib['validity'].rsplit("-")[1]
                self.add_parameter(name,  value,  validFrom, validTo)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_environment_file(file_name)
    # -------------------------------------------------------------------------
    def write_environment_file(self,  file_name):
        out_file = open(file_name + "-check.xml",  'w')

        text = "<environment title='" + self.identifier + "'>\n"
        text += "    <parameter type='numSweeps' value='" + str(self.static_parameters["numSweeps"]) + "'></parameter>\n"
        text += "    <parameter type='numSimulations' value='" + str(self.static_parameters["numSimulations"]) + "'></parameter>\n"
        text += "    <parameter type='numBanks' value='" + str(self.static_parameters["numBanks"]) + "'></parameter>\n"
        text += "    <parameter type='bankDirectory' value='" + str(self.static_parameters["bankDirectory"]) + "'></parameter>\n"
        text += "    <parameter type='graphType' value='" + str(self.static_parameters["graphType"]) + "'></parameter>\n"
        text += "    <parameter type='contractsNetworkFile' value='" + str(self.static_parameters["contractsNetworkFile"]) + "'></parameter>\n"

        for entry in self.variable_parameters:
            text += "    <parameter type='changing' name='" + str(entry) + "' value='" + str(self.variable_parameters[entry]['value']) + "' validity='" + str(self.variable_parameters[entry]['validity'][0]) + "-" + str(self.variable_parameters[entry]['validity'][1]) + "'></parameter>\n"

        text += "</environment>\n"

        out_file.write(text)
        out_file.close()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_banks_from_files
    # banks have to be initialized for each simulation as a number of banks might become inactive
    # in the previous simulation
    # -------------------------------------------------------------------------
    def initialize_banks_from_files(self,  bankDirectory, state,  time):
        from src.bank import Bank
        # this routine is called more than once, so we have to reset the list of banks each time
        self.banks = []

        listing = os.listdir(bankDirectory)
        if (len(listing) != self.static_parameters["numBanks"]):
            logging.error("    ERROR: number of configuration files in %s (=%s) does not match numBanks (=%s)",  bankDirectory,  str(len(listing)), str(self.static_parameters["numBanks"]))

        for infile in listing:
            bank = Bank()
            bank.get_parameters_from_file(bankDirectory + infile,  self.get_state(0),  self.static_parameters["numBanks"], time)
            self.banks.append(bank)
            bank.__del__()  # TODO not sure if this is really safe, but it is better than doing nothing about all those created instances...
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_state
    # -------------------------------------------------------------------------
    def get_state(self,  time):  # TODO bring parameters in same order as in environment file and in state.__str__()
        # for each time t in the simulation return the actual set of parameters
        for parameter in self.variable_parameters:
            validFrom = int(self.variable_parameters[parameter]['validity'][0])
            validTo = int(self.variable_parameters[parameter]['validity'][1])
            if (int(time) >= int(validFrom)) and (int(time) <= int(validTo)):  # we have a valid parameterset
                if parameter == 'rb':
                    self.static_parameters["rb"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'rd':
                    self.static_parameters["interest_rate_deposits"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'r':
                    self.static_parameters["r"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'collateralQuality':
                    self.static_parameters["collateralQuality"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'successProbabilityFirms':
                    self.static_parameters["successProbabilityFirms"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'positiveReturnFirms':
                    self.static_parameters["positiveReturnFirms"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'scaleFactorHouseholds':
                    self.static_parameters["scaleFactorHouseholds"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'dividendLevel':
                    self.static_parameters["dividendLevel"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'pFinancial':
                    self.static_parameters["pFinancial"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'rhoFinancial':
                    self.static_parameters["rhoFinancial"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'pReal':
                    self.static_parameters["pReal"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'rhoReal':
                    self.static_parameters["rhoReal"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'xiBank':
                    self.static_parameters["xiBank"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'thetaBank':
                    self.static_parameters["thetaBank"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'rhoBank':
                    self.static_parameters["rhoBank"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'shockType':
                    self.static_parameters["shockType"] = int(self.variable_parameters[parameter]['value'])
                if parameter == 'gammaBank':
                    self.static_parameters["gammaBank"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'assetNumber':
                    self.static_parameters["assetNumber"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'liquidationDiscountFactor':
                    self.static_parameters["liquidationDiscountFactor"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'riskAversionDiscountFactor':
                    self.static_parameters["riskAversionDiscountFactor"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'riskAversionAmplificationFactor':
                    self.static_parameters["riskAversionAmplificationFactor"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'interbankLoanMaturity':
                    self.static_parameters["interbankLoanMaturity"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'firmLoanMaturity':
                    self.static_parameters["firmLoanMaturity"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'sifiSurchargeFactor':
                    self.static_parameters["sifiSurchargeFactor"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'requiredCapitalRatio':
                    self.static_parameters["requiredCapitalRatio"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'liquidityCoverageRatio':
                    self.static_parameters["liquidityCoverageRatio"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'netStableFundingRatio':
                    self.static_parameters["netStableFundingRatio"] = float(self.variable_parameters[parameter]['value'])
                if parameter == 'leverageRatio':
                    self.static_parameters["leverageRatio"] = float(self.variable_parameters[parameter]['value'])

        #
        # at this point we have all the variables from the parameters[] list
        # now we need to update them to incorporate past defaults to calculate
        # new return and volatility for real and financial assets
        # self.update_state(time)

        return self
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # apply_sifi_surcharge
    # -------------------------------------------------------------------------
    def apply_sifi_surcharge(self):
        degree_sum = 0
        for bank in self.network.contracts:
            degree_sum += float(nx.degree(self.network.contracts)[bank])
        average_degree = float(degree_sum / len(self.network.contracts.nodes()))

        for bank in self.network.contracts:
            # the sifi surcharge is the product of the sifiSurchargeFactor and the connectedness as measured
            # by degree/average_degree
            # the maximum ensures that no bank has to hold less than 1.0 times their banking capital
            sifiSurcharge = max(self.get_state(0).static_parameters["sifiSurchargeFactor"]*(float(nx.degree(self.network.contracts)[bank]) / average_degree), 1.0)
            bank.apply_sifi_surcharge(sifiSurcharge)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # print_state
    # -------------------------------------------------------------------------
    def print_state(self):
        print "rb: " + str(self.static_parameters["rb"])
        print "rd: " + str(self.static_parameters["interest_rate_deposits"])
        print "r: " + str(self.static_parameters["r"])
        print "sifiSurchargeFactor: " + str(self.static_parameters["sifiSurchargeFactor"])
        print "successProbabilityFirms: " + str(self.static_parameters["successProbabilityFirms"])
        print "positiveReturnFirms: " + str(self.static_parameters["positiveReturnFirms"])
        print "scaleFactorHouseholds: " + str(self.static_parameters["scaleFactorHouseholds"])
        print "dividendLevel: " + str(self.static_parameters["dividendLevel"])
        print "shockType: " + str(self.static_parameters["shockType"])
        print "pBank: " + str(self.static_parameters["pBank"])
        print "xiBank: " + str(self.static_parameters["xiBank"])
        print "thetaBank: " + str(self.static_parameters["thetaBank"])
        print "rhoBank: " + str(self.static_parameters["rhoBank"])
        print "gammaBank: " + str(self.static_parameters["gammaBank"])
        print "assetNumber: " + str(self.static_parameters["assetNumber"])
        print "liquidationDiscountFactor: " + str(self.static_parameters["liquidationDiscountFactor"])
        print "interbankLoanMaturity: " + str(self.static_parameters["interbankLoanMaturity"])
        print "firmLoanMaturity: " + str(self.static_parameters["firmLoanMaturity"])
        print "requiredCapitalRatio: " + str(self.static_parameters["requiredCapitalRatio"])
        print "liquidityCoverageRatio: " + str(self.static_parameters["liquidityCoverageRatio"])
        print "netStableFundingRatio: " + str(self.static_parameters["netStableFundingRatio"])
        print "leverageRatio: " + str(self.static_parameters["leverageRatio"])
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # addInsolvencyToHistory(time)
    # -------------------------------------------------------------------------
    def addInsolvencyToHistory(self, time):
        lastInsolvency = [0, -1]  # if we have no insolvency yet
        for insolvency in self.static_parameters["insolvencyHistory"]:  # loop over the insolvencyHistory
            if insolvency[1] == time:  # to see if we have an insolvency in this time period
                lastInsolvency = insolvency  # if we do, update lastInsolvency

        if lastInsolvency[1] > -1:  # see if we found an insolvency in this time step
            lastInsolvency[0] += 1  # add one to the number of insolvencies
        else:  # there has not been an insolvency yet, so add one
            self.static_parameters["insolvencyHistory"].append([1, time])
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # update_state(time)
    # this method calculates the new expected returns for real and
    # financial assets
    # -------------------------------------------------------------------------
    def update_state(self,  time):
        #
        # real assets have an expected return as given in the environment file
        #
        pReal = self.static_parameters["pBank"]  # TODO change pBank to pReal everywhere in code
        rhoReal = self.static_parameters["rhoBank"]
        # TODO change rhoBank to rhoReal everywhere in code
        # TODO: now one could make the process for real assets a bit more interesting
        self.static_parameters["pBank"] = pReal
        self.static_parameters["rhoBank"] = rhoReal

        # financial assets start with some initial expected return and mean
        # then they are updated when the simulation proceeds and become
        # more volatile when more banks go into insolvency
        pFinancial = self.static_parameters["pFinancial"]
        rhoFinancial = self.static_parameters["rhoFinancial"]
        # TODO now we could make something interesting
        self.static_parameters["pFinancial"] = pFinancial
        self.static_parameters["rhoFinancial"] = rhoFinancial
