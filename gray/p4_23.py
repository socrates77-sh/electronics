from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
# from math import *

un = 450e-4
eox = 3.9*8.86e-12
esi = 11.6*8.86e-12
tox = 80e-10
dXd_n = 0.02e-6
NA = 5e21
ni = 1.45e16
q = 1.6e-19
VT = 26e-3

VDD = 3
Iin = 100e-6
Iout = 10e-6
Vov1 = 0.2
Ro = 50e6

Cox = eox/tox
kn = un*Cox

W_L1 = 2*Iin/(kn*Vov1**2)

Leff2 = 1e-6
lamb_n = dXd_n/Leff2
ro2 = 1/(lamb_n*Iout)

R2, W_L2 = symbols('R2 W_L2', positive=True)
gm2 = (2*Iout*kn*(W_L2))**0.5
Vov2 = (2*Iout/(kn*W_L2))**0.5
f1 = Iout*R2+Vov2-Vov1
f2 = ro2*(1+gm2*R2)-Ro
sol = solve((f1, f2), R2, W_L2, dict=True)

R2_r = sol[0][R2]
W_L2_r = sol[0][W_L2]


print('R2=%fohm' % (R2_r*1e-3))
print('(W/L)1=%f' % W_L1)
print('(W/L)2=%f' % W_L2_r)

# 81
