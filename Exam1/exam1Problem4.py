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

for x in hinv:
    t = np.linspace(0,1,x+1,endpoint=True)
    res=eulersMethod(ode1, t, y0, 1/x)
    print('At h = 1/{}: {}'.format(x,res[-1]))

print('')

x0=0
y0=1
hinv = [8,16,64]
for x in hinv:
    t = np.linspace(0,1,x+1,endpoint=True)
    res=eulersMethod(ode2, t, y0, 1/x)
    print('At h = 1/{}: {}'.format(x,res[-1]))

# Plotting portion
res1 = res2 = res3 = res4 = []
t1 = t2 = []

t1 = np.linspace(0,1,9,endpoint=True)
res1 = eulersMethod(ode1, t1, y0, 1/8)
t2 = np.linspace(0,1,65,endpoint=True)
res2 = eulersMethod(ode1, t2, y0, 1/64)
res3 = eulersMethod(ode2, t1, y0, 1/8)
res4 = eulersMethod(ode2, t2, y0, 1/64)

plt.figure(figsize=(7,8))      
plt.plot(t1,res1,label='ode 1 hinv = 8')
plt.plot(t2,res2,label='ode 1 hinv = 64')
plt.legend()

plt.figure(figsize=(7,8))
plt.plot(t1,res3,label='ode 2 hinv = 8')
plt.plot(t2,res4,label='ode 2 hinv = 64')
plt.legend()
plt.show()