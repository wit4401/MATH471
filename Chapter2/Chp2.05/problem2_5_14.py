"""
Will Townsend (Problem 2.5.14)

The length of the curve y=g(x) for x between a and b is given by the following integral

                        L(g)=\int_a^b\sqrt{1+[g'(x)]}dx

Use the trapezoidal rule with h = pi/4 and pi/16 to find the length of "one arc" of the
sine curve.
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp2 as ex

# Note: derivative of sine is cosine square it plug it into the integral
# Also note we cannot directly integrate or use any techniques on this function
# Thus, we need to approximate it using some approximation method
def funct(x):
    return math.sqrt(1+math.cos(x)**2)

a=0 # start of arc
b=math.pi # end of the arc
print('Trapezoidal Estimation (h=pi/4): {}'.format(ex.trapezoidal_method(funct, a, b, 4)))
print('Trapezoidal Estimation (h=pi/16): {}'.format(ex.trapezoidal_method(funct, a, b, 16)))