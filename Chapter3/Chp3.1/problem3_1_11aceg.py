"""
Problem 3.1.11

Modify Algorithm 3.2 to perform regula-falsi  and use the new method 
to find the same roots as in problem 3.1.3. Stop the program when the 
difference b/n the consecutive iterates is less than 10^-6.
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
    sol=ex.iteration_regula_falsi(functs[i], intervals[i][0], intervals[i][1], 10000)
    results=ex.err_regula_falsi(functs[i], intervals[i][0], intervals[i][1], err,True)
    print('f(x) = {}\tSteps to be accurate within {:6.6f}: {}'.format(funct_names[i],err,results))
    print('(aplha = {})\n'.format(sol))