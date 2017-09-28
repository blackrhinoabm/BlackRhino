#!/usr/bin/env python -W ignore::DeprecationWarning
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-


# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------

import numpy as np

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

        self.results_df = 0
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

        if current_step < 1:
            self.add_rates(environment)
            self.initialize_prices(environment, current_step)

            print "***In t=:", current_step , " This is the price matrix***\n", self.prices, "\n",

            self.initialize_assets_all_agents(current_step, environment)

            self.profit_all_agents(environment, current_step)


        else:

            self.update_all_agents_balance_sheets(environment, current_step, scenario)

            for pf in environment.pensionfunds:
                print pf.results_df
            # self.update_prices(environment, current_step, scenario)
            #
            # print "***In t=0:", current_step , " This is the price matrix***\n", self.prices, "\n",

            # self.system_equity += agent.state_variables['equity']
            # self.system_assets += agent.state_variables['total_assets']

    def initialize_assets_all_agents(self, current_step, environment):
        print "1.**** UPDATER.PY*** FIRST INITIALIZE ASSETS"

        for cbank in environment.cbanks:
            cbank.initialize_assets(self, current_step)

        for hf in environment.hedgefunds:
            hf.initialize_assets(self, current_step)

        for invfund in environment.investmentfunds:
            invfund.initialize_assets(self, current_step)

        for pf in environment.pensionfunds:
            pf.initialize_assets(self, current_step)

        for ic in environment.insurancecompanies:
            ic.initialize_assets(self, current_step)

        for dealer in environment.dealers:
            dealer.initialize_assets(self, current_step, environment)
            # dealer.print_balance_sheet()
            # dealer.check_consistency(current_step)

        for mmf in environment.mmf:
            mmf.initialize_assets(self, current_step, environment)

#####################
    #----------------------------------------------------------------
    # PROFIT FUNCTIONS
    # ------------------------------------------------------------------------
#######################

    def profit_all_agents(self, environment, current_step):
        print "2.**** UPDATER.PY*** Now calculate profit and loss"

        for hf in environment.hedgefunds:
            hf.profit(self, environment, current_step)

        for pf in environment.pensionfunds:
            pf.profit(self, environment, current_step)

        for ic in environment.insurancecompanies:
            ic.profit(self, environment, current_step)

        for invfund in environment.investmentfunds:
            invfund.profit(self, environment, current_step)

        for cbank in environment.cbanks:
            cbank.profit(self, environment, current_step)

        for dealer in environment.dealers:
            dealer.profit(self, environment, current_step)

        for mmf in environment.mmf:
            mmf.profit(self, environment, current_step)

#######################
    def update_all_agents_balance_sheets(self, environment, current_step, scenario):

        for hf in environment.hedgefunds:
            hf.update_balance_sheets(self, environment, current_step, scenario)
            hf.update_results_to_dataframe(current_step)

        for pf in environment.pensionfunds:
            pf.update_balance_sheets(self, environment, current_step, scenario)
            # pf.check_consistency(current_step)

        for ic in environment.insurancecompanies:
            ic.update_balance_sheets(self, environment, current_step, scenario)
            # ic.check_consistency(current_step)

        for invfund in environment.investmentfunds:
            invfund.update_balance_sheets(self, environment, current_step, scenario)
            # invfund.check_consistency(current_step)

        for cbank in environment.cbanks:
            cbank.update_balance_sheets(self, environment, current_step, scenario)
            # cbank.check_consistency(current_step)

        for dealer in environment.dealers:
            dealer.update_balance_sheets(self, environment, current_step, scenario)
            dealer.update_results_to_dataframe(current_step)


        for mmf in environment.mmf:
            mmf.update_balance_sheets(self, environment, current_step, scenario)

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
