#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = """Co-Pierre Georg (co-pierre.georg@uct.ac.za)"""

import abc
from xml.etree import ElementTree

# -------------------------------------------------------------------------
#
#  class Config
#
# -------------------------------------------------------------------------
class BaseConfig(object):
    """
    Class variables: __metaclass__, identifier, static_parameters, variable_parameters
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_identifier(self):
        return
    @abc.abstractmethod
    def set_identifier(self, _identifier):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        if not isinstance(_identifier, str):
            raise TypeError
        else:
            self.identifier = _identifier
        return
    identifier = abc.abstractproperty(get_identifier, set_identifier)

    @abc.abstractmethod
    def get_static_parameters(self):
        return
    @abc.abstractmethod
    def set_static_parameters(self, _params):
        """
        Class variables: static_parameters
        Local variables: _params
        """
        if not isinstance(_params, dict):
            raise TypeError
        else:
            self.static_parameters = _params
        return
    static_parameters = abc.abstractproperty(get_static_parameters, set_static_parameters)

    @abc.abstractmethod
    def get_variable_parameters(self):
        return
    @abc.abstractmethod
    def set_variable_parameters(self, _params):
        """
        Class variables: variable_parameters
        Local variables: _params
        """
        if not isinstance(_params, dict):
            raise TypeError
        else:
            self.variable_parameters = _params
        return
    variable_parameters = abc.abstractproperty(get_variable_parameters, set_variable_parameters)


    @abc.abstractmethod
    def __str__(self):
        """
        Class variables: identifier, static_parameters, variable_parameters
        Local variables: out_str, entry, value, from_value, to_value
        """
        out_str = "<config identifier='" + self.identifier + "'>\n"
        for entry in self.static_parameters:
            value = self.static_parameters[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                out_str += "  <parameter type='static' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
            else:
                raise TypeError
        for entry in self.variable_parameters:
            if isinstance(self.variable_parameters[entry], list):
                from_value = self.variable_parameters[entry][0]
                to_value = self.variable_parameters[entry][1]
                out_str += "  <parameter type='variable' name='" + entry + "' range='" + str(from_value) + "-" + \
                       str(to_value) + "'></parameter>\n"
            else:
                raise TypeError
        out_str += "</config>"

        return out_str


    @abc.abstractmethod
    def __init__(self):
        """
        Class variables: identifier, static_parameters, variable_parameters
        Local variables: 
        """
        self.identifier = ""
        self.static_parameters = {}
        self.variable_parameters = {}


    @abc.abstractmethod
    def read_xml_config_file(self, config_file_name):
        """
        Class variables: identifier, static_parameters, variable_parameters
        Local variables: xmlText, config_file_name, element, subelement, name, value, format_correct, range_from, range_to
        """
        xmlText = open(config_file_name).read()
        element = ElementTree.XML(xmlText)
        self.identifier = element.attrib['identifier']

        # loop over all entries in the xml file
        for subelement in element:
            name = subelement.attrib['name']

            if subelement.attrib['type'] == 'static':
                try:  # we see whether the value is a float
                    value = float(subelement.attrib['value'])
                except:  # if not, it is a string
                    value = str(subelement.attrib['value'])
                self.static_parameters[name] = value

            if subelement.attrib['type'] == 'variable':
                format_correct = True

                try:
                    range_from = float(subelement.attrib['range'].rsplit("-")[0])
                except:
                    format_correct = False
                    print "<< ERROR: range_from must be a float or int. Found: " + str(subelement.attrib['range'].rsplit("-")[0])

                try:
                    range_to = float(subelement.attrib['range'].rsplit("-")[1])
                except:
                    format_correct = False
                    print "<< ERROR: range_to must be a float or int. Found: " + str(subelement.attrib['range'].rsplit("-")[1])

                if format_correct:
                    self.variable_parameters[name] = [range_from, range_to]
                else:
                    print "<< ERROR: FOUND ERROR IN FILE " + config_file_name + ", ABORTING"
    #-------------------------------------------------------------------------
