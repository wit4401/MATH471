# This program calculates the absolute and relative error of an exact value
# and an approximate value to said exact value

import math

vals = [ math.pi, math.exp(1.0), 1.0/6.0, 1.0/6.0 ]
approxs = [ 22/7, 2.71828, 0.1667, 0.1666 ]

for i in list(range(4)):
    print('Absolute Error: {:8.20f}'.format(abs(vals[i] - approxs[i])))
    print('Relative Error: {:8.20f}\n'.format(abs(vals[i] - approxs[i])/abs(vals[i])))