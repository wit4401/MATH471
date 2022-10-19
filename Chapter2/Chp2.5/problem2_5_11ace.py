import trapHW as ex
import math

vals=[2,4,8,16,32,64,128]
functs=[ex.funct8,ex.funct10,ex.funct12]
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