"""
Will Townsend

Problem 1.3.7

"I accessed help from the numpy online manual"
numpy.org

a) Using the computer of your choice, find three values 
   a, b, and c s.t.:

            (a + b) + c != a + (b + c)

b) Now do this in single precision using MATLAB (or whatever 
   computing environment is available).
"""
import numpy
import math

# How are we gonna accomplish this?
# Similar to the machine epsilon problem/challenge (Problem 1.3.10) we can "break" the system by putting a number n (n != 0)
# into any value a, b, or c (here I use 1.0) and the other two values as 2-adic fractions decreasing at a unique rate

# Part a
a = b = c = 1.0  # set all of our initial values as 
i = 1 # setting up our iterrator to help decrease our values (in this case a, c)

# We must loop through the values until (a + b) + c != a + (b + c)
while (((a+b)+c==a+(b+c))):
   # prints out the result of the ith iteration of our loop 
   print('i = {:d}, ({:10.10e} + {:10.10e}) + {:10.10e} = {:10.10e}, {:10.10e} + ({:10.10e} + {:10.10e}) = {:10.10e}'\
      .format(i,a,b,c,(a+b)+c,a,b,c,a+(b+c)))
   
   a = 2**(-i) # decrease our value of 2-adic fraction
   
   # b will not be changed here since we need the value to stay constant

   c = 2.0 * 2**(-i) # also decrease however this one decreases half as fast
   
   i=i+1 # increase our iterator

# once the values that will make the statement true are found our loop stops

# printing our results
print('\nAfter {:d} iterations, when a = {:20.20f}, b = {:20.20f}, and c = {:20.20f}\n\n(a + b) + c != a + (b + c) or {:26.26f} != {:20.26f}\n'\
         .format(i,a,b,c,(a+b)+c,a+(b+c)))

# Interesting Observations:
# 1) It doesn't matter which value holds our 1.0
# 2) The resulting values from the calculation are approximantely equivalent but not quite
# 3) The higher we make our constant value the less iterations it takes to find a, and c

# Part b

# The loop here is essitially the same idea expect we are going to cast our values as 
# single precision floating points (use numpy)
#
# The single precision (32-bit) should result in taking less iterations for the system to "break"

a = b = c = numpy.single(1.0)
i= 1

# same loop
while (((a+b)+c==a+(b+c))):
   print('i = {:d}, ({:10.10e} + {:10.10e}) + {:10.10e} = {:10.10e}, {:10.10e} + ({:10.10e} + {:10.10e}) = {:10.10e}'\
      .format(i,a,b,c,(a+b)+c,a,b,c,a+(b+c)))
   
   # we have to cast the changed values as well or the system will treat them as doulble precision (64-bit)
   a = numpy.single(2**(-i))
   c = numpy.single(2.0 * 2**(-i))
   i=i+1

print('\nAfter {:d} iterations, when a = {:20.20f}, b = {:20.20f}, and c = {:20.20f}\n\n(a + b) + c != a + (b + c) or {:26.26f} != {:26.26f}\n'\
      .format(i,a,b,c,(a+b)+c,a+(b+c)))

# Final Obsevations:
# 1) Just as perdicted it takes less iterations for the system to find values a, b, and c that hold true when
#    in single precision vs double precision
# 2) And with that the two resulting values are also less accurate than double precision
