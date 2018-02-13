import math
import numpy
import random
import decimal
import scipy.linalg
import numpy.random as nrand
import matplotlib.pyplot as plt
import pandas as pd

def ornstein_uhlenbeck_levels(all_r0=0.0, all_time=1000000, all_delta=0.00396825396, all_sigma=0.125, ou_a=0.0, ou_mu=0.0):
    """
    This method returns the rate levels of a mean-reverting ornstein uhlenbeck process.
    :param param: the model parameters object
    :return: the interest rate levels for the Ornstein Uhlenbeck process
    """
    ou_levels = [all_r0]
    sqrt_delta_sigma = math.sqrt(all_delta) * all_sigma
    brownian_motion_returns = nrand.normal(loc=0, scale=sqrt_delta_sigma, size=all_time)
    for i in range(1, all_time):
        drift = ou_a * (ou_mu - ou_levels[i-1]) * all_delta
        randomness = brownian_motion_returns[i - 1]
        ou_levels.append(ou_levels[i - 1] + drift + randomness)
    return ou_levels