"""
Problem 3.1.2ab

For each of the functions listed below, find the rooot to an accuracy of 0.1. 
This process  will  take at  most 5 iterations f or all of these and 
fewer for several.

a) f(x)=x-e^(-x^2) [0,1]
b) f(x)=ln x + x   [0.1,1]
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

def f1(x):
    return x-math.exp(-1.0*x**2)
def f2(x):
    return math.log(x,math.exp(1))+x

print('Part a:')
print('It takes {} iterations to be accurate within 0.1.\n'.format(ex.err_bisection(f1, 0, 1, 0.1, True)[0]))
print('Part b:')
print('It takes {} iterations to be accurate within 0.1.'.format(ex.err_bisection(f2, 0.1, 1, 0.1, True)[0]))