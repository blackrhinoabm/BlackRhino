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

        from market import Market
        self.market = Market("market")

        self.count_trade_a = []
        self.count_trade_b = []

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

            for firm in environment.firms:
                print firm.number_of_shares

        else:
            # While market orders are submitted contineously,
            # dividends are only updated twice a year
            list = [i for i in range(1, environment.num_sweeps/180)]
            profit_frequency = list[::(1)]

            for ii, value2 in enumerate(profit_frequency):
                if time == ii:
                    "We collect dividends, fluctuate deposits and update profits of firms"
                    for fund in environment.funds:
            			# next, determine stochastic deposit outflows/inflows
                        change = fund.calc_new_deposits(environment.scaleFactorHouseholds, environment)

                    for firm in environment.firms:
                        profit = firm.calc_profit(time)
                        # determine new dividends and total assets after dividends
                        dividend = firm.update_and_distribute_dividends(environment, time)

                        funda_v = round (  firm.state_variables['dividend']/firm.discount  , 4)
                        logging.info(" %s's asset's fundamental value is %s per share in step %s", firm.identifier, funda_v , time)

                        if firm.identifier=="firm-0":
                            self.asset_a.funda_v = funda_v
                            self.asset_a.funda_values.append(funda_v)
                        if firm.identifier=="firm-1":
                            self.asset_b.funda_v = funda_v
                            self.asset_b.funda_values.append(funda_v)

            """Determine new expected prices and
            who is buying and selling"""
            rationed_a, rationed_b = self.update_expectation_demand(environment, time)


            """Trade risky assets"""
            self.exchange_assets_create_transactions(environment, rationed_a, rationed_b, time)
            tracking_a, tracking_b = self.exchange_assets_netting(environment, time)
            self.remove_transactions_after_sell(environment, tracking_a, tracking_b)

            """Exchange risk-free asset"""
            omega_bonds= self.exchange_bonds(environment, time) * 0.01

            # # self.drag_out_fund(environment, "fund-3")
            # for fund in environment.funds:
            #     print fund.check_accounts(environment), fund.identifier, "check",    time

            """ Get new price according to excess demand"""
            # self.market.show_open_orders(time)
            # omega negative : excess supply - price adjusts downwards
            #  omega positive : excess demand - price adjusts upwards
            #omega is  (demand -supply) and  passed into market maker
            omega_a =  self.market.current_demand_a  - self.market.current_supply_a
            print omega_a, "omega a"
            omega_b =  self.market.current_demand_b  - self.market.current_supply_b
            print omega_b, "omega b"
            self.determine_price_risky_assets(environment, omega_a, omega_b, time)
            self.determine_price_riskfree_asset(environment, omega_bonds, time)

            """Introduce Policy action"""
        # if time>50:
        #     self.policy_action(environment)

    def update_expectation_demand(self, environment, time):
        expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = 0, 0, 0, 0
        aggregate_demand_a, aggregate_demand_b, aggregate_supply_a,aggregate_supply_b   = 0, 0, 0, 0
        omega_a, omega_b = 0, 0 #Net demand

        for_rationing_a = []
        for_rationing_b = []
        # print "********************"
        # print "Demand for risky assets in the market (Quantity)"
        # print "********************"

        for fund in (environment.funds):
            expected_price_a, expected_price_b, exp_mu_a, exp_mu_b = fund.update_belief(environment, self.asset_a, self.asset_b, time)

            fund.calc_optimal_pf(environment,  exp_mu_a, exp_mu_b)

            target_a =  round ( fund.calc_demand_asset(self.asset_a, expected_price_a, time)   , 4)

            if target_a >0:
                target_a=(min(fund.get_account("investment_shares"), target_a))
            if target_a <0:
                target_a = 0


            target_b =   round (  fund.calc_demand_asset(self.asset_b, expected_price_b, time)  , 4)
            if target_b >0:
                target_b=(min(fund.get_account("investment_shares"), target_b))
            if target_b <0:
                target_b = 0
            #
            print fund.identifier, fund.strategy, "price:", self.asset_a.prices[-1], "expected price a",  expected_price_a,  "expected mu a", "\n"\
            ,  exp_mu_a, "dividend a", self.asset_a.firm.dividend, "funda_v", self.asset_a.funda_v, "target a ", target_a,\
              "has", fund.get_account("A"), "net", fund.get_net_demand_a(target_a),\
               fund.get_account("investment_shares"),  time

            print fund.identifier, fund.strategy, "price:", self.asset_b.prices[-1], "expected price b",  expected_price_b,  "expected mu b", "\n",\
             exp_mu_b,"dividend b", self.asset_b.firm.dividend, "funda_v", self.asset_b.funda_v, "target b", target_b,\
               "has", fund.get_account("B"), "net", fund.get_net_demand_b(target_b),\
                fund.get_account("investment_shares"), time

            # print "net a", fund.get_net_demand_a(target_a), fund.identifier
            # print "net b", fund.get_net_demand_b(target_b), fund.identifier
            # print  "Fund has", fund.get_account('A') , "Fund's target:",  target_a, "Fund net demand", fund.get_net_demand_a(target_a)
            # print  "Fund has", fund.get_account('B'), "B" , "Fund's target:",  target_b, "Fund net demand", fund.get_net_demand_b(target_b)

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
                 for_rationing_b.append([fund, -fund.get_net_demand_b(target_b)])
            else:
                 for_rationing_b.append([fund, -fund.get_net_demand_b(target_b)])
        # now we use rationing to find the actual transactions between agents
        # We also save the aggregate current demand and supply (useful later)
        self.market.current_demand_a =  self.market.return_total_demand(for_rationing_a)
        self.market.current_demand_b =  self.market.return_total_demand(for_rationing_b)
        self.market.current_supply_a =  self.market.return_total_supply(for_rationing_a)
        self.market.current_supply_b =  self.market.return_total_supply(for_rationing_b)

        temp = 0
        if self.market.current_demand_a and self.market.current_supply_a >0:
            temp = 1
            self.count_trade_a.append(temp)
        else:
            temp = 0
            self.count_trade_a.append(temp)

        temp = 0
        if self.market.current_demand_b and self.market.current_supply_b >0:
            temp = 1
            self.count_trade_b.append(temp)
        else:
            temp = 0
            self.count_trade_b.append(temp)



        self.count_trade_a

        print "********************"
        print "Aggregate demand and supply for risky assets in the market(Quantity) at step",time
        print "********************"
        print "A demand:",self.market.current_demand_a, 'A supply:', self.market.current_supply_a
        print "B demand:",self.market.current_demand_b, 'B supply:', self.market.current_supply_b
        logging.info("A demand: %s; A supply: %s at step %s", self.market.current_demand_a, self.market.current_supply_a, time)
        logging.info("B demand: %s; B supply: %s at step %s", self.market.current_demand_b, self.market.current_supply_b, time)

        # print "B demand:",self.market.current_demand_b, 'B supply:', self.market.current_supply_b")

        rationed_a = self.market.rationing_proportional(for_rationing_a)
        rationed_b = self.market.rationing_proportional(for_rationing_b)
        # print "**********", "Rations:"
        # self.show_ration(rationed_a, "A")
        # self.show_ration(rationed_b, "B")
        return rationed_a, rationed_b

    def determine_price_risky_assets(self, environment, excess_a, excess_b, time):
        """
        Let's try exogenous market maker function for price setting according to
        excess demand (see Day and Huang 1990)
        """
        self.asset_a.prices.append(max(0.01, self.market.market_maker( self.asset_a.prices[-1],excess_a )))
        self.asset_b.prices.append(max(0.01,   self.market.market_maker(self.asset_b.prices[-1],excess_b)  )   )

        # Look at the price series if you want
        # print "new price A", self.asset_a.prices
        # print "new price B", self.asset_b.prices
        #Save the new price in environment
        environment.variable_parameters['price_of_b'] = self.asset_b.prices[-1]
        environment.variable_parameters['price_of_a'] = self.asset_a.prices[-1]
        logging.info("New price for A is %s; new price for B is %s; at step %s", environment.variable_parameters['price_of_a'], environment.variable_parameters['price_of_b'], time)
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
                        if self.market.current_supply_a >0:
                            self.market.current_supply_a += -abs(balance_a) * 0.01
                        if self.market.current_supply_a <0:
                            self.market.current_supply_a += abs(balance_a) * 0.01

                        # Net the books
                        for firm in environment.firms:
                                for tranx in seller_a.accounts:
                                    if tranx.type_ == "A":
                                        if tranx.from_ == firm:
                                            tranx.set_amount(tranx.amount - balance_a, environment)
                                            # This is a little trick so avoid double counting
                                            balance_a = 0
        remaining_a_aggregate = 0
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
                # print x, fund.state_variables["net_demand_a"], "a net vs balance"
                remaining_a = abs(fund.state_variables["net_demand_a"]) - abs(x)
                remaining_a_aggregate += remaining_a

            # Set the A account to the new amount
            for tranx in fund.accounts:
                if tranx.type_ == "A" and tranx.to.identifier == fund.identifier and "firm" in tranx.from_.identifier :
                    tranx.set_amount( tranx.amount + x , environment)
        logging.info("  A assets netted on step: %s",  time)
        self.market.current_demand_a = remaining_a_aggregate * 0.01

        "Now everything for B"
        for seller_b in environment.funds:
            for tranx in seller_b.accounts:
                # Find the selling b-transactions
                if tranx.type_ == "B":
                    if tranx.from_.identifier == seller_b.identifier:
                        balance_b = balance_b + tranx.amount

                        # Add to the tracking set
                        to_delete_a.add(tranx)
                        # print balance_a, "balance", seller_a.identifier, "seller"
                        if self.market.current_supply_b >0:
                            self.market.current_supply_b += -abs(balance_b) * 0.01
                        if self.market.current_supply_b<0:
                            self.market.current_supply_b += abs(balance_b) * 0.01

                        # Net the books
                        for firm in environment.firms:
                                for tranx in seller_b.accounts:
                                    if tranx.type_ == "B":
                                        if tranx.from_ == firm:
                                            tranx.set_amount(tranx.amount - balance_b, environment)
                                            # This is a little trick so avoid double counting
                                            balance_b = 0
        remaining_b_aggregate = 0
        #Now we loop over the buyers of A
        for fund in environment.funds:
            # We get the balance amount of new A assets aquired
            # Some funds bought nothing, so the next functions returns None
            #In that case we set the balancing amount to 0
            if self.get_buyer_b_balance_amount(fund) is None:
                x = 0

            #otherwise we get x as balancing amount
            else:
                x = self.get_buyer_b_balance_amount(fund)
                # print x, fund.state_variables["net_demand_a"], "a net vs balance"
                remaining_b = abs(fund.state_variables["net_demand_b"]) - abs(x)
                remaining_b_aggregate += remaining_b

            # Set the A account to the new amount
            for tranx in fund.accounts:
                if tranx.type_ == "B" and tranx.to.identifier == fund.identifier and "firm" in tranx.from_.identifier :
                    tranx.set_amount( tranx.amount + x , environment)
        logging.info("  B assets netted on step: %s",  time)
        self.market.current_demand_b = remaining_b_aggregate * 0.01
        # print "A:",self.market.current_demand_a,    self.market.current_supply_a
        # print "B:",self.market.current_demand_b,   self.market.current_supply_b

        return to_delete_a,  to_delete_b

    def exchange_bonds(self, environment, time):

        net_demand_bonds = 0.0
        ag_demand_bonds = 0.0
        valuation_a, valuation_b, valuation_bond = 0,0,0
        difference = 0.0

        for fund in environment.funds:
            valuation_a = round( fund.get_account("A") * environment.price_of_a, 4)
            valuation_b =  round (fund.get_account("B") * environment.price_of_b, 4)
            valuation_bond = round (fund.get_account("Risk_free") * environment.price_of_bond, 4)

            # #if difference positive, fill in the gap with more risk-free Assets
            #if difference negative, sell risk-free asset until accounts balance
            difference = (round(fund.get_account("investment_shares"),4)-valuation_a -  valuation_b -valuation_bond)
            ag_demand_bonds+= round(difference/environment.price_of_bond, 4)
            net_demand_bonds = round(difference/environment.price_of_bond, 4)

            x = 0
            for tranx in fund.accounts:
                if tranx.from_.identifier == "Government":
                    tranx.set_amount(tranx.amount + net_demand_bonds , environment)
                    # print tranx.amount, net_demand_bonds , environment.price_of_bond , valuation_b  , valuation_a , fund.get_account("investment_shares")
                    x = ( (tranx.amount + net_demand_bonds ) *environment.price_of_bond + valuation_b   + valuation_a)- fund.get_account("investment_shares")
            # net the residual
                if tranx.type_ == "investment_shares":
                    tranx.set_amount(tranx.amount + x, environment)

        return ag_demand_bonds

    def determine_price_riskfree_asset(self, environment, excess_bond, time):
        "update_bond price and yield"
        # excess demand pushes the price upward, excess supply downwards
        price_bond=(self.market.market_maker( environment.price_of_bond, excess_bond ))
        # print environment.price_of_bond, price_bond
        environment.assets[2].prices.append(price_bond)
        environment.variable_parameters['price_of_bond'] = environment.assets[2].prices[-1]

        from functions.bond_price import calc_yield
        new_yield = calc_yield( environment.assets[2].years, environment.assets[2].coupon, -environment.price_of_bond, environment.assets[2].face_value)
        # The new price has an effect on the yield which will affect the new step
        environment.variable_parameters['r_f'] = new_yield
        logging.info("New price for bond is %s; new yield is %s; at step %s",environment.variable_parameters['price_of_bond'], environment.variable_parameters['r_f'] , time)

    def policy_action(self, environment):
        QE = environment.variable_parameters['r_f'] - 4 * (environment.variable_parameters['price_of_bond'] - environment.assets[2].prices[-2])




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
        balance_b = 0
        num_transactions = 0.0

        new_list = []
        for tranx in fund_identifier.accounts:
            # Find the transactions
            if tranx.type_ == "B" and tranx.to.identifier == fund_identifier.identifier and "firm" not in tranx.from_.identifier :
                num_transactions +=1
                new_list.append(tranx)
        for index, value in enumerate(new_list):
            if value.type_ == "B" and value.to.identifier == fund_identifier.identifier and "firm" not in value.from_.identifier :
                balance_b = balance_b + value.amount
                if index == (num_transactions-1):
                    return balance_b
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
        logging.info(" Endowed funds with transactions and investment_shares ")
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
            amount_a = round(fund.calc_demand_asset(self.asset_a, self.asset_a.prices[-1], time), 4)
            amount_b = round(fund.calc_demand_asset(self.asset_b, self.asset_b.prices[-1], time), 4)
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

    def show_ration(self, ration_list, ident):
        """
        Look at the rationing lists with the code below.
        """
        if ident == "A":
            for i, valu in enumerate(ration_list):
                print "A ration %s:" %i
                print "this is the seller %s" %valu[0].identifier
                print "this is the buyer %s" %(valu[1].identifier)
                print "Quantity %s" %valu[2]
        if ident == "B":
            for i, valu in enumerate(ration_list):
                print "B ration %s:" %i
                print "this is the seller %s" %valu[0].identifier
                print "this is the buyer %s" %(valu[1].identifier)
                print "Quantity %s" %valu[2]
        else:
            pass

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
