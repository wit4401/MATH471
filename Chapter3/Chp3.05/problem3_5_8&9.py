"""
Problem 3.5.8

Consider now the function f(x)= 7x-cos(2pix). Show that a root exists on
the interval [0,1], and then use newton's error estimation to determine how
close x0 has to be to the root to guarantee convergence.

Problem 3.5.9

Investigate your results in the previous problem by applying Newton's method
to f(x)=7x-cos(2pix), using several choices of x0 within the interval [0,1]
Comment on your results in light of the theory of the method.

"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

f = lambda x: 7*x-math.cos(2*math.pi*x)
