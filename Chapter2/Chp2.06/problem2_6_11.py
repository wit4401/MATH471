"""
Problem 2.6.11
"""
import math
import numpy as np
import sys
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

vals=[]

for i in range(1,11):
    temp=[]
    for j in range(1,11):
        if abs(i-j)==1:
            temp.append(1)
        elif i == j:
            temp.append(j+1)
        else:
            temp.append(0)
    vals.append(temp)

A = np.matrix([vals[0],vals[1],vals[2],vals[3],vals[4],vals[5],vals[6],vals[7],vals[8],vals[9]],dtype=np.float64)
coeff = np.array([1,1,1,1,1,1,1,1,1,1],dtype=np.float64)

print('Given Matrix:\n{}'.format(A))
print('Coefficients: {}\n'.format(coeff))

res = ex.tridiagonal(A,coeff)
print('Tridiagonal Solution: {}'.format(res))
