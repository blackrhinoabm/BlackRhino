
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from scipy.stats import norm

def brownian_drift(brown_dt, brown_mu, brown_sigma):

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
