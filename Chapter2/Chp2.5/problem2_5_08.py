import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def funct(x):
    return math.exp(-1.0*(x**2))

a=1
b=2
actualValue=0.1352572580
I8=ex.trapezoidal_method(funct, a, b, 8)
print('Trapezoidal Estimation (h=1/8): {}'.format(I8))
print('Actual Value: {}\n'.format(actualValue))

tolerances=[math.pow(10,-3.0),math.pow(10,-6.0)]
for val in tolerances:
    i=2
    errorTolerance=val
    err=abs(actualValue-ex.trapezoidal_method(funct, a, b, 1))
    while err >= errorTolerance:
        res=ex.trapezoidal_method(funct, a, b, i)
        err=abs(actualValue-res)
        print('Actual Value: {}, Trapezoidal Estimation (h=1/{}): {}, err: {:10.10f}'.format(actualValue,i,res,err))
            
        if err <= errorTolerance:
            print('\nn = {} for error tolerance {}\n'.format(i,errorTolerance))
        else:
            i+=1