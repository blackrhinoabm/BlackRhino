import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import norm
import numpy as np
import random
from math import sqrt
import pandas as pd
import cvxopt as opt
from cvxopt import blas, solvers


def create_pandas(ewma_realised_return, last_realised_return, expected_return):
    # Creating expected return matrix

    # Making covariance matrix
    list_temp_returns = []
    for key, value in ewma_realised_return.iteritems():
        ewma_realised_return[key] = [value]

    # For every asset key, make a list with the exp. weighted moving average and the last observation
    # E.g.      {  "domestic_high_risk" : [ ewma  , last_observation]   }

    # For some reason zip did not work - I had to iterate over the two dictionaries... not pretty
    for key, value in ewma_realised_return.items():
        for key2, value2 in  last_realised_return.items():
            if key == key2:
                value.append(value2)

    print ewma_realised_return
    # Now turn the dictionary into a panda
    for i, v in ewma_realised_return.iteritems():
        list_temp_returns.append(v)

    data = np.asarray(list_temp_returns).T
    asset_names = list(ewma_realised_return.keys())

    returns = pd.DataFrame(data, columns= asset_names)
    print returns.head()
    cov_mat = returns.cov()
    avg_mat = returns.mean()



    print avg_mat

    return returns, cov_mat

def optimal_portfolio(return_panda, cov_mat, exp_rets, risk_aversion):

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

def get_realised_returns_for_assets(asset_dict, day):
    for key, asset in asset_dict.iteritems():
        asset.calc_realised_returns(day)
