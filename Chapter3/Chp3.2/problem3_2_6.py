"""
Problem 3.2.6

Do three iterations of newton's method for f(x) = 3-e^x, using x0=1.
Repeat using x0=2,4,8,16. Comment your results.
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

def f(x):
    return 3-math.exp(x)

def fprime(x):
    return -math.exp(x)

x0s=[1,2,4,8,16]
for x0 in x0s:
    print('x0 = {}'.format(x0))
    ex.newtons_method_iter(f, fprime, x0, 3, True)
    print('')

