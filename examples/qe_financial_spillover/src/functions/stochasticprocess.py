import math
import numpy.random as nrand

def ornstein_uhlenbeck_levels(time=500, init_default_probability=10e-7 ,rate_of_time = 0.003968253968253968, sigma=0.125,
                              mean_reversion=0.99, long_run_average_default_probability=10e-7):
    """
    This function returns news about the as a mean-reverting ornstein uhlenbeck process.
    :param init_default_probability: starting point of the default probability
    :param time: total time over which the simulation takes place
    :param rate_of_time: e.g. daily, monthly, annually (default is daily)
    :param sigma: volatility of the stochastic processes
    :param mean_reversion: tendency to revert to the long run average
    :param long_run_average_default_probability:
    :return: list : simulatated default probability simulated over time
    """
    default_probability = [init_default_probability]
    sqrt_delta_sigma = math.sqrt(rate_of_time) * sigma
    brownian_motion_returns = nrand.normal(loc=0, scale=sqrt_delta_sigma, size=time)
    for t in range(1, time):
        drift = mean_reversion * (long_run_average_default_probability - default_probability[t-1]) * rate_of_time
        randomness = brownian_motion_returns[t - 1]
        default_probability.append(default_probability[t - 1] + drift + randomness)
    return default_probability