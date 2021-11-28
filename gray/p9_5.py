# from sympy import symbols, solve, nsolve, diff, re, im, Abs, arg
# from sympy.plotting import plot
# from sympy.polys.partfrac import apart_full_decomposition
from scipy.sparse.extract import find
from resp import *


import matplotlib.pyplot as plt
from sympy import init_printing
import numpy as np
from sympy import *
from control import *
from math import *


print('='*20)
print('Part (a)')
print('='*20)

p1 = 300e3
a0 = 5000
f = 1
T = a0*f
pd = p1/T

print('PD=%f (Hz)' % pd)

print('='*20)
print('Part (b)')
print('='*20)

A = 10
f = 1/A
T = a0*f
pd = p1/T

print('PD=%f (Hz)' % pd)

# 287
