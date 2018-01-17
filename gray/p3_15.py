from resp import *
from numpy import log, sqrt

VT = 26e-3
ID = 100e-6
W = 10e-6
Ldrwn = 0.4e-6
Xd = 0.1e-6
un = 450e-4
eox = 3.9 * 8.854e-12
tox = 80e-10
dXd = 0.02e-6
Ld = 0.09e-6

Cox = eox / tox
Leff = Ldrwn - 2 * Ld - Xd
VA = Leff / dXd
ro = VA / ID
gm = sqrt(2 * ID * un * Cox * W / Leff)
a = gm * ro
Ro = gm * (a + 1) * ro * ro
print('Ro=%f (Mohm)' % (Ro * 1e-6))
