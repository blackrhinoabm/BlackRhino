#!/usr/bin/env python -W ignore::DeprecationWarning
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-


class Dealer():

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self):


        self.identifier = ""  # identifier of the specific bank
        self.parameters = {}  # parameters of the specific bank
        self.stock_variables = {}  # stock variables of the
        self.net_income = 0.0

        self.parameters["institution_specific_interest_rate"] = 0.0  # interest rate on loans
        self.parameters["dividends"] = 0.0  # interest rate on deposits
        self.parameters["active"] = 0  # this is a control parameter checking whether HF is active
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __del__
    # -------------------------------------------------------------------------
    def __del__(self):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __str__
    # returns a string describing the bank and its properties
    # based on the implementation in the abstract class
    # but adds the type of agent () and lists all transactions
    # -------------------------------------------------------------------------
    def __str__(self):

            ret_str = "  <agent identifier='" + self.identifier + "'>\n "

            for entry in self.parameters:
                value = self.parameters[entry]
                ret_str = ret_str + " <parameter type='parameters' name=" + entry + "' value='" + str(value) + "'></parameter>\n"

            for entry in self.stock_variables:
                value = self.stock_variables[entry]
                if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                    ret_str = ret_str + "  <parameter type='stock_variables' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
                else:
                    raise TypeError
            ret_str = ret_str + "</agent>\n"
            return ret_str
    # -------------------------------------------------------------------------
    # get_parameters_from_file
    # reads the specified config file given the environment
    # and sets parameters to the ones found in the config file
    # the config file should be an xml file
    # -------------------------------------------------------------------------
    def get_parameters_from_file(self,  agent_filename, environment):
        from xml.etree import ElementTree

        xmlText = open(agent_filename).read()
        element = ElementTree.XML(xmlText)
        # we get the identifier
        self.identifier = element.attrib['identifier']
        # and then we're only interested in <parameter> fields
        element = element.findall('parameter')

        # loop over all <parameter> entries in the xml file
        for subelement in element:

            if subelement.attrib['type'] == 'stock_variables':

                name = subelement.attrib['name']
                try: # we see whether the value is a float
                    value = float(subelement.attrib['value'])
                except:
                    value = str(subelement.attrib['value'])
                # add them to stock_variables list
                self.stock_variables[name] = value

            if subelement.attrib['type'] == 'parameters':
                name = subelement.attrib['name']
                value = subelement.attrib['value']
                # add them to stock_variables list
                self.parameters[name] = float(value)
    # ------------------------------------------------------------------------
    def initialize_assets(self, updater, current_step):

        "****************Hedge Fund*******************"
        if any(c in self.identifier for c in ("HF", "Hedge", "Hedgefund", "Hedge Fund")):

            self.GB = self.GB * updater.pGB
            self.repo = self.GB * updater.pGB*(1 - updater.haircut)
            self.CB = self.CB + self.repo/updater.pCB
            self.stock_variables['total_assets'] = self.stock_variables['Cash'] + self.stock_variables['GB'] + self.stock_variables['CB']
            self.invshares=self.total_assets - self.repo

        "****************MMF*******************"
        if any(c in self.identifier for c in ("MMF", "Money Market", "Money Market fund")):
            self.stock_variables['total_assets'] = self.stock_variables['cash'] + self.stock_variables['reverse_repo']
            print self.identifier, current_step, self.stock_variables

        "****************DB Pension Fund*******************"
        if any(c in self.identifier for c in ("Pension Fund", "PF", "DB Pension")):
            self.repo = self.GB * updater.pGB*(1 - updater.rates['haircut'])
            self.GB = self.GB * updater.pGB + self.repo/updater.pGB
            self.CB = self.CB * updater.pCB
            self.stock_variables['total_assets'] = self.stock_variables['cash'] + self.stock_variables['GB'] + self.stock_variables['CB']
            print self.identifier, current_step, self.stock_variables


        "****************Investment Fund*******************"
        if any(c in self.identifier for c in ("Investment Fund", "IF")):
            self.GB = self.GB * updater.pGB
            self.CB = self.CB * updater.pCB
            self.stock_variables['total_assets'] = self.stock_variables['cash'] + self.stock_variables['GB'] + self.stock_variables['CB']
            self.invshares=self.total_assets


        "****************Insurance Company*******************"
        if any(c in self.identifier for c in ("Insurance", "IC")):
            self.GB = self.GB * updater.pGB
            self.CB = self.CB * updater.pCB
            self.stock_variables['total_assets'] = self.stock_variables['cash'] + self.stock_variables['GB'] + self.stock_variables['CB']


        "****************Dealer*******************"
        if any(c in self.identifier for c in ("dealer", "bank dealer", "BD")):
            self.GB = self.GB * updater.pGB
            self.CB = self.CB * updater.pCB
        # print self.total_assets, self.identifier
    # check_consistency
    # checks whether the assets and liabilities have the same total value
    # -------------------------------------------------------------------------
    def check_consistency(self):
        pass
    # -------------------------------------------------------------------------

    # __getattr__
    # if the attribute isn't found by Python we tell Python
    # to look for it first in parameters and then in stock variables
    # which allows for directly fetching parameters from the Agent class
    # def __getattr__(self, attr):
    #     if (attr in self.parameters) and (attr in self.stock_variables):
    #         raise AttributeError('The same name exists in both parameters and stock variables.')
    #     else:
    #         try:
    #             return self.parameters[attr]
    #         except:
    #             try:
    #                 return self.stock_variables[attr]
    #             except:
    #                 raise AttributeError('Agent %s has no attribute "%s".' % self.identifier, attr)
    # a standard method for retrieving items from dictionaries as class attributes

    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # functions for setting/changing id, parameters, and stock variables
    # these either return or set specific value to the above variables
    # with the exception of append (2 last ones) which append the dictionaries
    # which contain parameters or stock variables
    # -------------------------------------------------------------------------
    def get_identifier(self):
        return self.identifier

    def get_parameters(self):
        return self.parameters

    def get_stock_variables(self):
        return self.stock_variables

    # -------------------------------------------------------------------------
    # functions needed to make HF() hashable
    # -------------------------------------------------------------------------
    def __key__(self):
        return self.identifier

    def __eq__(self, other):
        return self.__key__() == other.__key__()

    def __hash__(self):
        return hash(self.__key__())
    # -------------------------------------------------------------------------
