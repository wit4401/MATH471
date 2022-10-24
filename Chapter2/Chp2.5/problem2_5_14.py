import math
import trapHW as ex

a=0
b=math.pi
print('Trapezoidal Estimation (h=pi/4): {}'.format(ex.trapezoidal_method(ex.funct18, a, b, 4)))
print('Trapezoidal Estimation (h=pi/16): {}\n'.format(ex.trapezoidal_method(ex.funct18, a, b, 16)))