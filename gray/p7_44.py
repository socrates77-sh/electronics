from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
Rs = 5e3
RL = 3e3
rb = 300
IC = 0.5e-3
beta = 200
fT = 500e6
Cu = 0.3e-12

gm = IC/VT
rpi = beta/gm
Cpi = gm/(2*pi*fT)-Cu

R=resp(Rs+rb,rpi)
T0=Cpi*R+Cu*(R+RL+gm*R*RL)
p1 = -1/T0

Rpis = resp(R,1/gm,RL)
t1 = Cpi*Rpis
t2 = Cu*RL
p2 = -(1/t1+1/t2)

print('p1=%f (rad/s)' % p1)
print('p2=%f (rad/s)' % p2)


# 246
