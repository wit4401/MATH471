import trapHW as ex
import math

a=0
b=1
actualValue=17/64
print('Trapezoidal Estimation (h=1/4): {}'.format(ex.trapezoidal_method(ex.funct1, a, b, 4)))
print('Actual Value: {}\n'.format(actualValue))

tolerances=[math.pow(10,-3.0),math.pow(10,-6.0)]
for val in tolerances:
    i=2
    errorTolerance=val
    err=abs(actualValue-ex.trapezoidal_method(ex.funct1, a, b, 1))
    while err >= errorTolerance:
        res=ex.trapezoidal_method(ex.funct1, a, b, i)
        err=abs(actualValue-res)
        print('Actual Value: {}, Trapezoidal Estimation (h=1/{}): {}, err: {:6.6f}'.format(actualValue,i,res,err))
            
        if err <= errorTolerance:
            print('\nn = {} for error tolerance {}\n'.format(i,errorTolerance))
        else:
            i+=1