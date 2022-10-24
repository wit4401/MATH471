import trapHW as ex
import math

functs=[ex.funct14,ex.funct15,ex.funct16,ex.funct17]
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