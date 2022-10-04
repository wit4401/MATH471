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
# a - start of interval of interest
# b - end of interval of interest
# hinv - number of subdivisions

def eulersMethod(f,t,y0,a,b,hinv):
    # Initialize numpy array
    ret = np.arange(a,b+1/hinv,1/hinv)
    print(ret)

# Our class ODE example function
def ode(t,y):
    return y*(1-2*t)

# Actual reference functional solution to ODE:
def exactSol(t):
    return math.exp(t-t**2.0)

x0=0.0
y0=exactSol(x0)

print('x0 = {}, y0 = {}'.format(x0,y0))

# Choose an interval which includes our desited value y(3):
a = x0
b = 3.0

# Determine the grid intervals:
hinv = 8   #divisor for grid
delta = (b-a)/hinv

# Print grid values
print('delta = {}'.format(delta))

# Set up plotting:
# Create domain for plot:
t = np.linspace(a,b,hinv,endpoint=True)
exact = np.array([exactSol(x) for x in t])
oSol = eulersMethod(ode, t, y0, a, b, hinv)

plt.plot(t,exact,label='exact')
plt.legend()
plt.show()

