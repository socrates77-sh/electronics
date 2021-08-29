from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

VT = 26e-3
IC1 = 1e-3
IC2 = 4e-3
beta1 = 200
tF1 = 0.2e-9
Cu1 = 0.2e-12
Cje1 = 1e-12
Ccs1 = 1e-12
beta2 = 200
tF2 = 0.2e-9
Cu2 = 0.8e-12
Cje2 = 4e-12
Ccs2 = 4e-12

gm1 = IC1/VT
rpi1 = beta1/gm1
gm2 = IC2/VT
rpi2 = beta1/gm2

Ai0 = gm2*resp(rpi1, rpi2, 1/gm1)

Cb1 = tF1*gm1
Cpi1 = Cb1+Cje1
Cb2 = tF2*gm2
Cpi2 = Cb2+Cje2

print(Cpi2)

T0 = (Cpi1+Ccs1+Cpi2+Cu2)*resp(rpi1, rpi2, 1/gm1)
f_3db = 1/(2*pi*T0)
tr = 0.35/f_3db

print('Ai0=%f' % Ai0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))
print('tr=%f (ns)' % (tr*1e9))

# 219
