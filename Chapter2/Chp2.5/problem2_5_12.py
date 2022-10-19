import trapHW as ex
import math

functs=[ex.funct8,ex.funct9,ex.funct10,ex.funct11,ex.funct12,ex.funct13]
bounds=[[0,2],[0,1],[-1,1],[1,3],[0,1],[0,math.pi]]
actualVal=[0.646647168,0.2*math.atan(5),math.pi/2,1.295836867,2/7,0.2251261368]
error_tolerances=[math.pow(10.0,-3.0),math.pow(10.0,-6.0)]
parts = ['a','b','c','d','e','f']
i=0
for funct in functs:
    print('Part {}:'.format(parts[i]))
    a=bounds[i][0]
    b=bounds[i][1]
    
    for errTol in error_tolerances:
        n = 1
        err=abs(ex.trapezoidal_method(funct, a, b, n)-actualVal[i])
        while err>errTol:
            n+=1
            err=abs(ex.trapezoidal_method(funct, a, b, n)-actualVal[i])
        print('Theoretical subdivisions: n = {}'.format(ex.ErrorTrap(a, b, errTol,1.0)))
        print('It actually takes {} subdivisions to have an accuracy of {}'.format(n,errTol))
    print('')
    i+=1