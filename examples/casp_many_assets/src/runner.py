#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2016 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)
Pawel Fiedor (pawel@fiedor.eu)

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
from src.updater import Updater
import logging
from abm_template.src.baserunner import BaseRunner
import matplotlib.pyplot as plt

# from abm_template.src.baserunner import BaseRunner

# -------------------------------------------------------------------------
#
# class Runner
#
# -------------------------------------------------------------------------


class Runner(BaseRunner):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""
    num_sweeps = 0

    #
    #
    # METHODS
    #
    #

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, environment):
        pass

    def initialize(self, environment):
        self.identifier = environment.identifier
        self.updater = Updater(environment)
        self.num_sweeps = int(environment.static_parameters['num_sweeps'])

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # get_identifier
    # -------------------------------------------------------------------------
    def get_identifier(self):
        return self.identifier

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # set_identifier
    # -------------------------------------------------------------------------
    def set_identifier(self, value):
        return super(Runner, self).set_identifier(value)

    # -------------------------------------------------------------------------
    # get_num_sweeps
    # -------------------------------------------------------------------------
    def get_num_sweeps(self):
        return self.num_sweeps
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # set_num_simulations
    # -------------------------------------------------------------------------
    def set_num_sweeps(self, value):
        super(Runner, self).set_num_sweeps(value)

    # -------------------------------------------------------------------------
    # do_run
    # -------------------------------------------------------------------------
    def do_run(self, environment, time):
        #For immediate plotting purposes we create lists we can put in stuff
        #to look at
        results_a=[]
        results_b=[]
        results_c=[]
        results_d=[]
        results_e=[]
        results_f=[]
        results_g=[]


        # loop over all time steps and do the updating

        # For each update step
        # logging.info('Call runner.do_run and start iteration over sweeps/update steps')
        for i in range(self.num_sweeps):

                self.current_step = i

                #Append results for plotting, e.g look at the evolution of net_demand_a for fund-0
                # results_a.append(self.updater.market.current_supply_a )
                # results_b.append(self.updater.market.current_demand_a)
                # results_c.append(self.updater.market.current_supply_b)
                # results_d.append(self.updater.market.current_demand_b)
                # results_e.append(environment.variable_parameters['r_f'])


                self.updater.do_update(environment, i)

                logging.info('Finished update step %s ', i)

        #######################
        # "Some plotting stuff"

        "Counting trade, prices and demand/supply"
        fig, ax = plt.subplots(nrows=4, ncols=2, figsize=(15,6))
        ###############
        ax[0][0].plot(self.updater.asset_a.funda_values)
        ax[0][0].plot(self.updater.asset_b.funda_values)
        # ax[0][0].plot(self.updater.count_trade_a)
        # ax[0][0].plot(self.updater.count_trade_a)
        # ax[0][0].set_xlim(xmin=xmin)
        ax[0][0].set_xlabel("period", fontsize=15)
        ax[0][0].legend(["funda_a", "funda b" ], loc='best')
        ax[1][0].plot(self.updater.asset_a.dividends,'bo')
        ax[1][0].plot(self.updater.asset_b.dividends, '--', color="red")
        # ax[1][0].set_xlim(xmin=xmin)
        ax[1][0].set_xlabel("period", fontsize=15)
        ax[1][0].legend(["dividends a", "dividends b"], loc='best')
        #
        ax[3][1].plot(results_e)
        ax[3][1].legend(["yield risk free"], loc='best')

        ax[2][1].plot(self.updater.asset_a.prices)
        ax[2][1].plot(self.updater.asset_b.prices, color="crimson" )
        ax[2][1].set_xlabel("period", fontsize=15)
        ax[2][1].legend(["price_a", "price_b"], loc='best')


        ax[3][0].plot(environment.assets[0].returns)
        ax[3][0].plot(environment.assets[1].returns)
        ax[3][0].set_xlabel("period", fontsize=15)
        ax[3][0].legend(["m_a", "m_b"], loc='best')
 
        # ax[3][1].set_xlim(xmin=xmin)
        # ax[4][1].set_xlabel("period", fontsize=15)
        ax[2][0].legend(["risk_free" ], loc='best')
        #

        #
        # plt.show()
        # plt.close()
        # ##############





    # ------------------------------------------------------------------------
