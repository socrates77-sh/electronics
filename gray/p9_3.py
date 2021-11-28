# from sympy import symbols, solve, nsolve, diff, re, im, Abs, arg
# from sympy.plotting import plot
# from sympy.polys.partfrac import apart_full_decomposition
from resp import *
from math import *

import matplotlib.pyplot as plt
from sympy import init_printing
from numpy import arange
import sympy

A = 200
fb = 0.05
f1 = 1e6
f2 = 2e6
f3 = 4e6


A=1/(1+e**(1j*160/180*pi))
print(20*log10(abs(A)))

# 287
