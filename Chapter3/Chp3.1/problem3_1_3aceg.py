"""
Problem 3.1.3

Write a program that uses the bisection method to find the root of a 
given function on a gicen interval, and apply this program to find the
roots of the functions below on the indicated intervals. Use the relationship
(3.2) to determine a priori the number of  steps neccessary for  the root to
be accurate within 10^-6.

a) x^3-2          [0,2]
c) x-e^-x         [0,1]
e) x^3-2x-5       [0,3]
g) 5-x^(-1)       [0.1,0.25]
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex


err=math.pow(10,-6)
functs = [
    lambda x: x**3-2,
    lambda x: x-math.exp(-1.0*x),
    lambda x: x**3-2*x-5,
    lambda x: 5-x**(-1)
]
intervals=[[0,2],[0,1],[0,3],[0.1,0.25]]
funct_names=['x^3-2','x-e^-x','x^3-2x-5','5-x^(-1)']

for i in range(0,4):
    results=ex.err_bisection(functs[i], intervals[i][0], intervals[i][1], err)
    print('f(x) = {}\tSteps to be accurate within {:6.6f}: {}'.format(funct_names[i],err,results[0]))
    print('(aplha = {})\n'.format(results[1]))
    
