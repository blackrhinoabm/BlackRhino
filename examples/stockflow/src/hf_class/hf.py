#!/usr/bin/env python -W ignore::DeprecationWarning
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-


class HF():

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
    # __str__
    # returns a string describing the bank and its properties
    # based on the implementation in the abstract class
    # but adds the type of agent () and lists all transactions
    # -------------------------------------------------------------------------
    def __str__(self):
        """
        Class variables: identifier, parameters, stock_variables
        Local variables: ret_str, entry, value
        """
        ret_str = "  <agent identifier='" + self.identifier + "'>\n"
        for entry in self.parameters:
            value = self.parameters[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                ret_str = ret_str + "    <parameter type='agent' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
            else:
                raise TypeError
        for entry in self.stock_variables:
            value = self.stock_variables[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                ret_str = ret_str + "    <variable name='" + entry + "' value='" + str(value) + "'></variable>\n"
            elif isinstance(value, list):
                ret_str = ret_str + "    <variable name='" + entry + "' value='[" + str(value[0]) + "," + str(value[1]) + \
                           "]'></variable>\n"
            else:
                raise TypeError

        return ret_str

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

        if self.does_repo == 'yes':

            self.GB = self.GB * updater.pGB
            self.Repo = self.GB * updater.pGB*(1 - updater.haircut)
            self.CB = self.CB + self.Repo/updater.pCB

            self.stock_variables['Total_assets'] = self.Cash + self.GB + self.CB
            self.Invshares = self.Total_assets - self.Repo


        else:
            pass

        "uncomment the next code snippet if you want to check balance sheet identity"
#        self.check_consistency()
        # self.print_balance_sheet()

    # -------------------------------------------------------------------------
    # check_consistency
    # checks whether the assets and liabilities have the same total value
    # -------------------------------------------------------------------------
    def check_consistency(self):

        print self.identifier, "total assets:", self.Total_assets
        print self.identifier, "total liabilities:", self.Total_liabilities

        if self.Total_assets == self.Total_liabilities:
            print "balance sheet identity for %s holds" % self.identifier
        else:
            print "ooups, balance sheet identity for %s does not hold" % self.identifier
    # -------------------------------------------------------------------------

    def print_balance_sheet(self):
        print "***********"
        print  self.identifier,
        print "Assets:" , "\n"
        print "Cash:", self.Cash, "\n"
        print "GB:", self.GB  , " \n"
        print "CB:", self.CB, " \n"
        print  "Total:", self.Total_assets , "\n"
        print "Liabilities:" , "\n"
        print "Repo", self.Repo, " \n"
        print "Investment shares:", self.Invshares, " \n"

    # __getattr__
    # if the attribute isn't found by Python we tell Python
    # to look for it first in parameters and then in stock variables
    # which allows for directly fetching parameters from the Agent class

    def __getattr__(self, attr):
        if (attr in self.parameters) and (attr in self.stock_variables):
            raise AttributeError('The same name exists in both parameters and state variables.')
        else:
            try:
                return self.parameters[attr]
            except:
                try:
                    return self.stock_variables[attr]
                except:
                    raise AttributeError('Agent %s has no attribute "%s".' % self.identifier, attr)
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
    # __del__
    # -------------------------------------------------------------------------
    def __del__(self):
        pass
    # -------------------------------------------------------------------------
