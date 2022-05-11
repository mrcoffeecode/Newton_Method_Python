'''
Created on Sep 22, 2021

@author: mrcof
'''
from scipy.optimize import newton 
import math

def Q1f(x):
    return (x * x * x) - (x * x) + 2

x = -1

x0 = newton(Q1f, x, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None)

x0 = '{0:.7g}'.format(x0)
print('\n A. Root: ', x0)


def Q2f(x):
    return math.exp(x) + x - 7
x = -1  

x0 = newton(Q2f, x, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None)

x0 = '{0:.7g}'.format(x0)
print('\n B. Root: ', x0)


def Q3f(x):
    return math.exp(x) + (math.sin(x)) - 4

x = -1  

x0 = newton(Q3f, x, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None)

x0 = '{0:.7g}'.format(x0)
print('\n C. Root: ', x0)

