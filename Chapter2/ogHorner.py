"""
This is a program for Horner's Rule Algorithm which is based off the pseudocode in Chapter 2.1
of our textbook An Introduction to Numerical Methods and Analysis 3rd Edition (James F. Epperson).

All code documented is 100% developed by me and used no resources besides the texbook.
"""

# implementation of algorithm 2.3 from the textbook using Python
def hornersRule(polyvec, val):

    # this empty list will eventually return the result of the algorithms
    result = []

    # variable holds the polyvec length
    veclen = len(polyvec)

    p = polyvec[veclen-1]
    
    # Implement horner's rule in our for loop
    for i in range(veclen-2,-1,-1):
        p = val*p + polyvec[i]

    result.append(p)

    dp = (veclen-1)*polyvec[veclen-1]

    # Implement Horner's Rule on the derivative of the polynomial
    for i in range(veclen-2,0,-1):
        dp = dp*val + polyvec[i]*i

    result.append(dp)
    return result

res = hornersRule([1, 0, 1, 0, 1/2, 0, 1/6], 0.0)

print('p(1.0) = {}'.format(res[0]))
print('p\'(1.0) = {}'.format(res[1]))