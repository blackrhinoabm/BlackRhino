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
    # identifier of the specific environment used for distinguishing them / logging
    # identifier should be a string

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
    # static parameters of the environment store parameters determining
    # the behaviour of the simulation with a fixed value
    # static_parameters should be a dictionary

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
    # variable parameters of the environment store parameters determining
    # the behaviour of the simulation with a range of values
    # variable_parameters should be a dictionary

    @abc.abstractmethod
    def add_static_parameter(self, name, value):
        """
        Class variables: static_parameters
        Local variables: name, value
        """
        self.static_parameters[name] = value
    # an abstract method for adding a static parameter to the stack of static parameters

    @abc.abstractmethod
    def add_variable_parameter(self, name, range_from, range_to):
        """
        Class variables: variable_parameters
        Local variables: name, range_from, range_to
        """
        self.variable_parameters[name] = [range_from, range_to]
    # an abstract method for adding a variable parameter to the stack of variable parameters

    @abc.abstractmethod
    def print_parameters(self):
        """
        Class variables: static_parameters, variable_parameters
        Local variables: key
        """
        for key in self.static_parameters:
            print(str(key) + ": " + str(self.static_parameters[key]))
        for key in self.variable_parameters:
            print(str(key) + ":" + " range: " + str(self.variable_parameters[key][0]) + "-" + str(self.variable_parameters[key][1]))
    # an abstract method for printing all (static and variable) parameters
    # this is for testing purposes, do not use print in production

    @abc.abstractmethod
    def write_environment_file(self,  file_name):
        out_file = open(file_name + "-check.xml",  'w')
        text = self.__str__()
        out_file.write(text)
        out_file.close()
    # an abstract method for writing a file with environment config to the current directory

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
                out_str = out_str + "  <parameter type='static' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
            else:
                raise TypeError
        for entry in self.variable_parameters:
            if isinstance(self.variable_parameters[entry], list):
                from_value = self.variable_parameters[entry][0]
                to_value = self.variable_parameters[entry][1]
                out_str = out_str + "  <parameter type='variable' name='" + entry + "' range='" + str(from_value) + "-" + \
                    str(to_value) + "'></parameter>\n"
            else:
                raise TypeError
        out_str = out_str + "</config>"

        return out_str
    # an abstract method returning a string with environment's config

    @abc.abstractmethod
    def __init__(self):
        """
        Class variables: identifier, static_parameters, variable_parameters
        Local variables:
        """
        self.identifier = ""
        self.static_parameters = {}
        self.variable_parameters = {}
    # an abstract method for initializing the environment

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
                    print("<< ERROR: range_from must be a float or int. Found: " + str(subelement.attrib['range'].rsplit("-")[0]))

                try:
                    range_to = float(subelement.attrib['range'].rsplit("-")[1])
                except:
                    format_correct = False
                    print("<< ERROR: range_to must be a float or int. Found: " + str(subelement.attrib['range'].rsplit("-")[1]))

                if format_correct:
                    self.variable_parameters[name] = [range_from, range_to]
                else:
                    print("<< ERROR: FOUND ERROR IN FILE " + config_file_name + ", ABORTING")
    # an abstract method for reading an xml file with config
    # and adding all the static and variable parameters

    @abc.abstractproperty
    def agents(self):
        pass
    # a list of all the agents, list of lists [types][instances]

    @abc.abstractmethod
    def agents_generator(self):
        if self.agents is not None:
            for agent_type in self.agents:
                if type(agent_type) == list:
                    for agent in agent_type:
                        yield agent
                else:
                    yield agent_type
        else:
            raise LookupError('There are no agents to iterate over.')
    # a standard method for iterating over all agents

    @abc.abstractmethod
    def get_agent_by_id(self, ident):
        to_return = None
        for agent in self.agents_generator():
            if agent.identifier == ident:
                if to_return is None:  # checks whether something has been found previously in the function
                    to_return = agent
                else:
                    raise LookupError('At least two agents have the same ID.')
                    # if we have found something before then IDs are not unique, so we raise an error
        if to_return is None:
            raise LookupError('No agents have the provided ID.')
            # if we don't find any agent with that ID we raise an error
        else:
            return to_return
    # a standard method for returning an agent based on a unique ID

    @abc.abstractmethod
    def check_global_transaction_balance(self, type_):
        sum_lists = 0  # global sum, for checking the consistency numerically
        # We check all the banks first
        for agent in self.agents_generator():
            # Dictionaries to keep all the incoming and outgoing transactions of the bank
            tranx_list_from = {}
            tranx_list_to = {}
            # We populate the above with the amounts
            for tranx in agent.accounts:
                if tranx.type_ == type_:
                    if tranx.from_ == agent:
                        if tranx.to in tranx_list_to:
                            tranx_list_to[tranx.to] = tranx_list_to[tranx.to] + tranx.amount
                        else:
                            tranx_list_to[tranx.to] = tranx.amount
                    else:
                        if tranx.from_ in tranx_list_from:
                            tranx_list_from[tranx.from_] = tranx_list_from[tranx.from_] + tranx.amount
                        else:
                            tranx_list_from[tranx.from_] = tranx.amount
            # And we check if the added transactions exist in the counterparty's books
            # If they do we subtract the amount from the dictionaries
            # So that we can check if the dictionaries go to 0 globally
            for key in tranx_list_from:
                for tranx in key.accounts:
                    if tranx.type_ == type_:
                        if tranx.from_ == key:
                            if tranx.to == agent:
                                tranx_list_from[key] = tranx_list_from[key] - tranx.amount
            for key in tranx_list_to:
                for tranx in key.accounts:
                    if tranx.type_ == type_:
                        if tranx.to == key:
                            if tranx.from_ == agent:
                                tranx_list_to[key] = tranx_list_to[key] - tranx.amount
            # Then we add the dictionary entries to the global check variable
            for key in tranx_list_from:
                sum_lists = sum_lists + abs(tranx_list_from[key])
            for key in tranx_list_to:
                sum_lists = sum_lists + abs(tranx_list_to[key])
        # We make the final check and return True if consistent, otherwise return False
        if sum_lists == 0:
            return True
        else:
            return False
        # a standard method for making sure the transactions of a given type
        # are consistent across all agents, ie the same transaction is of the same amount
        # on both agents it concerns

    @abc.abstractmethod
    def __getattr__(self, attr):
        if (attr in self.static_parameters) and (attr in self.variable_parameters):
            raise AttributeError('The same name exists in both static and variable parameters.')
        else:
            try:
                return self.static_parameters[attr]
            except:
                try:
                    return self.variable_parameters[attr]
                except:
                    raise AttributeError('Environment has no attribute "%s".' % attr)
    # a standard method for returning attributes from the dectionaries as attributes

    @abc.abstractmethod
    def accrue_interests(self):
        done_list = []  # This keeps the IDs of updated transactions
        # The above is important as the same transactions may be on the books
        # of different agents, we don't want to double count the interest
        for agent in self.agents_generator():  # Iterate over all agents
            for tranx in agent.accounts:  # Iterate over all transactions
                if tranx.identifier not in done_list:  # If not amended previously
                    # The below adds the interest on the principal amount
                    tranx.amount = tranx.amount + tranx.amount * tranx.interest
                    # The below makes sure that we don't double count
                    done_list.append(tranx.identifier)
    # a standard method for accruing interest on all transactions
