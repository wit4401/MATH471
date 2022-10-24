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

def ErrorTrap(lowlim,uplim,errtol,fdoubleprime_bound,verbose=False):
    MAX=100000
    for n in range(1,MAX):
        #Slower move linearly through # of subintervals:
        h=(uplim-lowlim)/n

        # Estimate error bound for Trapezoidal approx to integral:
        err=(uplim-lowlim)/12.0*math.pow(h,2)*fdoubleprime_bound

        if err<=errtol:
            if verbose:
               print('Approx within {:8.8f} for {} where h  = {:10.8f}'\
                     .format(err,n,h))
            return n

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

def funct8(x):
    return x**2*math.exp(-1.0*x)

def funct9(x):
    return 1/(1+25*x**2)

def funct10(x):
    return math.sqrt(1-x**2)

def funct11(x):
    return math.log(x,math.exp(1.0))

def funct12(x):
    return x**(5/2)

def funct13(x):
    return math.exp(-1.0*x)*math.sin(4*x)

def funct14(x):
    return math.exp(-1.0*x**2)

def funct15(x):
    return math.log(x,math.exp(1.0))

def funct16(x):
    return 1/(1+x**2)

def funct17(x):
    return math.cos(math.pi*x/2)

def funct18(x):
    return math.sqrt(1+math.cos(x)**2)

def funct19(x):
    return math.sqrt(1+(1/x)**2)