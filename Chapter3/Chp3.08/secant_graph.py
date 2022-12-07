import sys
import math
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

def plot_function(f,a,b,name='f(x)'):
    retval=[]
    x=np.linspace(a,b,100,endpoint=True)
    retval.append(x)
    retval.append(np.array([f(val) for val in x]))
    return retval

def get_secants(x0,x1,f,n,verbose=False):
    secants=[]
    x=0
    i=n+1

    f0=f(x0)
    f1=f(x1)

    while n>0:
        secantList=[]
        x = x1 - f1*(x1-x0)/(f1-f0)
        secantList.append((f0*x1-f1*x0)/(x1-x0))
        secantList.append((f1-f0)/(x1-x0))
        x0=x1
        x1=x
        f0=f1
        f1=f(x)
        if verbose:
            print('Iteration {}: {:10.10f}'.format(i-n,x))
        n-=1
        secants.append(secantList)
    return secants

if __name__ == "__main__":
    f = lambda x: x**3-2

    sec=[]
    secant_plots=[]
    secs=get_secants(0, 2, f, 6, True)
    for line in secs:
        secant_plots.append(plot_function(lambda x: line[0]+line[1]*x, -1, 3))
    axis=plot_function(f, -1, 3)

    i=1
    for sec in secant_plots:
        plt.figure(figsize=(7,8))
        l=str(i)
        plt.plot(axis[0],axis[1],label='x^3-2')
        plt.plot(sec[0],sec[1],label=l)
        i+=1
    plt.legend()
    plt.show()
