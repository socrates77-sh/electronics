from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
beta = 150
IC = 1e-3
rb = 200
RE = 200
VA = 80


gm = IC/VT
rpi = beta/gm
ro = VA/IC

f = RE
a = gm/(1+(rb+RE)/rpi)

T = a*f
A = a/(1+a*f)

Ri = rb+RE+rpi*(1+gm*RE)
Ro = ro*(1+gm*RE/(1+(rb+RE)/rpi))

print('T=%f' % T)
print('A=%f mA/V' % (A*1e3))
print('Ri=%f (Kohm)' % (Ri*1e-3))
print('Ro=%f (Kohm)' % (Ro*1e-3))

# 267
