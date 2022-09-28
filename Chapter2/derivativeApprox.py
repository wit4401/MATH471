"""
Problem 2.2.3

Write a computer program that uses the same derivative
approximations as in the previous problem to approximate
the first derivative at x=1 for each of the following 
functions using h^-1=4, 8, 16, 32. Verigy that the predicted
theoretical accuracy is obtained - in other words, show that
your results are consistent with the analysis in this section.

Functions:
a) (x+1)^1/2
b) arctan x
c) sin(pi*x)
d) e^-x
e) ln x
"""
import math

def naiveApprox(f,x,h):
    return (f(x+h)-f(x))/h

def betterApprox(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

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
hvals = [2**-4,2**-8,2**-16,2**-32]
for i in hvals:
    print('When h = {}:'.format(i))
    print('Naive Approximation of the function at {}: {}'.format(xval, naiveApprox(funct, xval, i)))
    print('Better Approximation of the function at {}: {}'.format(xval,betterApprox(funct, xval, i)))
    print('"Exact" Value of of the function at {}: {}\n'.format(xval, dfunct(xval)))

