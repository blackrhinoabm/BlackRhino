from fund import Fund
import random

def init_funds(identifiers, thetas, regions, percentage_allocation_domestic, assets):
    """
    :param theta: risk_aversion parameter - list of integers
    :param region: integer
    :param assets:
    :return:
    """

    number_domestic =  int(len(identifiers)* percentage_allocation_domestic)
    number_abroad =  percentage_allocation_foreign) * int(len(identifiers))

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

    for fund in fund_list:
        if fund.parameters['region'] == 0:
            for index, value in number_domestic:
                fund.parameters['region'] = "domestic"


    return fund_list








