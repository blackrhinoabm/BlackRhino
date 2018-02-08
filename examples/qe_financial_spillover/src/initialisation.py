from fund import Fund
from functions 

import random

def init_funds(identifiers, thetas, regions, assets):
    """
    :param theta: risk_aversion parameter - list of integers
    :param region: integer
    :return:
    """
 
    #Instantiate investor funds using the number of identifiers as range
    fund_list = []
    # Loop over number of funds
    for i in range(len(identifiers)):
        # loop of identifer strings

        for ident, theta  in zip(identifiers, thetas):
            # Instantiate fund object
            fund = Fund(ident, theta)
            # Save in list
            fund_list.append(fund)


    return fund_list








