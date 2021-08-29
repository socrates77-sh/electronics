from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

Vsu = 10
Rs = 20e3
Ldrwn = 2e-6
Ld = 0.2e-6
Xd = 1e-6
phi0 = 0.6
W1 = W2 = W5 = W6 = 100e-6
W3 = W4 = 50e-6
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
ID5 = 1e-3

L = Ldrwn-2*Ld-Xd

ID1 = ID3 = ID5/2
gm1 = (2*ID1*kn*W1/L)**0.5
ro1 = 1/(lambn*ID1)
ro3 = 1/(lambp*ID3)
ro = resp(ro1, ro3)

Av0 = -gm1*ro

Cgs1 = (2/3)*W1*L*Cox+W1*Ld*Cox
Rgs10 = Rs

AD = 5e-6*W1
PD = W1
Cdb01 = AD*Cj0n+PD*Cjsw0n
AD = 5e-6*W3
PD = W3
Cdb03 = AD*Cj0p+PD*Cjsw0p

VDB1 = VDB3 = 5
Cdb1 = Cdb01/(1+VDB1/phi0)**0.5
Cdb3 = Cdb03/(1+VDB3/phi0)**0.5
Rdb10 = Rdb30 = ro

Cgd1 = W1*Ld*Cox
Rgd10 = Rs+ro+gm1*Rs*ro
T0 = Cgs1*Rgs10+Cdb1*Rdb10+Cdb3*Rdb30+Cgd1*Rgd10

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))

# 211
