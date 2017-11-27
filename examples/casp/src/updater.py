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
from abm_template.src.basemodel import BaseModel
import logging

# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------


class Updater(BaseModel):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""

    model_parameters = {}
    #
    #
    # METHODS
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Updater, self).set_identifier(value)

    def __str__(self):
        super(Updater, self).__str__(self)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, values):
        super(Updater, self).set_model_parameters(values)

    def get_interactions(self):
        return self.interactions

    def interactions(self):
        super(Updater, self).interactions(self)

    def set_interactions(self, values):
        super(Updater, self).set_interactions(values)

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, environment):
        self.environment = environment
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, time):

        self.allocate_returns(environment, time)

        for index, fund in enumerate(environment.funds):
            fund.calc_optimal_pf(environment)
            fund.endow_funds_with_shares(time)
        logging.info(" Optimal portfolio for %s funds calculated", len(environment.funds))
        logging.info("Endowed funds with investment_shares on the liability side in fund.accounts")



    # -----------------------------------------------------------------------
    def allocate_returns(self, environment, time):
        for i, value in enumerate(environment.initialize_ame_returns()):
            for k, v in enumerate(environment.funds):
                if i == k:
                    dict={"r_ame" : value}
                    v.append_state_variables(dict)


        for i, value in enumerate(environment.initialize_eme_returns()):
            for k, v in enumerate(environment.funds):
                if i == k:
                    dict={"r_eme" : value}
                    v.append_state_variables(dict)


    def divide_sum(self, n, total):
    #Return a randomly chosen list of n positive integers summing to total.
    #Each such list is equally likely to occur.
        import random
        random.seed(9001)
        dividers = sorted(random.sample(xrange(1, total), n - 1))
        return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

### Moved this to environment to call after initializing environment and agents
    # def allocate_fund_size(self, environment):
    #     # default is 20% eme and 80% ame market cap
    #     sum_ame = 0
    #     sum_eme = 0
    #     for fund in environment.funds:
    #         if fund.parameters['domicile'] == 0:
    #             sum_ame += 1
    #         if fund.parameters['domicile'] == 1:
    #             sum_eme += 1
    #
    #     list_temp_eme  = []
    #     list_eme = []
    #     for fund in environment.funds:
    #         if fund.domicile == 1.0:
    #             list_temp_eme = self.divide_sum(int(sum_eme), int((environment.global_assets_under_management)*0.2))
    #             list_eme.append(fund)
    #     # itrange = list(range(0, len(list_temp)))
    #     for index, elem in enumerate(list_eme):
    #         for index2, elem2 in enumerate(list_temp_eme):
    #             if index == index2:
    #                 dict={"total_assets" : elem2}
    #                 elem.append_state_variables(dict)
    #
    #     list_temp_ame  = []
    #     list_ame = []
    #     for fund in environment.funds:
    #         if fund.domicile == 0:
    #             list_temp_ame = self.divide_sum(int(sum_ame), int((environment.global_assets_under_management)*0.8))
    #             list_ame.append(fund)
    #     # itrange = list(range(0, len(list_temp)))
    #     for index, elem in enumerate(list_ame):
    #         for index2, elem2 in enumerate(list_temp_ame):
    #             if index == index2:
    #                 dict={"total_assets" : elem2}
    #                 elem.append_state_variables(dict)
