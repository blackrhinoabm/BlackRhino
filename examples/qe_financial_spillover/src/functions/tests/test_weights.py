from numpy.testing import assert_equal
from qe_financial_spillover.src.functions.weights import *

def test_exp_weighted_moving_average():
    last_exp_w_ma_average = 240
    phi = 0.4
    variable_of_interest = 200

    assert_equal(exp_weighted_moving_average(last_exp_w_ma_average, phi, variable_of_interest) > variable_of_interest,
                 True)
    assert_equal(exp_weighted_moving_average(last_exp_w_ma_average, phi, variable_of_interest) < last_exp_w_ma_average,
                 True)