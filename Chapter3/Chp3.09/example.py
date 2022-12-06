import sys
import math
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

print("alpha: {}".format(ex.fixed_point_solver(1.01, 1, 2, lambda x:math.exp(-1.0*x)+1,err=math.pow(10,-10.0),verbose=True)))