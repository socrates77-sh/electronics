from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

un = 450e-4
up = 150e-4
eox = 3.9*8.86e-12
tox = 80e-10
Ld = 0.09e-6
Xd = 0.1e-6
L = 1e-6
dXd_dVDS = 0.04e-6

Cox = eox/tox
Leff = L-2*Ld-Xd

W_L1 = 150e-6/Leff
ID1 = 100e-6
gm1 = (2*ID1*up*Cox*W_L1)**0.5

W_L6 = 100e-6/Leff
ID6 = 200e-6
gm6 = (2*ID6*un*Cox*W_L6)**0.5

ID2 = 100e-6
ro2 = ro4 = Leff/(ID2*dXd_dVDS)

ID6 = 200e-6
ro6 = ro7 = Leff/(ID6*dXd_dVDS)

Av = -gm1*resp(ro2, ro4)*gm6*resp(ro6, ro7)

print('Av=%f' % Av)

W_L3 = 50e-6/Leff
ID3 = 100e-6
Vov3 = (2*ID3/(un*Cox*W_L3))**0.5

Vov1 = (2*ID1/(up*Cox*W_L1))**0.5

W_L5 = 150e-6/Leff
ID5 = 200e-6
Vov5 = (2*ID5/(up*Cox*W_L5))**0.5

Vt1 = 0.8
Vt3 = 0.6
VDD = VSS = 1.5

VIC_min = Vt3-Vt1+Vov3-VSS
VIC_max=VDD-Vt1-Vov1-Vov5

print('%0.2f(V) < VIC < %0.2f(V)' % (VIC_min, VIC_max))

# 150
