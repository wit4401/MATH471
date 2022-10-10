# Will Townsend
# Problem 4

import math
import numpy as np
import matplotlib.pyplot as plt

def eulersMethod(f,t,y0,delta):
    retval = np.arange(t[0],t[-1]+delta,delta)
    retval[0] = y0

    for i in range(1,len(t),1):
        retval[i]=retval[i-1]+delta*f(t[i-1],retval[i-1])

    return retval

def ode1(t,y):
    return math.exp(t-y)

def ode2(t,y):
    return 2-2*y-math.exp(-4*t)

x0=0
y0=-1
hinv = [8,16,64]
res1 = res2 = res3 = res4 = []
t1 = t2 = t3 = t4 = []
for x in hinv:
    t = np.linspace(0,1,x+1,endpoint=True)
    
    if hinv == 8:
        t1 = np.linspace(0,1,x+1,endpoint=True)
        res1 = eulersMethod(ode2, t, y0, 1/x)
    elif hinv == 64:
        t2 = np.linspace(0,1,x+1,endpoint=True)
        res2 = eulersMethod(ode2, t, y0, 1/x)
    
    res=eulersMethod(ode1, t, y0, 1/x)
    print('At h = 1/{}: {}'.format(x,res[-1]))

print('')

x0=0
y0=1
hinv = [8,16,64]
for x in hinv:
    t = np.linspace(0,1,x+1,endpoint=True)
    
    if hinv == 8:
        t3 = np.linspace(0,1,x+1,endpoint=True)
        res3 = eulersMethod(ode2, t, y0, 1/x)
    elif hinv == 64:
        t4 = np.linspace(0,1,x+1,endpoint=True)
        res4 = eulersMethod(ode2, t, y0, 1/x)
    
    res=eulersMethod(ode2, t, y0, 1/x)
    print('At h = 1/{}: {}'.format(x,res[-1]))

# small error in the plotting cannot get it to print properly
plt.figure(figsize=(7,8))      
plt.plot(t1,res1,label='ode 1 hinv = 8')
plt.plot(t2,res2,label='ode 1 hinv = 64')
plt.legend()

plt.figure(figsize=(7,8))
plt.plot(t3,res3,label='ode 2 hinv = 8')
plt.plot(t4,res4,label='ode 2 hinv = 64')
plt.legend()
plt.show()