from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from sympy.polys.partfrac import apart_full_decomposition
from resp import *
from math import *

ID = 0.5e-3
WL = 100
kn = 180e-6
phi_f = 0.3
gam = 0.3
Ri = 1e6
Ro = 10e3
av = 1000

gm = (2*ID*kn*WL)**0.5
VSB = 0
gmb = gm*gam/(2*(2*phi_f+VSB)**0.5)

print('='*10)
print('Part (a)')
print('='*10)

a = av*gm/(gm+gmb)
f = 1
T = a*f
A = a/(1+T)

ria = Ri
roa = resp(1/gm, 1/gmb)
Rin = ria*(1+T)
Rout = roa/(1+T)

print('T=%f' % T)
print('A=%f' % A)
print('Rin=%f (Mohm)' % (Rin*1e-6))
print('Rout=%f (ohm)' % Rout)

print('='*10)
print('Part (b)')
print('='*10)

R = gm*av/(gm+gmb+1/Ri)
A_inf = 1
d = resp(1/gm, 1/gmb)/(Ri+resp(1/gm, 1/gmb))
A = A_inf*R/(1+R)+d/(1+R)

Ri_0 = Ri+resp(1/gm, 1/gmb)
Rin_short = R
Rin_open = 0
Ri = Ri_0*(1+Rin_short)/(1+Rin_open)

Ro_0 = resp(1/gm, 1/gmb, 1/Ri)
Rout_short = 0
Rout_open = R
Ro = Ro_0*(1+Rout_short)/(1+Rout_open)

print('A=%f' % A)
print('Rin=%f (Mohm)' % (Rin*1e-6))
print('Rout=%f (ohm)' % Rout)

# 280
