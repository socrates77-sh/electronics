# from sympy import symbols, solve, nsolve, diff, re, im, Abs, arg
# from sympy.plotting import plot
# from sympy.polys.partfrac import apart_full_decomposition
from scipy.sparse.extract import find
from resp import *


import matplotlib.pyplot as plt
from sympy import init_printing
import numpy as np

from control import *
from math import *
from sympy import *


f2=500e3

f1=f2/(10e6/26)
f=f1*5.7e6/26

print('f=%f (KHz)' % (f*1e-3))

# Gmc = 6.39e-3
# Roc = 86.3e3
Ric = 1.95e6

Cc = 1/(2*3.14*f1*Ric)

print('Cc=%f (uF)' % (Cc*1e6))

# 289
