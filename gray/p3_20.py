from resp import *
from numpy import log, sqrt, log10

VT = 26e-3
RTAIL = 10e3
RC = 10e3
VEE = 15
VCC = 15
beta = 200

IC = 0.5 * (VEE - 0.7) / RTAIL

gm = IC / VT
rpi = beta / gm
Adm = -gm * RC
Acm = -gm * RC / (1 + gm * 2 * RTAIL)

Av = 0.5 * (Acm - Adm)
Ri = 2*rpi
Ro = RC

print('Av=%f' % Av)
print('Ri=%f (Kohm)' % (Ri*1e-3))
print('Ro=%f (Kohm)' % (Ro*1e-3))
