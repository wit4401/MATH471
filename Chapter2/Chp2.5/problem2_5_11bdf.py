import trapHW as ex
import math

vals=[2,4,8,16,32,64,128]
functs=[ex.funct9,ex.funct11,ex.funct13]
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