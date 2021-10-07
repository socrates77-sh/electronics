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
Rs = 1e3
phi0 = 0.6
phi_f = 0.3
gam = 0.4
Vtn = 0.7
Vtp = -0.7
kn = 60e-6
tox = 20e-9
Col = 0.3e-9
Cdb0u = Csb0u = 0.8e-15
eox = 3.9 * 8.854e-12
W = 100e-6
L = 2e-6
kp = 30e-6
lam = 0.03
VI = VO = 2.5
ID = 100e-6

VGS3 = VGS4 = -(2*ID/(kp*W/L))**0.5+Vtp
VGS2 = VGS6 = VGS7 = (2*ID/(kn*W/L))**0.5+Vtn
VGS5 = VGS6-(VDD+VGS4)
W5 = L*2*ID/(kp*(VGS5-Vtp)**2)
VGS1 = VI-VGS2
VSB1 = VGS2
Vt1 = Vtn+gam*((2*phi_f+VSB1)**0.5-(2*phi_f)**0.5)
W1 = L*2*ID/(kn*(VGS1-Vt1)**2)

gm1 = (2*ID*kn*W1/L)**0.5
gm2 = (2*ID*kn*W/L)**0.5
gmb1 = gam*gm1/(2*(2*phi_f+VSB1)**0.5)
ro2 = ro3 = 1/(lam*ID)
Ro1 = 1/(gm1+gmb1)
Ro3 = resp(ro2, ro3)

print(Ro1, Ro3)

Av0 = -gm1*Ro1*gm2*Ro3

Cox = eox / tox
Csb1 = Csb0u*(W1/L)/(1+VSB1/phi0)**0.5
VDB7 = VGS2
Cdb7 = Cdb0u*W*1e6/(1+VDB7/phi0)**0.5
Cgd2 = Cgd7 = Col*W
Cgs2 = 2/3*W*L*Cox+Col*W
VDB2 = VO
Cdb2 = Cdb3 = Cdb0u*W*1e6/(1+VDB2/phi0)**0.5
Cgd3 = Cgd2
Rgd02 = Ro1+Ro3+gm2*Ro1*Ro3

T0 = Ro1*(Csb1+Cdb7+Cgd7+Cgs2)+Ro3*(Cdb2+Cdb3+Cgd3)+Rgd02*Cgd2
f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (MHz)' % (f_3db*1e-6))


# 230
