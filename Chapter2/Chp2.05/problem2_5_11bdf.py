import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

def funct1(x):
    return 1/(1+25*x**2)

def funct2(x):
    return math.log(x,math.exp(1.0))

def funct3(x):
    return math.exp(-1.0*x)*math.sin(4*x)

vals=[2,4,8,16,32,64,128]
functs=[funct1,funct2,funct3]
bounds=[[0,1],[1,3],[0,math.pi]]
actualVal=[0.2*math.atan(5),1.295836867,0.2251261368]
part=['b','d','f']
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