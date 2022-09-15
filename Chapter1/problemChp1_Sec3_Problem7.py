"""
Problem 1.3.7

a) Using the computer of your choice, find three values 
   a, b, and c s.t.:

            (a + b) + c != a + (b + c)

b) Now do this in single precision using MATLAB (or whatever 
   computing environment is available).
"""
import numpy
import math

# Part a
a = 1.0
b = 2.0
c = 3.0
i = 1.0

while (not((a+b)+c==a+(b+c))):
   if((a+b)+c==a+(b+c)):
      print('i = {},\t({} + {}) + {} = {},\t{} + ({} + {}) = {}'\
         .format(i,a,b,c,(a+b)+c,a,b,c,a+(b+c)))
      a = 2**(-i)
      b = 1 + 2**(-i)
      c = -1.0 * 2**(-i)
      i=i+1

print('After {} iterations, when a = {}, b = {}, and c = {}\n(a + b) + c != a + (b + c)'.format(i,a,b,c))

# Part b

while (not((a+b)+c==a+(b+c))):
   pass

