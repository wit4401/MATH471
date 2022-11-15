"""
Problem 3.1.5

Use Algorithm 3.2 to solve the nonlinear equation x=e^-x. Again, choose
your own interval by some judicious experimentation with a calculator.
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

f=lambda x:x-math.exp(-1.0*x)
a=0
b=1

ex.iteration_bisection(f, a, b, 10000, True)