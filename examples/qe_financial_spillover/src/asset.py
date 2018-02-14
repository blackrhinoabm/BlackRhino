import pandas as pd


class Asset:

    def __init__(self, identifier, m, rho, omega, face_value, global_supply , price):

        self.identifier = identifier
        self.state_variables = {}
        self.parameters = {"face_value": face_value , "omega" : omega , "m" : m, "rho":rho, "global_supply" : global_supply }
        self.returns = []
        self.prices_history = []
        self.prices = [price]
        self.prices_intermediate = [price]
        self.current_price = price

        self.news_process = []

    def calc_realised_returns(self, day):
        """
        Saves intermediate realised return in object
        """
        if day ==0: #no price changes
            if "cash" not in self.identifier:
                self.state_variables['intermediate_return'] = self.parameters['face_value']/  ( self.prices[-1] * self.parameters['global_supply']  ) * (self.parameters['rho'] + 1 - self.parameters['m'])
            else:
                self.state_variables['intermediate_return'] =  0.0

    def print_variables(self):
        print self.state_variables
        print self.parameters


    def __str__(self):
        """
        Class variables: identifier, parameters, state_variables
        Local variables: ret_str, entry, value
        """
        ret_str = "  <asset identifier='" + self.identifier + "'>\n"
        for entry in self.parameters:
            value = self.parameters[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                ret_str = ret_str + "    <parameter type='asset' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
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
