from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

RF = 10e3
R1 = R2 = R3 = 5e3
IC = 1e-3
beta = 200
VA = 50
VT = 26e-3

gm = IC/VT
rpi = beta/gm
ro = VA/IC

print('='*10)
print('Part (a)')
print('='*10)

a = -gm**3*resp(RF, rpi)*resp(ro, R1, rpi)*resp(ro, R2, rpi)*resp(ro, R3, RF)
f = -1/RF
T = a*f
A = a/(1+a*f)
ria = resp(RF, rpi)
roa = resp(ro, R3, RF)
Ri = ria/(1+T)
Ro = roa/(1+T)

print('T=%f' % T)
print('A=%f (Kohm)' % (A*1e-3))
print('Ri=%f (ohm)' % Ri)
print('Ro=%f (ohm)' % Ro)


print('='*10)
print('Part (b)')
print('='*10)
RS = 1e3

a1 = a*resp(RF, RS, rpi)/resp(RF, rpi)
T = a1*f
Ro = roa/(1+T)

print('Ro=%f (ohm)' % Ro)

# 254
