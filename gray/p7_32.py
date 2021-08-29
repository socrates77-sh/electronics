from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

Vsu = 6
Rs = 10e3
RL = 5e3
Ldrwn = 2e-6
Ld = 0.2e-6
phi0 = 0.6
W = 100e-6
Vt = 1
kn = 60e-6
Col = 0.15e-9
Cox = 0.7e-3
Cj0 = 0.4e-3
Cjsw0 = 0.4e-9
phi0 = 0.6
ID1 = 10e-6
ID2 = 0.5e-3

L = Ldrwn-2*Ld

gm1 = (2*ID1*kn*W/L)**0.5
gm2 = (2*ID2*kn*W/L)**0.5

Av0 = -gm2*RL

Cgd1 = W*Ld*Cox
Rgd10 = Rs
AD = 5e-6*W
PD = W
Csb01 = AD*Cj0+PD*Cjsw0
Vov1 = (2*ID1/(kn*W/L))**0.5
VS1 = -Vt-Vov1
VSB1 = VS1+Vsu
Csb1 = Csb01/(1+VSB1/phi0)**0.5
Rsb10 = 1/gm1
Cgs2 = (2/3)*W*L*Cox+W*Ld*Cox
Rgs20 = 1/gm1
Cdb02 = AD*Cj0+PD*Cjsw0
VD2 = Vsu-ID2*RL
VDB2 = VD2+Vsu
Cdb2 = Cdb02/(1+VDB2/phi0)**0.5
Rdb20 = RL
Cgd2 = W*Ld*Cox
Rgd20 = 1/gm1+RL+gm2*RL/gm1

T0 = Cgd1*Rgd10+Csb1*Rsb10+Cdb2*Rdb20+Cgs2*Rgs20+Cgd2*Rgd20
f_3db = 1/(2*pi*T0)

print('Av0=%f (Kohm)' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))


# 217
