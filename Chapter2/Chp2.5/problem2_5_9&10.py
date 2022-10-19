import math
import trapHW as ex

# Problem 2.5.9
I8 = ex.trapezoidal_method(ex.funct7, 1, 2, 8)
I4 = ex.trapezoidal_method(ex.funct7, 1, 2, 4)
res=(4*I8-I4)/3
actualValue = 0.1352572580
print('\n(4I8-I4)/3 = {}'.format(res))
print('Actual Value: {}'.format(actualValue))
print('Error = {}\n'.format(abs(actualValue-res)))

# Problem 2.5.10
I8 = ex.trapezoidal_method(ex.funct7, 0, 1, 8)
I4 = ex.trapezoidal_method(ex.funct7, 0, 1, 4)
res=(4*I8-I4)/3
actualValue = (1/3)*math.log(2,math.exp(1.0))+(1/9)*math.sqrt(3)*math.pi
print('(4I8-I4)/3 = {}'.format(res))
print('Actual Value: {}'.format(actualValue))
print('Error = {}'.format(abs(actualValue-res)))