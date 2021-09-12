from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

VT = 26e-3
beta = 200
fT = 400e6
ICx = 1e-3
Cu = 0.3e-12
Cje = 3e-12
Ccs = 1.5e-12
VBE_on = 0.6
beta3 = 100
fT3 = 6e6
ICx3 = 0.5e-3
Cbs = 1.5e-12
VCC = 6
RL1 = 12.5e3
RL3 = 10e3
RE3 = 1e3
R1 = 1e3
R2 = 2.5e3
R3 = 10e3
Rs = 10e3

IC5 = (VCC-VBE_on)/(R1+R3)
IC4 = R1/R2*IC5
IC1 = IC2 = IC4/2
VC2x = VCC-IC2*RL1
IC3x = (VCC-VC2x-VBE_on)/RE3
IB3 = IC3x/beta3
VC2 = VCC-(IC2-IB3)*RL1
IC3 = (VCC-VC2-VBE_on)/RE3

gm1 = IC1/VT
rpi1 = beta/gm1
gm3 = IC3/VT
rpi3 = beta3/gm3

Ri3 = rpi3*(1+gm3*RE3)
Gm3 = gm3/(1+gm3*RE3)

Av0 = 0.5*rpi1/(rpi1+Rs)*gm1*resp(Ri3, RL1)*Gm3*RL3

gmx = ICx/VT
Cpi1x = gmx/(2*3.1416*fT)-Cu
Cb1x = Cpi1x-Cje
Cb1 = Cb1x*IC1/ICx
Cpi1 = Cb1+Cje

gmx3 = ICx3/VT
Cpi3x = gmx3/(2*3.1416*fT3)-Cu-Cbs
Cpi3x1 = 0.5/(26*2*3.1416*fT3)-Cu-Cbs
Cb3x = Cpi3x-Cje
Cb3 = Cb3x*IC3/ICx3
Cpi3 = Cb3+Cje

Rpi01 = resp(Rs, rpi1)
Rcs01 = resp(RL1, Ri3)
Ru01 = Rpi01+Rcs01+gm1*Rpi01*Rcs01
Rpi03 = resp(rpi3, (RL1+RE3)/(1+gm3*RE3))
Ru03 = Rcs01+RL3+Gm3*Rcs01*RL3
Rbs03 = Rcs01

print(Rpi03, Ru03, Rbs03)

T0 = Cpi1*Rpi01+Cu*Ru01+Ccs*Rcs01+Cpi3*Rpi03+Cu*Ru03+Cbs*Rbs03
f_3db = 1/(2*pi*T0)
# tr = 0.35/f_3db

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))
# print('tr=%f (ns)' % (tr*1e9))

# 222
