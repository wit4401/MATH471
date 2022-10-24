import math
import trapHW as ex

a=1
b=math.exp(1.0)
print('Trapezoidal Estimation (h=1/4): {}'.format(ex.trapezoidal_method(ex.funct19, a, b, 4)))
print('Trapezoidal Estimation (h=1/16): {}\n'.format(ex.trapezoidal_method(ex.funct19, a, b, 16)))