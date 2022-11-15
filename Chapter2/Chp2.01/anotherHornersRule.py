"""
This is a program for Horner's Rule Algorithm which is based off the pseudocode in Chapter 2.1
of our textbook An Introduction to Numerical Methods and Analysis 3rd Edition (James F. Epperson).

All code documented is 100% developed by me and used no resources besides the texbook.
"""

# implementation of algorithm 2.3 from the textbook using Python
def hornersRule(polyvec, centers, val):

    # variable holds the polyvec length
    veclen = len(polyvec)

    p = polyvec[veclen-1]
    
    # Implement horner's rule in our for loop
    for i in range(veclen-2,-1,-1):
        p = (val-centers[i])*p + polyvec[i]
        
    return p

xVal = 1.0
print('p({}) = {}'.format(hornersRule([],[],xVal)))