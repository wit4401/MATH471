# Answers for our textbook practice problems 
# in 2.3 using Python3
#
# Will Townsend
import math
import numpy as np
import matplotlib.pyplot as plt

def eulersMethod(f,t,y0,delta):
    retval = np.arange(t[0],t[-1]+delta,delta)
    retval[0] = y0

    for i in range(1,len(t),1):
        retval[i]=retval[i-1]+delta*f(t[i-1],retval[i-1])

    return retval

# Problems 1 - 4
def ode(t,y):
    return math.sin(y+t)

a=0
b=1
y0=1
delta = [4, 5, 8]
res = []
for i in delta:
    t = np.linspace(a,b,i+1,endpoint=True)
    res.append(eulersMethod(ode, t, y0, 1/i))

print('Problems 1-3')
print('y4 is approx {}'.format(res[0][-1]))
print('y5 is approx {}'.format(res[1][-1]))
print('y8 is approx {}'.format(res[2][-1]))

# Problems 4 - 6
def ode2(t,y):
    return math.exp(t-y)

y0=-1
res2 = []
for i in delta:
    t = np.linspace(a,b,i+1,endpoint=True)
    res2.append(eulersMethod(ode2, t, y0, 1/i))

print('\nProblems 4-6')
print('y4 is approx {}'.format(res2[0][-1]))
print('y5 is approx {}'.format(res2[1][-1]))
print('y8 is approx {}'.format(res2[2][-1]))

# Problem 7
def ode3(t,y):
    return t-y
def exactSol(t):
    return 3*math.exp(-t)+t-1

y0=2
t = np.linspace(a,b,17,endpoint=True)
res3=eulersMethod(ode3, t, y0, 1/16)
exact = np.array([exactSol(x) for x in t])

plt.figure(figsize=(7,8))
plt.plot(exact,label='7) exact')
plt.plot(res3,label='7) approx')
plt.legend()

# Problem 8
def exactSol2(t):
    return math.log(math.exp(t)-1+math.exp(-1))

plt.figure(figsize=(7,8))
res2 = eulersMethod(ode2, t, -1, 1/16)
exact2 = np.array([exactSol2(x) for x in t])
plt.plot(exact2,label='8) exact')
plt.plot(res2,label='8) approx')
plt.legend()

# Problem 9
def ode4(t,y):
    return math.sin(t)-y
def exactSol3(t):
    return (-1*math.cos(t)+math.sin(t)-math.exp(-1*t))/2

plt.figure(figsize=(7,8))
res4 = eulersMethod(ode4, t, -1, 1/16)
exact3 = np.array([exactSol3(x) for x in t])
plt.plot(exact3,label='9) exact')
plt.plot(res4,label='9) approx')
plt.legend()
plt.show()
