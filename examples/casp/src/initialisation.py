
import logging
import os

def init_firms(environment, firm_directory, time):
    initialize_firms_from_files(environment, firm_directory, time)
    init_profits(environment)

def init_funds(environment, fund_directory, time):
    initialize_funds_from_files(environment, fund_directory, time)
    allocate_fund_size(environment)
    init_fund_type(environment)

def init_assets(environment):
    """
    Assets A and B are intiantilized with a randomized initial price
    pA and pB.

    Calls method init_return in same script.

    Argument
    ===

    Result
    ===
    2 asset objects, stored in environment.assets[]

    """
    import random
    from src.asset import Asset
    for i in environment.firms:
        asset = Asset(i)
        environment.assets.append(asset)

    random.seed(000)
    pA = random.randint(35, 41)

    pB = random.randint(39, 42)

    prices_a = [random.uniform(38, 41) for _ in range(int(3))]
    prices_b = [random.uniform(39, 42) for _ in range(int(3))]

    prices_a.append(pA)
    prices_b.append(pB)

    # print "Price history of A:", prices_a
    # print "Price history of B:", prices_b

    environment.variable_parameters['price_of_b'] = pB
    environment.variable_parameters['price_of_a'] = pA

    for i in environment.assets:
        if i.identifier == "A":
            i.mu = init_return(i.firm.dividend, pA)
            environment.variable_parameters['mu_a'] = i.mu
            # i.prices.append(prices_a)
            i.prices.extend(prices_a)
        else:
            i.mu = init_return(i.firm.dividend, pB)
            environment.variable_parameters['mu_b'] = i.mu
            i.prices.append(prices_b)
            i.prices.extend(prices_b)

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
    gamma_cs = [random.uniform(0, 1) for _ in range(int((environment.variable_parameters["chartists"]*len(environment.funds))))]

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

def init_profits(environment):
    "Add some variables to firms and initialize profits"
    for firm in environment.firms:
         firm.add_stuff()
         firm.initialize_profits()

         # In case we want to add variables
         # firm.add_stuff()

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
            list_temp_b = divide_sum(int(sum_b), int((environment.global_assets_under_management)*0.2))
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
            list_temp_a = divide_sum(int(sum_a), int((environment.global_assets_under_management)*0.8))
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

def divide_sum(n, total):
#Return a randomly chosen list of n positive integers summing to total.
#Each such list is equally likely to occur.
    import random
    random.seed(9001)
    dividers = sorted(random.sample(xrange(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
