from resp import *
from numpy import log, sqrt, exp
from sympy import symbols, simplify, evalf, solve, diff
from sympy import init_printing

VT = 26e-3
IS = 1e-16
beta = 100
kn = 200e-6
Vt0 = 0.6
VBE = 0.7
VCC = 5
RL1 = 1e3
RL2 = 10e3
RL3 = 1e3
RL4 = 10e3
WL1 = 300
WL2 = 20

VGS2, ID2 = symbols('VGS2 ID2', positive=True)
eq1 = ID2 * RL4 + VBE + VGS2 - VCC
eq2 = WL2 * kn / 2 * (VGS2 - Vt0)**2 - ID2
sol = solve((eq1, eq2), VGS2, ID2, dict=True)
VGS2 = sol[0][VGS2]
ID2 = sol[0][ID2]

VBQ2 = VCC - ID2 * RL4
VEQ1 = VBQ2 - VBE
IRL1 = (VCC - VEQ1) / RL1
IRL2 = ID2
IC1 = ID2
IC2 = IC1
ID1 = IRL1 + IRL2
VGS1 = Vt0 + (ID1 / (WL1 * kn / 2))**0.5
VCQ1 = VCC - IC1 * RL2
IC3 = (VCQ1 - VBE) / RL3

gm_M1 = (2 * ID1 * kn * WL1)**0.5
gm_M2 = (2 * ID2 * kn * WL2)**0.5
gm_Q1 = IC1 / VT
gm_Q2 = IC2 / VT
gm_Q3 = IC3 / VT
rpi_Q3 = beta / gm_Q3
Ri1 = 1 / gm_Q1 + (1 / gm_Q2 + 1 / gm_M2) / beta

av = -gm_M1 * RL1 / (RL1 + Ri1) * beta / (beta + 1) * \
    resp(RL2, (rpi_Q3 + (beta + 1) * RL3)) * \
    gm_Q3 * RL3 / (1 + gm_Q3 * RL3)

print('av=%f' % av)

