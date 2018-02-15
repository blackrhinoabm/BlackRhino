from math import log
from math import exp, expm1
import numpy as np
from src.functions.weights import *



def exp_price( mhat, phi, last_price ):

    """
    The new expected price is the old price times a growth factor. The growth factor is the
    exponentially weighted moving average of past prices with a memory parameter
    :param mhat: last exponentially weighted moving average
    :param phi_p: Memory parameter. If phi_p is 1, only the last observation is considered
    :return:
    """
    exp_price_var = exp_weighted_moving_average( mhat, phi, last_price )  #Calls function from weights.py
    return exp_price_var


def exp_omega(omega, news_process, theta,  current_exp_omega, std_noise, day):   #Equation 1.6
    """
    Function to calculate the new expected default probability

    :param omega: default probability of last period per asset
    :param news_process: stochastic process underlying the default probability of the asset (defined in functions.stochasticprocess)
    :param theta: asset specific correction parameter
    :param current_exp_omega: last  expected default probability per fund
    :param std_noise: fund specific noise influencing the evaluation of news
    :param day: t
    :return: new expected default probability of the underlying asset (float)
    """
    #Fund specific noise parameter
    noise = np.random.normal(0,std_noise)

    if day != 0:
      # log of (last period expected omega) + evaluation of news +  past_error_correction
        log_omega =  log(current_exp_omega) + news_process[day] - news_process[day - 1] + noise + theta*( log(omega) - log(current_exp_omega))
        # take the inverse exponent
        exp_omega_var = exp(log_omega)
        return  exp_omega_var

    # If there are not more than one day (at initialisation), we take omega_0 as expected omega
    if day == 0:
        return omega


def exp_return_home_asset( ident,  rho, m, face_value, exp_omega, exp_price, actual_price, global_quantity):
    """
    Method to calculate the expected returns of home assets which go into portfolio optimisation
    Equation 1.1

    :param ident: asset identifier
    :param rho: nominal interest rate of asset
    :param m: constant repayment parameter
    :param face_value:  face_value
    :param exp_omega: expected default probability of the underlying asset (different for every fund)
    :param exp_price: expected price (different for every fund)
    :param actual_price: current price
    :param global_quantity: global quantity of the asset
    :return:
    """
    # Exclude cash
    if not "cash" in ident:
         # Returns of the asset = returns from interest payment, returns from price changes, returns from principal payment
        var = (1 - exp_omega )  * (    (face_value/(actual_price * global_quantity)) * (rho + 1 -m) +    (  (m * exp_price / actual_price)  -1 )    -  exp_omega   )
        return var
    # if it's cash, expected return is 0
    else:
        return 0.0

def exp_return_abroad_asset( ident, fund_region, rho, m, face_value, exp_omega, exp_price, actual_price, global_quantity, actual_x_rate, expected_x_rate):
    "We need the actual and expected exchange rate "

    # We exclude cash; not pretty but ok
    if not "cash" in ident:
        #We need to be careful if the fund_region is "home" or "abroad". According to the region,
        # the exchange rate has to be taken as direct quote or indirect quote

        #So we first take the "domestic" fund guys and DIRECT exchange rate quotation:
        if "domestic" in fund_region:
            # Assign the actual and expected direct xrate quotation
            expected_x = expected_x_rate["x_domestic_to_foreign"]
            actual_x = actual_x_rate["x_domestic_to_foreign"][-1]

            var = (1 - exp_omega) * ((  (expected_x * face_value) / ( actual_x  * actual_price * global_quantity)) * (rho + 1 - m) + ((m * expected_x *  exp_price / (actual_x *actual_price) ) - 1) - exp_omega)
            return var

        # Now the  "foreign" fund guys which need INDIRECT  exchange rate quotation:
        if "foreign" in fund_region:
            # Assign the actual and expected indirect xrate quotation
            expected_x = 1/ expected_x_rate["x_domestic_to_foreign"]
            actual_x = 1/ actual_x_rate["x_domestic_to_foreign"][-1]

            var = (1 - exp_omega) * (
                    ((expected_x * face_value) / (actual_x * actual_price * global_quantity)) * (rho + 1 - m) + (
                        (m * expected_x * exp_price / (actual_x * actual_price)) - 1) - exp_omega)

            return var
    # if it's cash, expected return is 0 (easy)
    else:
        return 0.0

def realised_return_home_asset(key, rho, m, face_value, current_price, previous_price, global_quantity ):
    # Exclude cash
    if not "cash" in key:
        # Returns of the asset = returns from interest payment, returns from price changes, returns from principal payment
        var =  ((face_value / (current_price * global_quantity)) * (rho + 1 - m) + (
                    (m * current_price / previous_price) - 1))
        return var
    # if it's cash, return is 0
    else:
        return 0.0

def realised_return_abroad_asset(key, fund_region, rho, m, face_value, current_price, previous_price, global_quantity, exchange_rate, day):
    "We need the current and previous exchange rate and must be careful with direct and indirect exchange rate quotations "

    # We exclude cash; not pretty but ok
    if not "cash" in key:

        # We need to be careful if the fund_region is "home" or "abroad". According to the region,
        # the exchange rate has to be taken as direct quote or indirect quote

        # So we first take the "domestic" fund guys and DIRECT exchange rate quotation:
        if "domestic" in fund_region:
            # Assign the actual and expected direct xrate quotation

            current_x = exchange_rate["x_domestic_to_foreign"][-1]

            if day == 0:
                previous_x = current_x
            else:
                previous_x = exchange_rate["x_domestic_to_foreign"][-2]

            var =   ((current_x * face_value) / (previous_x * previous_price * global_quantity)) * (rho + 1 - m) + ((m * current_x * current_price / (previous_x * previous_price)) - 1)
            return var

        # Now the  "foreign" fund guys which need INDIRECT  exchange rate quotation:
        if "foreign" in fund_region:
            # Assign the actual and expected indirect xrate quotation
            current_x = 1 / exchange_rate["x_domestic_to_foreign"][-1]

            if day == 0:
                previous_x = current_x
            else:
                previous_x = 1 / exchange_rate["x_domestic_to_foreign"][-2]

            var =   ((current_x * face_value) / (previous_x * previous_price * global_quantity)) * (rho + 1 - m) + ((m * current_x * current_price / (previous_x * previous_price)) - 1)

            return var

    # if it's cash, expected return is 0 (easy)
    else:
        return 0.0


