import trapHW as ex
import math

a=0
b=1
actualValue=2*math.log(2,math.exp(1.0))-1
print('Trapezoidal Estimation (h=1/8): {}'.format(ex.trapezoidal_method(ex.funct5, a, b, 8)))
print('Actual Value: {}\n'.format(actualValue))

tolerances=[math.pow(10,-3.0),math.pow(10,-6.0)]
for val in tolerances:
    i=2
    errorTolerance=val
    err=abs(actualValue-ex.trapezoidal_method(ex.funct5, a, b, 1))
    while err >= errorTolerance:
        res=ex.trapezoidal_method(ex.funct5, a, b, i)
        err=abs(actualValue-res)
        print('Actual Value: {}, Trapezoidal Estimation (h=1/{}): {}, err: {:10.10f}'.format(actualValue,i,res,err))
            
        if err <= errorTolerance:
            print('\nn = {} for error tolerance {}\n'.format(i,errorTolerance))
        else:
            i+=1