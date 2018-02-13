from numpy.testing import assert_equal
from qe_financial_spillover.src.functions.distribute import *

""" Helper functions to assign funds to countries """

def test_distribute_funds_equally():
    assert_equal(distribute_funds_equally(n_funds=2, list_countries=["US", "EU"]), ["US", "EU"])

def test_weighted_choice():
    assert_equal(weighted_choice(choices=[("Germany", 100), ("SA", 0)]), "Germany")


