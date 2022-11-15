"""
Problem 3.1.10

Do three iterations of the regula-falsi applied to f(x)=x^3-2, using a=0 b=2.
Compare to your results from problem 3.1.10.
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

f = lambda x:x**3-2
a=0
b=2

ex.iteration_regula_falsi(f, a, b, 3, True)