

import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from pylab import plot, show, grid, xlabel, ylabel
import random
from math import sqrt

#There is a parameter inside def brownian - loc, with whom it's possible to get
#a drift
def brownian(x0, n, dt, delta, out=None):

	x0 = np.asarray(x0)
	r = norm.rvs(loc=0.1, size=x0.shape + (n,), scale=delta*sqrt(dt))

    # If `out` was not given, create an output array.
	if out is None:
		out = np.empty(r.shape)

    # This computes the Brownian motion by forming the cumulative sum of
    # the random samples.
	np.cumsum(r, axis=-1, out=out)

    # Add the initial conditionn
	out += np.expand_dims(x0, axis=-1)
	return out

def geom_brownian_drift(brown_dt, brown_mu, brown_sigma):

	"""

	Arguments
	---
	Wiener process parameters:
	dt : lenght of steps

	mu:
		The drift factor (e.g. of firm profits)

	sigma:
		volatility in per cent
	(T: float
		for the process as a whole there is T: total time periods and
		steps: T/dt	)
	"""

	#source: https://scipy.github.io/old-wiki/pages/Cookbook/BrownianMotion.html

	W = np.random.standard_normal()
	W = np.cumsum(W)*np.sqrt(brown_dt) ### standard brownian motion ###
	X = (brown_mu-0.5*brown_sigma**2) + brown_sigma*W
	return float(np.exp(X)) ### geometric brownian motion ###

# def main():
#
#     # The Wiener process parameter.
#     delta = 2
#     # Total time.
#     T = 2.0
#     # Number of steps.
#     N = 50
#     # Time step size
#     dt = T/N
#     # Number of realizations to generate.
#     m = 2
#     # Create an empty array to store the realizations.
#     x = np.empty((m,N+1))
#
#     # Initial values of x.
#     x[:,0] = 100
#     # np.random.seed(seed=4) # m = 2
#
#     np.random.seed(seed=4) # without loc=0.01 in function, looks like SA
#     #There is a parameter inside def brownian - loc, with whom it's possible to get
#     #a drift  # mu = 0.05
#
#     brownian(x[:,0], N, dt, delta, out=x[:,1:])
#
#     t = np.linspace(0.0, N*dt, N+1)
#     for k in range(m):
#         plot(t, x[k])
#     xlabel('t', fontsize=16)
#     ylabel('x', fontsize=16)
#     grid(True)
#     show()

#
# if __name__ == "__main__":
#     main()

def brownian_process(intitial_profit, sweeps, num_firms):
    # The Wiener process parameter.
    delta = 0.3
    # Total time.
    T = 2.0
    # Number of steps.
    N = sweeps
    # Time step size
    dt = sweeps
    # Number of realizations to generate.
    m = num_firms
    # Create an empty array to store the realizations.
    x = np.empty((m,N+1))

    # Initial values of x.
    x[:,0] = intitial_profit
    np.random.seed(seed=360) # 4, 36

    # np.random.seed(seed=4) # without loc=0.01 in function, looks like SA
    #There is a parameter inside def brownian - loc, with whom it's possible to get
    #a drift  # mu = 0.0 np.random.seed(seed=1)
    return brownian(x[:,0], N, dt, delta, out=x[:,1:])

	# return x
    # t = np.linspace(0.0, N*dt, N+1)
    # for k in range(m):
    #     plot(t, x[k])
    # xlabel('t', fontsize=16)
    # ylabel('x', fontsize=16)
    # grid(True)
    # show()

def brownian_process_individual(intitial_profit, sweeps, num_firms, delta):
    # The Wiener process parameter.
    delta = delta
    # Total time.
    T = 1
    # Number of steps.
    N = sweeps
    # Time step size
    dt = sweeps
    # Number of realizations to generate.
    m = num_firms
    # Create an empty array to store the realizations.
    x = np.empty((m,N+1))

    # Initial values of x.
    x[:,0] = intitial_profit
    np.random.seed(seed=75) # 4, 37

    # np.random.seed(seed=4) # without loc=0.01 in function, looks like SA
    #There is a parameter inside def brownian - loc, with whom it's possible to get
    #a drift  # mu = 0.0 np.random.seed(seed=1)
    return brownian(x[:,0], N, dt, delta, out=x[:,1:])

    # t = np.linspace(0.0, N*dt, N+1)
    # for k in range(m):
    #     plot(t, x[k])
    # xlabel('t', fontsize=16)
    # ylabel('x', fontsize=16)
    # grid(True)
    # show()
