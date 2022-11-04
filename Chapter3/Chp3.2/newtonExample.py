# Example file to test newtons_method in course_functs library
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

def f(x):
    return math.exp(x)-x**2

def fprime(x):
    return math.exp(x)-2*x

print('Newton\'s Method Root Estimate: {}'.format(ex.newtons_method(f, fprime, 0, math.pow(10,-5),True)))