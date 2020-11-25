# from sympy import symbols, solve, nsolve, diff, exp, integrate, evalf
from sympy.plotting import plot
from resp import *
from math import pi, log, sqrt

epi = 1.04e-10
eox = 3.9*8.86e-12
tox = 400e-10
q = 1.6e-19
NA = 2.1e22
un = 700e-4
Ld = 0.3e-6
VDS = 5
Ldrwn1 = 7e-6
W1 = 100e-6
ID1 = 10e-6
ro1 = 5e6

Ldrwn2 = 12e-6
W2 = 50e-6
ID2 = 30e-6

Cox = eox/tox

L1 = Ldrwn1-2*Ld
Vov1 = sqrt(2*ID1/(un*Cox*W1/L1))
Xd1 = sqrt(2*epi*(VDS-Vov1)/(q*NA))
Leff1 = L1-Xd1
dXd = Leff1/(ID1*ro1)

L2 = Ldrwn2-2*Ld
Vov2 = sqrt(2*ID2/(un*Cox*W2/L2))
Xd2 = sqrt(2*epi*(VDS-Vov2)/(q*NA))
Leff2 = L2-Xd2
ro2 = Leff2/(ID2*dXd)

print('ro2=%f Mohm' % (ro2*1e-6))


# 23
