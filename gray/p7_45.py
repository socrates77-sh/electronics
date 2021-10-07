from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

Rs = 10e3
RL = 5e3
ID = 0.5e-3
W = 100e-6
Ldrwn = 2e-6
Ld = 0.2e-6
kn = 60e-6
Cox = 0.7e-3
Cgd = 14e-15

L = Ldrwn-2*Ld
gm = (2*kn*W*ID/L)**0.5
Cgs = 2*W*L*Cox/3+W*Ld*Cox

T0 = Cgs*Rs+Cgd*(Rs+RL+gm*Rs*RL)
p1 = -1/T0

t1 = Cgs*resp(Rs, 1/gm, RL)
t2 = Cgd*RL
p2 = -(1/t1+1/t2)

print('p1=%f (rad/s)' % p1)
print('p2=%f (rad/s)' % p2)


# 247
