from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VDD = 5
R1 = 10e3
W_L = 20
W_L4 = 5/2
Vtn = 0.8
Vtp = -0.8
kn = 60e-6
kp = 30e-6
gam_n = 0.5
phi_f = 0.3

VGS2 = symbols('VGS2')
f1 = 0.5*kp*W_L*(VGS2+Vtp)**2-(VDD-VGS2)/R1
sol = solve((f1), VGS2)
VGS2 = sol[1]
ID2 = (VDD-VGS2)/R1
ID1 = ID3 = ID5 = ID6 = ID2

gm = (2*kn*W_L*ID1)**0.5

VSB4 = VGS6 = Vtn+(2*ID6/(kn*W_L))**0.5
Vt4 = Vtn+gam_n*((VSB4+2*phi_f)**0.5-(2*phi_f)**0.5)

VC = 3
VGS4 = VC-VGS6
gds4 = kn*W_L4*(VGS4-Vt4)
rds4 = 1/gds4
Av = -1+gm*rds4
print('Av=%f' % Av)

VC = 4
VGS4 = VC-VGS6
gds4 = kn*W_L4*(VGS4-Vt4)
rds4 = 1/gds4
Av = -1+gm*rds4
print('Av=%f' % Av)

Ro = 1/gm

print('Ro=%f' % Ro)

# 273
