"""
Problem 3.1.3

Write a program that uses the bisection method to find the root of a 
given function on a gicen interval, and apply this program to find the
roots of the functions below on the indicated intervals. Use the relationship
(3.2) to determine a priori the number of  steps neccessary for  the root to
be accurate within 10^-6.

b) e^x-2          [0,1]
d) x^6-x-1        [0,2]
f) 1-2xe^(-x/2)   [0,2]
h) x^2-sin x    [0,pi]
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

err=math.pow(10,-6)
functs = [
    lambda x: math.exp(x)-2,
    lambda x: x**6-x-1,
    lambda x: 1-2*x*math.exp(-1.0*(x/2)),
    lambda x: x**2-math.sin(x)
]
intervals=[[0,1],[0,2],[0,2],[0,math.pi]]
funct_names=['e^x-2','x^6-x-1','1-2xe^(-x/2)','x^2-sin x']

for i in range(0,4):
    sol=ex.iteration_bisection(functs[i], intervals[i][0], intervals[i][1], 10000)
    results=ex.err_bisection(functs[i], intervals[i][0], intervals[i][1], err)
    print('f(x) = {}\tSteps to be accurate within {:6.6f}: {}'.format(funct_names[i],err,results[0]))
    print('(aplha = {})\n'.format(sol))