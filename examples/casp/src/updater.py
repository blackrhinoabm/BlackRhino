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

        self.current_demand_a, self.current_demand_b = 0.0, 0.0
        self.current_supply_a, self.current_demand_b = 0.0, 0.0

        self.net_demand_bonds = 0.0

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, time):
        import random
        random.seed(000)

        """We set up optimal portfolios and
        initialize accounts """
        if time ==0:
            self.pre_trade(environment, time)

        else:
            "We collect dividends and update profits of firms"


            """Determine new expected prices and
            who is buying and selling"""
            rationed_a, rationed_b = self.update_expectation_demand(environment, time)

            # self.drag_out_fund(environment, "fund-1")

            """Trade assets"""
            self.exchange_assets_create_transactions(environment, rationed_a, rationed_b, time)
            tracking_a, tracking_b = self.exchange_assets_netting(environment, time)
            self.remove_transactions_after_sell(environment, tracking_a, tracking_b )

            """Update books"""
            for fund in environment.funds:
                self.net_demand_bonds += fund.net_bond_quantity_demanded(time, environment)
            print self.net_demand_bonds

            from market import Market
            market = Market("market")
            price_bond=(market.market_maker( environment.price_of_bond, self.net_demand_bonds ))
            print environment.price_of_bond,    price_bond

            # The new price has an effect on the yield which will affect the new step

    def update_expectation_demand(self, environment, time):
        expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = 0, 0, 0, 0
        aggregate_demand_a, aggregate_demand_b, aggregate_supply_a,aggregate_supply_b   = 0, 0, 0, 0
        omega_a, omega_b = 0, 0 #Net demand

        for_rationing_a = []
        for_rationing_b = []

        for fund in (environment.funds):
                # print  fund.get_account('A')
            expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = fund.update_belief(environment, self.asset_a, self.asset_b)
            fund.calc_optimal_pf(environment,  exp_mu_a, exp_mu_b)

            target_a = fund.calc_demand_asset(self.asset_a, expected_price_a)
            target_b = fund.calc_demand_asset(self.asset_b, expected_price_a)

            print "net", fund.get_net_demand_a(target_a), fund.identifier

            # print  "Fund has", fund.get_account('A') , "Fund's target:",  target_a, "Fund net demand", fund.get_net_demand_a(target_a)

            omega_a +=fund.get_net_demand_a(target_a)
            omega_b +=fund.get_net_demand_b(target_b)

            """Save quantities demanded and supplied in lists"""

            "A:"
            if fund.get_net_demand_a(target_a) >0:
                 for_rationing_a.append([fund, -fund.get_net_demand_a(target_a)])

            else:
                 for_rationing_a.append([fund, -fund.get_net_demand_a(target_a)])
            "B:"
            if fund.get_net_demand_b(target_b) >0:
                 for_rationing_b.append([fund, -fund.get_net_demand_a(target_a)])
            else:
                 for_rationing_b.append([fund, -fund.get_net_demand_a(target_a)])
        """
        Let's try exogenous market maker function for price setting according to
        excess demand (see Day and Huang 1990)
        """
        from market import Market
        market = Market("market")
        self.asset_a.prices.append(market.market_maker( self.asset_a.prices[-1],omega_a ))
        self.asset_b.prices.append(market.market_maker( self.asset_b.prices[-1],omega_b ))

        # Look at the price series if you want
        # print "new price A", self.asset_a.prices
        # print "new price B", self.asset_b.prices

        #Save the new price in environment
        environment.variable_parameters['price_of_b'] = self.asset_b.prices[-1]
        environment.variable_parameters['price_of_a'] = self.asset_a.prices[-1]

        # now we use rationing to find the actual transactions between agents
        # We also save the aggregate current demand and supply (useful later)
        self.current_demand_a =  market.return_total_demand(for_rationing_a)
        self.current_demand_b =  market.return_total_demand(for_rationing_b)
        self.current_supply_a =  market.return_total_supply(for_rationing_a)
        self.current_supply_b =  market.return_total_supply(for_rationing_b)
        print "*************"
        rationed_a = market.rationing_proportional(for_rationing_a)
        rationed_b = market.rationing_proportional(for_rationing_b)

        """ Look at the rationing list for A with the code below: """
        for i, valu in enumerate(rationed_a):
            print "A ration %s:" %i
            print "this is the seller %s" %valu[0].identifier
            print "this is the buyer %s" %(valu[1].identifier)
            print "Quantity %s" %valu[2]

        residual_a =[]
        residual_b =[]

        return rationed_a, rationed_b

    # -----------------------------------------------------------------------
    def exchange_assets_create_transactions(self, environment, list_for_a, list_for_b, time):
        """Method to exchange assets via ration.
        We start with the A asset and create new transactions."""

        #Loop over the rationed list of agent pairs
        for index, item in enumerate(list_for_a):
            # if index==2:  # Uncomment to keep track of only one ration
                # print item, "Seller:", item[0].identifier  #This is the seller of the specific ration

            # Create the sell transaction between the agent pair
            environment.new_transaction("A", "assets", item[0].identifier, item[1].identifier,item[2], 0,  0, -1, environment)

        "Now the B asset"
        for index, item in enumerate(list_for_b):
            environment.new_transaction("B", "assets", item[0].identifier, item[1].identifier,item[2], 0,  0, -1, environment)

    def exchange_assets_netting(self, environment, time):
        """
        Method to net the books of the sellers and buyers of asset A and B.
        We net the transactions, so they don't accumulate
        over the course of the simulation

        Argument
        ========
        Environment to loop over buyers and sellers

        Output
        ======
        Two sets with transactions (one for each traded asset) marked for deletion.
        """

        #To keep track of the sell operations, we use these balance floats
        balance_a, balance_b = 0.0, 0.0
        # We create a proxy set for deleting transaction
        to_delete_a = set([])
        to_delete_b = set([])

        # We start with the sellers of A and loop over them
        for seller_a in environment.funds:
            for tranx in seller_a.accounts:
                # Find the selling A-transactions
                if tranx.type_ == "A":
                    if tranx.from_.identifier == seller_a.identifier:
                        balance_a = balance_a + tranx.amount

                        # Add to the tracking set
                        to_delete_a.add(tranx)
                        # print balance_a, "balance", seller_a.identifier, "seller"

                        # Net the books
                        for firm in environment.firms:
                                for tranx in seller_a.accounts:
                                    if tranx.type_ == "A":
                                        if tranx.from_ == firm:
                                            tranx.set_amount(tranx.amount - balance_a, environment)
                                            # This is a little trick so avoid double counting
                                            balance_a = 0
        #Now we loop over the buyers of A
        for fund in environment.funds:
            # We get the balance amount of new A assets aquired
            # Some funds bought nothing, so the next functions returns None
            #In that case we set the balancing amount to 0
            if self.get_buyer_a_balance_amount(fund) is None:
                x = 0
            #otherwise we get x as balancing amount
            else:
                x = self.get_buyer_a_balance_amount(fund)

            # Set the A account to the new amount
            for tranx in fund.accounts:
                if tranx.type_ == "A" and tranx.to.identifier == fund.identifier and "firm" in tranx.from_.identifier :
                    tranx.set_amount( tranx.amount + x , environment)
        logging.info("  A assets netted on step: %s",  time)


        "Now everything for B"

        "Net the buyer's account."
        for seller_b in environment.funds:
            for tranx in seller_b.accounts:
                # Find the B transactions
                if tranx.type_ == "B":
                    if tranx.from_.identifier == seller_b.identifier:
                        balance_b = balance_b + tranx.amount
                        to_delete_b.add(tranx)

                        for firm in environment.firms:
                                for tranx in seller_b.accounts:
                                    if tranx.type_ == "B":
                                        if tranx.from_ == firm:
                                            # print tranx.amount, "before"
                                            tranx.set_amount(tranx.amount - balance_b, environment)
                                            balance_b = 0
                                            # print tranx.amount, "after"

        "Net the buyer's account."
        for fund in environment.funds:
            if self.get_buyer_b_balance_amount(fund) is None:
                x = 0
            else:
                x = self.get_buyer_b_balance_amount(fund)
        # Add new Assets to total
            for tranx in fund.accounts:
                if tranx.type_ == "B" and tranx.to.identifier == fund.identifier and "firm" in tranx.from_.identifier :
                    tranx.set_amount( tranx.amount + x , environment)
        logging.info("  B assets netted on step: %s",  time)

        return to_delete_a,  to_delete_b

    def remove_transactions_after_sell(self, environment, tracking_a, tracking_b):
        for tranx in tracking_a:
            tranx.remove_transaction(environment)

        for tranx in tracking_b:
            tranx.remove_transaction(environment)

    def get_buyer_a_balance_amount(self, fund_identifier):
        """
        Method to get buyer's balance amount

        Argument
        =====
        Fund object

        Output
        ===
        None or float

        Call this before transactions are deleted!
        """

        balance_a = 0
        num_transactions = 0.0

        new_list = []

        for tranx in fund_identifier.accounts:
            # Find the transactions
            if tranx.type_ == "A" and tranx.to.identifier == fund_identifier.identifier and "firm" not in tranx.from_.identifier :
                num_transactions +=1
                new_list.append(tranx)
        for index, value in enumerate(new_list):
            if value.type_ == "A" and value.to.identifier == fund_identifier.identifier and "firm" not in value.from_.identifier :
                balance_a = balance_a + value.amount
                if index == (num_transactions-1):
                    return balance_a

    def get_buyer_b_balance_amount(self, fund_identifier):
        "call this before transactions are deleted!"
        balance  = 0
        num_transactions = 0.0

        new_list = []

        for tranx in fund_identifier.accounts:
            # Find the transactions
            if tranx.type_ == "B" and tranx.to.identifier == fund_identifier.identifier and "firm" not in tranx.from_.identifier :
                num_transactions +=1
                new_list.append(tranx)
        for index, value in enumerate(new_list):
            if value.type_ == "B" and value.to.identifier == fund_identifier.identifier and "firm" not in value.from_.identifier :
                balance = balance + value.amount
                if index == (num_transactions-1):
                    return balance


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

    def drag_out_fund(self, environment, ident):
        """
        Method to print individual fund to screen.
        Useful to see if updater process achieved
        correct output.

        Argument
        =====
        str of fund.identifier

        Output
        ====

        Returns an agent object according to the passed in identifier str()
        """
        for fund in environment.funds:
            if fund.identifier==str(ident):
                print fund



    """
    tentative - walrasian equilibrium
    """
    # suppliers_a = []
    # suppliers_b = []
    # buyers_a = []
    # buyers_b = []
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
