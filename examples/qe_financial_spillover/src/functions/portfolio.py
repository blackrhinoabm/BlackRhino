import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import norm
import numpy as np
import random
from math import sqrt
import pandas as pd
import cvxopt as opt
from cvxopt import blas, solvers

def create_pandas(environment, exp_returns):

    asset_names = []
    list_temp_returns = []

    for i in environment.region['domestic_market']:
        asset_names.append(str(i.identifier))

    #Create dictionary with key value pairs of asset names and returns and put in percentage terms
    return_dict = {}
    for i in asset_names:
        number = environment.get_agent_by_id(i).returns
        # Multiply with 100
        number = [ii * 100 for ii in number]
        return_dict[i] = number

    # If we have new expected returns, we update the return vector
    if  exp_returns!=0:
          # Iterate over the two dictionaries
        for (k,v), (k2,v2) in zip(return_dict.items(), exp_returns.items()):

            if k == k2:
                v.append(v2)
    else:
        pass

    #Convert dict in list of returns to make a panda
    for i, v in return_dict.iteritems():
        list_temp_returns.append(v)

    data = np.asarray(list_temp_returns).T
    asset_names = list(return_dict.keys())
    returns = pd.DataFrame(data, columns= asset_names)
    # print returns.head()
    avg_rets = returns.mean()
    cov_mat = returns.cov()
    return returns, cov_mat, avg_rets

def optimal_portfolio(return_panda, cov_mat, avg_rets, risk_aversion):
	P = opt.matrix( risk_aversion*cov_mat.as_matrix())
	q = opt.matrix(-avg_rets.as_matrix())
	G = opt.matrix(0.0, (len(q),len(q)))
	G[::len(q)+1] = -1.0
	h = opt.matrix(0.0, (len(q),1))
	A = opt.matrix(1.0, (1,len(q)))
	b = opt.matrix(1.0)

	solvers.options['show_progress'] = False
	sol = solvers.qp(P, q, G, h, A, b)
	weights = pd.Series(sol['x'], index=cov_mat.index)
	np.set_printoptions(suppress=True)
	return weights

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