

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
	r = norm.rvs(loc=(0.0000001)/2, size=x0.shape + (n,), scale=delta*sqrt(dt))

    # If `out` was not given, create an output array.
	if out is None:
		out = np.empty(r.shape)

    # This computes the Brownian motion by forming the cumulative sum of
    # the random samples.
	np.cumsum(r, axis=-1, out=out)

    # Add the initial conditionn
	out += np.expand_dims(x0, axis=-1)
	return out


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
    np.random.seed(seed=32) # 4, 37

    # np.random.seed(seed=4) # without loc=0.01 in function, looks like SA
    #There is a parameter inside def brownian - loc, with whom it's possible to get
    #a drift  # mu = 0.0 np.random.seed(seed=1)
    return brownian(x[:,0], N, dt, delta, out=x[:,1:])


def ornstein_uhlenbeck():
	import numpy as np
	import matplotlib.pyplot as plt
	t_0 = 0
	t_end = 2
	length = 10000
	theta  = 1.1
	mu =0.3
	sigma = 0.1

	t = np.linspace(t_0,t_end,length) # define time axis
	dt = np.mean(np.diff(t))
	y = np.zeros(length)
	y0 = np.random.normal(loc=0.0,scale=1.0) # initial condition
	drift = lambda y,t: theta*(mu-y) # define drift term, google to learn about lambda
	diffusion = lambda y,t: sigma # define diffusion term
	noise = np.random.normal(loc=0.0,scale=1.0,size=length)*np.sqrt(dt) #define noise process

	 # solve SDE
	for i in xrange(1,length):
		y[i] = y[i-1] + drift(y[i-1],i*dt)*dt + diffusion(y[i-1],i*dt)*noise[i]

	plt.plot(t,y)
	plt.show()

# ornstein_uhlenbeck()
