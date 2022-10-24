"""
Created on Tue Aug 30 11:39:49 2022

Note: this program is not an original
Copied as notes from Dr. Randall Cone
 
Will Townsend
"""

# import necessary libraries
import math

# We will create a polynomial approximating function for e^x centered at
# x0=0 where the incoming parameters are
# val = value we want to estimate for e^val
# n = degree of the Taylor polynomial approximation:
    
def approxE(val,n):
    # print('Hi numnuts')
    
    # establish an initial return value, which in this case is f^0(val)= 1:
    retval = 1.0
    
    # Build Taylor Polynomial approx for e^x centered at 0 with given
    # degree (n) and given value (val)
    for i in list(range(1,n+1)):
        
        # build the terms of polynomial and add sum, all terms of degree
        # 1 to n
        retval = retval + 1/(math.factorial(i)) * math.pow(val,i)
        
    # The only return from this function should be from the last line of
    # the function, and nowhere else
    return retval

# call the function and store the result:
result = approxE(1/2, 100)

#print result
print('Our result: {}'.format(result))

# print the actual value of e^{1/2}
print('"Actual" Result: {}'.format(math.e**(0.5)))