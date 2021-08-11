from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

Rs = 100e3
RL = 3e3
ID1 = 50e-6
ID2 = 1e-3
W = 100e-6
Ldrwn = 2e-6
Ld = 0.2e-6
kn = 60e-6
Cox = 0.7e-3
Cgd = 14e-15
Cdb = 200e-15
Csb = 180e-15

L = Ldrwn-2*Ld
gm1 = (2*kn*W*ID1/L)**0.5
gm2 = (2*kn*W*ID2/L)**0.5
Cgs = 2*W*L*Cox/3+W*Ld*Cox

Av0 = -gm2*RL

Rdb01 = Rdb02 = RL
Rgs01 = Rgs02 = 1/gm1

Rgd01 = Rs+RL+gm2*RL*Rs
Rgd02 = gm2*RL/gm1+1/gm1

T0 = (Rdb01+Rdb02)*Cdb+Rgs01*Cgs+Rgs02*(Cgs+Csb)+(Rgd01+Rgd02)*Cgd

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (MHz)' % (f_3db*1e-6))

Rdb01 = 0
Rgd01 = Rs

T0 = (Rdb01+Rdb02)*Cdb+Rgs01*Cgs+Rgs02*(Cgs+Csb)+(Rgd01+Rgd02)*Cgd

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (MHz)' % (f_3db*1e-6))


# 207
