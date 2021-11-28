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

a0 = 10**(108/20)
f2 = 10e6

f1 = 26
f = symbols('f')
a = a0/((1+I*f/f1)*(1+I*f/f2))

fun1 = ((1+(f/f1)**2)*(1+(f/f2)**2))-a0**2
fun2 = -atan(f/f1)-atan(f/f2)

sol = solve(fun1)

f_r = sol[1]
a_arg = fun2.evalf(subs={f: f_r})*180/3.1416

print('f=%f (MHz)' % (f_r*1e-6))

Gmc = 6.39e-3
Roc = 86.3e3
Ric = 1.95e6

CM = 1/(2*3.14*f1*Ric)
Cc = CM/(1+Gmc*Roc)

print('Cc=%f (pF)' % (Cc*1e12))

# 289
