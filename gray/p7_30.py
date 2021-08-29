from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
Rs = 5e3
RL = 3e3
IC = 1e-3
beta = 100
Cu = 0.4e-12
Ccs = 1e-12
fT = 500e6

gm1 = IC/VT
rpi1 = beta/gm1
Cpi1 = gm1/(2*3.1416*fT)-Cu

print('==== CE ====')

Av0 = -(rpi1/(Rs+rpi1))*gm1*RL

Rpi10 = resp(Rs, rpi1)
Ru10 = Rpi10+RL+gm1*Rpi10*RL
Rcs10 = RL
Cu1 = Cu
Ccs1 = Ccs

T0 = Cpi1*Rpi10+Cu1*Ru10+Ccs1*Rcs10
f_3db = 1/(2*pi*T0)
tr = 0.35/f_3db

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))
print('tr=%f (ns)' % (tr*1e9))

print('==== Cascode ====')
gm2 = gm1

Ru10 = 2*Rpi10+1/gm2
Rcs10 = 1/gm2
Cpi2 = Cpi1
Rpi20 = 1/gm2
Cu2 = Cu
Ccs2 = Ccs

T0 = Cpi1*Rpi10+Cu1*Ru10+Ccs1*Rcs10+Cpi2*Rpi20+(Cu2+Ccs2)*RL
f_3db = 1/(2*pi*T0)
tr = 0.35/f_3db

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))
print('tr=%f (ns)' % (tr*1e9))

# 213
