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
import random
import logging
from src.transaction import Transaction

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
    interactions = None

    #
    #
    # METHODS
    #
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Updater, self).set_identifier(_value)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, _value):
        super(Updater, self).set_model_parameters(_value)

    def get_interactions(self):
        return self.interactions

    def set_interactions(self, _value):
        super(Updater, self).set_interactions(_value)

    def __str__(self):
        return super(Updater, self).__str__()

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self,  environment):
        self.environment = environment
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self,  environment,  time):
        # As a first step, we accrue all interest over the transactions
        # Thus, important to notice to keep 0 as interest by default
        # Unless transaction should carry interest
        # DON'T DO INTERESTS SO FAR, DO ONCE THE REST WORKS
        # self.find_interbank_liquidity(environment, time)
        self.accrue_interests(environment, time)
        self.maturities(environment, time)
        self.amortisation(environment, time)
        self.get_funding(environment, time)
        # TODO: make sure finding in firms is positive
        # The households sell labour to firms
        self.sell_labour(environment, time)
        # The firms sell goods to households
        self.consume_rationed(environment, time)
        # We net deposits and loans
        # self.net_loans_deposits(environment, time)
        # We remove the perishable transactions
        self.remove_perishable(environment, time)
        # And add capital to balance the books
        # self.capitalise(environment, time)
        self.capitalise_new(environment, time)
        # Investing of the banks
        # self.invest(environment, time)
        # self.invest_interbank(environment, time)
        # Purging accounts at every step just in case
        transaction = Transaction()
        transaction.purge_accounts(environment)
        # And finally we check if all the books are balanced
        # print(environment.banks[0])
        # print(environment.firms[0])
        # print(environment.households[0])
        # TODO here:
        # - simplify the code
        # - careful about acrrue interests - so it doesn't explode, and think about the fluctuations
        # - so banks will have A: loans(investments)+reserves L: deposits+cb_loans
        self.check_consistency(environment, time)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # accrue_interests(environment, time)
    # This method accrues interest on all transaction
    # making sure we don't double count the transactions that are
    # on the books of multiple agents, interest is specified within the
    # transaction itself
    # -------------------------------------------------------------------------
    def accrue_interests(self,  environment, time):
        # First, add interests to all the transactions
        # The function in environment makes sure we don't double count interests
        # environment.accrue_interests()
        for bank in environment.banks:
            for tranx in bank.accounts:
                if tranx.type_ == "loans" or tranx.type_ == "deposits" or tranx.type_ == "ib_loans":
                    tranx.from_.funding = tranx.from_.funding + tranx.amount * tranx.interest
                    tranx.to.funding = tranx.to.funding - tranx.amount * tranx.interest
                elif tranx.type_ == "cb_loans":
                    tranx.to.funding = tranx.to.funding - tranx.amount * tranx.interest
                elif tranx.type_ == "cb_reserves":
                    tranx.from_.funding = tranx.from_.funding - tranx.amount * tranx.interest
                else:
                    pass

        # Do dividends
        for bank in environment.banks:
            if round(bank.funding, 3) > 0.0:
                num_households = len(environment.households)
                to_fund = bank.funding / num_households
                for household in environment.households:
                    household.funding = household.funding + to_fund
                bank.funding = 0.0
            elif round(bank.funding, 3) == 0.0:
                pass  # do nothing, neutral on interests
            else:
                raise LookupError("Bank has negative position on interests. To implement.")
                # num_households = len(environment.households)
                # to_fund = bank.funding / num_households
                # for household in environment.households:
                #     household.funding = household.funding + to_fund
                # bank.funding = 0.0
                # Should that not be negative funding to households (negative dividend)?
        logging.info("  interest accrued on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # maturities(environment, time)
    # -------------------------------------------------------------------------
    def maturities(self,  environment, time):
        # Update maturities
        already_matured = []
        for agent in environment.agents_generator():
            for tranx in agent.accounts:
                if (int(tranx.maturity) > 0):  # reduce maturity if duration longer than 0
                    if tranx not in already_matured:
                        tranx.maturity = int(tranx.maturity) - 1
                        already_matured.append(tranx)

            # If maturity is zero then we must remove the transaction
            # (remembering the economics properly)
            # liquidate_due_transactions()
        to_delete = []
        for firm in environment.firms:
            for tranx in firm.accounts:
                if tranx.type_ == "deposits":
                    to_delete.append(tranx)
                    tranx.from_.funding = tranx.from_.funding + tranx.amount
        for tranx in to_delete:
            tranx.remove_transaction()

        to_delete = []
        for household in environment.households:
            for tranx in household.accounts:
                if tranx.type_ == "deposits":
                    to_delete.append(tranx)
                    tranx.from_.funding = tranx.from_.funding + tranx.amount
        for tranx in to_delete:
            tranx.remove_transaction()

        to_delete = []
        for bank in environment.banks:
            for tranx in bank.accounts:
                if ((tranx.type_ == 'loans') and (int(tranx.maturity) == 0)):
                    tranx.to.funding = tranx.to.funding - float(tranx.amount)
                    to_delete.append(tranx)
                    # Nor particularly necessary since banks close books anyway
                    # tranx.from_.liquidity = tranx.from_.liquidity + float(tranx.amount))
        for tranx in to_delete:
            tranx.remove_transaction()
        logging.info("  maturities resolved on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # amortisation(environment, time)
    # -------------------------------------------------------------------------
    def amortisation(self,  environment, time):
        # We perform amortisation of capital at each firm
        # the amortisation parameter shows the % of capital
        # that is lost at each time step (due to age, use, etc.)
        for firm in environment.firms:
            # And here it's depreciated
            firm.capital = firm.capital * (1 - firm.amortisation)
        logging.info("  capital amortisation performed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_funding(environment, time)
    # -------------------------------------------------------------------------
    def get_funding(self,  environment, time):
        # This part is for kickstarting the simulation
        # We give each firm starting capital of 30
        # And a loan of equal value from a random bank
        if time == 0:
            for firm in environment.firms:
                firm.funding = 100.0
                random_bank = random.choice(environment.banks)
                environment.new_transaction("loans", "",  random_bank.identifier, firm.identifier,
                                            firm.funding, random_bank.interest_rate_loans,  2, -1)
        # During the simulation, i.e. after the first time step
        # We find the amount of new loans based on the previous capital stock
        # (we assume firms want to have a specific), and existing loans
        else:
            # For every firm
            for firm in environment.firms:
                # We find the demand for loans in the firms
                # As difference between demand for capital and labour minus the existing loans
                # here we assume, as in the rest of the code that price of labour and capital is equal
                to_delete = []
                for tranx in firm.accounts:
                    if tranx.type_ == "deposits":
                        firm.funding = firm.funding + tranx.amount / 10.0
                        to_delete.append(tranx)
                for tranx in to_delete:
                    tranx.remove_transaction()
                target_loans = 1.1 * firm.capital * 10.0  # TO THINK ABOUT
                new_loans = target_loans - firm.get_account("loans")
                # If we have loans to take
                if new_loans > 0.0:
                    # We take it with the random bank (HERE PORTFOLIO STUFF WILL HAPPEN LATER)
                    random_bank = random.choice(environment.banks)
                    # We add new loans to the funding
                    firm.funding = firm.funding + new_loans
                    # And add the loan to the books
                    environment.new_transaction("loans", "",  random_bank.identifier, firm.identifier,
                                                new_loans, random_bank.interest_rate_loans,  2, -1)
                # If we have too much funding already
                # Remember to check funding at the end and sell capital if necessary

                total_funding = firm.funding + firm.capital * 10.0
                firm.capital = firm.capital_elasticity * total_funding / 10.0
                firm.funding = (1 - firm.capital_elasticity) * total_funding
            logging.info("  funding performed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # sell_labour(environment, time)
    # This function allows the households to sell their labour to firms
    # For now we assume that firms want to buy all the labour they can get
    # And that they need to use cash for this purpose, they can't take loans
    # And firms keep cash, they do not keep deposits, these will be updated
    # in later time
    # -------------------------------------------------------------------------
    def sell_labour(self,  environment, time):
        for firm in environment.firms:
            firm.parameters["labour"] = 0.0
        # First we find the market equilibrium price
        # Important to note that this currently does
        # not depend on the wealth of the buyers
        # That is their demand may be higher than
        # what they can actually buy, which may be ok
        # We set the values necessary for tatonnement
        # The list of sellers and their supply functions
        sellers = []
        for agent in environment.households:
            sellers.append([agent, agent.supply_of_labour_solow])
        # And the list of buyers and their demand functions
        buyers = []
        for agent in environment.firms:
            print(agent.capital)
            buyers.append([agent, agent.demand_for_labour_grid])
        # We may start the search for price at some specific point
        # Here we pass 0, which means it'll start looking at a
        # random point between 0 and 10

        if time == 0:
            self.price = 10.0
            price = self.price
            # We initialize the price
        else:
            from random import Random
            random = Random()
            oldValue = self.price
            newValue = 0.0
            scaleFactor = 0.01

            newValue = max((1.0 - scaleFactor + 2.0*scaleFactor*random.random())*oldValue, 0.0)  # make sure we have only positive prices

            self.price = newValue
            price = self.price

        # Import market clearing class
        from market import Market
        # Put the appropriate settings, i.e. desired identifier
        market = Market("market")
        # And we find the market price of labour
        # given supply and demand of the agents
        # and tolerance of error, resolution of search
        # and amplification factor for exponential search
        price = market.tatonnement(sellers, buyers, price, 0.001, 0.01, 1.1)
        environment.variable_parameters["price_of_labour"] = price
        # now we use rationing to find the actual transactions between agents
        for_rationing = []
        for household in environment.households:
            for_rationing.append([household, household.supply_of_labour_solow(price)])  # TODO: some function of price, maybe the original now, since it's constrained anyway
            # for_rationing.append([household, household.labour])
        for firm in environment.firms:
            for_rationing.append([firm, -firm.funding/price])
        # And we find the rationing, ie the amounts
        # of goods sold between pairs of agents
        rationed = market.rationing_proportional(for_rationing)
        #
        #             A (from)    L (to)
        # bank        loan        deposit
        # household   deposit     labour
        # firm        labour      loan
        #
        for ration in rationed:
            # The labour is an asset (production factor) for the firm
            # and a liability (promise to work) for the household
            # ration[0]: household
            # ration[1]: firm
            ration[1].parameters["labour"] = ration[1].parameters["labour"] + ration[2]
            # random_bank = random.choice(environment.banks)
            # Deposit is a liability of the bank
            # and an asset of the household
            ration[0].funding = ration[0].funding + ration[2]*price
            # environment.new_transaction("deposits", "",  ration[0].identifier, random_bank.identifier,
            #                             ration[2]*price, random_bank.interest_rate_deposits,  -1, -1)
            # random_bank = random.choice(environment.banks)
            # Loan is an asset of the bank
            # and a liability of the firm
            ration[1].funding = ration[1].funding - ration[2]*price
            # environment.new_transaction("loans", "",  random_bank.identifier, ration[1].identifier,
            #                             ration[2]*price, random_bank.interest_rate_loans,  -1, -1)
            # We print the action of selling to the screen
            print("%s sold %d units of labour at a price %f to %s at time %d.") % (ration[0].identifier,
                                                                                   ration[2], price, ration[1].identifier, time)

        logging.info("  labour sold to firms on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # consume_rationed(environment, time)
    # This function lets households buy the goods the firms have produced
    # so they can satisfy their needs through consumption
    # This consumption depends on the propensity to save of the households
    # The matching of buyers and sellers on the market is random
    # -------------------------------------------------------------------------
    def consume_rationed(self, environment, time):
        # We want the consumption to be done in random pairs
        # We use rationing from market clearing class to do that
        # Price is static for this example, otherwise we can't use rationing
        # and need some other market clearing
        price = 10.0
        environment.variable_parameters["price_of_goods"] = price
        # We need a list of agents and their demand or supply
        # Supply is denoted with positive float, demand with negative float
        for_rationing = []
        # Firms give us their supply, we assume that since the goods are
        # perishable their supply is all they have in stock
        from src.helper import Helper
        helper = Helper()
        for firm in environment.firms:
            # Firms produce based on their capital, for generality
            # we use their net capital, as in their capital stock
            # minus the capital owned of other agents
            # We find the amount produced through the Cobb-Douglas function
            amount = helper.cobb_douglas(firm.parameters["labour"], firm.capital,
                                         firm.total_factor_productivity, firm.labour_elasticity, firm.capital_elasticity)*price
            # And assume firm wants to sell whole production given the perishable nature of the goods
            for_rationing.append([firm, amount])
        # Here firms sell
        # TODO
        for ration in for_rationing:
            ration[0].funding = ration[0].funding + ration[1]*price
        # Households give use their demand, we assume that they want to
        # consume the part of their wealth (cash and deposits) that they
        # do not want to save (determined through propensity to save)
        # We denote demand in units of the goods, so we divide the cash
        # households want to spend by price to get the demand
        for_rationing = []
        for household in environment.households:
            demand = 0.0
            wealth = 0.0
            # For generality we calculate net wealth for this, that is the
            # amount of deposits they carry minus the amount of loans
            for tranx in household.accounts:
                if tranx.type_ == "deposits" and tranx.from_ == household:
                    wealth = wealth + tranx.amount
                if tranx.type_ == "loans" and tranx.to == household:
                    wealth = wealth - tranx.amount
            # Then the demand is determined by the agent's propensity to save
            # and the wealth calculated above
            wealth = wealth + household.funding
            print("wealth")
            print(wealth)
            demand = ((wealth * (1 - household.propensity_to_save)) / price)
            for_rationing.append([household, demand])
        # We import the market clearing class
        for ration in for_rationing:
            ration[0].funding = ration[0].funding - ration[1]*price
        logging.info("  goods produced, sold, and consumed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # remove_perishable(environment, time)
    # This function removes the perishable transactions in the system
    # which need to be removed from the books before the end of the step
    # all methods that use these temporary transactions need to be invoked
    # before this method, currently it removes labour and goods
    # -------------------------------------------------------------------------
    def remove_perishable(self,  environment, time):
        for firm in environment.firms:
            firm.parameters["labour"] = 0.0

        for firm in environment.firms:
            if firm.funding >= 0.0:
                # add a deposit
                one_deposits = firm.funding/len(environment.banks)  # add a network here later
                for bank in environment.banks:
                    environment.new_transaction("deposits", "",  firm.identifier, bank.identifier,
                                                one_deposits, bank.interest_rate_deposits,  -1, -1)
                # random_bank = random.choice(environment.banks)
                # environment.new_transaction("deposits", "",  firm.identifier, random_bank.identifier,
                #                             firm.funding, random_bank.interest_rate_deposits,  -1, -1)
                firm.funding = 0.0
            else:
                raise LookupError("Firm has negative funding at the end of the step.")

        for household in environment.households:
            if household.funding >= 0.0:
                # add a deposit
                one_deposits = firm.funding/len(environment.banks)  # add a network here later
                for bank in environment.banks:
                    environment.new_transaction("deposits", "",  firm.identifier, bank.identifier,
                                                one_deposits, bank.interest_rate_deposits,  -1, -1)
                # random_bank = random.choice(environment.banks)
                # environment.new_transaction("deposits", "",  household.identifier, random_bank.identifier,
                #                             household.funding, random_bank.interest_rate_deposits,  -1, -1)
                household.funding = 0.0
            else:
                # remove old deposits randomly (can do proportional but let's have some fun)
                if abs(household.funding) <= household.get_account("deposits"):
                    # remove the deposits
                    for tranx in household.accounts:
                        if tranx.type_ == "deposits":
                            to_remove = min(abs(household.funding), tranx.amount)
                            tranx.amount = tranx.amount - to_remove
                            household.funding = household.funding + to_remove
                else:
                    raise LookupError("Household has more shortfall than deposits.")

        logging.info("  perishables removed on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # capitalise_new(environment, time)
    # This function makes capital transactions which represent final
    # ownership of firms by the household which is done through the bank
    # deposits and bank loans, these are in principle not necessary for the
    # model to work, as we can assume the loans are the capital, and produce off
    # that assumption, but this ensures the books are balanced for all agents
    # -------------------------------------------------------------------------
    def capitalise_new(self,  environment, time):
        #
        # add reserves
        #
        to_delete = []
        for tranx in environment.central_bank[0].accounts:
            if tranx.type_ == "cb_reserves":
                to_delete.append(tranx)
        for tranx in to_delete:
            tranx.remove_transaction()
        for bank in environment.banks:
            reserves = environment.required_reserves * bank.get_account("deposits")
            environment.new_transaction("cb_reserves", "",  bank.identifier, environment.central_bank[0].identifier,
                                        reserves, 0,  -1, -1)
        #
        # add interbank market
        #
        for_rationing = []
        from market import Market
        # Put the appropriate settings, i.e. desired identifier
        market = Market("market")
        to_delete = []
        for bank in environment.banks:
            demand = -bank.get_account("loans")-bank.get_account("cb_reserves")+bank.get_account("deposits")
            for tranx in bank.accounts:
                if tranx.type_ == "ib_loans":
                    to_delete.append(tranx)
            for_rationing.append([bank, demand])
        for tranx in to_delete:
            tranx.remove_transaction()
        rationed = market.rationing_proportional(for_rationing)
        for ration in rationed:
            environment.new_transaction("ib_loans", "",  ration[0].identifier, ration[1].identifier,
                                        ration[2], 0,  -1, -1)
            # And print it to the screen for easy greping
            print("%s lent %f worth of interbank loans to %s at time %d.") % (ration[0].identifier,
                                                                              ration[2], ration[1].identifier, time)

        #
        # central bank loans
        #

        to_delete = []
        for tranx in environment.central_bank[0].accounts:
            if tranx.type_ == "cb_loans":
                to_delete.append(tranx)
        for tranx in to_delete:
            tranx.remove_transaction()

        for bank in environment.banks:
            # Then we add or remove central bank loans
            # We assume that since there is only one central bank we can keep those
            # in one transaction for now, if we fiddle with maturities this may change
            # If we don't yet have a central bank loan we create one
            cb_volume = bank.get_account("loans") + bank.get_account("cb_reserves") - bank.get_account("deposits")
            for tranx in bank.accounts:
                if tranx.type_ == "ib_loans":
                    if tranx.from_ == bank:
                        cb_volume = cb_volume + tranx.amount
                    elif tranx.to == bank:
                        cb_volume = cb_volume - tranx.amount
            if cb_volume > 0.0:
                environment.new_transaction("cb_loans", "",  environment.central_bank[0].identifier, bank.identifier,
                                            cb_volume, environment.central_bank[0].interest_rate_cb_loans,  -1, -1)
            elif cb_volume < 0.0:
                environment.new_transaction("cb_reserves", "",  bank.identifier, environment.central_bank[0].identifier,
                                            -cb_volume, environment.central_bank[0].interest_rate_cb_loans,  -1, -1)
        #
        # excess reserves ???
        #

        logging.info("  capitalised on step: %s",  time)
        # Keep on the log with the number of step, for debugging mostly
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # check_consistency(environment, time)
    # This function checks whether the books of agents are balanced
    # Based on the functions defined for agents
    # Note that central bank does not have a balanced book as they can
    # always create money, so to speak
    # -------------------------------------------------------------------------
    def check_consistency(self, environment, time):
        for bank in environment.banks:
            check_status = bank.check_consistency()
            if check_status is False:
                print(bank)
                raise LookupError("Bank's books are not balanced.")
        # for firm in environment.firms:
        #     check_status = firm.check_consistency()
        #     if check_status is False:
        #         print(firm)
        #         raise LookupError("Firm's books are not balanced.")
        # for household in environment.households:
        #     check_status = household.check_consistency()
        #     if check_status is False:
        #         print(household)
        #         raise LookupError("Household's books are not balanced.")
    # -------------------------------------------------------------------------
