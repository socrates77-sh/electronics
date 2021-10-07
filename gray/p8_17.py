from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
beta = 200
IC1 = IC2 = 1e-3
VA = 100
RF = 1e3
RE = 100
RL1 = 4e3
RS = 1e3

gm1 = gm2 = IC1/VT
rpi1 = rpi2 = beta/gm1
ro1 = ro2 = VA/IC1

Rx1 = RE+RF
Rx2 = resp(RE, RF)
f = -RE/(RF+RE)

Ri2 = resp(RL1, ro1, rpi2*(1+gm2*Rx2))
a = -gm1*gm2*Ri2*(resp(RS, Rx1, rpi1))/(1+gm2*Rx2)

T = a*f
A = a/(1+a*f)
ria = resp(RS, Rx1, rpi1)
RS2 = resp(ro2, RL1)
roa = ro2*(1+gm2*Rx2*rpi2/(rpi2+RS2))

Ri = ria/(1+T)
Ro = roa*(1+T)

print('T=%f' % T)
print('A=%f' % A)
print('Ri=%f (ohm)' % Ri)
print('Ro=%f (Mohm)' % (Ro*1e-6))

# 266
