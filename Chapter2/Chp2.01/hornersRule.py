"""
This program is an implentation of Horner's rule (Nested Multiplication) from Chapter 2.1
(This is not my original code and taken as class notes)

Similiar to the psuedocode presented in the chapter just implemented in Python3

Taken from Class example where
p(x)= x^4 + 5x^3 + 2x^2 + 13x + 1
"""
def HornersRuleNaive(incvec, val, verbose=True):
    
    #initialization of length of vector parameter
    lenvec=len(incvec)

    #print if verbose
    if verbose:
        print('Size of incoming vector: {}'.format(lenvec))
    
    p = incvec[lenvec-1]  #(p in Horner's rule algorithm)

    # Iterate (backwards) from the list of coefficients
    for i in range(lenvec-2, -1,-1):
        
        #complete horner's rule
        p = p*val + incvec[i]

        if verbose:
            print('p = {}, Index i = {}'.format(p,i))
    
    # Return value
    return p

# Create example function call and report result
polyvec=[1,13,2,5,1]
val=10.0

# Call function and record the result
result=HornersRuleNaive(polyvec, val)

# Report Results
print('p(x) evaluated  at {} is: {}'.format(val,result))