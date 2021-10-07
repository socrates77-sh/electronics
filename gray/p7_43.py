from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

ID = 100e-6
W = 20e-6
L = 0.5e-6
kn = 180e-6
lam = 0.04
CL = 2e-12
Cp = 0.2e-12

gm2 = (2*ID*kn*W/L)**0.5
ro1 = ro2 = 1/(lam*ID)

RL0 = ro1+ro2+gm2*ro1*ro2

T0 = Cp*ro1+CL*RL0
p1 = -1/T0

RLs = ro2
Rps = resp(ro1, ro2, 1/gm2)
t1 = CL*RLs
t2 = Cp*Rps
p2 = -(1/t1+1/t2)

print('p1=%f (rad/s)' % p1)
print('p2=%f (rad/s)' % p2)

# 245
