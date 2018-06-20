from initialisation import *
from qe_financial_spillover.src.functions.portfolio import *

def qe_casp_model(days, identifiers_funds, lambdas, thetas, phis,  phis_p, phis_x, regions, std_noises , identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices, backward_simulated_time, exchange_rate):
    """
    Initialisation
    """
    random.seed(54)
    np.random.seed(54)
    asset_dict  = init_assets(regions, identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices)
    funds = init_funds(identifiers_funds, lambdas, thetas, phis, phis_p, phis_x,  regions, std_noises , asset_dict)

    init_price_history(asset_dict, backward_simulated_time)
    init_ewma_price(asset_dict, funds, exchange_rate)
    init_exp_default_probabilities(asset_dict, funds)
    init_news_process(asset_dict, days)
    global_capital = get_fund_size(funds)
    """
    Simulation starts
    1. Funds form expectation about future returns
    """
    for day in range(days-1):
        # while not cleared
        for fund in funds:
            fund.update_expectation(asset_dict, exchange_rate,  day)    #Equation 1.1 to 1.8

            """ 2. Funds form optimal portfolios """

            # Todo:
            #weights = fund.pf_opt(var_covariance)

            """ 3. Funds post demands """
            # demands = fund.get_demand(asset_dict, exchange_rate)   Equation 1.9 to 1.11
            """ 4. Incomplete walrasian auction  """
        # lazy_wal_auction(weights, demands)   Equation 1.12 to 1.15
        """
        5. Trading and updating of balance sheets """
        # for fund in funds:
            # fund.update_balance_sheets  Equation 1.16 to 1.18


