# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt

# height (cm)
x = np.array([[147, 150, 153, 158]]).T
#, 163, 165, 168, 170, 173, 175, 178, 180, 183
# weight (kg)
y = np.array([[ 49, 50, 51,  54]]).T
#, 58, 59, 60, 62, 63, 64, 66, 67, 68

one = np.ones((x.shape[0], 1))
Xbar = np.concatenate((one, x), axis = 1)

# Calculating weights of the fitting line
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
c = np.linalg.pinv(A)
w = np.dot(c, b)

print(Xbar)
print("= = = = = = = = = =")
print(Xbar.T)
print("= = = = = = = = = =")
for i in range(0,len(A)):
    for j in range(0,len(A[i])):
        print(A[i][j], end = " ")
    print()
print("= = = = = = = = = =")
for i in range(0,len(b)):
    for j in range(0,len(b[i])):
        print(b[i][j], end = " ")
    print()
print("= = = = = = = = = =")
for i in range(0,len(c)):
    for j in range(0,len(c[i])):
        print(c[i][j], end = " ")
    print()
print("= = = = = = = = = =")

print('w = ', w)

# Preparing the fitting line
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(145, 185, 2)
y0 = w_0 + w_1*x0


