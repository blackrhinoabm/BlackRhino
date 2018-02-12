import pandas as pd
from qe_financial_spillover.src.functions.portfolio import *


class Fund:

    def __init__(self, identifier, theta, phi ):

        self.identifier = identifier
        self.state_variables = {}
        self.parameters = {"theta": theta  , "phi": phi}

        self.weights = pd.Series()

    def update_expectation(self, assets):
        #Returns of the asset = returns from interest payment, returns from price changes, returns from principal payment

        exp_omega, exp_price, exp_exchange_rate, exp_return = 0, 0, 0 ,0
        return exp_omega, exp_price, exp_exchange_rate, exp_return

    def calc_optimal_pf(self, asset_dict):

        print asset_dict

        weights = 0
        return weights

    def print_variables(self):
        print self.state_variables
        print self.parameters


    def __str__(self):
        """
        Class variables: identifier, parameters, state_variables
        Local variables: ret_str, entry, value
        """
        ret_str = "  <agent identifier='" + self.identifier + "'>\n"
        for entry in self.parameters:
            value = self.parameters[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                ret_str = ret_str + "    <parameter type='agent' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
            else:
                raise TypeError
        for entry in self.state_variables:
            value = self.state_variables[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                ret_str = ret_str + "    <variable name='" + entry + "' value='" + str(value) + "'></variable>\n"
            elif isinstance(value, list):
                ret_str = ret_str + "    <variable name='" + entry + "' value='[" + str(value[0]) + "," + str(value[1]) + \
                           "]'></variable>\n"
            else:
                raise TypeError
        # for transaction in self.accounts:
        #     ret_str = ret_str + transaction.write_transaction()
        # ret_str = ret_str + "  </agent>\n"
        return ret_str
