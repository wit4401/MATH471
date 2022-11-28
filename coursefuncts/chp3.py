import math
import numpy as np
import coursefuncts.chp2 as chp2
import matplotlib.pyplot as pyplot

""" Chapter 3.1 The Bisection Method """
# prints out all iterations 1 to n of bisection method using the algorithm in Chp 3.1
def iteration_bisection(f,a,b,n,verbose=False):
    retval=False
    if f(a)*f(b) > 0:
        print('Error! f(a)f(b)>0!') 
    else:
        low=a
        up=b
        for i in range(1,n+1):
            c=low+(up-low)/2
            if f(c)*f(low) < 0:
                up=c
            elif f(up)*f(c) < 0:
                low=c
            elif f(c) == 0:
                retval=c
                if verbose:
                    print('Root of f(x) is {} after {} iterations'.format(c,i))
                break
            else:
                print('Iteration Error!')
                break
            if verbose:
                print('Iteration {}:\tRoot of f(x): {}'.format(i,c))
    return retval

# Returns a list [number of iterations, the root at final iteration]
def err_bisection(f,a,b,err,verbose=False):
    if f(a)*f(b) > 0:
        print('Error! f(a)f(b)>0!')
        res=False
    else:
        res=[]
        low=a
        up=b
        n = math.ceil((math.log(b-a,2)-math.log(err,2)))
        res.append(n)
        for i in range(1,n+1):
            c=low+(up-low)/2
            if f(c)*f(low) < 0:
                up=c
            elif f(up)*f(c) < 0:
                low=c
            if verbose:
                print('Iteration {}:\tRoot: {}'.format(i,c))
        res.append(c)
    return res

def err_regula_falsi(f,a,b,err,verbose=False):
    if f(a)*f(b) > 0:
        print('Error! f(a)f(b)>0!')
        res=False
    else:
        res=0
        low=a
        up=b

        c=up-(f(up)*(up-low))/(f(up)-f(low))
        if f(c)*f(low) < 0:
            up=c
        elif f(up)*f(c) < 0:
            low=c
        res+=1
        if verbose:
            print('Iteration {}:\tRoot: {}'.format(res,c))
        temp=up-(f(up)*(up-low))/(f(up)-f(low))

        while abs(temp-c)>err:
            temp=c
            c=up-(f(up)*(up-low))/(f(up)-f(low))
            if f(c)*f(low) < 0:
                up=c
            elif f(up)*f(c) < 0:
                low=c
            if verbose:
                print('Iteration {}:\tRoot: {}'.format(res+1,c))
            res+=1
    return res

def iteration_regula_falsi(f,a,b,n,verbose=False):
    retval=False
    if f(a)*f(b) > 0:
        print('Error! f(a)f(b)>0!')
    else:
        low=a
        up=b
        for i in range(1,n+1):
            c=up-(f(up)*(up-low))/(f(up)-f(low))
            if f(c)*f(low) < 0:
                up=c
            elif f(up)*f(c) < 0:
                low=c
            elif f(c) == 0:
                retval=c
                if verbose:
                    print('Root of f(x) is {} after {} iterations'.format(c,i))
                break
            else:
                print('Iteration Error!')
                break
            if verbose:
                print('Iteration {}:\tRoot of f(x): {}'.format(i,c))
    return retval

""" Chapter 3.2 Newton's Method: Derivation and Examples """
def newtons_method(f,fprime,x0,err,verbose=False):
    if fprime:
        if verbose:
            print('Derivative Function Given.')
        
        temp = x0-(f(x0)/fprime(x0))
        retval = temp-(f(temp)/fprime(temp))

        if verbose:
            print('Iteration 1: {}'.format(temp))
            print('Iteration 2: {}'.format(retval))

        i = 3
        iter_max = 101
        while i<iter_max and (retval-temp)>=err:
            temp=retval
            retval=temp-(f(temp)/fprime(temp))
            if verbose:
                print('Iteration {}: {}'.format(i,retval))  
            i+=1
        if verbose:
            print('')
    else:
        if verbose:
            print('Derivative Function NOT Given.')
        
        temp = x0-(f(x0)/chp2.evenBetterApprox(f, x0, err/10.0))
        retval = temp-(f(temp)/chp2.evenBetterApprox(f, temp, err/10.0))

        if verbose:
            print('Iteration 1: {}'.format(temp))
            print('Iteration 2: {}'.format(retval))

        i = 3
        iter_max = 101
        while i<iter_max and (retval-temp)>=err:
            temp=retval
            retval=temp-(f(temp)/chp2.evenBetterApprox(f, temp, err/10.0))
            if verbose:
                print('Iteration {}: {}'.format(i,retval)) 
            i+=1
        if verbose:
            print('')
    return retval

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

""" Chapter 3.3 How to Stop Newton's Method """
def another_newtons_method(f,fprime,x0,err,verbose=False):
    if fprime:
        if verbose:
            print('Derivative Function Given.')
        
        temp = x0-(f(x0)/fprime(x0))
        retval = temp-(f(temp)/fprime(temp))

        if verbose:
            print('Iteration 1: {}'.format(temp))
            print('Iteration 2: {}'.format(retval))

        i = 3
        iter_max = 101
        while i<iter_max and abs(retval-temp) + abs(f(retval))>=err/5.0:
            temp=retval
            retval=temp-(f(temp)/fprime(temp))
            if verbose:
                print('Iteration {}: {}'.format(i,retval))  
            i+=1
        if verbose:
            print('')
    else:
        if verbose:
            print('Derivative Function NOT Given.')
        
        temp = x0-(f(x0)/chp2.evenBetterApprox(f, x0, err/10.0))
        retval = temp-(f(temp)/chp2.evenBetterApprox(f, temp, err/10.0))

        if verbose:
            print('Iteration 1: {}'.format(temp))
            print('Iteration 2: {}'.format(retval))

        i = 3
        iter_max = 101
        while i<iter_max and abs(retval-temp) + abs(f(retval))>=err/5.0:
            temp=retval
            retval=temp-(f(temp)/chp2.evenBetterApprox(f, temp, err/10.0))
            if verbose:
                print('Iteration {}: {}'.format(i,retval)) 
            i+=1
        if verbose:
            print('')
    return retval
""" Chapter 3.4 Application: Division Using Newton's Method """
def newtons_division(adiv,err,verbose=False):
    # using knowlege from 3.4 we can derive this formula for our intial value
    x0=3-2*adiv

    # then apply the equation to the inverse of fraction we are finding and the 
    # initial value starting with the first two iterations.
    temp=x0*(2-x0*adiv)
    retval=temp*(2-temp*adiv)

    if verbose:
        print('x{} = {}'.format(1,temp))
        print('x{} = {}'.format(2,retval))
    i = 3
    iter_max = 101
    while i<iter_max and abs(1/adiv-retval)>=err/5.0:
        temp=retval
        retval=temp*(2-temp*adiv)
        if verbose:
            print('x{} = {}'.format(i,retval))
        i+=1

""" Chapter 3.7 Application: Computation of the Square Root """
def sqrt_estimate():
    pass
""" Chapter 3.8 The Secant Method: Derivation and Examples """
def secant_method(x0,x1,f,err,verbose=False):
    i=1
    max_iter = 101

    f0=f(x0)
    f1=f(x1)

    retval= x1 - f1*((x1-x0)/(f1-f0))
    temp=x1
    while i < max_iter and abs(retval-temp)>err:
        if verbose:
            print('Iteration {}: {:10.10f}'.format(i,retval))
        retval = retval - f(retval)*((retval-temp)/(f(retval)-f(temp)))
        temp=retval
        i+=1
    return retval
""" Chapter 3.9 Fixed-Point Iteration """

""" Chapter 3.10  Roots of Polynomials Part I """