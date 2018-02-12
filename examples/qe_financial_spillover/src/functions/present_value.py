import random
from bisect import bisect

""" Get bond price from YTM """
import numpy as np

def calc_bond_price(par, T, ytm, coup, freq):
    freq = float(freq)
    periods = T*freq
    coupon = coup/100.*par/freq
    dt = [(i+1)/freq for i in range(int(periods))]
    price = sum([coupon/(1+ytm/freq)**(freq*t) for t in dt]) + \
            par/(1+ytm/freq)**(freq*T)
    return price

def calc_yield(nper, pmt, pv, fv):
    return np.rate(nper, pmt, pv, fv)

# calc_yield(10, 0, -62, 100)
# print calc_bond_price(100, 10, 0.05 , 0, 1)
