import pandas as pd
from qe_financial_spillover.src.functions.portfolio import *
from functions.portfolio import *

class Fund:

    def __init__(self, identifier, lambda_, theta, phi ):

        """How will the assets be saved
        self.assets = { asset.identifier : quantity   }
        """
        # self.assets = { asset.identifier :  quantity   }
        # self.exp_returns = { asset.identifier : expe_returns}
        # self.exp_default_probability = { asset.identifier : exp_default}

        self.identifier = identifier
        self.assets = {}
        self.exp_returns = {}
        self.exp_prices = {}
        self.exp_default_probability = {}
        self.parameters = {"lambda": lambda_  , "theta" : theta, "phi": phi}
        self.weights = pd.Series()
#
    # quantity = fund.assets[id]
    # exp = fund.exp[id]
    # exp_def = fund.exp_default_probatility[id]
#
    # for var in [fund.assets, fund.exp, fund.exp_default_probatility]
    #     print(var[id])

    def update_expectation(self, assets):
        #Returns of the asset = returns from interest payment, returns from price changes, returns from principal payment
        for id in assets:
        #1) new exp omega
            self.exp_default_probatility[id] =exp_omega()
        #2) new expect price

        exp_omega, exp_price, exp_exchange_rate, exp_return = 0, 0, 0 ,0
        # exp_weighted_moving_average(last_exp_w_ma_average, fund.parameters['phi'], variable_of_interest)
        # weights = fund.calc_optimal_pf(asset_dict)

        return exp_omega, exp_price, exp_exchange_rate, exp_return

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

