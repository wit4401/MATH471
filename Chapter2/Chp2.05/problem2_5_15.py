import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def funct(x):
    return math.sqrt(1+(1/x)**2)

a=1
b=math.exp(1.0)
print('Trapezoidal Estimation (h=1/4): {}'.format(ex.trapezoidal_method(funct, a, b, 4)))
print('Trapezoidal Estimation (h=1/16): {}\n'.format(ex.trapezoidal_method(funct, a, b, 16)))