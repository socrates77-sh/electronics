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

a0 = 200
p1 = 1
p2 = 3
p3 = 4

s = symbols('s')
A = 1/((s+p1)*(s+p2)*(s+p3))
D0 = denom(A)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(A)
# N1 = Poly(N0).all_coeffs()
# N2 = [float(k) for k in N1]
N2 = [float(N0)]
B1b = tf(N2, D2)
data = rlocus(B1b, grid=True)
# plt.show()

s = I*4.62
T0 = abs(s-p1)*abs(s-p2)*abs(s-p3)/(p1*p2*p3)

f = T0/a0
print('f=%f' % f)

# 290
