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

a = -gm**3*RF*resp(ro, R1)*resp(ro, R2)*resp(ro, R3, RF)
f = -1/RF
T = a*f
A = a/(1+a*f)
ria = RF
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
RS=1e3

a1=a*resp(RF,RS)/RF
T = a1*f
Ro = roa/(1+T)

print('Ro=%f (ohm)' % Ro)

# 253
