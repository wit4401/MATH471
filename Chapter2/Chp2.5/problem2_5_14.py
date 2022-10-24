import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def funct(x):
    return math.sqrt(1+math.cos(x)**2)

a=0
b=math.pi
print('Trapezoidal Estimation (h=pi/4): {}'.format(ex.trapezoidal_method(funct, a, b, 4)))
print('Trapezoidal Estimation (h=pi/16): {}\n'.format(ex.trapezoidal_method(funct, a, b, 16)))