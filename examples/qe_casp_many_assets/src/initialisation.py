
import logging
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def init_firms(environment, firm_directory, time):
    initialize_firms_from_files(environment, firm_directory, time)

def init_funds(environment, fund_directory, time):
    initialize_funds_from_files(environment, fund_directory, time)
    allocate_fund_size(environment)
    init_fund_type(environment)

def init_assets(environment, asset_directory, time, risky_assets_funda_values):
    global_assets = []
    list_shares = initialize_shares(environment, asset_directory, time)
    list_bonds = initialize_bond_from_files(environment, asset_directory)
    init_asset_prices(environment, risky_assets_funda_values )

    for asset in list_shares:
        global_assets.append(asset)
    for asset in list_bonds:
        if asset.domicile == 0:
            global_assets.append(asset)
    dict2 = {"domestic_market" : global_assets}
    environment.region.update(dict2)
    print environment.region

def initialize_shares(environment, asset_directory, time):
    from src.asset import Asset_risky
    shares_list = []
    for i in environment.firms:
        asset = Asset_risky(i)
        environment.assets.append(asset)
        shares_list.append(asset)
    return shares_list

def initialize_bond_from_files(environment, asset_directory):
    from src.asset import Asset_riskfree
    asset_files = os.listdir(asset_directory)
    bond_list = []

    for each_agent_file in asset_files:
        if '.xml' in each_agent_file:
            bond = Asset_riskfree()
            agent_filename = asset_directory + each_agent_file
            bond.get_parameters_from_file(agent_filename, environment)
            environment.assets.append(bond)
            bond_list.append(bond)
    # logging.info('Fetched bond data and read into program')
    return bond_list

def init_asset_prices(environment, risky_assets_funda_values):
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

    # do this better if there are more assets
    for asset, value in risky_assets_funda_values.items():
        if asset == "A":
            asset_a = environment.get_agent_by_id("A")
            asset_a.funda_values.extend(value)
        if asset == "B":
            asset_b = environment.get_agent_by_id("B")
            asset_b.funda_values.extend(value)

    pA = round(random.randint(37, 37),4)
    asset_a.funda_values.append(environment.assets[0].funda_v)
    asset_b.funda_values.append(environment.assets[1].funda_v)
    print environment.assets[0].funda_v, environment.assets[1].funda_v, "Fundamental values"

    pB = round(random.randint(25,25),4)
    print pB, "Initialisation pB"
    print pA, "Initialisation pA"

    prices_a = [random.uniform(37, 39) for _ in range(int(1))]
    prices_b = [random.uniform(25, 25) for _ in range(int(1))]

    prices_a.append(pA)
    prices_b.append(pB)

    environment.prices.append(prices_a)
    environment.prices.append(prices_b)

    # print "Price history of A:", prices_a
    # print "Price history of B:", prices_b

    environment.variable_parameters['price_of_b'] = pB
    environment.variable_parameters['price_of_a'] = pA

    xtra_values = 2
    i = environment.get_agent_by_id("A")
    i.mu = init_return(i.firm.dividend, pA)
    environment.variable_parameters['mu_a'] = i.mu
    i.riskyness.append(environment.variable_parameters["std_a"])
    i.returns.append(i.mu)
    i.std=environment.variable_parameters["std_a"]
    # print i.mu
    i.prices.extend(prices_a)

    for ii in range(xtra_values):
	 		# Instantiate the generator
	 	norm1 = sp.stats.norm(loc = i.mu, scale = i.std)
		#Generate a random value for history:
		i.returns.append(norm1.rvs())
		# print i.returns, i.identifier

    i = environment.get_agent_by_id("B")

    i.mu = init_return(i.firm.dividend, pB)
    i.returns.append(i.mu)
    environment.variable_parameters['mu_b'] = i.mu
    i.riskyness.append(environment.variable_parameters["std_b"])
    i.std=environment.variable_parameters["std_b"]
    i.prices.extend(prices_b)

    for ii in range(xtra_values):
	 		# Instantiate the generator
	 	norm1 = sp.stats.norm(loc = i.mu, scale = i.std)
		#Generate a random value for history:
		i.returns.append(norm1.rvs())
		print i.returns, i.identifier

    i = environment.get_agent_by_id("riskfree_A")
    for ii in range(xtra_values):
	 		# Instantiate the generator
	 	norm1 = sp.stats.norm(loc = i.mu, scale = i.std)
		#Generate a random value for history:
		i.returns.append(norm1.rvs())
		print i.returns, i.identifier

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
    gamma_fs = [random.uniform(0, 0.5) for _ in range(int((environment.variable_parameters["fundamentalists"]*len(environment.funds))))]
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

    x_a = brownian_process_individual(1, environment.num_sweeps, 1, brown_delta_a )
    # print x_a, "profit process a"

    x_b = brownian_process_individual(1, environment.num_sweeps  ,1 , brown_delta_b)
    # print x_b, "profit process b"

    #Make a copy for fundamental values
    x_a_funda =  x_a
    x_b_funda =  x_b

    #for profits
    for firm in environment.firms:
        if firm.domicile == 0:
            x_a[0] = np.multiply(x_a[0], firm.initial_profit)
        if firm.domicile == 1:
            x_b[0] = np.multiply(x_b[0], firm.initial_profit)

    profit_history1 = x_a[0].tolist()
    profit_history2 = x_b[0].tolist()

    # for fundamental values
    for firm in environment.firms:
        if firm.domicile == 0:
            x_a_funda[0] = np.divide(x_a_funda[0], (firm.number_of_shares * firm.discount))
        if firm.domicile == 1:
            x_b_funda[0] = np.divide(x_b_funda[0], (firm.number_of_shares * firm.discount))

    #save and return this list (will be used later when assets are initialised)
    # To do - make this a matrix, it's way too complicated if there are more assets
    profit_funda_a = x_a_funda[0].tolist()
    profit_funda_b = x_b_funda[0].tolist()
    risky_assets_funda_values = { "A" : profit_funda_a , "B": profit_funda_b}

    # plt.plot(profit_funda1)
    # plt.plot(profit_funda2 )
    # plt.legend(["a", "b"])
    # plt.show()

    for firm in environment.firms:
        if firm.domicile==0:
            firm.profit_results = profit_history1
        if firm.domicile==1:
            firm.profit_results = profit_history2

        if firm.get_account("number_of_shares") != 0:
            firm.dividend = firm.profit_results[0]/firm.get_account("number_of_shares")
            firm.state_variables["cum_profit"] = firm.dividend

    return risky_assets_funda_values
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
            list_temp_b = split_equal(int(sum_b), int((environment.global_assets_under_management)*0))
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
            list_temp_a = split_equal(int(sum_a), int((environment.global_assets_under_management)*1))
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
