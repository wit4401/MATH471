"""
Problem 3.1.13

The bisection method with always cut the interval of uncertainty in half, but 
regula-falsi might cut the interval by less, or might cut it by more. Do both
the bisection method and regula-falsi on the function f(x)=e^(-4x)-1/10, using
the initial interval [0,5]. Which on gets to the root the fastest?
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

f=lambda x: math.exp(-4.0*x)-0.1
a=0
b=5

print("Bisection Method:")
sol=ex.iteration_bisection(f, a, b, 10000000)
if not sol:
    print('Root Not Found')
else:
    print('Root: {:10.10f}'.format(sol))

print("Regula-Falsi Method:")
sol=ex.iteration_regula_falsi(f, a, b, 10000000)
if not sol:
    print('Root Not Found')
else:
    print('Root: {:10.10f}'.format(sol))