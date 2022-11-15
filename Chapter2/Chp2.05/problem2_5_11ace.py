import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def funct1(x):
    return x**2*math.exp(-1.0*x)

def funct2(x):
    return math.sqrt(1-x**2)

def funct3(x):
    return x**(5/2)

vals=[2,4,8,16,32,64,128]
functs=[funct1,funct2,funct3]
bounds=[[0,2],[-1,1],[0,1]]
actualVal=[0.646647168,math.pi/2,2/7]
part=['a','c','e']
i=0
for funct in functs:
    print('Part {}'.format(part[i]))
    for n in vals:
        a=bounds[i][0]
        b=bounds[i][1]
        actual_value=actualVal[i]
        res=ex.trapezoidal_method(funct, a, b, n)
        print('Trapezoidal Result n = {}: {}'.format(n,res))
        print('Actual Value: {}'.format(actual_value))
        print('Error: {}\n'.format(abs(actual_value-res)))   
    i+=1