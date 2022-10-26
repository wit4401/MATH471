"""
Problem 2.6.4
Solve the following system of equations (Tridiagonal Matrix):
6x_1 + x_2 = 8
2x_1 + 4x_2 + x_3 = 13
x_2 + 4x_3 + 2x_4 = 22
x_3 + 6x_4 = 27
"""
import math
import numpy as np
import sys
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

A = np.matrix('6 1 0 0; 2 4 1 0; 0 1 4 2; 0 0 1 6',dtype=np.float64)
coeff = np.array([8,13,22,27],dtype=np.float64)

print('Given Matrix:\n{}'.format(A))
print('Coefficients: {}\n'.format(coeff))

res = ex.tridiagonal(A,coeff)
print('Tridiagonal Solution: {}'.format(res))