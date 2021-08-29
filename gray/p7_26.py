from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

Vsu = 10
R1 = 30e3
Ldrwn = 2e-6
Ld = 0.2e-6
Xd = 1e-6
phi0 = 0.6
W1 = 200e-6
W2 = W3 = 100e-6
Vtn = 1
kn = 60e-6
lambn = 1/100
Cox = 0.7e-3
Cj0n = 0.4e-3
Cjsw0n = 0.4e-9
Vtp = -1
kp = 20e-6
lambp = 1/50
Cj0p = 0.2e-3
Cjsw0p = 0.2e-9

L = Ldrwn-2*Ld-Xd

ID3x = (Vsu+Vtp)/R1
Vov3 = (2*ID3x/(kn*W3/L))**0.5
ID3 = (Vsu+Vtp-Vov3)/R1
ID1 = ID2 = 315e-6
gm1 = (2*ID1*kp*W1/L)**0.5
ro1 = 1/(lambp*ID1)
gm2 = (2*ID2*kn*W2/L)**0.5
ro2 = 1/(lambn*ID2)
gm3 = (2*ID3*kn*W3/L)**0.5
ro3 = 1/(lambn*ID3)

ro = resp(ro1, ro2)
Avi0 = ro

Cgs1 = (2/3)*W1*L*Cox+W1*Ld*Cox
Rgs10 = 1/gm1

AD = 5e-6*W1
PD = W1
Cdb01 = AD*Cj0p+PD*Cjsw0p
AD = 5e-6*W2
PD = W2
Cdb02 = AD*Cj0n+PD*Cjsw0n

VDB1 = VDB2 = Vsu
Cdb1 = Cdb01/(1+VDB1/phi0)**0.5
Cdb2 = Cdb02/(1+VDB2/phi0)**0.5
Rdb10 = Rdb20 = ro

Cgd2 = W2*Ld*Cox
Rx = resp(1/gm3, ro3, R1)
Rgd20 = Rx+ro+gm2*Rx*ro

Cgd1 = W1*Ld*Cox
Rgd10 = 1/gm1+2*ro

T0 = Cgs1*Rgs10+Cdb1*Rdb10+Cdb2*Rdb20+Cgd1*Rgd10+Cgd2*Rgd20

f_3db = 1/(2*pi*T0)

print('Avi0=%f (Kohm)' % (Avi0*1e-3))
print('f-3db=%f (KHz)' % (f_3db*1e-3))

T0 = Cgs1*Rgs10+Cdb1*Rdb10+Cdb2*Rdb20+(20e-12+Cgd1)*Rgd10+Cgd2*Rgd20

f_3db = 1/(2*pi*T0)

print('f-3db=%f (KHz)' % (f_3db*1e-3))

# 209
