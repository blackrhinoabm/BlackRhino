import matplotlib.pyplot as plt
import numpy as np


# N = 100


# Z = np.random.normal(size = N)


# # method 1
# H,X1 = np.histogram( Z, bins = 10, normed = True )
# dx = X1[1] - X1[0]

# F1 = np.cumsum(H)*dx

# #method 2
# X2 = np.sort(Z)
# F2 = np.array(range(N))/float(N)

# plt.plot(X1[1:], F1)
# plt.plot(X2, F2)
# plt.show()

# # create some randomly ddistributed data:
# data = np.random.randn(1000)
# print data
# # sort the data:
# data_sorted = np.sort(data)
# print data_sorted
# # calculate the proportional values of samples
# p = 1. * np.arange(len(data)) / (len(data) - 1)

# print p

# # plot the sorted data:
# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# ax1.plot(p, data_sorted)
# ax1.set_xlabel('$p$')
# ax1.set_ylabel('$x$')

# ax2 = fig.add_subplot(122)
# ax2.plot(data_sorted, p)
# ax2.set_xlabel('$x$')
# ax2.set_ylabel('$p$')

# plt.show()

mu, sigma = 3., 0.6 # mean and standard deviation
x = np.random.lognormal(mu, sigma, 1000).tolist()

print np.mean(x)

# array([1, 2, 3, 2, 3, 4])
# >>> a = np.array([[1],[2],[3]])
# >>> b = np.array([[2],[3],[4]])
# >>> np.hstack((a,b))
# array([[1, 2],
#        [2, 3],
#        [3, 4]])



