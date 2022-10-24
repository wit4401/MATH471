import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def funct1(x):
    return math.exp(-1.0*x**2)

def funct2(x):
    return math.log(x,math.exp(1.0))

def funct3(x):
    return 1/(1+x**2)

def funct4(x):
    return math.cos(math.pi*x/2)

functs=[funct1,funct2,funct3,funct4]
bounds=[[0,1],[1,3],[-5,5],[0,1]]
actualVal=[0.7468241328,1.295836866,2.746801534,0.6366197724]
error_tolerance=math.pow(10.0,-8.0)
parts = ['a','b','c','d']
i=0
for funct in functs:
    print('Part {}:'.format(parts[i]))
    a=bounds[i][0]
    b=bounds[i][1]
    n = 1
    err=abs(ex.trapezoidal_method(funct, a, b, n)-actualVal[i])
    while err>=error_tolerance:
        n+=1
        res=ex.trapezoidal_method(funct, a, b, n)
        err=abs(res-actualVal[i])
    print('It takes n = {} subdivisions to have an accuracy of {:8.8f}'.format(n,error_tolerance))
    print('')
    i+=1