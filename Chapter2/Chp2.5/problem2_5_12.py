import trapHW as ex
import math

bounds=[[0,2],[0,1],[-1,1],[1,3],[0,1],[0,math.pi]]
error_tolerances=[math.pow(10.0,-3.0),math.pow(10.0,-6.0)]
parts = ['a','b','c','d','e','f']
i=0
for dbl in range(0,6,1):
    print('Part {}:'.format(parts[i]))
    a=bounds[i][0]
    b=bounds[i][1]
    for errTol in error_tolerances:
        n = 1
        if errTol==0.001:
            print('Theoretical subdivisions for error within {:3.3f}: n = {}'.format(errTol,ex.ErrorTrap(a, b, errTol,1.0)))
        else:
            print('Theoretical subdivisions for error within {:6.6f}: n = {}'.format(errTol,ex.ErrorTrap(a, b, errTol,1.0)))
    print('')
    i+=1