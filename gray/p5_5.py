from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
R3 = 5e3
Vce_on = 0.2
Vbe_on = 0.7
VCC = 15
RL = 2e3

IQ = (VCC-Vbe_on)/R3
gm = IQ/VT
Av_Q = RL/(RL+1/gm)
print('Av_Q = %f' % Av_Q)

Vo = 1
IC1 = IQ+Vo/RL
gm1 = IC1/VT
Av_1 = RL/(RL+1/gm1)
print('Av_1 = %f' % Av_1)

Vo = -1
IC2 = IQ+Vo/RL
gm2 = IC2/VT
Av_2 = RL/(RL+1/gm2)
print('Av_2 = %f' % Av_2)

# 111
