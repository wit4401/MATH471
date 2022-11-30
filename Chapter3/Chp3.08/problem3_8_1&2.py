import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

f=lambda x: x**3-2
print('Problem 3.8.1')
ex.secant_method_iter(0, 1, f, 3, True)

print('\nProblem 3.8.2')
ex.secant_method_iter(1, 0, f, 3, True)