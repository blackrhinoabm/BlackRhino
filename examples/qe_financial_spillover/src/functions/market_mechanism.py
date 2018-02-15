from math import log
from math import exp
import numpy as np

def incomplete_walrasian_auction_price(asset, funds, previous_price, imperfection_tolerance, gamma, std_market_noise):
    """
    Find the next tau price .
    :param asset: current asset of interest
    :param funds: list of funds which participate in the market
    :param previous_price: float
    :param imperfection_tolerance: amount by how much the market maker is willing to settle for an equilibrium
    :param gamma: price step
    :param std_market_noise: standard deviation of the noise in price formation
    :return: next_price
    """
    # set initial price at last price
    price = previous_price
    cleared = False
    # collect supply and demand from agents at price
    excess_demand = 0
    market_noise = np.random.normal(0, std_market_noise)
    for fund in funds:
        excess_demand += fund.get_demand(price, asset)
    # if excesss aggregate demand: increase price by step
    if abs(excess_demand) > imperfection_tolerance:
        cleared = False
        imperfect_price = log(price) + gamma * (excess_demand / asset.parameters["global_quantity"]) + market_noise  #price_step # equation 1.14
        imperfect_price = exp(imperfect_price)
        return cleared, imperfect_price
    else:
        cleared = True
        return cleared, price
