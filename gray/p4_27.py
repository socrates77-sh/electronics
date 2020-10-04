from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT0 = 26e-3
K1 = 1500e-6
VG0 = 1.205
gamma = 3.2
T0 = 25+273

Vout = VG0+VT0*gamma+VT0*K1*T0

# print('Iout=%f (mA)' % (Iout*1e3))
# print('Rout=%f (Mohm)' % (Rout*1e-6))
print('Vout=%f (V)' % Vout)

# 94
