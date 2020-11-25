# from sympy import symbols, solve, nsolve, diff, exp, integrate, evalf
from sympy.plotting import plot
from resp import *
from math import pi, log, sqrt

eox = 3.9*8.86e-12
esi = 11.6*8.86e-12
tox = 400e-10
q = 1.6e-19
ni = 1.45e16
NA = 1e22
phi_ms = -0.1
Qss = q*1e15
VT = 26e-3

Cox = eox/tox
phi_f = VT*log(NA/ni)
Qb = sqrt(2*q*NA*esi*2*phi_f)

Vt = phi_ms+2*phi_f+Qb/Cox-Qss/Cox

print('Vt=%f V' % Vt)


# 22
