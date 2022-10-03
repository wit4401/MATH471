# lectureNotes.py (10.03.2022)
#
# Euler's Method Solver (Chp 2.3)

import math
import numpy as np
import matplotlib.pyplot as plt

#actual functional solution to ODE:
def exactSol(t):
    return math.exp(t-t**2.0)

x0=0.0
y0=exactSol(x0)

print('x0 = {}, y0 = {}'.format(x0,y0))

#choose an interval which includes our desited value y(3):
a = x0
b = 3.0

# Determine the grid intervals:
h = 64   #divisor for grid
gridh = (b-a)/8

