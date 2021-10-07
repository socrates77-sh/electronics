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

R = gm**3*resp(ro, rpi, R1)*resp(ro, rpi, R2)*resp(ro, R3, RF+rpi)*rpi/(rpi+RF)
A_inf = -RF
d = resp(ro, R3)*rpi/(resp(ro, R3)+RF+rpi)
A = A_inf*R/(1+R)+d/(1+R)

Ri_0 = resp(rpi, RF+resp(ro, R3))
Rin_short = 0
Rin_open = R
Ri = Ri_0*(1+Rin_short)/(1+Rin_open)

Ro_0 = resp(ro, R3, RF+rpi)
Rout_short = 0
Rout_open = R
Ro = Ro_0*(1+Rout_short)/(1+Rout_open)

print('A=%f (Kohm)' % (A*1e-3))
print('Ri=%f (ohm)' % Ri)
print('Ro=%f (ohm)' % Ro)


print('='*10)
print('Part (b)')
print('='*10)
RS = 1e3

R = gm**3*resp(ro, rpi, R1)*resp(ro, rpi, R2)*resp(ro, R3, RF+resp(rpi, RS))*resp(rpi, RS)/(resp(rpi, RS)+RF)
Ro_0 = resp(ro, R3,RF+resp(rpi,RS))
Rout_short = 0
Rout_open = R
Ro = Ro_0*(1+Rout_short)/(1+Rout_open)

print('Ro=%f (ohm)' % Ro)

# 256
