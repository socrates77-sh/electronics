from resp import *
from numpy import log, sqrt

VT = 26e-3
I1 = 200e-6
I2 = 100e-6
W1 = 30e-6
W2 = 10e-6
Ldrwn = 0.4e-6
Xd = 0.1e-6
un = 450e-4
up = 150e-4
eox = 3.9 * 8.854e-12
tox = 80e-10
dXd = 0.04e-6
Ld = 0.09e-6

ID1 = I2
ID2 = I1 - ID1
Cox = eox / tox
Leff = Ldrwn - 2 * Ld - Xd
VA = Leff / dXd
ro1 = VA / ID1
gm1 = sqrt(2 * ID1 * up * Cox * W1 / Leff)
gm2 = sqrt(2 * ID2 * un * Cox * W2 / Leff)
Gm = -gm1 * ro1 * gm2
# print(Leff, VA, ro1, gm1, gm2)
print('Gm=%f (mA/V)' % (Gm * 1e3))
