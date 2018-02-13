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
<<<<<<< HEAD
	return weights

def get_realised_returns_for_assets(asset_dict, day):
    for key, list in asset_dict.iteritems():
        for asset in list:
            asset.calc_realised_returns(day)
=======
	return weights
>>>>>>> origin/master
