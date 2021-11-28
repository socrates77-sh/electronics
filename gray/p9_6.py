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


p1 = 300e3
p2 = 2e6
p3 = 25e6
a0 = 5000

print('='*20)
print('Part (a)')
print('='*20)

f = 1
T = a0*f
p1_n = p2/T

print('P1_n=%f (Hz)' % p1_n)

print('='*20)
print('Part (b)')
print('='*20)

A = 10
f = 1/A
T = a0*f
p1_n = p2/T

print('P1_n=%f (Hz)' % p1_n)

# 288
