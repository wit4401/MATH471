""" Program uses the example tridiagonal matrix to test the algorithm/function for tridiagonal matricies Chapter 2.6 """
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

upper=[2.0,6.0,0.0]
lower=[0.0,2.0,4.0]
diagonal=[1.0,3.0,8.0]
coeff=[2.0,8.0,16.0]

print('{}'.format(ex.solve_tridiagonal(lower, diagonal, upper, coeff)))