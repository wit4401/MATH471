"""
Problem 3.1.1

Do three iterations  of the bisection method, applied to f(x)=x^3-2 using
a=0 and b=2
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

def f(x):
    return x**3-2

ex.iteration_bisection(f, 0, 2, 3)