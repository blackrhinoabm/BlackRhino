import pandas as pd
from functions.expectation_formation import *
from functions.portfolio import *


class Fund:

    def __init__(self, identifier, lambda_, theta, phi , phi_p,  phi_x, std_noise):
        """

        How stuff is saved:
        The simulation has a big loop (one day) and an intra-day loop (intermediate steps).
        So we save variables for big loops in

        self.exp_var = {}  and
        self.exp_var_intermediate = {} for small loops

        In total, there are     ;  the ewma dicts are needed to get to the expected values

        2 x dictionaries  for expected returns (t & tau )
        4 x dictionaries  for expected prices (price_t & price_tau; ewma_price_t & ewma_price_tau)
        4 x dictionaries  for expected exchange rates  ( x_t & x_tau; ewma_x_t & ewma_x_tau )

        4 x dictionaries  for realised return  ( x_t & x_tau; ewma_x_t & ewma_x_tau )

        1 x dictionary for expected default probability


        """
        self.parameters = {"lambda": lambda_  , "theta" : theta, "phi": phi, "phi_p": phi_p,  "phi_x" : phi_x, "std_noise": std_noise}
        self.identifier = identifier
        self.assets = {}

        #Expectation of returns - dictionaries containing the different assets as keys, expected returns as values
        self.exp_return = {}
        self.exp_return_intermediate = {}

        self.exp_price = {}
        self.exp_price_intermediate = {}
        # exponentially weighted moving average of prices; needed for calculation of new expected price
        # ( M^hat from the paper)
        self.ewma_price = {}  #  EWMMA_t : We have to save the ewma  separately for t and tau
        self.ewma_price_intermediate = {}  # EWMMA_tau

        # Dictionary to access exchange rate expectations
        self.exp_x  = {}
        self.exp_x_intermediate = {}
        self.ewma_x = {}   #  EWMMA_t : We have to save the ewma  separately for t and tau
        self.ewma_x_intermediate = {}  # EWMMA_tau

        self.exp_default_probability = {}

        self.weights = pd.Series()

        # Dictionary to access realised returns per asset
        self.realised_returns = {}
        self.realised_returns_intermediate = {}
        self.ewma_realised_returns = {}  # EWMMA_t
        self.ewma_realised_returns_intermediate = {}   # EWMMA_tau
        # for var in [fund.assets, fund.exp, fund.exp_default_probatility]
        #     print(var[id])

    def update_expectation(self, assets,  exchange_rate, day):
        """
        Method to update expected asset attribute for next iteration

        1) New expected default probability
        2) New expected prices, exchange rates
        3) New expected returns

        4) Get realised returns for covariance variance matrix
        5) Compute new ewma for returns
        6) Use latest realised return and ewma return for covariance
        5) Calculate new ewma covariance
        6) Plug it into portfolio optimisation
        7) get weights  ... phew!

        :param assets: dictionary of assets
        :param exchange_rate dictionary with exchange rate list
        :param day: iteration step (big loop)
        :return:
        """
        #1) New expected default probability
        for key, value in assets.iteritems():
            if not 'cash' in key:

                new_exp_omega_var = exp_omega(assets[key].parameters['omega'], assets[key].news_process,
                                          self.parameters['theta'], self.exp_default_probability[key],
                                          self.parameters['std_noise'], day)
        # Attach to dictionary within fund
        self.exp_default_probability[key] = new_exp_omega_var

        #2) a ) new expected price for all assets
        for key, value in assets.iteritems():
            new_exp_price_var  =  exp_price( self.ewma_price[key],
                                             self.parameters['phi_p'],
                                             assets[key].current_price)
            self.exp_price_intermediate[key] = new_exp_price_var

        #2) b) #) new expected exchange rates
        current_x =  exchange_rate['x_domestic_to_foreign'][-1]

        new_exp_x_var = exp_price(self.ewma_x['x_domestic_to_foreign'],
                                    self.parameters['phi_x'],
                                    current_x)

        self.exp_x_intermediate['x_domestic_to_foreign'] = new_exp_x_var
        #
        #3) Expected returns of the asset = returns from interest payment, returns from price changes, returns from principal payment
        #   Expected returns for abroad assets include an exchange rate component

            #So  I) exp_return_home_asset
             #  II) exp_return_abroad_asset

        for key, value in assets.iteritems():
        #Check if assets are in the same region as fund, in that case we need expected
        #exchange rates in the return calculation
        # First, the easy case; asset and funds are in the same region
            if value.parameters['region'] == self.parameters[ 'region']:
                new_exp_r_var = exp_return_home_asset(key,
                                                        value.parameters['rho'],  # nominal interest rate of asset
                                                      value.parameters['m'],  # constant repayment parameter
                                                      value.parameters['face_value'],
                                                      self.exp_default_probability[key],  # expected omega
                                                      self.exp_price_intermediate[key],
                                                      value.current_price,  # actual price
                                                      value.parameters['global_supply'])  # global supply/quantity

                self.exp_return_intermediate[key] = new_exp_r_var

         # So we have the home assets, now we need the abroad assets' expected returns. Be careful with the perspective: for a foreign
         # fund, the "foreign" asset is domestic, and the "domestic" asset is foreign

            if value.parameters['region'] != self.parameters['region']:  # Asset and fund are not in the same region

                new_exp_r_var = exp_return_abroad_asset(key, self.parameters['region'], # asset identifier and region of fund
                                                        value.parameters['rho'],  # nominal interest rate of asset
                                                        value.parameters['m'],  # constant repayment parameter
                                                        value.parameters['face_value'],
                                                        self.exp_default_probability[key],  # expected omega
                                                        self.exp_price_intermediate[key],
                                                        value.current_price,  # actual price
                                                        value.parameters['global_supply'],  # global supply/quantity of the asset
                                                        exchange_rate, # actual exchange rate dictionary
                                                        self.exp_x_intermediate)  # expected exchange rate dictionary
                self.exp_return_intermediate[key] = (new_exp_r_var)

        #4) get realised returns for covariance variance matrix
        # Be careful with the regions again

        for key, value in assets.iteritems():
            # Assign variables; in the first step, previous price is current price; otherwise it's the second last entry in asset.prices[-2]

            if day == 0:
                previous_price = value.current_price
            else:
                previous_price = value.prices[-2]  # Which price?  t, never tau!!

            # First, the easy case; asset and funds are in the same region - no exchange rate effects
            if value.parameters['region'] == self.parameters['region']:
                new_re_return = realised_return_home_asset(key,
                                                           value.parameters['rho'],  # nominal interest rate of asset
                                                           value.parameters['m'],  # constant repayment parameter
                                                           value.parameters['face_value'],
                                                           value.current_price, # actual price
                                                           previous_price,  # previous  price
                                                           value.parameters['global_supply'])  # global supply/quantity

                self.realised_returns_intermediate[key] = (new_re_return)

            if value.parameters['region']!= self.parameters['region']:
                new_re_return = realised_return_abroad_asset(key, self.parameters['region'],
                                                           value.parameters['rho'],
                                                           # nominal interest rate of asset
                                                           value.parameters['m'],  # constant repayment parameter
                                                           value.parameters['face_value'],
                                                            value.current_price,  # actual price
                                                           previous_price,  # previous  price
                                                           value.parameters['global_supply'],
                                                            exchange_rate, day)  # global supply/quantity
                self.realised_returns_intermediate[key] = (new_re_return)

        # Investor funds only hold regional cash. Since we are using this dictionary for covariance-variance matrix
        # we need to delete the abroad cash from the books
        if self.parameters['region'] == "domestic":
            del self.realised_returns_intermediate["foreign_cash"]

        if self.parameters['region'] == "foreign":
            del self.realised_returns_intermediate["domestic_cash"]

       # 5) Compute new ewma for realised returns

        for key, value in assets.iteritems():
            #We simplify and take the first ewma as the actual return
            if day == 0:
                 if key in self.realised_returns_intermediate:

                    self.ewma_realised_returns_intermediate[key] = self.realised_returns_intermediate[key]
            #
                    new_ewma  = exp_weighted_moving_average(self.ewma_realised_returns_intermediate[key], self.parameters['phi'], self.realised_returns_intermediate[key])
                    self.ewma_realised_returns[key] = new_ewma


        print  self.ewma_realised_returns

        # new_Covariance_(return r_domestic_low, return r_domestic_high)



        # covariance
        # weighted_covariance
        # portfolio
        # price clearing
        # weights = fund.calc_optimal_pf(asset_dict)   



    def calc_optimal_pf(self, asset_dict):

        print asset_dict

        weights = 0
        return weights

    def print_variables(self):
        print self.assets
        print self.parameters


    def __str__(self):
        ret_str =  "<fund identifier=" + self.identifier + ">\n"
        for entry in self.parameters:
            value = self.parameters[entry]
            ret_str = ret_str + '<parameter ' + entry  + "=" + str(value) + "></parameter>\n"

        for entry in self.assets:
            value = self.assets[entry]
            ret_str = ret_str + '<variable type = asset ' + entry.identifier + " quantity= " + str(value) + "></variable>\n"

        for entry in self.exp_default_probability:
            value = self.exp_default_probability[entry]
            ret_str = ret_str + '<variable type = asset ' + entry + " expected_default_probability= " + str(
                value) + "></variable>\n"

        for entry in self.exp_price:
            value = self.exp_price[entry]
            ret_str = ret_str + '<variable type = asset ' + entry + " expected_price= " + str(
                value) + "></variable>\n"

        return ret_str

    def get_noise(std_noise):
        return np.random.normal(0, std_noise, 1)

