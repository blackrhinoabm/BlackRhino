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
        # results_a=[]
        # results_b=[]
        # results_c=[]
        # results_d=[]

        # loop over all time steps and do the updating

        # For each update step
        # logging.info('Call runner.do_run and start iteration over sweeps/update steps')
        for i in range(self.num_sweeps):

                self.current_step = i

                #Append results for plotting, e.g look at the evolution of net_demand_a for fund-0
                # results_a.append(environment.funds[0].get_account("A"))
                # results_b.append(environment.funds[1].get_account("A"))
                # results_c.append(environment.funds[2].get_account("A"))
                # results_d.append(environment.funds[3].get_account("A"))

                self.updater.do_update(environment, i)
                logging.info('Finished update step %s ', i)

        #######################
        # "Some plotting stuff"
        # fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))
        # #
        # ax[0].plot(self.updater.asset_a.prices )
        # ax[0].plot(  self.updater.asset_b.prices )

        # PROFIT RESULTS
        # ax[1].plot(environment.firms[0].profit_results )
        # ax[1].plot(  environment.firms[1].profit_results)
        # ax[0].legend([environment.firms[0].identifier, environment.firms[1].identifier], loc='best')
        # ax[1].legend([environment.firms[0].identifier, environment.firms[1].identifier], loc='best')

        # ax[1].plot(results_a)
        # ax[1].plot(results_b)
        # ax[1].plot(results_c)
        # ax[1].plot(results_d)
        # ax[1].legend(["fund-0", "fund-1", "fund-2", "fund-3"], loc='best')

        # ax[1].plot(environment.assets[2].prices)
        # ax[1].legend(["bond"], loc='best')]

        #RISK FREE YIELD
        # ax[1].plot(results_b)
        # ax[1].legend(["Risk_free yield"], loc='best')
        # plt.show()
        # plt.close()

        # "Plots 2x2"
        # fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(15,6))
        #
        # ax[0][0].plot(  )
        # ax[0][0].plot(  )
        # ax[1][0].plot( )
        # # ax[0][1].plot(  )
        # ax[0][1].plot(  )
        # ax[0][1].plot(  )
        # # ax[1][0].plot(  )
        #
        # ax[1][1].plot(  environment.assets[2].prices  ) #
        # ax[0][0].legend(["  ",  "], loc='best')
        # ax[1][0].legend(["yield"], loc='best')
        #
        # ax[1][1].legend(["risk free "], loc='best')
        # ax[0][1].legend(["price a", "price b"], loc='best')
        # # ax[1][0].legend(["   "], loc='best' )
        # #
        # plt.show()
        # plt.close()

    # ------------------------------------------------------------------------
