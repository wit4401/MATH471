"""
Problem 1.3.10

"Using the computer and language of your choice write a program to estimate the machine epsilon (of your machine)"
Machine epsilon is a number such that any number epsilon where:
epsilon + 1.0 = 1.0

Note: this program is not an original. Copied as notes from Dr. Randall Cone
"""
import math

# Strategy?
# Let's iterate through 2-adic fractions as they get smaller,
# and use a while loop to do so.

# Variable Setup
e = 1.0 # Epsilon  starting with it equaling a non-trivial 2-adic fractional number e = 1/(2^n)
n = 1.0 # track where in the iteration we are

# we need to keep the loop going until e + 1 = 1
while(not (1==1+e)):
    # in order to not loop forever these numbers need to get smaller
    e = (2**(-n))
    # print the result of the iteration
    print('n = {},\te = {}'.format(n,e))
    # and then increase our counter
    n=n+1

# finally print out the resulting answer
print('\nSmallest value epsilon: {:24.24f}'.format(e))

# proof that this is our true epsilon value
print('e + 1 = {:24.24f}'.format(e+1))

