# eulersMethodNotes.py (10.03.2022)
#
# Euler's Method for IVP (Chp 2.3)

import math
import numpy as np
import matplotlib.pyplot as plt

# Naive Eulers Method:
#
# f - ode function
# t - domain (gridded) for the function
# y0 - initial y value
# delta - length of subdivisions of interval

def eulersMethod(f,t,y0,delta,verbose=False):
    # Initialize numpy array to hold the y values for our solution function
    ret = np.arange(t[0],t[-1]+delta,delta)
    
    # error checking
    if verbose:
        print(ret)
    # set our initial value
    ret[0]=y0

    for i in range(1,len(t),1):
        # Eulers Method
        ret[i]=ret[i-1]+delta*f(t[i-1],ret[i-1])
    
    #reuturn the values obtained through euler's method
    return ret

# Our class ODE example function
def ode(t,y):
    return y*(1-2*t)

# Actual reference functional solution to ODE:
def exactSol(t):
    return math.exp(t-t**2.0)

x0=0.0
y0=exactSol(x0)

print('x0 = {}, y0 = {}'.format(x0,y0))

# Choose an interval which includes our desired value y(3):
a = x0
b = 3.0

# Determine the grid intervals:
hinv = 16   #divisor for grid
delta = (b-a)/hinv

# Print grid values
print('delta = {}'.format(delta))

# Set up plotting:
# Create domain for plot (Notice  we should add +1  to hinv - why?):
t = np.linspace(a,b,hinv+1,endpoint=True)

oSol = eulersMethod(ode, t, y0, delta)
exact = np.array([exactSol(x) for x in t])

plt.figure(figsize=(8,6))
plt.plot(t,exact,label='exact')
plt.plot(t,oSol,label='oSol')
plt.legend()
plt.show()


