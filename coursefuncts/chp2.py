# This file is a library that contains all the functions buit for the sections
# covered in Chapter 2 (2.1-2.7)
import sys
import math
import matplotlib.pyplot as plt
import numpy as np

""" Chapter 2.1: Horner's Rule and Nested Multiplication """
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

def HornersRuleEven(polyvec,val):
    # define our first coefficient
    p = polyvec[len(polyvec)-1]

    # Applying Horner's rule (assuming all even powers)
    for i in range(len(polyvec)-2,-1,-1):

        # notice val is being taken to the second power
        p = p * val**2 + polyvec[i]

    return p

# Horner's Rule w/ Derivative of the polynomial
#
# Same thing here our implementation is a bit different for the derivative of our
# polynomials. In our derivative of the polynomials we can take advantage that all
# the powers are odd the same as we could with the original polynomial.
def HornersDerivative(polyvec,val):
    
    # define the first coefficient
    p = polyvec[len(polyvec)-1] * (len(polyvec)-1)*2
    
    # similar to our HornersRuleEven() however slightly modified to 
    # calculate the derivative instead (assuming original polynomial
    # had all even powers) (based on algorithm 2.2 in the text)
    for i in range(len(polyvec)-2,0,-1):
        p = p * val**2 + polyvec[i] * i*2

    # However we are not done since we need to account for the fact our
    # polynomial has all odd powers after the derivative is taken 
    # 
    # All the powers taken of the value are even which will result in an 
    # inaccurate result for our derivative (this was not needed in the
    # original algorithm)
    # 
    # this is fixed by multiplying our result from the above loop by our val
    # (think back to how to do a nested loop for odd powers)
    p = p * val

    return p

""" Chapter 2.2 Difference Approximations to the Derivative """
def naiveApprox(f,x,h):
    return (f(x+h)-f(x))/h

def betterApprox(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

def evenBetterApprox(f,x,h):
    return (8*f(x+h)-8*f(x-h)-f(x+2*h)+f(x-2*h))/(12*h)

""" Chapter 2.3 Application: Euler's Method for Initial Value Problems """
def eulersMethod(f,t,y0,delta):
    retval = np.arange(t[0],t[-1]+delta,delta)
    retval[0] = y0

    for i in range(1,len(t),1):
        retval[i]=retval[i-1]+delta*f(t[i-1],retval[i-1])

    return retval

""" Chapter 2.4 Linear Interpolation """

# No code here as of now...

""" Chapter 2.5 Application: Trapezoid Rule """
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
               print('Approx within {} for {} where h  = {:10.8f}'\
                     .format(err,n,h))
            return n

""" Chapter 2.6 Solutions to Tridiagonal Linear Systems """
def __solve_tridiagonal(A,b):
    numrows,numcols = A.shape
    
    # obtains the diagonals from the matrix
    diagonal=np.diagonal(A,0,0,1).copy()
    upper=np.diagonal(A,1,0,1).copy()
    lower=np.diagonal(A,-1,0,1).copy()
    coeff=b

    # Forward phase
    for i in range(1,numrows):
        diagonal[i]-=upper[i-1]*lower[i-1]/diagonal[i-1]
        coeff[i]-=coeff[i-1]*lower[i-1]/diagonal[i-1]
    # Backsolve phase
    coeff[-1]/=diagonal[-1]
    for i in range(numrows-2,-1,-1):
        coeff[i]-=upper[i]*coeff[i+1]
        coeff[i]/=diagonal[i]
    return coeff

def isTridiagonal(A):
    retval=True
    numcols,numrows=A.shape
    for i in range(0,numrows):
        for j in range(0,numcols):
            if i!=j and i-1!=j and i+1!=j:
                if A[i,j] != 0:
                    retval=False
                    break
    return retval

def isDominant(A):
    retval=True
    numrows,numcols=A.shape
    for i in range(0,numrows):
        total=0
        for j in range(0,numcols):
            if i!=j:
                total+=abs(A[i,j])
        # Our check condition for each row to check for dominance
        if total > abs(A[i,i]):
            retval=False
            break
    return retval

def tridiagonal(A,b):
    retval=False
    if isTridiagonal(A):
        if isDominant(A):
            retval = __solve_tridiagonal(A, b)
        else:
            print('Given matrix is not Diagonally Dominant')
            print('Try to compute anyway (y/n)? ',end='')
            inp = str(input())
            if inp == 'y' or inp == 'Y':
                retval = __solve_tridiagonal(A, b)
    else:
        print("Given matrix is not Tridiagonal!")
    return retval

def __solve_pentadiagonal(A,b):
    numcols,numrows = A.shape

    # obtains the diagonals from the matrix
    diagonal=np.diagonal(A,0,0,1).copy()
    upper=np.diagonal(A,1,0,1).copy()
    upperMid=np.diagonal(A,2,0,1).copy()
    lowerMid=np.diagonal(A,-2,0,1).copy()
    lower=np.diagonal(A,-1,0,1).copy()
    coeff=b

    for i in range(0,numcols-1):
        diagonal[i]-=upper[i-1]*lower[i-1]/diagonal[i-1]
        coeff[i]-=coeff[i-1]*lower[i-1]/diagonal[i-1]
    
    for i in range(numcols-2,-1,-1):
        coeff[i]-=upper[i]*coeff[i+1]
        coeff[i]/=diagonal[i]
    return coeff

def pentadiagonal(A,b):
    retval = False
    if isDominant(A):
        retval = __solve_pentadiagonal(A,b)
    else:
        print('Given matrix is not Diagonally Dominant')
        print('Try to compute anyway (y/n)? ',end='')
        inp = str(input())
        if inp == 'y' or inp == 'Y':
            retval = __solve_pentadiagonal(A, b)
    return retval

# the main function for the current program
def main(argv):
    print('Hello World {}'.format(argv))
    
if __name__ == "__main__":
    #call main function
    main(sys.argv[1:])