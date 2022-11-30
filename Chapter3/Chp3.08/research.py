import sys
import math
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

def plot_function(f,a,b,name='f(x)'):
    x=np.linspace(a,b,100,endpoint=True)
    y=np.array([f(val) for val in x])
    plt.plot(x,y,label=name)

def plot_secant(f,a,b,name='a secant line'):
    x=np.linspace(a,b,100,endpoint=True)
    y=np.array([f(val) for val in x])
    plt.plot(x,y,label=name)

def get_secants(x0,x1,f,n,verbose=False):
    secants=[]
    i=n+1

    f0=f(x0)
    f1=f(x1)

    while n>0:
        x = x1 - f1*(x1-x0)/(f1-f0)
        secants.append(f1*(x1-x0)/(f1-f0))
        x0=x1
        x1=x
        f0=f1
        f1=f(x)
        if verbose:
            print('Iteration {}: {:10.10f}'.format(i-n,x))
        n-=1
    return x

if __name__ == "__main__":
    functions = [lambda x: x**3-2,
                lambda x: math.exp(x)-2,
                lambda x: x-math.exp(-1.0*x),
                lambda x: x**6-x-1,
                lambda x: x**3-2*x-5,
                lambda x: 1-2*x*math.exp(-1.0*x/2.0),
                lambda x: 5-x**(-1.0),
                lambda x:x**2-math.sin(x)]
    x0s = [0,0,0,0,0,0,0.1,0]
    x1s = [2,1,1,2,3,2,0.25,math.pi]
    func_names = ['x^3-2','e^x-2','x-e^(-x)','x^6-x-1','x^3-2x-5','1-2xe^(-x/2)','5-e^(-x)','x^2-sinx']
    parts = ['a','b','c','d','e','f','g','h']