# from sympy import symbols, solve, nsolve, diff, re, im, Abs, arg
# from sympy.plotting import plot
# from sympy.polys.partfrac import apart_full_decomposition
# from scipy.sparse.extract import find
from resp import *


import matplotlib.pyplot as plt
from sympy import init_printing
import numpy as np

from control import *
from sympy import *
from math import *

a0 = 4000
p1 = -3
p2 = -6
RF = 5e3
RE = 50
CF = 1.5e-12

fz = 1/(2*pi*RF*CF)

f = RE/RF

s = symbols('s')
a = a0/((1-s/p1)*(1-s/p2))
A = a/(1+a*f)
print(simplify(A))
D0 = denom(A)
sol = solve(D0)
print(sol)

z = -fz/1e6
f = f*(1-s/z)
A = a/(1+a*f)
print(simplify(A))
D0 = denom(A)
sol = solve(D0)
print(sol)

# D1 = Poly(D0).all_coeffs()
# D2 = [float(k) for k in D1]
# N0 = numer(A)
# # N1 = Poly(N0).all_coeffs()
# # N2 = [float(k) for k in N1]
# N2 = [float(N0)]
# B1b = tf(N2, D2)
# data = rlocus(B1b, grid=True)
# # plt.show()

# s = I*2425
# T0 = abs(s+p1)*abs(s+p2)*abs(s+p3)/(p1*p2*p3)

# f = T0/a0
# print('f=%f' % f)

# 291
