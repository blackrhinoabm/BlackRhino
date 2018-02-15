from initialisation import *
from qe_financial_spillover.src.functions.portfolio import *

def qe_casp_model(days, identifiers_funds, lambdas, thetas, phis,  phis_p, phis_x, regions, std_noises , identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices, backward_simulated_time, exchange_rate):
    """
    Initialisation
    """
    asset_dict  = init_assets(regions, identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices)
    funds = init_funds(identifiers_funds, lambdas, thetas, phis, phis_p, phis_x,  regions, std_noises , asset_dict)

    init_returns(asset_dict) # initialize returns

    init_price_history(asset_dict, backward_simulated_time)
    init_ewma_price(asset_dict, identifiers_assets, funds, exchange_rate)
    init_exp_default_probabilities(asset_dict, identifiers_assets, funds)
    init_news_process(asset_dict, days)
    global_capital = get_fund_size(funds)
    """
    Simulation starts
    1. Funds form expectation about future returns
    """
    for day in range(days-1):
        # while not cleared
        for fund in funds:
            fund.update_expectation(asset_dict, exchange_rate,  day)
