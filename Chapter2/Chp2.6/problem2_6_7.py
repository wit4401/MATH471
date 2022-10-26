"""
Problem 2.6.7
Solve the following two system of equations (Tridiagonal Matrix):
A)
x_1 + (1/2)x_2 = 2
(1/2)x_1 + (1/3)x_2 + (1/4)x_3 = 23/12
(1/4)x_2 + (1/5)x_3 + (1/6)x_4 = 53/30
(1/6)x_3 + (1/7)x_4 = 15/14

B)
x_1 + (1/2)x_2 = 2
(1/2)x_1 + (1/3)x_2 + (1/4)x_3 = 2
(1/4)x_2 + (1/5)x_3 + (1/6)x_4 = 53/30
(1/6)x_3 + (1/7)x_4 = 15/14
"""
import math
import numpy as np
import sys
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

A = np.matrix([[1, 1/2, 0, 0],[1/2, 1/3, 1/4, 0],[0, 1/4, 1/5, 1/6],[0, 0, 1/6, 1/7]],dtype=np.float64)
coeff1 = np.array([2,23/12,53/30,15/14],dtype=np.float64)

print('Matrix A:\n{}'.format(A))
print('Coefficients: {}\n'.format(coeff1))

res = ex.tridiagonal(A,coeff1)
print('Tridiagonal Solution: {}\n'.format(res))

B = np.matrix([[1, 1/2, 0, 0],[1/2, 1/3, 1/4, 0],[0, 1/4, 1/5, 1/6],[0, 0, 1/6, 1/7]],dtype=np.float64)
coeff2 = np.array([2,2,53/30,15/14],dtype=np.float64)

print('Matrix A:\n{}'.format(B))
print('Coefficients: {}\n'.format(coeff2))

res = ex.tridiagonal(B,coeff2)
print('Tridiagonal Solution: {}\n'.format(res))
