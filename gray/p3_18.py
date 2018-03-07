from resp import *
from numpy import log, sqrt, log10

VT = 26e-3
ITAIL = 20e-6
RTAIL = 10e6
RC = 100e3
VEE = 5
VCC = 5
beta = 200

gm = (ITAIL / 2) / VT
rpi = beta / gm
Adm = -gm * RC
Acm = -gm * RC / (1 + 2 * gm * RTAIL)
Rid = 2 * rpi
Ric = rpi + 2 * RTAIL * (beta + 1)

CMRR = 20 * log10(Adm / Acm)

print('Adm=%f' % Adm)
print('Acm=%f' % Acm)
print('Rid=%f (Mohm)' % (Rid * 1e-6))
print('Ric=%f (Mohm)' % (Ric * 1e-6))
print('CMRR=%f (db)' % CMRR)
