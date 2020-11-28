from sympy import symbols, solve, nsolve, diff, exp, integrate
from sympy.plotting import plot
from resp import *
# from math import *

IC = 10e-6
q = 1.6e-19
VT = 26e-3
Dp = 10e-4
un = 800e-4
A = 2*(30e-6*75e-6+10e-6*30e-6)
ni = 1.414e16
Vbe1 = 525e-3
Vbe2 = 560e-3

QB1 = A*Dp*q*ni**2/IC*exp(Vbe1/VT)
QB2 = A*Dp*q*ni**2/IC*exp(Vbe2/VT)

# print('QB1=%e atom/m2' % QB1)
# print('QB2=%e atom/m2' % QB2)

R_sheet_1 = 1/(q*un*QB1)
R_sheet_2 = 1/(q*un*QB2)

print('R_sheet_1=%f Kohm/sq' % (R_sheet_1*1e-3))
print('R_sheet_2=%f Kohm/sq' % (R_sheet_2*1e-3))

# 20
