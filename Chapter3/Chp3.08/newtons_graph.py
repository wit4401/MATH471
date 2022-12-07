import sys
import math
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def plot_function(f,a,b,name='f(x)'):
    retval=[]
    x=np.linspace(a,b,100,endpoint=True)
    retval.append(x)
    retval.append(np.array([f(val) for val in x]))
    return retval

def get_tangents(f,fprime,x0,n,verbose=False):
    tansList=[]
    if fprime:
        if verbose:
            print('Derivative Function Given.')
        temp=x0-(f(x0)/fprime(x0))
        tans=[]
        tans.append(f(x0)-x0*fprime(x0))
        tans.append(fprime(x0))
        tansList.append(tans)
        retval=0
        for i in range(1,n+1):
            tans=[]
            retval = temp-(f(temp)/fprime(temp))
            tans.append(f(temp)-temp*fprime(temp))
            tans.append(fprime(temp))
            tansList.append(tans)
            temp=retval
            if verbose:
                print('Iteration {}\tRoot: {:20.20f}'.format(i,retval))
    else:
        if verbose:
            print('Derivative Function NOT Given.')
        temp=x0-(f(x0)/ex.evenBetterApprox(f, x0, math.pow(10,-5)))
        tans=[]
        tans.append(f(x0)-x0*ex.evenBetterApprox(f, x0, math.pow(10,-5)))
        tans.append(ex.evenBetterApprox(f, x0, math.pow(10,-5)))
        tansList.append(tans)
        retval=0
        for i in range(1,n+1):
            tans=[]
            retval = temp-(f(temp)/ex.evenBetterApprox(f, temp, math.pow(10,-5)))
            tans.append(f(temp)-temp*ex.evenBetterApprox(f, temp, math.pow(10,-5)))
            tans.append(ex.evenBetterApprox(f, temp, math.pow(10,-5)))
            tansList.append(tans)
            temp=retval
            if verbose:
                print('Iteration {}\tRoot: {:20.20f}'.format(i,retval))
    return tansList

if __name__ == "__main__":
    f = lambda x: x**3-2
    fprime=lambda x: 3*x**2
    x0 = 5

    tan=[]
    tan_plots=[]
    tans=get_tangents(f, fprime, x0, 6, True)
    for line in tans:
        tan_plots.append(plot_function(lambda x:line[0]+line[1]*x, -1, 7))
    axis=plot_function(f, -1, 7)
    
    i=1
    for tan in tan_plots:
        plt.figure(figsize=(7,8))
        l=str(i)
        plt.plot(axis[0],axis[1],label='x^3-2')
        plt.plot(tan[0],tan[1],label=l)
        i+=1
    plt.legend()
    plt.show()
