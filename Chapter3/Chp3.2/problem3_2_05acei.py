"""
Problem 3.2.5

Do three iterations of Newton's method for each of the following functions:
a) x^6-x-1         x0=1
c) 1-2xe^(-x/2)    x0=0
e) x^2-sinx        x0=0.5
i) x-e^(-x)        x0=1
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

functs =[
    lambda x: x**6-x-1,
    lambda x: 1-2*x*math.exp(-1.0*x/2),
    lambda x: x**2-math.sin(x),
    lambda x: x-math.exp(-1.0*x)
]
x0s = [3, 1/2, 2, 1/3]
funct_derivatives=[
    lambda x: 6*x**5-1,
    lambda x: -2*math.exp(-1.0*x/2)+x*math.exp(-1.0*x/2),
    lambda x: 2*x-math.cos(x),
    lambda x: 1+math.exp(-1.0*x)
]
funct_names=['x^6-x-1','1-2xe^(-x/2)','x^2-sinx','x-e^(-x)']

for i in range(0,len(functs)):
    print('f(x) = {}\tx0 = {}'.format(funct_names[i],x0s[i]))
    ex.newtons_method_iter(functs[i], funct_derivatives[i], x0s[i], 3, True)
    print('')