from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from sympy.polys.partfrac import apart_full_decomposition
from resp import *
from math import *

VT = 26e-3
RF = 2e3
RL = 2e3
IC = 1e-3
beta = 200
VA = 100

gm = IC/VT
rpi = beta/gm
ro = VA/IC
print(gm, rpi, ro)

print('='*10)
print('Part (a)')
print('='*10)

a = -resp(RF, rpi)*gm*resp(RL, RF, ro)
f = -1/RF
T = a*f
A = a/(1+T)

ria = resp(RF, rpi)
roa = resp(RL, RF, ro)
Ri = ria/(1+T)
Ro = roa/(1+T)

print('T=%f' % T)
print('A=%f (Kohm)' % (A*1e-3))
print('Ri=%f' % Ri)
print('Ro=%f (ohm)' % Ro)

print('='*10)
print('Part (b)')
print('='*10)

R = gm*resp(RL, ro, RF+rpi)*rpi/(RF+rpi)
A_inf = -RF
d = resp(rpi, RF+resp(ro, RL))*resp(ro, RL)/RF+resp(ro, RL)
A = A_inf*R/(1+R)+d/(1+R)

Ri_0 = resp(rpi, RF+resp(ro, RL))
Rin_short = 0
Rin_open = R
Ri = Ri_0*(1+Rin_short)/(1+Rin_open)

Ro_0 = resp(ro, RL, RF+rpi)
Rout_short = 0
Rout_open = R
Ro = Ro_0*(1+Rout_short)/(1+Rout_open)

print('A=%f (Kohm)' % (A*1e-3))
print('Ri=%f' % Ri)
print('Ro=%f (ohm)' % Ro)


# 279
