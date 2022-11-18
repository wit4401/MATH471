# Example file to test the another_newtons_method created using the knowledge from section 3.3
# compares the two functions by applying f(x)=e^x-x^2 x0=0.1
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

f = lambda x: math.exp(x)-x**2
fprime = lambda x: math.exp(x)-2*x
x0 = 0.1
err=math.pow(10,-6.0)

print('newtons_method():')
ex.newtons_method(f, fprime, x0, err, True)
print('another_newtons_method():')
ex.another_newtons_method(f, fprime, x0, err, True)