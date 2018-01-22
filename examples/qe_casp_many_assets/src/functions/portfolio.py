import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import norm
import numpy as np
from pylab import plot, show, grid, xlabel, ylabel
import random
from math import sqrt
import pandas as pd
import cvxopt as opt
from cvxopt import blas, solvers

# No shortselling
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
    opt.solvers.options['show_progress'] = False
    sol = opt.solvers.qp(P, q, G, h, A, b)

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
	Source:
    Print information on expected portfolio performance.
    """
    ret = (weights * avg_rets).sum()
    std = (weights * returns).sum(1).std()
    sharpe = ret / std
    print("Optimal weights:\n{}\n".format(weights))
    print("Expected return:   {}".format(ret))
    print("Expected variance: {}".format(std**2))
    print("Expected Sharpe:   {}".format(sharpe))

def markowitz_portfolio(cov_mat, exp_rets, target_ret,
                        allow_short=False, market_neutral=False):
    """
	Source:
    Computes a Markowitz portfolio.

    Parameters
    ----------
    cov_mat: pandas.DataFrame
        Covariance matrix of asset returns.
    exp_rets: pandas.Series
        Expected asset returns (often historical returns).
    target_ret: float
        Target return of portfolio.
    allow_short: bool, optional
        If 'False' construct a long-only portfolio.
        If 'True' allow shorting, i.e. negative weights.
    market_neutral: bool, optional
        If 'False' sum of weights equals one.
        If 'True' sum of weights equal zero, i.e. create a
            market neutral portfolio (implies allow_short=True).

    Returns
    -------
    weights: pandas.Series
        Optimal asset weights.
    """
    if not isinstance(cov_mat, pd.DataFrame):
        raise ValueError("Covariance matrix is not a DataFrame")

    if not isinstance(exp_rets, pd.Series):
        raise ValueError("Expected returns is not a Series")

    if not isinstance(target_ret, float):
        raise ValueError("Target return is not a float")

    if not cov_mat.index.equals(exp_rets.index):
        raise ValueError("Indices do not match")

    if market_neutral and not allow_short:
        warnings.warn("A market neutral portfolio implies shorting")
        allow_short=True

    n = len(cov_mat)
    P = opt.matrix(cov_mat.values)
    q = opt.matrix(0.0, (n, 1))

    # Constraints Gx <= h
    if not allow_short:
        # exp_rets*x >= target_ret and x >= 0
        G = opt.matrix(np.vstack((-exp_rets.values,
                                  -np.identity(n))))
        h = opt.matrix(np.vstack((-target_ret,
                                  +np.zeros((n, 1)))))
    else:
        # exp_rets*x >= target_ret
        G = opt.matrix(-exp_rets.values).T
        h = opt.matrix(-target_ret)

    # Constraints Ax = b
    # sum(x) = 1
    A = opt.matrix(1.0, (1, n))

    if not market_neutral:
        b = opt.matrix(1.0)
    else:
        b = opt.matrix(0.0)

    # Solve
    optsolvers.options['show_progress'] = False
    sol = optsolvers.qp(P, q, G, h, A, b)

    if sol['status'] != 'optimal':
        warnings.warn("Convergence problem")

    # Put weights into a labeled series
    weights = pd.Series(sol['x'], index=cov_mat.index)
    return weights

def pf_risk_aversion(environment, returns, list_assets,  time, number_of_assets ):
	# Generate data for long only portfolio optimization.
	import numpy as np
	import matplotlib.pyplot as plt
 	n = number_of_assets

	list_temp = []

	for i, ii in enumerate(list_assets):
   	# 	if "riskfree" not in str(i.identifier):
		list_temp.append(ii.returns[-1])

	mu = np.array(list_temp).reshape(n,1)
 	mu = np.abs(np.random.randn(n, 1))

	Sigma = returns.as_matrix()
	Sigma = Sigma.T.dot(Sigma)

	# Sigma = np.asarray(returns)
	# print Sigma

	# Long only portfolio optimization.
	from cvxpy import *
	w = Variable(n)
	gamma = 3

	ret = mu.T*w
	risk = quad_form(w, Sigma)
	prob = Problem(Maximize(ret -  gamma*risk),
	               [sum_entries(w) == 1,
	                w >= 0])
	w_vals = []
	# Compute trade-off curve.
	SAMPLES = 4
	risk_data = np.zeros(SAMPLES)
	ret_data = np.zeros(SAMPLES)
	np.set_printoptions(suppress=True)
	prob.solve()
	risk_data[i] = sqrt(risk).value
	ret_data[i] = ret.value

def create_matrices(environment, list_assets, list_returns, time , number_of_assets):
 	list_temp_returns = []
	random.seed(10)
	for i in list_assets:
  	# 	if "riskfree" not in str(i.identifier):
		list_temp_returns.append(i.returns)

	list_temp_identifier = []
	for i in list_assets:
		# if "riskfree" not in str(i.identifier):
		list_temp_identifier.append(i.identifier)

	assets = list_temp_identifier
	data = np.asarray(list_temp_returns).T
  	dates = pd.date_range('1/1/2013', periods=len(list_returns) ,   index='time')
	#Alternative for dates
	# dates = [i for i in range(time)]
	# periods = np.array([dates] )
	# period = periods.T
	# print period

 	returns = pd.DataFrame(data, columns= assets, index=dates)
	avg_rets = returns.mean()
	cov_mat = returns.cov()
	# print cov_mat
	return returns, cov_mat, avg_rets

def optimal_portfolio(returns):
	n = len(returns)
	returns = np.asmatrix(returns)
	print returns[0,:]        # selects all but 1st col from row given by 'row_index'
	# print returns[0,1:]        # selects all but 1st col from row given by 'row_index'
	N = 100
	mus = [10**(5.0 * t/N - 1.0) for t in range(N)]
	# Convert to cvxopt matrices
	S = opt.matrix(np.cov(returns))
	pbar = opt.matrix(np.mean(returns, axis=1))
	# Create constraint matrices
	G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
	h = opt.matrix(0.0, (n ,1))
	A = opt.matrix(1.0, (1, n))
	b = opt.matrix(1.0)
	# Calculate efficient frontier weights using quadratic programming
	portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x']
	              for mu in mus]
				  ## CALCULATE RISKS AND RETURNS FOR FRONTIER
	returns = [blas.dot(pbar, x) for x in portfolios]
	risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios]
	## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
	m1 = np.polyfit(returns, risks, 2)
	x1 = np.sqrt(m1[2] / m1[0])
	# CALCULATE THE OPTIMAL PORTFOLIO
	wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
	return np.asarray(wt), returns, risks

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

def optimal_portfolio_world(return_panda, cov_mat, avg_rets, risk_aversion):
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

 
def section(caption):
    print('\n\n' + str(caption))
    print('-' * len(caption))
