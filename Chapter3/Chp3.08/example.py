import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

f = lambda x: x**2-math.exp(-1.0*x)

ex.secant_method(0, 1, f, math.pow(10,-6.0),True)

