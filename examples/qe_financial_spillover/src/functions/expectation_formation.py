from math import log
from math import exp, expm1
import numpy as np
from src.functions.weights import *

def exp_price(   emwa_price, ewma_price_intermediate , phi_p, last_price , last_intermediate_price, day):

    """

    The new expected price is the old price times a growth factor. The growth factor is the
    exponentially weighted moving average of past prices with a memory parameter

    :param phi_p: Memory parameter. If phi_p is 1, only the last observation is considered
    :return:
    """
    emwa_price = 0
    exp_price_var = exp_weighted_moving_average( emwa_price, phi_p, last_price )

def exp_omega(omega, news_process, theta,  current_exp_omega, std_noise, day):
    """
    Function to calculate the new expected default probability

    :param omega: default probability of last period
    :param news_process: stochastic process underlying the default probability of the asset (defined in functions.stochasticprocess)
    :param theta: asset specific correction parameter
    :param current_exp_omega: last  expected default probability
    :param std_noise: fund specific noise influencing the evaluation of news
    :param day: t
    :return: new expected default probability of the underlying asset (float)
    """
    #Fund specific noise parameter
    noise = np.random.normal(0,std_noise)

    #Cash has omega zero, in that case the expected probability is 0
    if omega !=0:
        try:   # log of (last period expected omega) + evaluation of news +  past_error_correction
            log_omega =  log(current_exp_omega)  +    news_process[day] - news_process[day - 1]  + noise + theta*( log(omega) - log(current_exp_omega))
            # take the inverse exponent
            exp_omega_var = exp(log_omega)
            return  exp_omega_var

        # If there are not more than one day (at initialisation), we take omega_0
        except IndexError:
            return omega
    # return the 0 exp propability of cash
    if omega== 0:
        return 0


def exp_return():
    pass