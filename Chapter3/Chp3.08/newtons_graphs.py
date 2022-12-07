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
    functions = [lambda x: x**3-2,
                lambda x: x-math.exp(-1.0*x),
                lambda x: x**6-x-1,
                lambda x: 5-x**(-1.0)]
    derivatives=[lambda x: 3*x**2,
                lambda x: 1+math.exp(-1.0*x),
                lambda x: 6*x**5-1,
                lambda x: x**(-2.0)]
    x0s = [2,1.25,1.5,1]
    func_names = ['x^3-2','x-e^(-x)','x^6-x-1','5-x^(-1.0)']

    figure,graphs=plt.subplots(2,2)
    for i in range(0,len(functions)):
        tan=[]
        tan_plots=[]
        tans=get_tangents(functions[i], derivatives[i], x0s[i], 3, True)
        if i!=3:
            for line in tans:
                tan_plots.append(plot_function(lambda x:line[0]+line[1]*x, -1, 3))
        else:
            for line in tans:
                tan_plots.append(plot_function(lambda x:line[0]+line[1]*x, 0.01, 1))
        if i==0:
            axis=plot_function(functions[i], -1, 3)
            graphs[0,0].plot(axis[0],axis[1])
            for tan in tan_plots:
                graphs[0,0].plot(tan[0],tan[1])
            graphs[0,0].set_title(func_names[i])
        elif i==1:
            axis=plot_function(functions[i], -1, 3)
            graphs[0,1].plot(axis[0],axis[1])
            for tan in tan_plots:
                graphs[0,1].plot(tan[0],tan[1])
            graphs[0,1].set_title(func_names[i])
        elif i==2:
            axis=plot_function(functions[i], -1, 3)
            graphs[1,0].plot(axis[0],axis[1])
            for tan in tan_plots:
                graphs[1,0].plot(tan[0],tan[1])
            graphs[1,0].set_title(func_names[i])
        else:
            axis=plot_function(functions[i], 0.01, 1)
            graphs[1,1].plot(axis[0],axis[1])
            for tan in tan_plots:
                graphs[1,1].plot(tan[0],tan[1])
            graphs[1,1].set_title(func_names[i])
    plt.show()
