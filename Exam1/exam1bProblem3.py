# Will Townsend
# Problem 3

import math

def naiveApprox(f,x,h):
    return (f(x+h)-f(x))/h

def betterApprox(f,x,h):
    return (8*f(x+h)-8*f(x-h)-f(x+2*h)+f(x-2*h))/(12*h)

def funct1(x):
    return 10*math.cos(2*x)

def funct2(x):
    return (math.exp(x)-math.exp(-1.0*x))/2

def funct3(x):
    return x**x

xval = math.pi/4
hval = 2**(-6)
functs = [funct1,funct2,funct3]
i = 0
for func in functs:
    i+=1
    print('Part {}:'.format(i))
    print('When h = {}:'.format(hval))
    print('Naive Approximation of the function at {}: {}'.format(xval, naiveApprox(func, xval, hval)))
    print('Better Approximation of the function at {}: {}'.format(xval,betterApprox(func, xval, hval)))
    print('')