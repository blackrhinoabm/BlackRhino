from initialisation import *
from qe_financial_spillover.src.functions.show import *

def qe_casp_model(identifiers_funds, thetas, regions, global_capital, identifiers_assets, ms, rhos, omegas, face_values):
    """
    Initialisation
    """
    funds = init_funds(identifiers_funds, thetas, regions, global_capital)
    assets  = init_assets(regions, identifiers_assets, ms, rhos, omegas, face_values)
    init_returns(assets) # initialize returns
    init_prices(assets)
    # show_assets(assets) # print to screen


    """
    Simulation starts
    1. Funds form expectation about future returns
    """

    for fund in funds:
        exp_omega, exp_price, exp_exchange_rate, exp_return = fund.update_expectation(assets)