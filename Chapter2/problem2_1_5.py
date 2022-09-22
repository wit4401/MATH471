"""
Will Townsend

Problem 2.1.5

Write a computer code/program that takes a polynomial, defined by its coefficients,
and evaluates that polynomial and takes its first derivative using Horner's Rule.
Test this code by applying it to each of the polynomials in Problem 2.

Polynomials:
a) p(x) = 1 + x^2 + (1/2)x^4 + (1/6)x^6
b) p(x) = 1 - (1/2)x^2 + (1/24)x^4
"""
import math

# Horner's Rule on polynomial
#
# The implementation will be a little different than the one we did during class
# since we can take advatage of the powers of x are all even

def HornersRuleEven(polyvec,val):
    # define our first coefficient
    p = polyvec[len(polyvec)-1]

    # Applying Horner's rule (assuming all even powers)
    for i in range(len(polyvec)-2,-1,-1):

        # notice val is being taken to the second power
        p = p * val**2 + polyvec[i]

    return p

# Horner's Rule w/ Derivative of the polynomial
#
# Same thing here our implementation is a bit different for the derivative of our
# polynomials. In our derivative of the polynomials we can take advantage that all
# the powers are odd the same as we could with the original polynomial.
def HornersDerivative(polyvec,val):
    
    # define the first coefficient
    p = polyvec[len(polyvec)-1] * (len(polyvec)-1)*2
    
    # similar to our HornersRuleEven() however slightly modified to 
    # calculate the derivative instead (assuming original polynomial
    # had all even powers) (based on algorithm 2.2 in the text)
    for i in range(len(polyvec)-2,0,-1):
        p = p * val**2 + polyvec[i] * i*2

    # however we are not done since we need to account for the fact our
    # polynomials have all odd powers after the derivative was taken 
    # 
    # All the powers taken of the value are even which will result in an 
    # inaccurate result for our derivative (this was not needed in the
    # original algorithm)
    # 
    # this is fixed by divide our result from the above loop by our val
    p = p / val

    return p

# Finally let's test the two functions by applying the polynomials given in Problem 2
poly1 = [1, 1, 1/2, 1/6]
poly2 = [1, -1/2, 1/24]