import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from pylab import plot, show, grid, xlabel, ylabel
import random
from math import sqrt
import cvxopt as opt
from cvxopt import blas, solvers
import pandas as pd

def create_matrices(environment, list_assets, time, number_of_assets):
	np.random.seed(123)

	# for asset in list_assets:
	# 	for i in asset:
    #
	data = np.array([0.05, 0.04, 0.03,0.04])

	# print data
	dates = [i for i in range(time)]
	periods = np.array([dates] )
	period = periods.T
	# print period
	# returns = np.((data, periods))
	assets = [str(asset_a)]
	returns = pd.DataFrame(data, columns=assets, index=period)

	avg_rets = returns.mean()
	cov_mat = returns.cov()

	return returns, cov_mat, avg_rets

returns, cov_mat, avg_rets = create_matrices()

#No shortselling
def min_var_portfolio(cov_mat, allow_short=False):
    if not isinstance(cov_mat, pd.DataFrame):
        raise ValueError("Covariance matrix is not a DataFrame")
    n = len(cov_mat)
    P = opt.matrix(cov_mat.values)
    q = opt.matrix(0.0, (n, 1))

    # Constraints Gx <= h
    if not allow_short:
        # x >= 0
        G = opt.matrix(-np.identity(n))
        h = opt.matrix(0.0, (n, 1))
    else:
        G = None
        h = None

    # Constraints Ax = b
    # sum(x) = 1
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)
    # Solve
    optsolvers.options['show_progress'] = False
    sol = optsolvers.qp(P, q, G, h, A, b)

    if sol['status'] != 'optimal':
        warnings.warn("Convergence problem")

    # Put weights into a labeled series
    weights = pd.Series(sol['x'], index=cov_mat.index)
    return weights

def print_pf(model):
    print('\n\n' + str(model))
    print('-' * len(model))

def print_portfolio_info(returns, avg_rets, weights):
    """
    Print information on expected portfolio performance.
    """
    ret = (weights * avg_rets).sum()
    std = (weights * returns).sum(1).std()
    sharpe = ret / std
    print("Optimal weights:\n{}\n".format(weights))
    print("Expected return:   {}".format(ret))
    print("Expected variance: {}".format(std**2))
    print("Expected Sharpe:   {}".format(sharpe))
