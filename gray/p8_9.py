from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

RF = 10e3
R1 = R2 = R3 = 5e3
ID = 1e-3
W_L = 100
k = 60e-6
lam = 1/50

gm = gm1 = gm2 = gm3 = (2*ID*k*W_L)**0.5
ro = 1/(lam*ID)

print('='*10)
print('Part (a)')
print('='*10)

R = gm**3*resp(ro, R1)*resp(ro, R2)*resp(ro, R3)
A_inf = -RF
d = resp(ro, R3)
A = A_inf*R/(1+R)+d/(1+R)

Ri_0 = RF+resp(ro, R3)
Rin_short = 0
Rin_open = R
Ri = Ri_0*(1+Rin_short)/(1+Rin_open)

Ro_0 = resp(ro, R3)
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

R = gm**3*resp(ro, R1)*resp(ro, R2)*resp(ro, R3, RF+RS)*RS/(RS+RF)
Ro_0 = resp(ro, R3,RF+RS)
Rout_short = 0
Rout_open = R
Ro = Ro_0*(1+Rout_short)/(1+Rout_open)

print('Ro=%f (ohm)' % Ro)

# 255
