from resp import *
from numpy import log, sqrt

VT = 26e-3
ID1 = 250e-6
ID2 = 250e-6
WL = 100
kn = 90e-6
lamb = 0.1
chi = 0.1

gm1 = sqrt(2 * ID1 * kn * WL)

gm2 = sqrt(2 * ID2 * kn * WL)
gmb2 = chi * gm2
ro1 = 1 / (lamb * ID1)
ro2 = 1 / (lamb * ID2)
Ro = (gm2 + gmb2) * ro1 * ro2
print('Ro=%f (Mohm)' % (Ro * 1e-6))

Gm = gm1
print('Gm=%f (mA/V)' % (Gm * 1e3))

Av = -Gm * Ro
print('Av=%f' % Av)
