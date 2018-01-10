
import logging
import os
import numpy as np
import matplotlib.pyplot as plt

def init_firms(environment, firm_directory, time):
    initialize_firms_from_files(environment, firm_directory, time)


def init_funds(environment, fund_directory, time):
    initialize_funds_from_files(environment, fund_directory, time)
    allocate_fund_size(environment)
    init_fund_type(environment)

def init_assets(environment, asset_directory, time):
    initialize_shares(environment, asset_directory, time)
    initialize_bond_from_files(environment, asset_directory)
    init_asset_prices(environment)

def initialize_shares(environment, asset_directory, time):
    from src.asset import Asset_risky
    for i in environment.firms:
        asset = Asset_risky(i)
        environment.assets.append(asset)

def initialize_bond_from_files(environment, asset_directory):

    from src.asset import Asset_riskfree

    asset_files = os.listdir(asset_directory)

    for each_agent_file in asset_files:

        if '.xml' in each_agent_file:
            bond = Asset_riskfree()
            agent_filename = asset_directory + each_agent_file
            bond.get_parameters_from_file(agent_filename, environment)

            environment.assets.append(bond)

    logging.info('Fetched bond data and read into program')

def init_asset_prices(environment):
    """
    Assets A and B are intiantilized with a randomized initial price
    pA and pB.

    Bond is initialised with given return (e.g. 5%)
    and price is calculated with calc_bond_price

    Calls method init_return in same script.

    Argument
    Environment
    ===

    Result
    ===
    2 asset objects, stored in environment.assets[]

    """
    import random
    pA = round(random.randint(38, 38),4)
    environment.assets[0].funda_values.append(environment.assets[0].funda_v)
    environment.assets[1].funda_values.append(environment.assets[1].funda_v)
    print environment.assets[0].funda_v, environment.assets[1].funda_v, "Fundamental values"

    pB = round(random.randint(24, 25),4)
    print pB, "Initialisation pB"
    print pA, "Initialisation pA"

    prices_a = [random.uniform(37, 39) for _ in range(int(1))]
    prices_b = [random.uniform(24, 25) for _ in range(int(1))]

    prices_a.append(pA)
    prices_b.append(pB)

    environment.prices.append(prices_a)
    environment.prices.append(prices_b)


    # print "Price history of A:", prices_a
    # print "Price history of B:", prices_b

    environment.variable_parameters['price_of_b'] = pB
    environment.variable_parameters['price_of_a'] = pA

    for i in environment.assets:
        if i.identifier == "A":
            i.mu = init_return(i.firm.dividend, pA)
            environment.variable_parameters['mu_a'] = i.mu
            # print i.mu
            i.prices.extend(prices_a)
        if i.identifier == "B":
            i.mu = init_return(i.firm.dividend, pB)
            environment.variable_parameters['mu_b'] = i.mu
            # print i.mu
            i.prices.extend(prices_b)
        else:
            pass
    logging.info(" Price of A initialised at %s per unit  ",  pA  )
    logging.info(" Price of B initialised at %s per unit  ",  pB )

    """For the deterministic bond price (present value) we use the
    bond price formula stored in functions/bond_price
    and parameters read in from bond config file.
    Alternatively, just pass in the values (see uncommented example)
    """
    from functions.bond_price import calc_bond_price
    environment.variable_parameters['price_of_bond'] = round(calc_bond_price(100, 10, environment.variable_parameters["r_f"] , 0, 2),4)

    environment.assets[2].prices.append(environment.variable_parameters['price_of_bond'])
    logging.info(" Price of bond initialised at %s per unit",  environment.variable_parameters['price_of_bond'] )

    environment.prices.append(environment.assets[2].prices)

    # environment.variable_parameters['price_of_bond'] = calc_bond_price(100, 10, environment.variable_parameters["r_f"] , 0, 2)

def init_return(div, current):
    return div/current

def init_fund_type(environment):
    """
    Initialize fund type (fundamentalists vs chartist).
    Not the most elegant code, but it works.

    Arguments
    ===
    Share of fundamentalists and chartists from Environment.variable_parameters

    Result
    ===
    Funds receive a state variable str "strategy", as well as float gamma_c or gamma_f according to
    proportions defined in environment config file.

    """
    import random
    gamma_fs = [random.uniform(0, 1) for _ in range(int((environment.variable_parameters["fundamentalists"]*len(environment.funds))))]
    gamma_cs = [random.uniform(1, 1.5) for _ in range(int((environment.variable_parameters["chartists"]*len(environment.funds))))]

    fundamentalist_guys = [fundamentalist_guy for fundamentalist_guy in range(int((environment.variable_parameters["fundamentalists"]*len(environment.funds))))]
    for index, agent in zip(fundamentalist_guys, environment.funds):
        agent.state_variables['strategy'] = "fundamentalist"
        agent.parameters['initial_strategy'] = "fundamentalist"

    for i in environment.funds:
        if not hasattr(i, "strategy"):
            i.state_variables['strategy'] = "chartist"
            i.parameters['initial_strategy'] = "chartist"

    for index, agent in zip(gamma_fs, environment.funds):
        if agent.strategy == "fundamentalist":
            agent.state_variables["gamma_f"]  = index

    other_agents=[]
    for agent in (environment.funds):
        if agent.state_variables['strategy'] == "chartist":
            other_agents.append(agent)

    for index, agent in zip(gamma_cs, other_agents):
        agent.state_variables["gamma_c"] = index

def initialize_firms_from_files(environment, firm_directory, time):
    from src.firm import Firm
    while len(environment.firms) > 0:
        environment.firms.pop()

    agent_files = os.listdir(firm_directory)

    for each_agent_file in agent_files:

        if '.xml' in each_agent_file:
            agent = Firm()
            agent_filename = firm_directory + each_agent_file
            agent.get_parameters_from_file(agent_filename, environment)
            environment.firms.append(agent)

    logging.info('Fetched firms data and read into program')

def init_profits(environment, time):
    "Add some variables to firms and initialize profits"
    # for firm in environment.firms:
    #      firm.add_stuff( initial_profit=[firm.initial_profit] ,growth = [0])
    for firm in environment.firms:
        if firm.domicile == 0:
            brown_delta_a = firm.brown_delta
        if firm.domicile == 1:
            brown_delta_b = firm.brown_delta

    from src.functions.brownian_motion import brownian_process_individual

    x_a = brownian_process_individual(100, environment.num_sweeps, 1, brown_delta_a )
    x_a = np.divide(x_a, 100)

    x_b = brownian_process_individual(100, environment.num_sweeps, 1, brown_delta_b)
    x_b = np.divide(x_b, 100)

    for firm in environment.firms:
        if firm.domicile == 0:
            x_a[0] = np.multiply(x_a[0], firm.initial_profit)
        if firm.domicile == 1:
            x_b[0] = np.multiply(x_b[0], firm.initial_profit)
    #
    profit_history1 = x_a[0].tolist()
    profit_history2 = x_b[0].tolist()
    # plt.plot(profit_history1 )
    # plt.plot(profit_history2 )
    # # plt.legend(["a", "b"])
    # plt.show()

    for firm in environment.firms:
        if firm.domicile==0:
            firm.profit_results = profit_history1
        else:
            firm.profit_results = profit_history2

        if firm.get_account("number_of_shares") != 0:
            firm.dividend = firm.profit_results[0]/firm.get_account("number_of_shares")

    # For both simultaneously
    # from src.functions.brownian_motion import brownian_process
    #
    # x = brownian_process(100, environment.num_sweeps, environment.num_firms)
    # x = np.divide(x, 100)
    #
    # for firm in environment.firms:
    #     if firm.domicile == 0:
    #         x[1] = np.multiply(x[1], firm.initial_profit)
    #     if firm.domicile == 1:
    #         x[0] = np.multiply(x[0], firm.initial_profit)
    # profit_history1 = x[1].tolist()
    # profit_history2 = x[0].tolist()
    # for firm in environment.firms:
    #     if firm.domicile==0:
    #         firm.profit_results = profit_history1
    #     else:
    #         firm.profit_results = profit_history2
    #
    #     if firm.get_account("number_of_shares") != 0:
    #         firm.dividend = firm.profit_results[0]/firm.get_account("number_of_shares")

def initialize_funds_from_files(environment, fund_directory, time):
    from src.fund import Fund
    while len(environment.funds) > 0:
        environment.funds.pop()

    agent_files = os.listdir(fund_directory)

    for each_agent_file in agent_files:

        if '.xml' in each_agent_file:
            agent = Fund()
            agent_filename = fund_directory + each_agent_file
            agent.get_parameters_from_file(agent_filename, environment)
            environment.funds.append(agent)

    logging.info('Fetched funds data and read into program')

    # check if agents were read in correctly
    # for i in self.funds:
    #     print i.identifier
    #     print i.print_variables()
    #     print i


def allocate_fund_size(environment):
    # default is 20% B and 80% A market cap
    sum_a = 0
    sum_b = 0
    for fund in environment.funds:
        if fund.parameters['domicile'] == 0:
            sum_a += 1
        if fund.parameters['domicile'] == 1:
            sum_b += 1

    list_temp_b  = []
    list_b = []
    eme_market_cap = 0
    for fund in environment.funds:
        if fund.domicile == 1.0:
            list_temp_b = split_equal(int(sum_b), int((environment.global_assets_under_management)*0.5))
            list_b.append(fund)
    # itrange = list(range(0, len(list_temp)))
    for index, elem in enumerate(list_b):
        for index2, elem2 in enumerate(list_temp_b):
            if index == index2:
                dict={"total_assets" : elem2}
                elem.append_state_variables(dict)
                eme_market_cap+=elem.total_assets
    environment.variable_parameters["eme_market_cap"] = eme_market_cap

    "The same for A funds"

    list_temp_a  = []
    list_a = []
    ame_market_cap = 0
    for fund in environment.funds:
        if fund.domicile == 0:
            list_temp_a = split_equal(int(sum_a), int((environment.global_assets_under_management)*0.5))
            print list_temp_a
            list_a.append(fund)
    # itrange = list(range(0, len(list_temp)))
    for index, elem in enumerate(list_a):
        for index2, elem2 in enumerate(list_temp_a):
            if index == index2:
                dict={"total_assets" : elem2}
                elem.append_state_variables(dict)
                ame_market_cap += elem.total_assets
    environment.variable_parameters["ame_market_cap"] = ame_market_cap
    logging.info("Determined fund size according to global market cap and data given in the agents configs")

def split_equal(parts, value ):
    value = float(value)
    return [1*value/parts for i in range(1,parts+1)]

def divide_sum_unequal(n, total):
#Return a randomly chosen list of n positive integers summing to total.
#Each such list is equally likely to occur.
    import random
    random.seed(9001)
    dividers = sorted(random.sample(xrange(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
