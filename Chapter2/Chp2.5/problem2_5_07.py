import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def funct(x):
    return 1/(1+x**3)

a=0
b=1
actualValue=(1/3)*math.log(2,math.exp(1.0))+(1/9)*math.sqrt(3)*math.pi
print('Trapezoidal Estimation (h=1/8): {}'.format(ex.trapezoidal_method(funct, a, b, 8)))
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