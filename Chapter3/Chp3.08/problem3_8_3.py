import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

functions = [lambda x: x**3-2,
             lambda x: math.exp(x)-2,
             lambda x: x-math.exp(-1.0*x),
             lambda x: x**6-x-1,
             lambda x: x**3-2*x-5,
             lambda x: 1-2*x*math.exp(-1.0*x/2.0),
             lambda x: 5-x**(-1.0),
             lambda x:x**2-math.sin(x)]
x0s = [0,0,0,0,0,0,0.1,0]
x1s = [2,1,1,2,3,2,0.25,math.pi]
func_names = ['x^3-2','e^x-2','x-e^(-x)','x^6-x-1','x^3-2x-5','1-2xe^(-x/2)','5-e^(-x)','x^2-sinx']
parts = ['a','b','c','d','e','f','g','h']
err=math.pow(10,-6.0)

for i in range(0,len(functions)):
    print('{}) f(x) = {} x0 = {}\tx1 = {}:'.format(parts[i],func_names[i],x0s[i],x1s[i]))
    result = ex.secant_method_err(x0s[i], x1s[i], functions[i], err)
    print('alpaha: {} (accurate within {:f})\n'.format(result,err))