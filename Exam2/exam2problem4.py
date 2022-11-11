import math
import numpy as np

def __solve_tridiagonal(A,b):
    numrows,numcols = A.shape
    
    # obtains the diagonals from the matrix
    diagonal=np.diagonal(A,0,0,1).copy()
    upper=np.diagonal(A,1,0,1).copy()
    lower=np.diagonal(A,-1,0,1).copy()
    coeff=b.copy()

    # Forward phase
    for i in range(1,numrows):
        diagonal[i]-=upper[i-1]*lower[i-1]/diagonal[i-1]
        coeff[i]-=coeff[i-1]*lower[i-1]/diagonal[i-1]
    # Backsolve phase
    coeff[-1]/=diagonal[-1]
    for i in range(numrows-2,-1,-1):
        coeff[i]-=upper[i]*coeff[i+1]
        coeff[i]/=diagonal[i]
    return coeff

def isTridiagonal(A):
    retval=True
    numcols,numrows=A.shape
    for i in range(0,numrows):
        for j in range(0,numcols):
            if i!=j and i-1!=j and i+1!=j:
                if A[i,j] != 0:
                    retval=False
                    break
    return retval

def isDominant(A):
    retval=True
    numrows,numcols=A.shape
    for i in range(0,numrows):
        total=0
        for j in range(0,numcols):
            if i!=j:
                total+=abs(A[i,j])
        # Our check condition for each row to check for dominance
        if total > abs(A[i,i]):
            retval=False
            break
    return retval

def tridiagonal(A,b):
    retval=False
    if isTridiagonal(A):
        if isDominant(A):
            retval = __solve_tridiagonal(A, b)
        else:
            print('Given matrix is not Diagonally Dominant')
            print('Try to compute anyway (y/n)? ',end='')
            inp = str(input())
            if inp == 'y' or inp == 'Y':
                retval = __solve_tridiagonal(A, b)
    else:
        print("Given matrix is not Tridiagonal!")
    return retval

vals=[]

for i in range(1,11):
    temp=[]
    for j in range(1,11):
        if i-j==1:
            temp.append(1)
        elif j-i==1:
            temp.append(-1)
        elif i == j:
            temp.append(j+1)
        else:
            temp.append(0)
    vals.append(temp)

A = np.matrix([vals[0],vals[1],vals[2],vals[3],vals[4],vals[5],vals[6],vals[7],vals[8],vals[9]],dtype=np.float64)
coeff = np.array([2,2,2,2,2,2,2,2,2,2],dtype=np.float64)

print('Given Matrix:\n{}'.format(A))
print('Coefficients: {}\n'.format(coeff))

res = tridiagonal(A,coeff)
print('Tridiagonal Solution:\n{}\n'.format(res))

r=[]
for i in range(0,len(coeff)):
    r.append(coeff[i]-res[i])

print('r:\n{}\n'.format(r))

maximum=0
for val in r:
    if maximum<abs(val):
        maximum=val
print('Maximum r_i: {}'.format(maximum))