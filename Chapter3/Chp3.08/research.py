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
        x = x1 - f1*(x1-x0)/(f1-f0)
        secants.append(-1.0*(x1-x0)/(f1-f0))
        x0=x1
        x1=x
        f0=f1
        f1=f(x)
        if verbose:
            print('Iteration {}: {:10.10f}'.format(i-n,x))
        n-=1
    return secants

if __name__ == "__main__":
    functions = [lambda x: x**3-2,
                lambda x: x-math.exp(-1.0*x),
                lambda x: x**6-x-1,
                lambda x: 5-x**(-1.0)]
    x0 = 0
    x1s = [2,1,2,0.25]
    func_names = ['x^3-2','x-e^(-x)','x^6-x-1','5-x^(-1.0)']

    figure,graphs=plt.subplots(2,2)

    for i in range(0,len(functions)):
        sec=[]
        if i!=3:
            secs=get_secants(x0, x1s[i], functions[i], 5,True)
        else:
            secs=get_secants(0.1, x1s[i], functions[i], 5,True)
        axis=plot_function(functions[i], -2, 2)
        secant_plots=[]
        for line in secs:
            secant_plots.append(plot_function(lambda x: line*x, -2, 2))
        if i==0:
            graphs[0,0].plot(axis[0],axis[1])
            for sec in secant_plots:
                graphs[0,0].plot(sec[0],sec[1])
            graphs[0,0].set_title(func_names[i])
        elif i==1:
            graphs[0,1].plot(axis[0],axis[1])
            for sec in secant_plots:
                graphs[0,1].plot(sec[0],sec[1])
            graphs[0,1].set_title(func_names[i])
        elif i==2:
            graphs[1,0].plot(axis[0],axis[1])
            for sec in secant_plots:
                graphs[1,0].plot(sec[0],sec[1])
            graphs[1,0].set_title(func_names[i])
        else:
            graphs[1,1].plot(axis[0],axis[1])
            for sec in secant_plots:
                graphs[1,1].plot(sec[0],sec[1])
            graphs[1,1].set_title(func_names[i])
    
    plt.show()
