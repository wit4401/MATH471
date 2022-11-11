import math

def trapezoidal_method(f,lowerLim,upperLim,n):
    h = (upperLim-lowerLim)/n
    sum = 0.5*(f(upperLim)+f(lowerLim))
    for i in range(1,n):
        x = lowerLim + i*h
        sum+=f(x)
    return sum*h

f1=lambda x:(math.exp(x)-math.exp(-1.0*x))/2
f2=lambda x:math.sqrt(1-x**4)

ns=[2,4,8,16,32,64,128]

print('f(x)=(e^x-e^-x)/2:')
for n in ns:
    print('Integral Approximation of f(x) over [{},{}] with h={}: {}'.format(0,2,2/n,trapezoidal_method(f1, 0, 2, n)))

print('\nf(x)=sqrt(1-x^4):')
for n in ns:
    print('Integral Approximation of f(x) over [{},{}] with h={}: {}'.format(-1,1,2/n,trapezoidal_method(f2, -1, 1, n)))