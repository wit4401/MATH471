"""
This file contains a library of functions required for each HW problem in section 2.5
"""
import math

def trapezoidal_method(f,lowerLim,upperLim,n):
    h = (upperLim-lowerLim)/n
    sum = 0.5*(f(upperLim)+f(lowerLim))
    for i in range(1,n):
        x = lowerLim + i*h
        sum+=f(x)
    return sum*h

def funct1(x):
    return x**3

def funct2(x):
    return math.sin(x)

def funct3(x):
    return 1/math.sqrt(1+x**4)

def funct4(x):
    return x*(1-x**2)

def funct5(x):
    return math.log(1+x,math.exp(1.0))

def funct6(x):
    return 1/(1+x**3)

def funct7(x):
    return math.exp(-1.0*(x**2))