import numpy as np 
import random 
import matplotlib.pyplot as plt
import math

from scipy import interpolate

import numpy as np
import pandas as pd

# mu, sigma = 2., 0.7 # mean and standard deviation
# mylist = np.random.lognormal(mu, sigma, 10).tolist()
# print mylist

# shocks =[i/-100 for i in mylist]



# HSBC
# CITYBANK
# INVESTEC
# African Bank
# CAPITEC
# NEDBANK
# FNB
# ABSA
# grindrod
# SOCIETE
# BNP
# DB
# BoC
# JpM
# CHARTERED
# SBSA


# mu, sigma = 2., 0.7 # mean and standard deviation
# s = np.random.lognormal(mu, sigma, 1000)

# count, bins, ignored = plt.hist(s, 100, normed=True, align='mid')
# x = np.linspace(min(bins), max(bins), 10000)
# pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))\
#        / (x * sigma * np.sqrt(2 * np.pi)))

# plt.plot(x, pdf, linewidth=2, color='r')
# plt.axis('tight')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interpolate

mu, sigma = -10, 1 # mean and standard deviation
# mylist = np.random.lognormal(mu, sigma, 100).tolist()

mylist = np.random.normal(mu, sigma, 100).tolist()
    
# mu, sigma = 2., 0.8 # mean and standard deviation
# mylist = np.random.lognormal(mu, sigma, 100).tolist()

# some fake data
data = np.random.randn(1000)
# evaluate the histogram
values, base = np.histogram(data, bins=40)
#evaluate the cumulative
cumulative = np.cumsum(values)
# plot the cumulative function
plt.plot(base[:-1], cumulative, c='blue')
#plot the survival function
plt.plot(base[:-1], len(data)-cumulative, c='green')

plt.show()

#Visualizing shocks
# count, bins, ignored = plt.hist(mylist, 100, normed=True, align='mid')
# x = np.linspace(min(bins), max(bins), 10000)
# pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))\
#    / (x * sigma * np.sqrt(2 * np.pi)))

# plt.plot(x, pdf, linewidth=2, color='r')
# plt.axis('tight')
# plt.show()
#
#print mylist

# plt.show()