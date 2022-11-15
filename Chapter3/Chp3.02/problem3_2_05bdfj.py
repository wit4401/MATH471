"""
Problem 3.2.5

Do three iterations of Newton's method for each of the following functions:
b) x+tanx         x0=3
d) 5-x^(-1)       x0=0.5
f) x^3-2x-5       x0=2
j) 2-x^(-1)lnx    x0=1/3
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

functs =[
    lambda x: x+math.tan(x),
    lambda x: 5-x**(-1),
    lambda x: x**3-2*x-5,
    lambda x: 2-x**(-1)*math.log(x,math.exp(1))
]
x0s = [3, 1/2, 2, 1/3]
funct_derivatives=[
    lambda x: 1+(1/math.cos(x)**2),
    lambda x: x**(-2),
    lambda x: 3*x**2-2,
    lambda x: x**(-2)*(-math.log(x,math.exp(1))+1)
]
funct_names=['x+tanx','5-x^(-1)','x^3-2x-5 ','2-x^(-1)lnx']

for i in range(0,len(functs)):
    print('f(x) = {}\tx0 = {}'.format(funct_names[i],x0s[i]))
    ex.newtons_method_iter(functs[i], funct_derivatives[i], x0s[i], 3, True)
    print('')