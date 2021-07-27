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
R1 = 900

L = Ldrwn-2*Ld
gm = (2*kn*W*ID/L)**0.5
Cgs = 2*W*L*Cox/3+W*Ld*Cox

Av0 = -gm*RL/(1+gm*R1)
Rgs0 = (Rs+R1)/(1+gm*R1)
Rgd0 = RL+Rs+gm*Rs*RL/(1+gm*R1)

T0 = Rgs0*Cgs+Rgd0*Cgd

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (MHz)' % (f_3db*1e-6))

# 202
