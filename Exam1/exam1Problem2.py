# Will Townsend
# Problem 2

import numpy as np
import math

# implementation of algorithm 2.3 from the textbook using Python
def hornersRule(polyvec, val):

    # this empty list will eventually return the result of the algorithms
    result = []

    # variable holds the polyvec length
    veclen = len(polyvec)

    p = polyvec[veclen-1]
    
    # Implement horner's rule in our for loop
    for i in range(veclen-2,-1,-1):
        p = val*p + polyvec[i]

    result.append(p)

    dp = (veclen-1)*polyvec[veclen-1]

    # Implement Horner's Rule on the derivative of the polynomial
    for i in range(veclen-2,0,-1):
        dp = dp*val + polyvec[i]*i

    result.append(dp)
    return result

poly1 = [13,0,0,0,0,0,0,0,0,0,0,0,0,1]
poly2=[-6,5,-4,3,-2,1]
poly3=[1,1,1,1,1,1,1,1,1,1,1]
x0=[1,2]

for x in x0:
    res = hornersRule(poly1,x)
    print('p1({}) = {}'.format(x,res[0]))
    print('p1\'({}) = {}'.format(x,res[1]))
    print('')

    res = hornersRule(poly2,x)
    print('p2({}) = {}'.format(x,res[0]))
    print('p2\'({}) = {}'.format(x,res[1]))
    print('')

    res = hornersRule(poly3,x)
    print('p3({}) = {}'.format(x,res[0]))
    print('p3\'({}) = {}'.format(x,res[1]))
    print('')

