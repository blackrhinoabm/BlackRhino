from initialisation import *
from qe_financial_spillover.src.functions.show import *
from qe_financial_spillover.src.functions.portfolio import *


def qe_casp_model(days, identifiers_funds, lambdas, thetas, phis, regions, identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices):
    """
    Initialisation
    """

    asset_dict  = init_assets(regions, identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices)
    init_returns(asset_dict) # initialize returns
    funds = init_funds(identifiers_funds, lambdas, thetas, phis, regions, asset_dict)
    global_capital = get_fund_size(funds)

    # show_assets(asset_dict) # print to screen
    """
    Simulation starts
    1. Funds form expectation about future returns
    """
    for day in range(days-1):
        get_realised_returns_for_assets(asset_dict, day)

        show_assets(asset_dict)
        for fund in funds:
            exp_omega, exp_price, exp_exchange_rate, exp_return = fund.update_expectation(asset_dict)
