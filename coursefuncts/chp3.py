import math
import numpy as np
import coursefuncts.chp2 as chp2
import matplotlib.pyplot as pyplot

""" Chapter 3.1 The Bisection Method """
# prints out all iterations 1 to n of bisection method using the algorithm in Chp 3.1
def iteration_bisection(f,a,b,n,verbose=False):
    if f(a)*f(b) > 0:
        print('Error! f(a)f(b)>0!')
        c=False
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
                if verbose:
                    print('Root of f(x) is {} after {} iterations'.format(c,i))
                break
            else:
                print('Iteration Error!')
                break
            if verbose:
                print('Iteration {}:\tRoot of f(x): {}'.format(i,c))
    return c

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
        temp=x0-(f(x0)/fprime(x0))
        retval=0
        for i in range(1,n+1):
            retval = temp-(f(temp)/fprime(temp))
            temp=retval
            if verbose:
                print('Iteration {}\tRoot: {}'.format(i,retval))
    else:
        temp=x0-(f(x0)/chp2.evenBetterApprox(f, x0, math.pow(10,-5)))
        retval=0
        for i in range(1,n+1):
            retval = temp-(f(temp)/chp2.evenBetterApprox(f, temp, math.pow(10,-5)))
            temp=retval
            if verbose:
                print('Iteration {}\tRoot: {}'.format(i,retval))
    return retval

""" Chapter 3.3 How to Stop Newton's Method """

""" Chapter 3.4 Application: Division Using Newton's Method """

""" Chapter 3.5 The Newton Error Formula """

""" Chapter 3.6 Newton's Method: Theory and Convergence """

""" Chapter 3.7 Application: Computation of the Square Root """

""" Chapter 3.8 The Secant Method: Derivation and Examples """

""" Chapter 3.9 Fixed-Point Iteration """

""" Chapter 3.10  Roots of Polynomials Part I """

""" Chapter 3.11 Special Topics in Root Finding Methods """