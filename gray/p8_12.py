from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

beta = 120
VA = 40
VT = 26e-3
IC1 = 0.5e-3
IC2 = 0.77e-3
IC3 = 0.73e-3
RE1 = RE2 = 290
RF = 1.9e3
RL1 = 10.6e3
RL2 = 6e3

gm1 = IC1/VT
gm2 = IC2/VT
gm3 = IC3/VT
rpi1 = beta/gm1
rpi2 = beta/gm2
rpi3 = beta/gm3
ro1 = VA/IC1
ro2 = VA/IC2
ro3 = VA/IC3

R = resp(RF+RE1, RE1)
Ri3 = rpi3*(1+gm3*R)
R1 = resp(RL1, rpi2)
R2 = resp(RL2, ro2, Ri3)
a = gm1*R1*gm2*R2*gm3/((1+gm1*R)*(1+gm3*R))*R

f = RE1/(RE1+RF)

T = a*f
A = a/(1+a*f)
ria = rpi1*(1+gm1*R)
roa = resp(R, 1/gm3+resp(ro2, RL2)/beta)
Ri = ria*(1+T)
Ro = roa/(1+T)

print('T=%f' % T)
print('A=%f' % A)
print('Ri=%f (Mohm)' % (Ri*1e-6))
print('Ro=%f (ohm)' % Ro)


# 257
