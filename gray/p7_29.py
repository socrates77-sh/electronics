from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

ID = 0.5e-3
W = 100e-6
Ldrwn = 2e-6
Ld = 0.2e-6
kn = 60e-6
Cox = 0.7e-3
Cgd = 14e-15
Rs=10e3
RL=20e3

L = Ldrwn-2*Ld

print('==== CS ====')

gm1 = (2*ID*kn*W/L)**0.5
Av0 = -gm1*RL

Cgs1 = (2/3)*W*L*Cox+W*Ld*Cox
Rgs10 = Rs

Cgd1=Cgd
Rgd10 = Rs+RL+gm1*Rs*RL

T0 = Cgs1*Rgs10+Cgd1*Rgd10
f_3db = 1/(2*pi*T0)
tr=0.35/f_3db

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))
print('tr=%f (ns)' % (tr*1e9))

print('==== Cascode ====')
gm2=gm1
Av0 = -gm1*RL

Rgd10=2*Rs+1/gm2
Cgs2=Cgs1
Rgs20=1/gm2
Cgd2=Cgd
Rgd20=RL

T0 = Cgs1*Rgs10+Cgd1*Rgd10+Cgs2*Rgs20+Cgd2*Rgd20
f_3db = 1/(2*pi*T0)
tr=0.35/f_3db

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))
print('tr=%f (ns)' % (tr*1e9))

# 212
