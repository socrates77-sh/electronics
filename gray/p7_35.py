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
fT = 600e6
ICx = 1e-3
Cu = 0.2e-12
Cje = 2e-12
Ccs = 1e-12
VBE_on = 0.6
VCC = 6
RL1 = 10e3
RL2 = 5e3
RE2 = 5e3
R1 = 1e3
R2 = 2e3
R3 = 5e3
Rs = 20e3

IC6 = (VCC-VBE_on)/(R1+R3)
IC5 = IC6/2
IC1 = IC5/2
VC1 = VCC-IC1*RL1
IC3 = 0.5*(VC1-VBE_on)/RE2
VC3 = VCC-IC3*RL2

gm1 = IC1/VT
rpi1 = beta/gm1
gm3 = IC3/VT
rpi3 = beta/gm3

Av0 = 0.5*rpi1/(rpi1+Rs)*gm1*resp(rpi3, RL1)*gm3*RL2

gmx = ICx/VT
Cpix = gmx/(2*3.1416*fT)-Cu
Cbx = Cpix-Cje
Cb1 = Cbx*IC1/ICx
Cpi1 = Cb1+Cje
Cb3 = Cbx*IC3/ICx
Cpi3 = Cb3+Cje

Rpi01 = resp(Rs, rpi1)
Rcs01 = resp(RL1, rpi3)
Ru01 = Rpi01+Rcs01+gm1*Rpi01*Rcs01
Rpi03 = Rcs01
Ru03 = Rpi03+RL2+gm3*Rpi03*RL2
Rcs03 = RL2

T0 = Cpi1*Rpi01+Cu*Ru01+Ccs*Rcs01+Cpi3*Rpi03+Cu*Ru03+Ccs*Rcs03
f_3db = 1/(2*pi*T0)
tr = 0.35/f_3db

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))
print('tr=%f (ns)' % (tr*1e9))

# 219
