from initialisation import *
from qe_financial_spillover.src.functions.portfolio import *

def qe_casp_model(days, identifiers_funds, lambdas, thetas, phis,  phis_p, regions, std_noises , identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices):
    """
    Initialisation
    """
    asset_dict  = init_assets(regions, identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices)
    funds = init_funds(identifiers_funds, lambdas, thetas, phis, phis_p,  regions, std_noises , asset_dict)

    init_returns(asset_dict) # initialize returns
    init_ewma_price(asset_dict, identifiers_assets, funds)
    init_exp_default_probabilities(asset_dict, identifiers_assets, funds)
    init_news_process(asset_dict, days)

    global_capital = get_fund_size(funds)
    """
    Simulation starts
    1. Funds form expectation about future returns
    """
    for day in range(days-1):
        get_realised_returns_for_assets(asset_dict, day) # function inside portfolio

        for fund in funds:
            fund.update_expectation(asset_dict, identifiers_assets,  day)
