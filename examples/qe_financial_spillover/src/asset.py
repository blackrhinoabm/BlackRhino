import pandas as pd


class Asset:

    def __init__(self, identifier, m, rho, omega, face_value, global_supply , price):

        self.identifier = identifier
        self.state_variables = {}
        self.parameters = {"face_value": face_value , "omega" : omega , "m" : m, "rho":rho, "global_supply" : global_supply }
        self.returns = []
        self.prices = [price]
        self.current_price = price



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

    # def __getattr__(self, attr):
    #     if (attr in self.parameters) and (attr in self.state_variables):
    #         raise AttributeError('The same name exists in both parameters and state variables.')
    #     else:
    #         try:
    #             return self.parameters[attr]
    #         except:
    #             try:
    #                 return self.state_variables[attr]
    #             except:
    #                 raise AttributeError('Agent %s has no attribute "%s".' % self.identifier, attr)