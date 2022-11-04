# An example file for the purposes of testing iteration_bisection and err_bisection in coursefuncts library.
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

def f(x):
    return math.exp(x)-x**2

if __name__ == "__main__":
    actual=ex.iteration_bisection(f, -1, 0, 45)
    results=ex.err_bisection(f, -1, 0, math.pow(10,-5),True)
    print('\nRoot of f(x) within {} is {} in {} iterations.'.format(math.pow(10,-6),results[1],results[0]))