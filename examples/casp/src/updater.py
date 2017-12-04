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

        #In the first step, assets are allocated according to fair value (pre-trading) = price
        self.endow_returns_expectations(environment, time)

        # #pre-trade stuff, could also be in environment
        for fund in (environment.funds):
            fund.calc_optimal_pf(environment)
        logging.info(" Optimal portfolio for %s funds calculated", len(environment.funds))

        # Initialize investment shares:
        for i in environment.funds:
            i.endow_funds_with_shares(environment, time)
        logging.info(" Endowed funds with %s transactions and investment_shares ", len(i.accounts))

        # "endow firms with equity (add transaction to accounts)"
        # for i in environment.firms:
        #     i.endow_firms_with_equity(environment, time)
        # logging.info(" Endowed firms with equity  ")

        # Now we allocate iptimal portfolio to funds
        self.allocate_optimal_shares_to_funds(environment, time)


        #these worked in previous versions where firms had a fixed supply
        # self.sell_a_priced(environment, time)
        # logging.info(" Found the price of the A risky asset: %s currency units ", environment.variable_parameters["price_of_a"]    )
        # self.sell_b_priced(environment, time)
        # logging.info(" Found the price of the B risky asset: %s currency units ", environment.variable_parameters["price_of_b"]    )
        #


    # -----------------------------------------------------------------------


    def sell_a_priced(self, environment, time):
        # We find the market price of A shares
        # given supply and demand of the agents
        # and tolerance of error, resolution of search
        # and amplification factor for exponential search
        suppliers = []
        for agent in environment.firms:
            if agent.domicile==0:
                # print agent.get_account("number_of_shares"), agent.identifier
                suppliers.append([agent, agent.supply_of_shares])
        # And the list of buyers and their demand functions
        buyers = []
        for agent in environment.funds:
            buyers.append([agent, agent.demand_a])

        price_dummy = 75

        from market import Market
        # Put the appropriate settings, i.e. desired identifier
        market = Market("market")
        price = market.tatonnement(suppliers, buyers, price_dummy, 0.001, 0.01, 1.1)
        environment.variable_parameters["price_of_a"] = price
        print price
        # now we use rationing to find the actual transactions between agents
        for_rationing = []
        for firm in environment.firms:
            if firm.domicile==0:
                for_rationing.append([firm, firm.supply_of_shares(price)])

        for fund in environment.funds:
            for_rationing.append([fund, -fund.demand_a(price)])

        # And we find the rationing, ie the amounts
        # of shares sold between pairs of agents
        rationed = market.rationing_proportional(for_rationing)



    def allocate_optimal_shares_to_funds(self, environment, time):
        sum_a = 0
        sum_b = 0
        a_supply_of_shares = 0
        b_supply_of_shares = 0

        for fund in environment.funds:
            fund.endow_portfolio_transactions(environment, time)
            fund.demand_a(environment.fair_value_a)
            sum_a += fund.demand_a(environment.fair_value_a)
            fund.demand_b(environment.fair_value_b)
            sum_b +=fund.demand_b(environment.fair_value_b)

        # The supply of shares is the same as total demand (assumption)
        # initialize firm transactions: number of shares (liability side)
        # this supply is then fixed over the simulation horizon(no new shares issued)
        for firm in environment.firms:
            if firm.domicile == 0:
                firm.endow_firms_with_equity(environment, time, sum_a)
            if firm.domicile == 1:
                firm.endow_firms_with_equity(environment, time, sum_b)



    def sell_b_priced(self, environment, time):
        # We find the market price of A shares
        # given supply and demand of the agents
        # and tolerance of error, resolution of search
        # and amplification factor for exponential search
        suppliers = []
        for agent in environment.firms:
            if agent.domicile==1.0:
                # print agent.get_account("number_of_shares"), agent.identifier
                suppliers.append([agent, agent.supply_of_shares])
        # And the list of buyers and their demand functions
        buyers = []
        for agent in environment.funds:
            buyers.append([agent, agent.demand_a])

        price_dummy = 75

        from market import Market
        # Put the appropriate settings, i.e. desired identifier
        market = Market("market")
        price = market.tatonnement(suppliers, buyers, price_dummy, 0.001, 0.01, 1.1)
        environment.variable_parameters["price_of_b"] = price
        print price


    #This function is used in the beginning so funds have expected returns
    def endow_returns_expectations(self, environment, time):

        environment.initialize_returns(environment)
        for i in environment.funds:
            dict={"r_a" : environment.mu_a, "r_b" : environment.mu_b,\
                    "fair_value_a": environment.fair_value_a,\
                    "fair_value_b":environment.fair_value_b,}
            i.append_state_variables(dict)


    def divide_sum(self, n, total):
    #Return a randomly chosen list of n positive integers summing to total.
    #Each such list is equally likely to occur.
        import random
        random.seed(9001)
        dividers = sorted(random.sample(xrange(1, total), n - 1))
        return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


        "This is old code: if global supply is given.. not used"
    def allocate_firm_size(self):
        # default is 10% B and 90% A supply of global equity assets
        sum_a = 0
        sum_b = 0
        for firm in self.firms:
            if firm.parameters['domicile'] == 0:
                sum_a += 1
            if firm.parameters['domicile'] == 1:
                sum_b += 1

        list_temp_b  = []
        list_b = []
        eme_supply_shares = 0
        for firm in self.firms:
            if firm.domicile == 1.0:
                list_temp_b = self.divide_sum(int(sum_b), int((self.global_supply_shares)*0.1))
                list_b.append(firm)
        # itrange = list(range(0, len(list_temp)))
        for index, elem in enumerate(list_b):
            for index2, elem2 in enumerate(list_temp_b):
                if index == index2:
                    dict={"number_of_shares" : elem2}
                    elem.append_state_variables(dict)
                    eme_supply_shares+=elem.number_of_shares

        self.variable_parameters["eme_supply_shares"] = eme_supply_shares

        # print eme_supply_shares, self.global_supply_shares*0.1

        "The same for A firms"

        list_temp_a  = []
        list_a = []
        ame_supply_shares = 0
        for firm in self.firms:
            if firm.domicile == 0:
                list_temp_a = self.divide_sum(int(sum_a), int((self.global_supply_shares)*0.9))
                list_a.append(firm)
        # itrange = list(range(0, len(list_temp)))
        for index, elem in enumerate(list_a):
            for index2, elem2 in enumerate(list_temp_a):
                if index == index2:
                    dict={"number_of_shares" : elem2}
                    elem.append_state_variables(dict)
                    ame_supply_shares += elem.number_of_shares
        self.variable_parameters["ame_supply_shares"] = ame_supply_shares

        # print ame_supply_shares, self.global_supply_shares*0.9
