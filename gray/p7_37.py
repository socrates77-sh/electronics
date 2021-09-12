from random import vonmisesvariate
from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

VDD = 5
Vo = 2.5
Rs = 1e3
CL = 100e-15
W1 = 100e-6
L1 = 1e-6
W2 = 4e-6
L2 = 1e-6
Rs = 1e3
phi0 = 0.6
phi_f = 0.3
gam = 0.4
Vt = 0.7
kn = 60e-6
tox = 20e-9
Col = 0.3e-9
Cdb0u = Csb0u = 0.8e-9
eox = 3.9 * 8.854e-12

VSB = Vo
VGS2 = VDD-Vo
Vt2 = Vt+gam*((2*phi_f+VSB)**0.5-(2*phi_f)**0.5)
ID = 0.5*kn*(W2/L2)*(VGS2-Vt2)**2

gm1 = (2*ID*kn*W1/L1)**0.5
gm2 = (2*ID*kn*W2/L2)**0.5
gmb2 = gam*gm2/(2*(2*phi_f+VSB)**0.5)

Av0 = -gm1/(gm2+gmb2)

Cox = eox / tox
Cgs1 = 2/3*W1*L1*Cox+Col*W1
Cgs2 = 2/3*W2*L2*Cox+Col*W2
Cgd1 = Col*W1

VDB1 = Vo
Cdb1 = Cdb0u*W1/(1+VDB1/phi0)**0.5
Csb2 = Csb0u*W2/(1+VSB/phi0)**0.5

RL = 1/(gm2+gmb2)
Rgd01 = Rs+RL+gm1*Rs*RL

T0 = Cgs1*Rs+Cgd1*Rgd01+(Cdb1+Cgs2+Csb2+CL)*RL
f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (MHz)' % (f_3db*1e-6))


# 224
