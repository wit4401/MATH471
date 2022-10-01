"""
This is another version of derivative approximation
Based on problem 2.2.11
"""
import math

def betterApprox(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

def evenBetterApprox(f,x,h):
    return (8*f(x+h)-8*f(x-h)-f(x+2*h)+f(x-2*h))/(12*h)

def funct(x):
    return math.sqrt(x+1)
    #return math.atan(x)
    #return math.sin(math.pi*x)
    #return math.exp(-1.0*x)
    #return math.log(x)

def dfunct(x):
    return 1/(2*math.sqrt(x+1))
    #return 1/(x**2+1)
    #return math.pi * math.cos(math.pi * x)
    #return -1.0*math.exp(-1.0*x)
    #return 1/x

xval = 1.0
hvals = [1/2,1/4,1/8,1/16]
for i in hvals:
    print('When h = {}:'.format(i))
    print('Better Approximation of the function at {}: {}'.format(xval, betterApprox(funct, xval, i)))
    print('Even Better Approximation of the function at {}: {}'.format(xval,evenBetterApprox(funct, xval, i)))
    print('"Exact" Value of of the function at {}: {}\n'.format(xval, dfunct(xval)))
