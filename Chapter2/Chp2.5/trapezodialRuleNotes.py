# Note: max_[0,1] |f''(x)| need to be calculated/estimated!

#
# Example 2.6 from Section 2.5:
#
# "For example, consider the integral:
#      I(f) = \int_0^1 * e^{-x^2}
#  How small does h have to be to guarentee that
#      |I(f)-T_n(f)| < 10^{-3}?"

import math
import numpy as np

# Approximates integral of given function f using the Trapezodial Rule
# on an evenly-spaced grid when n is the number of subintervals, lowlim is
# lower limit of integration and uplim is upper limit of integration.

def Trap1(f,n,lowlim,uplim):
    h = (uplim-lowlim)/n
    val = f(lowlim)+f(uplim)
    x_i = np.linspace(lowlim+h,uplim-h,n-1)
    
    for i in x_i:
        val+=2*f(i) 

    return (h/2)*val

def ErrorTrap(lowlim,uplim,errtol,fdoubleprime_bound,verbose=False):
    MAX=1000
    for n in range(1,MAX):
        #Slower move linearly through # of subintervals:
        h=(uplim-lowlim)/n

        #Faster-double the number of subinterval on each estimation
        #h=(uplim-lowlim)/n

        # Estimate error bound for Trapezoidal approx to integral:
        err=(uplim-lowlim)/12.0*math.pow(h,2)*fdoubleprime_bound

        if err<=errtol:
            if verbose:
               print('Approx within {:8.8f} for {} where h  = {:10.8f}'\
                     .format(err,n,h))
            return n
def err_function(x):
    return math.exp(-1*math.pow(x,2.0))

a=0.0
b=1.0
T4=Trap1(err_function,4,a,b)
T8=Trap1(err_function,8,a,b)
T16=Trap1(err_function,16,a,b)
IR=(4.0*T8-T4)/3.0

# What does theory tell us?
# We have a bound: |I(f)-T_n(f)|<=1/12*(b-a)*h^2*max_[0,1]|f''(x)|

#example 2.6 check trapezodial rule:
checkval=0.746824132812 #precalculated

print('Integral approx Ex 2.6 (h=1/4): {:8.8f}, checkval: {:8.8f}'.format(T4,checkval))
print('Integral approx Ex 2.6 (h=1/8): {:8.8f}, checkval: {:8.8f}'.format(T8,checkval))
print('Integral approx Ex 2.6 (h=1/16): {:8.8f}, checkval: {:8.8f}'.format(T16,checkval))

error_tolerance=math.pow(10,-6.0)
fdpb=1.0

numtraps=ErrorTrap(a,b,error_tolerance,fdpb)
print('Number of trapezoids theoretically required to guarantee approximation within {} error tolerance: n = {}'.format(error_tolerance,numtraps))

