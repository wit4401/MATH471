import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def funct(x):
    return math.exp(-1.0*(x**2))

def funct2(x):
    return 1/(1+x**3)

# Problem 2.5.9
I8 = ex.trapezoidal_method(funct, 1, 2, 8)
I4 = ex.trapezoidal_method(funct, 1, 2, 4)
res=(4*I8-I4)/3
actualValue = 0.1352572580
print('(4I8-I4)/3 = {}'.format(res))
print('Actual Value: {}'.format(actualValue))
print('Error = {:10.10f}\n'.format(abs(actualValue-res)))

# Problem 2.5.10
I8 = ex.trapezoidal_method(funct2, 0, 1, 8)
I4 = ex.trapezoidal_method(funct2, 0, 1, 4)
res=(4*I8-I4)/3
actualValue = (1/3)*math.log(2,math.exp(1.0))+(1/9)*math.sqrt(3)*math.pi
print('(4I8-I4)/3 = {}'.format(res))
print('Actual Value: {}'.format(actualValue))
print('Error = {:10.10f}'.format(abs(actualValue-res)))