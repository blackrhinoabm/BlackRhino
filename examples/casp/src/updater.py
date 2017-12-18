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
import numpy as np

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
        if  environment.assets[0].identifier =="A":
            self.asset_a = environment.assets[0]
            self.asset_b = environment.assets[1]
        else:
            self.asset_b = environment.assets[0]
            self.asset_a = environment.assets[1]

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, time):
        import random
        # print environment.price_of_a, self.asset_a.prices[-1]
        random.seed(000)
        if time ==0:
            self.pre_trade(environment, time)

        else:
            """Determine new expected prices and
            who is buying and selling"""

            self.update_expectation_demand(environment, time)


    def update_expectation_demand(self, environment, time):
        expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = 0, 0, 0, 0
        aggregate_demand_a, aggregate_demand_b, aggregate_supply_a,aggregate_supply_b   = 0, 0, 0, 0
        omega_a, omega_b = 0, 0 #excess demand


        suppliers_a = []
        suppliers_b = []
        buyers_a = []
        buyers_b = []
        for_rationing_a = []

        for fund in (environment.funds):
                # print  fund.get_account('A')
            expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = fund.update_belief(environment, self.asset_a, self.asset_b)
            fund.calc_optimal_pf(environment,  exp_mu_a, exp_mu_b)

            target_a = fund.calc_demand_asset(self.asset_a, expected_price_a)
            target_b = fund.calc_demand_asset(self.asset_b, expected_price_a)
            print  "Fund has", fund.get_account('A') , "Fund's target:",  target_a, "Fund net demand", fund.get_net_demand_a(target_a)

            omega_a +=fund.get_net_demand_a(target_a)
            omega_b +=fund.get_net_demand_b(target_b)

            """Save quantities demanded and supplied in lists"""

            "A:"
            if fund.get_net_demand_a(target_a) >0:
                 buyers_a.append([fund, fund.get_net_demand_a(target_a)])
                 for_rationing_a.append([fund, -fund.get_net_demand_a(target_a)])
            else:
                 suppliers_a.append([fund, fund.get_net_demand_a(target_a)])
                 for_rationing_a.append([fund, -fund.get_net_demand_a(target_a)])
            "B:"
            if fund.get_net_demand_b(target_b) >0:
                 buyers_b.append([fund,fund.get_net_demand_b(target_b)])
            else:
                 suppliers_b.append([fund, fund.get_net_demand_b(target_b)])

        """
        Let's try exogenous market maker function for price setting according to
        excess demand (see Day and Huang 1990)
        """
        from market import Market
        market = Market("market")
        self.asset_a.prices.append(market.market_maker( self.asset_a.prices[-1],omega_a ))
        self.asset_b.prices.append(market.market_maker( self.asset_b.prices[-1],omega_b ))

        # print "new price", self.asset_a.prices
        # print "new price", self.asset_b.prices


        # now we use rationing to find the actual transactions between agents

        # # And we find the rationing, ie the amounts
        # # of shares sold between pairs of agents
        rationed_a = market.rationing_proportional(for_rationing_a)
        print rationed_a

        # for ration in rationed_a:

        """
        tentative - walrasian equilibrium
        """
        # "A:"
        # if fund.get_net_demand_a(target_a) >0:
        #     aggregate_demand_a += fund.get_net_demand_a(target_a)
        #     buyers_a.append([fund, fund.demand_tatonnement_a(self.asset_a.prices(-1)))])
        # else:
        #     aggregate_supply_a += fund.get_net_demand_a(target_a)
        #     suppliers_a.append([fund, fund.demand_tatonnement_a])
        # "B:"
        # if fund.get_net_demand_b(target_b) >0:
        #     aggregate_demand_b += fund.get_net_demand_b(target_b)
        #     buyers_b.append([fund, fund.demand_tatonnement_b])
        # else:
        #     aggregate_supply_b += fund.get_net_demand_b(target_b)
        #     suppliers_b.append([fund, fund.demand_tatonnement_b])
        # from market import Market
        #
        # market = Market("market")
        # price_a = market.tatonnement(suppliers_a, buyers_a, expected_price_a , 0.001, 0.01, 1.1)
        # print price_a, "A"
        #
        # market = Market("market")
        # price_b = market.tatonnement(suppliers_b, buyers_b, expected_price_b , 0.001, 0.01, 1.1)
        # print price_b, "B"




    # -----------------------------------------------------------------------
    def pre_trade(self, environment, time):
        #pre-trade stuff, could also be in environment
        """
        Sets up funds with optimal portfolio and
        initializes accounts
        """
        for fund in (environment.funds):
            fund.endow_funds_with_shares(environment, time)
            fund.calc_optimal_pf(environment, self.asset_a.mu, self.asset_b.mu)
        logging.info(" Optimal portfolio for %s funds calculated", len(environment.funds))
        logging.info(" Endowed funds with %s transactions and investment_shares ", len(fund.accounts))
    # Now we allocate initial portfolio to funds
        self.allocate_optimal_shares_to_funds(environment, time)

    def trade_a_priced(self, environment, time):
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

        for fund in environment.funds:
        #     fund.endow_portfolio_transactions(environment, time)
            amount_a = fund.calc_demand_asset(self.asset_a, self.asset_a.prices[-1])
            amount_b = fund.calc_demand_asset(self.asset_b, self.asset_b.prices[-1])

            sum_a += amount_a
            sum_b += amount_b

            if time == 0:
                fund.init_portfolio_transactions(environment, time, amount_a, amount_b)


    def divide_sum(self, n, total):
    #Return a randomly chosen list of n positive integers summing to total.
    #Each such list is equally likely to occur.
        import random
        random.seed(9001)
        dividers = sorted(random.sample(xrange(1, total), n - 1))
        return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
