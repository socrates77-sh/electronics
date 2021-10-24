from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from sympy.polys.partfrac import apart_full_decomposition
from resp import *
from math import *

RF = 100e3
RL = 15e3
ID = 0.5e-3
WL = 100
kn = 180e-6

gm = (2*ID*kn*WL)**0.5
print(gm)


print('='*10)
print('Part (a)')
print('='*10)

a = -RF*gm*resp(RL, RF)
f = -1/RF
T = a*f
A = a/(1+T)

ria = RF
roa = resp(RL, RF)
Ri = ria/(1+T)
Ro = roa/(1+T)

print('T=%f' % T)
print('A=%f (Kohm)' % (A*1e-3))
print('Ri=%f (Kohm)' % (Ri*1e-3))
print('Ro=%f (ohm)' % Ro)

print('='*10)
print('Part (b)')
print('='*10)

R = gm*RL
A_inf = -RF
d = RL
A = A_inf*R/(1+R)+d/(1+R)

Ri_0 = RF+RL
Rin_short = 0
Rin_open = R
Ri = Ri_0*(1+Rin_short)/(1+Rin_open)

Ro_0 = RL
Rout_short = 0
Rout_open = R
Ro = Ro_0*(1+Rout_short)/(1+Rout_open)

print('A=%f (Kohm)' % (A*1e-3))
print('Ri=%f (Kohm)' % (Ri*1e-3))
print('Ro=%f (ohm)' % Ro)


# 278
