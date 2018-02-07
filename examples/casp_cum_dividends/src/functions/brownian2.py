
import matplotlib.pyplot as plt
import random
from math import sqrt


"""
# source: https://scipy.github.io/old-wiki/pages/Cookbook/BrownianMotion.html

brownian() implements one dimensional Brownian motion (i.e. the Wiener process).
"""

# File: brownian.py


from scipy.stats import norm
import numpy as np

def brownian(x0, n, dt, delta, out=None):

	x0 = np.asarray(x0)
	random.seed(00)
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

def profit_process():
    # The Wiener process parameter.
    delta = 2
    # Total time.
    T = 2.0
    # Number of steps.
    N = 50
    # Time step size
    dt = T/N
    # Number of realizations to generate.
    m = 2
    # Create an empty array to store the realizations.
    x = np.empty((m,N+1))

    # Initial values of x.
    x[:,0] = 100
    # np.random.seed(seed=4) # m = 2

    np.random.seed(seed=3) # without loc=0.01 in function, looks like SA
    # np.random.seed(seed=863)b
    #There is a parameter inside def brownian - loc, with whom it's possible to get
    #a drift  # mu = 0.05

    # x = 2.0 / 4.0

    brownian(x[:,0], N, dt, delta, out=x[:,1:])
	t = np.linspace(0.0, N*dt, N+1)
    for k in range(m):
        plot(t, x[k])
    xlabel('t', fontsize=16)
    ylabel('x', fontsize=16)
    grid(True)
    show()

profit_process()

#This code is for testing; plots the geom. brownian motion as coded above
# over t time periods

# T = 20
# mu = 0.07
# sigma = 0.01
# P0 = 100
# dt = 0.001
# N = round(T/dt)
# t = np.linspace(0, T, N)
# W = np.random.standard_normal(size = N)
# W = np.cumsum(W)*np.sqrt(dt) ### standard brownian motion ###
# X = (mu-0.5*sigma**2)*t + sigma*W
# P = P0*np.exp(X) ### geometric brownian motion ###
# plt.plot(t, P)
# plt.show()
