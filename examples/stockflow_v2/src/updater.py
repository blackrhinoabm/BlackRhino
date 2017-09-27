#!/usr/bin/env python -W ignore::DeprecationWarning
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-


# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------

import numpy as np
import warnings

class Updater():
    #
    #
    # METHODS
    #
    def get_identifier(self):
        return self.identifier

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, environment, runner):
        self.environment = environment
        self.runner = runner


        self.prices = np.array([])
        self.rates={}

        self.system_equity = 0
        self.system_assets = 0

        self.delta_pGB = 0
        self.delta_pGB = 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update_benchmark(self, environment, current_step, scenario):

        """The Update Step is broken down into two steps; i.e.
        first round effects and second round feedback effects.
        """
        if current_step < 1:
            self.add_rates(environment)
            self.initialize_prices(environment, current_step)
            print "***In t=:", current_step , " This is the price matrix***\n", self.prices, "\n",

            print "1.**** UPDATER.PY*** FIRST ROUND EFFECTS:INITIALIZE ASSETS"
            for agent in environment.agents:
                agent.initialize_assets(self, current_step)

            self.profit_all_agents(environment, current_step)

        else:

            self.update_prices(environment, current_step, scenario)
            print "***In t=0:", current_step , " This is the price matrix***\n", self.prices, "\n",

            # self.system_equity += agent.state_variables['equity']
            # self.system_assets += agent.state_variables['total_assets']
#####################
    #----------------------------------------------------------------
    # PROFIT FUNCTIONS
    # ------------------------------------------------------------------------
#######################
    def profit_all_agents(self,environment, current_step):
        self.profit_hf(environment, current_step)
        self.profit_mmf(environment, current_step)
        self.profit_pf(environment, current_step)
        # self.profit_if(environment, current_step)
        # self.profit_ic(environment, current_step)
        # self.profit_bd(environment, current_step)


    def profit_hf(self, environment, current_step):
        for agent in environment.agents:
            if any(c in agent.identifier for c in ("HF", "Hedge Fund", "Hedge Fund")):

                "*check Repo*"
                agent.net_income = agent.stock_variables['GB']* self.i_GB\
                            + agent.stock_variables['CB']* self.i_CB\
                            - agent.stock_variables['Fin_loans']*self.i_L\
                            - agent.Repo * self.i_R\
                            + self.delta_pGB * agent.stock_variables['GB']\
                            + self.delta_pCB * agent.stock_variables['CB']
# (float(self.prices[t+1,1]) -

                print "******* The", agent.identifier, " has profit in t=", current_step+1, "of", agent.net_income
                return agent.net_income

    def profit_mmf(self, environment, current_step):
        for agent in environment.agents:

            if any(c in agent.identifier for c in ("Money Market", "MMF", "Money Market Fund")):

                agent.net_income = agent.reverse_repo * self.i_R
                print "******* The", agent.identifier, " has profit in t=", current_step+1, "of", agent.net_income
                return agent.net_income

    def profit_pf(self, environment, current_step):

        for agent in environment.agents:
            if any(c in agent.identifier for c in ("Pension Fund", "PF", "Pension Fund")):
                print agent.stock_variables
                agent.net_income =  agent.GB * self.i_GB\
                                    + agent.CB * self.i_CB\
                                    - agent.repo * self.i_R\
                                    # - agent.stock_variables['HHPO'] * self.i_R\
                #             - agent.stock_variables['HHPO'] * self.i_R\
                            # + self.delta_pGB * agent.stock_variables['GB']\
                            # + self.delta_pCB * agent.stock_variables['CB']
                print "******* The", agent.identifier, " has profit in t=", current_step+1, "of", agent.net_income
                return agent.net_income

    # def profit_if(self, environment, current_step):
    #
    #     for agent in environment.agents:
    #         if any(c in agent.identifier for c in ("Investment Fund", "IF", "Investment Fund")):
    #
    #             agent.net_income = agent.stock_variables['GB']* self.i_GB\
    #                         + agent.stock_variables['CB']* self.i_CB\
    #                         - agent.Repo * self.i_R\
    #                         - agent.HHPO * self.i_R\
    #                         + self.delta_pGB * agent.stock_variables['GB']\
    #                         + self.delta_pCB * agent.stock_variables['CB']
    #             print "******* The", agent.identifier, " has profit in t=", current_step+1, "of", agent.net_income
    #             return agent.net_income

    def initialize_prices(self, environment, current_step):
        import numpy as np
        columns = 0
        pGB = float(environment.exogenous_parameters['price_GB'])
        pCB = float(environment.exogenous_parameters['price_CB'])

        columns = np.array([['t', 'pGB', 'pCB']])
        values = np.array([current_step, pGB, pCB])

        self.prices = np.vstack((columns, values))
        t = current_step + 1
        self.pGB = float(self.prices[t,1])
        self.pCB = float(self.prices[t,2])
        self.delta_pCB = 0
        self.delta_pGB = 0
        return self.prices, self.pGB, self.pCB,self.delta_pCB, self.delta_pGB

    def update_prices(self, environment, current_step, scenario):
        t = current_step + 1

        if any(c in scenario for c in ("benchmark", "normal", "noshock", "no_shock")):
            import numpy as np
            "In the benchmark simulation the prices stay the same as in the initialisation"
            pGB = environment.exogenous_parameters['price_GB']
            pCB = environment.exogenous_parameters['price_CB']
            new_prices = np.array([current_step, pGB, pCB])

            self.prices = np.vstack((self.prices, new_prices))
            self.pGB = float(self.prices[t,1])
            self.pCB = float(self.prices[t,2])

            if self.prices.shape[0] >2:
                self.delta_pCB = float(self.prices[t,2]) - float(self.prices[current_step,2])
                self.delta_pGB = float(self.prices[t,1]) - float(self.prices[current_step,1])
                # this is to print price change for corporate bonds to screen
                # print "delta corporate bonds is", self.delta_pCB
            else:
                self.delta_pCB = 0
                self.delta_pGB = 0

            return self.prices, self.delta_pCB, self.delta_pGB

# -------------------------------------------------------------------------

    def add_rates(self, environment):

        self.rates['i_R'] = environment.exogenous_parameters['interest_repo']
        self.rates['i_Q']= environment.exogenous_parameters['interest_finloans']
        self.rates['i_L']= environment.exogenous_parameters['interest_loans']
        self.rates['i_D']= environment.exogenous_parameters['interest_deposits']
        self.rates['i_GB'] = environment.exogenous_parameters['interest_GB']
        self.rates['i_CB'] = environment.exogenous_parameters['interest_CB']
        self.rates['haircut'] = environment.exogenous_parameters['haircut']
        self.rates['hc']= environment.exogenous_parameters['haircut']
        return self.rates

        # a standard method for returning attributes from the dectionaries as attributes

    def __getattr__(self, attr):
        if (attr in self.prices) and (attr in self.rates):
            raise AttributeError('The same name exists in both prices and rates')
        else:
            try:
                return (self.prices[int(attr)])
            except:
                try:
                    return self.rates[attr]
                except:
                    raise AttributeError('Updater has no attribute "%s".' % attr)
