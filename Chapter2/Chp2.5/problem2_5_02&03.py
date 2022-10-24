import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def funct(x):
    return math.sin(x)

def problem2():
    a=0
    b=math.pi/2
    actualValue=1
    print('Trapezoidal Estimation (h=pi/4): {}'.format(ex.trapezoidal_method(funct, a, b, 2)))
    print('Actual Value: {}\n'.format(actualValue)) 

def problem3():
    a=0
    b=math.pi/2
    actualValue=1
    print('Trapezoidal Estimation (h=pi/6): {}'.format(ex.trapezoidal_method(funct, a, b, 3)))
    print('Actual Value: {}\n'.format(actualValue))

    tolerances=[math.pow(10,-3.0),math.pow(10,-6.0)]
    for val in tolerances:
        i=2
        errorTolerance=val
        err=abs(actualValue-ex.trapezoidal_method(funct, a, b, 1))
        while err >= errorTolerance:
            res=ex.trapezoidal_method(funct, a, b, i)
            err=abs(actualValue-res)
            print('Actual Value: {}, Trapezoidal Estimation (h=pi/{}): {}, err: {:10.10f}'.format(actualValue,i,res,err))
            
            if err <= errorTolerance:
                print('\nn = {} for error tolerance {}\n'.format(i,errorTolerance))
            else:
                i+=1 
if __name__ == "__main__":
    problem2()
    problem3()
