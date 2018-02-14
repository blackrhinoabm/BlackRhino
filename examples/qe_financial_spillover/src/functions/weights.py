def exp_weighted_moving_average(last_exp_w_ma_average, phi, variable_of_interest):
    """
    returns new weighted moving average
    param: last_exp_w_ma_average
    param: phi
        memory parameter
    param: variable_of_interest
        can be anything
    return: new_exp_w_ma_average
    """
    new_exp_w_ma_average =  (1 - phi) * last_exp_w_ma_average + phi * variable_of_interest
    return new_exp_w_ma_average


def covar_between_two_variable(var1, var2, ewma1, ewma2, phi, cov_ewma, previous_weighted_covariance, ewma_function):
    """
    param: var1 float
    param: var2 float
    param: ewma1 float
        exponentially weighted moving average of variable 1
    param: ewma2 float
        exponentially weighted moving average of variable 2
    param: cov_ewma float
        exponentially weighted moving average of covariance between variable 1 and variable 2
    """
    weighted_covariance = (var1 - ewma1) * (var2 - ewma2)
    new_weighted_covariance = ewma_function(weighted_covariance, phi, weighted_covariance)

    return new_weighted_covariance


def simple_moving_average_list(data_list, window):
    """
    Calculates Simple Moving Average from data list specifying window for moving average

    :param data_list: e.g. [1, 0.9, 1.1 , ...]
    :param window: 4; e.g. the last 4 observations
    :return: float
    """
    if len(data) < window:
        return None
    # Take the last i window observations

    return sum(data[-window:]) / float(window)


def ew_moving_average_list(data_list, window, weight):
    """
    Calculates exponentially moving average from data list

    :param data_list:
    :param window:
    :param weight: weight the last observation counts
    :return: float
    """
    if len(data) < 2 * window:
        raise ValueError("data is too short")
    c = weight/ (window + 1)
    current_ema = simple_moving_average_list(data[-window * 2:-window], window)

    for value in data[-window:]:
        current_ema = (c * value) + ((1 - c) * current_ema)
    return current_ema