"""
Problem 2.6.10
Solve the following two system of equations (Tridiagonal Matrix):
A)
(1/2)x_1 + (10/21)x_2 = 61/42
(1/4)x_1 + (1/3)x_2 + (1/13)x_3 = 179/156
(1/5)x_2 + (1/4)x_3 + (1/21)x-4 = 563/420
(1/6)x_3 + (1/5)x_4 = 13/10

B)
(1/2)x_1 + (10/21)x_2 = 61/42
(1/4)x_1 + (1/3)x_2 + (1/13)x_3 = 180/156
(1/5)x_2 + (1/4)x_3 + (1/21)x-4 = 563/420
(1/6)x_3 + (1/5)x_4 = 13/10
"""
import math
import numpy as np

import sys
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

# Create the matrix A and the coefficients for solving
A = np.matrix([[1/2, 10/21, 0, 0],[1/4, 1/3, 1/13, 0],[0, 1/5, 1/4, 1/21],[0, 0, 1/6, 1/5]],dtype=np.float64)
coeff1 = np.array([61/42,179/156,563/420,13/10],dtype=np.float64)

# Print out our Matrix A and the corresponding coefficients
print('Matrix A:\n{}'.format(A))
print('Coefficients: {}\n'.format(coeff1))

# Call tridiagonal function to find solutions to matrix A
res = ex.tridiagonal(A,coeff1)
print('Tridiagonal Solution: {}'.format(res))

# Create the matrix B and the coefficients for solving
B = np.matrix([[1/2, 10/21, 0, 0],[1/4, 1/3, 1/13, 0],[0, 1/5, 1/4, 1/21],[0, 0, 1/6, 1/5]],dtype=np.float64)
coeff2 = np.array([61/42,180/156,563/420,13/10],dtype=np.float64)

# Print out our Matrix B and the corresponding coefficients
print('Matrix B:\n{}'.format(B))
print('Coefficients: {}\n'.format(coeff2))

# Call tridiagonal function to find solutions to matrix B
res = ex.tridiagonal(B,coeff2)
print('Tridiagonal Solution: {}'.format(res))
