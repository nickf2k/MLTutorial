from __future__ import division, print_function, unicode_literals

import matplotlib.pyplot as plt
import numpy as np

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
# show data
# plt.plot(x,y,'ro')
# plt.axis([140, 190, 45, 75])
# plt.xlabel("height")
# plt.ylabel("weight")
# plt.show()

'''build xbar'''
one = np.ones((X.shape[0], 1))  # tao ma tran don vi x.shape[0]*1 trong do x.shape[0] = so hang cua x
print(one)

Xbar = np.concatenate((one, X),
                      axis=1)  # tra ve truc X, ban chat la noi cac mang voi nhau, axis la truc doc ma cac mang se dc noi
# vi du ket qua in duoi day
print(Xbar)
''' calculating weight of the fitting line'''
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print("w = ", w)

'''prepare the fitting line'''
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(145, 185, 2)  # tra ve 1 tap cac so: 145,147,149,.....185
y0 = w_0 + w_1 * x0  # khai bao y0
# drawing the fitting line
plt.plot(X.T, y.T, 'ro')
plt.plot(x0, y0)
plt.axis([140, 190, 45, 75])
plt.xlabel("height")
plt.ylabel("weight")
plt.show()
dp = [0] * 4
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
print(dp)
