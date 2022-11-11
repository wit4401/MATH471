import math

def betterApprox(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

def another_approx(f,x,h):
    return (4*betterApprox(f,x,h)-betterApprox(f,x,2*h))/3

f1 = lambda x: -math.log(math.cos(x),math.exp(1))
f2 = lambda x: x**x**x

hinv=[4,8,16,32,64]

print('f(x)=-ln(cos x):')
for h in hinv:
    print('Derivative Approximation of f(0.5) h={}: {}'.format(1/h,another_approx(f1, 0.5, 1/h)))

print('\nf(x)=x^x^x:')
for h in hinv:
    print('Derivative Approximation of f(0.5) h={}: {}'.format(1/h,another_approx(f2, 0.5, 1/h)))

