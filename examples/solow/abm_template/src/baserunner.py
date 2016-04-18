#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

__author__ = """Paweł Fiedor (pawel.fiedor@uct.ac.za)"""

# -------------------------------------------------------------------------
#
#  class Runner
#
# -------------------------------------------------------------------------


class BaseRunner(object):
    """
    Class variables: __metaclass__, identifier, num_simulations
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
    def get_num_simulations(self):
        return
    @abc.abstractmethod
    def set_num_simulations(self, _num_simulations):
        """
        Class variables: num_simulations
        Local variables: _num_simulations
        """
        if not isinstance(_num_simulations, int):
            raise TypeError
        else:
            self.num_simulations = _num_simulations
        return
    num_simulations = abc.abstractproperty(get_num_simulations, set_num_simulations)

    @abc.abstractmethod
    def __init__(self, model_config):
        """
        Class variables:
        Local variables: _params, model_config
        """
        _num_simulations = model_config.get_model_parameters()['num_sweeps']

        self.set_identifier(model_config.identifier)
        self.set_num_simulations(_num_simulations)

    @abc.abstractmethod
    def do_run(self):
        pass
