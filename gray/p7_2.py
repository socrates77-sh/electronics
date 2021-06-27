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
f_3db = 1/(2*pi)/(Rs*(Cgs+Cgd*(1+gm*RL)))
p2 = -1/(2*pi)*(1/(RL*Cgd)+1/(Rs*Cgs)+1/(RL*Cgs)+gm/Cgs)

print('f-3db=%f (MHz)' % (f_3db*1e-6))
print('p2=%f (MHz)' % (p2*1e-6))


# 185
