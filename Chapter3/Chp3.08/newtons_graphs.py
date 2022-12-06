import sys
import math
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def newtons_method_iter(f,fprime,x0,n,verbose=False):
    if fprime:
        if verbose:
            print('Derivative Function Given.')
        temp=x0-(f(x0)/fprime(x0))
        retval=0
        for i in range(1,n+1):
            retval = temp-(f(temp)/fprime(temp))
            temp=retval
            if verbose:
                print('Iteration {}\tRoot: {:20.20f}'.format(i,retval))
    else:
        if verbose:
            print('Derivative Function NOT Given.')
        temp=x0-(f(x0)/chp2.evenBetterApprox(f, x0, math.pow(10,-5)))
        retval=0
        for i in range(1,n+1):
            retval = temp-(f(temp)/chp2.evenBetterApprox(f, temp, math.pow(10,-5)))
            temp=retval
            if verbose:
                print('Iteration {}\tRoot: {:20.20f}'.format(i,retval))
    return retval
