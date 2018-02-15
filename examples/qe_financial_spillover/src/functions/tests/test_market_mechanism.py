from numpy.testing import assert_equal
from qe_financial_spillover.src.functions.market_mechanism import *
import pytest

@pytest.fixture
def set_of_funds():
    """Creates a set of simple funds where the market clears at p=1"""
    class Fund():
        def __init__(self, price_belief):
            self.price_belief = price_belief

        def get_demand(self, price, asset):
            # demand is a function of the price
            demand = (self.price_belief - price) * 100
            return int(demand)

    return [Fund(p) for p in (0.7, 0.8, 0.9, 1.1, 1.2, 1.3)]

@pytest.fixture
def asset():
    class Asset():
        def __init__(self, global_quantity):
            self.parameters = {"global_quantity": global_quantity}

    return Asset(global_quantity=500)

def test_incomplete_walrasian_auction_price_clears(set_of_funds, asset):
    """Test if the market clears at price 1 and does not clear at other prices"""
    asset = asset
    std_market_noise = 0.001
    imperfection_tolerance = 10
    price_step = 0.05
    funds = set_of_funds
    previous_price = 1
    assert_equal(incomplete_walrasian_auction_price(asset, funds, previous_price,
                                                    imperfection_tolerance,
                                                    price_step, std_market_noise)[0], True)
    previous_price = 0.7
    assert_equal(incomplete_walrasian_auction_price(asset, funds, previous_price,
                                                    imperfection_tolerance,
                                                    price_step, std_market_noise)[0], False)
    previous_price = 1.4
    assert_equal(incomplete_walrasian_auction_price(asset, funds, previous_price,
                                                    imperfection_tolerance,
                                                    price_step, std_market_noise)[0], False)


def test_incomplete_walrasian_auction_price_moves(set_of_funds, asset):
    """
    Test if the price moves in the right direction
    Excess demand (supply) should push the price up (down)
    """
    asset = asset
    std_market_noise = 0.001
    imperfection_tolerance = 10
    price_step = 0.05
    funds = set_of_funds
    # a low price should lead to excess demand and a higher price
    previous_price = 0.8
    assert_equal(incomplete_walrasian_auction_price(asset, funds, previous_price,
                                                    imperfection_tolerance,
                                                    price_step, std_market_noise)[1] > previous_price, True)
    # a high price should lead to excess supply and a lower price
    previous_price = 1.3
    assert_equal(incomplete_walrasian_auction_price(asset, funds, previous_price,
                                                    imperfection_tolerance,
                                                    price_step, std_market_noise)[1] < previous_price, True)