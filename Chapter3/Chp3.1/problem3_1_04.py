"""
Problem 3.1.4

Use Algorithm 3.2 to solve the nonlinear equation x=cos x. Choose
your own interval by some judicious experimentation with a calculator.
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

f=lambda x:x-math.cos(x)
a=0
b=math.pi/2

ex.iteration_bisection(f, a, b, 10000, True)