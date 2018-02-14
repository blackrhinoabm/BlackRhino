import pandas as pd
from functions.expectation_formation import *
from functions.portfolio import *



class Fund:

    def __init__(self, identifier, lambda_, theta, phi , phi_p, std_noise):
        """How will the assets be saved
        self.assets = { asset.identifier : quantity   }
        # self.exp_returns = { asset.identifier : exp_returns}
        # self.exp_default_probability = { asset.identifier : exp_default}

        The simulation has a big loop (one day) and an intra-day loop (intermediate steps).
        So we save variables for big loops in
        self.exp_var = {}  and
        self.exp_var_intermediate = {} for small loops

        """
        self.parameters = {"lambda": lambda_  , "theta" : theta, "phi": phi, "phi_p": phi_p, "std_noise": std_noise}
        self.identifier = identifier
        self.assets = {}

        self.exp_return = {}
        self.exp_return_intermediate = {}

        self.exp_price = {}
        self.exp_price_intermediate = {}
        # exponentially weighted moving average of prices; needed for calculation of new expected price
        self.ewma_price  = {}
        self.ewma_price_intermediate = {}

        self.exp_default_probability = {}
        self.weights = pd.Series()


        # for var in [fund.assets, fund.exp, fund.exp_default_probatility]
        #     print(var[id])

    def update_expectation(self, assets, asset_identifiers, day):
        """
        Method to update expected asset attribute for next iteration

        1) New expected default probability
        2) New expected prices
        3) New expected returns

        :param assets: dictionary of assets
        :param asset_identifiers: list of asset ident
        :param day: iteration step (big loop)
        :return:
        """

        for ident in asset_identifiers:
            if not 'cash' in ident:
                for key, value in assets.iteritems():
                    new_exp_omega_var = exp_omega(assets[ident].parameters['omega'], assets[ident].news_process,
                                                  self.parameters['theta'], self.exp_default_probability[ident],
                                                  self.parameters['std_noise'], day)
            # Attach to dictionary within fund
            self.exp_default_probability[ident] = new_exp_omega_var




        #2) new expect price
        for ident in asset_identifiers:
            for key, value in assets.iteritems():

                new_exp_price_var  =  exp_price( self.ewma_price[ident],
                                                 self.ewma_price_intermediate[ident],
                                                 self.parameters['phi'],
                                                 assets[ident].current_price,
                                                 assets[ident].prices_intermediate , day)



        # exp_weighted_moving_average(last_exp_w_ma_average, fund.parameters['phi'], variable_of_interest)
        # weights = fund.calc_optimal_pf(asset_dict)

        #Returns of the asset = returns from interest payment, returns from price changes, returns from principal payment

        #1) new exp omega



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
            ret_str = ret_str + '<variable type = asset ' + entry.identifier + " expected default probability= " + str(
                value) + "></variable>\n"

        for entry in self.exp_prices:
            value = self.exp_prices[entry]
            ret_str = ret_str + '<variable type = asset ' + entry.identifier + " expected default probability= " + str(
                value) + "></variable>\n"

        for entry in self.exp_returns:
            value = self.exp_returns[entry]
            ret_str = ret_str + '<variable type = asset ' + entry.identifier + " expected default probability= " + str(
                value) + "></variable>\n"

        return ret_str

    def get_noise(std_noise):
        return np.random.normal(0, std_noise, 1)

