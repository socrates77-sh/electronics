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
R1 = 50e3

L = Ldrwn-2*Ld
gm = (2*kn*W*ID/L)**0.5
Cgs = 2*W*L*Cox/3+W*Ld*Cox

vo = symbols('vo')
vgs = symbols('vgs')
f1 = vo/RL+gm*vgs+(vo-vgs)/R1
f2 = (vgs-vo)/R1-(1-vgs)/Rs
sol = solve((f1, f2), vo, vgs)
Av0 = sol[vo]

v1 = symbols('v1')
v2 = symbols('v2')
f1 = v2/RL+gm*v1+(v2-v1)/R1
f2 = (v1-v2)/R1+v1/Rs-1
sol = solve((f1, f2), v1, v2)
Rgs0 = sol[v1]

Rgd0 = resp(R1, RL+Rs+gm*Rs*RL)

T0 = Rgs0*Cgs+Rgd0*Cgd

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (MHz)' % (f_3db*1e-6))

# 203
