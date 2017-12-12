from numpy import log, sqrt
from resp import *
from sympy import symbols, simplify, evalf, solve, diff
from sympy import init_printing

init_printing()

VT = 26e-3
RL = 1e3
RB = 1e3
Vo = 2
VCC = 3
beta = 100
IS = 1e-16
gamma = 0.25
phi = 0.3

W = 10e-6
L = 1e-6
kn = 200e-6
Vt0 = 0.6

ID_est = 0.7 / RB
IC_est = (VCC - Vo) / RL - ID_est
VBE = VT * log(IC_est / IS)

ID = VBE / RB
IC = (VCC - Vo) / RL - ID

print('ID=%f (mA)' % (ID * 1e3))
print('IC=%f (mA)' % (IC * 1e3))

gm1 = symbols('gm1')
gmb1 = symbols('gmb1')
gm2 = symbols('gm2')
v1 = symbols('v1')
v2 = symbols('v2')
vo = symbols('vo')
vi = symbols('vi')
R = symbols('R')
RL = symbols('RL')

f1 = (gmb1 * v2 - gm1 * v1 - gm2 * v2) * RL - vo
f2 = v1 + v2 - vi
f3 = (gm1 * v1 - gmb1 * v2) * R - v2
sol = solve((f1, f2, f3), v1, v2, vo)
Av = sol[vo] / vi

RL_v = 1e3
gm1_v = sqrt(2 * ID * kn * W / L)
gmb1_v = gm1_v * gamma / (2 * sqrt(2 * phi + VBE))
gm2_v = IC / VT
rpi2 = beta / gm2_v
R_v = resp(rpi2, RB)

Av_v = Av.evalf(subs={RL: RL_v, gm1: gm1_v, gmb1: gmb1_v, gm2: gm2_v, R: R_v})
print('Av=%f' % Av_v)
