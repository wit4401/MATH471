"""
Problem 3.1.6 and 3.1.7

If you borrow L dollars at an annual interest rate of r, for a period of m
years, then the size of the monthly payment, M, is given by the annuity equation

                  L = (12M/r)[1-(1+(r/12))^(-12m)]

The author needs to borrow $150,000 to buy the new house that he wants, and he can 
only afford to pay $600 per month. Assuming a 30 year mortage, use the bisection
method to determine what interest rate he can afford to pay.

What is the interest rate that the author can afford if he only has to borrow $100,000?
"""
import sys
import math
sys.path.append('/Users/williamtownsend/Desktop/SchoolWork/Fall2022/MATH471')
import coursefuncts.chp3 as ex

M = 600
m = 30
L = 150000
annuity=lambda r: ((12*M)/r)*(1-(1+(r/12))**(-12*m))-L

sol=ex.iteration_bisection(annuity, 0.01, 0.04, 10000)
print('Interest Rate Needed if $150,000 is borrowed: {:5.5f}%'.format(sol*100))

L = 100000
annuity=lambda r: ((12*M)/r)*(1-(1+(r/12))**(-12*m))-L
sol=ex.iteration_bisection(annuity, 0.05, 0.075, 10000)
print('Interest Rate Needed if $100,000 is borrowed: {:5.5f}%'.format(sol*100))