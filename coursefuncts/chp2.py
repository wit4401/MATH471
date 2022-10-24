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
