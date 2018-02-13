from numpy.testing import assert_equal
from qe_financial_spillover.src.functions.stochasticprocess import *

def test_ornstein_uhlenbeck_levels():
    """Basic checks for ornstein uhlenbeck function"""
    assert_equal(len(ornstein_uhlenbeck_levels(time=20)), 20)
    assert_equal(ornstein_uhlenbeck_levels(time=20, long_run_average_default_probability=10e-7)[0], 0.000001)