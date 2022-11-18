"""
Problem 3.5.8

Consider now the function f(x) = 7x-cos(2pix). Show that a root exists on
the interval [0,1], and then use newton's error estimation to determine how
close x0 has to be to the root to guarantee convergence.

Problem 3.5.9

Investigate your results in the previous problem by applying Newton's method
to f(x)=7x-cos(2pix), using several choices of x0 within the interval [0,1]
Comment on your results in light of the theory of the method.

"""
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

f = lambda x: 7*x-math.cos(2*math.pi*x)
fprime = lambda x:7+2*math.pi*math.sin(2*math.pi*x)

x=np.linspace(-3,3,400,endpoint=True)
y=np.array([f(val) for val in x])
plt.figure(figsize=(7,8))
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,label='f(x) = 7x - cos(2pix)')

x=np.linspace(-3,3,400,endpoint=True)
y=np.array([0 for i in x])
plt.plot(x,y,label='y=0')
plt.legend()

ex.newtons_method(f, fprime, 0.1, math.pow(10,-8.0),True)

x0s = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
for x0 in x0s:
    print("x0={}:".format(x0))
    ex.newtons_method_iter(f, fprime, x0, 50, True)
    print('')

plt.show()