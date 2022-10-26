"""
Problem 2.6.2

Solve the following system of equations (Tridiagonal Matrix):
4x_1 + 2x_2 = pi/9
x_1 + 4x_2 + x_3 = sqrt(3)/2
x_2 + 4x_3 + x_4 = sqrt(3)/2
2x_3 + 4x_4 = -pi/9
"""
import math
import numpy as np
import sys
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

A = np.matrix('4 2 0 0; 1 4 1 0; 0 1 4 1; 0 0 2 4',dtype=np.float64)
coeff = np.array([math.pi/9,math.sqrt(3)/2,math.sqrt(3)/2,-math.pi/9],dtype=np.float64)

print('Given Matrix:\n{}'.format(A))
print('Coefficients: {}\n'.format(coeff))

res = ex.tridiagonal(A,coeff)
print('Tridiagonal Solution: {}'.format(res))
