from initialisation import *
from qe_financial_spillover.src.functions.show import *

def qe_casp_model(identifiers_funds, thetas, phis, regions, identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices):
    """
    Initialisation
    """

    asset_dict  = init_assets(regions, identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices)
    init_returns(asset_dict) # initialize returns
    funds = init_funds(identifiers_funds, thetas, phis, regions, asset_dict)
    global_capital = complete_balance_sheets(funds)

    # show_assets(asset_dict) # print to screen
    # init_portfolio_transactions(identifiers_funds, funds, asset_dict)

    """
    Simulation starts
    1. Funds form expectation about future returns
    """

    for fund in funds:
        exp_omega, exp_price, exp_exchange_rate, exp_return = fund.update_expectation(asset_dict)