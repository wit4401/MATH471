#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 10:02:49 2022
 
Will Townsend
"""
# Student Challenge:
#
# classChallenge1_2.py
# 

# We investigate representing the following function as a Taylor
# Polynomial degree 2, at different centers:
#
# For the following function:
# f(x) = e^(-x^2)
#
# Part A. Create f and Create degree 2 approximation of f
#         centered at 1.
#
# Part B. Plot f and approximation function.
#
# Part C. Create second approximating function with changeable (given)
#         center of approximation; plot f, approx, and approx2.
#
# Part D. Play (different centers, different orders of approximating 
#              functions)
#
# Research: Does the error in approximation improve much for higher degree
#           approximations on [-2,2] near 0? Near 1? Why or why not?
#
#

# import libraries
import math
import numpy

# import plotting library
import matplotlib.pyplot as plt

# Create f(x) = e^(-x^2)
def f( x ):
    
    #initialize a return value
    retval = 0.0
    
    # Do stuff to retval - evaluate given function
    retval = math.exp(-1.0 * math.pow(x,2))
    
    # return of retval
    return retval

# approximate f(x) above with taylor poly of degree 2 center of 1
def approx(x):
    
    # return the result of the function approximation
    return math.exp(-1.0)-2*math.exp(-1.0)*(x-1)+math.exp(-1.0)*math.pow(x-1,2)

# approximate f(x) with taylor polynomial of degree 2 with a center of c
def approx2(x,c):
    
    retval = f(c)\
    - 2*c*math.exp(-1.0*math.pow(c,2))*(x-c)\
    + math.exp(-1.0*math.pow(c,2))*(2*math.pow(c,2)-1)*math.pow(x-c,2)
    
    return retval

# set up a list oof values
vals = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]

# iterate thu values to test the function f(x) and approx(x)
for v in vals:
    #print('x = {:8.8f},\tf(x) = {:8.8f},\tapprox(x) = {:8.8f}'\
    #    .format(v, f(v), approx(v,1)))
    
    print('x = {:8.8f},\tf(x) = {:8.8f},\tapprox(x) = {:8.8f},\tapprox2(x,c) = {:8.8f}'\
          .format(v, f(v), approx(v), approx2(v,-1)))

# Plotting Below 
# ***This is not original code from me but class notes for future reference***

# Create domain space for our plot
t = numpy.linspace(-2,2,num=200,endpoint=True)
# print(t)

# Create range (y-values) for our plot of the original, reference fn:
y = numpy.array([f(x) for x in t])
# print(y)

# Create y-coordinates for the approximating function
a = numpy.array([approx(x) for x in t])

# Create y-coordinates for the second approximating function
x_1 = 0.0
b = numpy.array([approx2(x,x_1) for x in t])

#begin plot here
plt.plot(t,y,label='f(x)')
plt.plot(t,a,label='approx(x), x0 = {}'.format(1.0))
plt.plot(t,b,label='approx2(x), x0 = {}'.format(x_1))
plt.legend()
plt.show()
