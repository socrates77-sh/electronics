from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

a = 1e5
f = 1e-3
da_a = 0.1

A = a/(1+a*f)
dA_A = da_a/(1+a*f)

print('A=%f' % A)
print('dA/A=%f%%' % (dA_A*100))

f = 0.1
A = a/(1+a*f)
dA_A = da_a/(1+a*f)

print('A=%f' % A)
print('dA/A=%f%%' % (dA_A*100))

# 251
