from resp import *
from numpy import log, sqrt, log10

VT = 26e-3
ITAIL = 20e-6
RTAIL = 10e6
RC = 100e3
RE = 4e3
VEE = 5
VCC = 5
beta = 200

gm = (ITAIL / 2) / VT
rpi = beta / gm
Adm = -gm * RC / (1 + gm * RE)
Acm = -gm * RC / (1 + gm * (RE + 2 * RTAIL))

CMRR = 20 * log10(Adm / Acm)

print('Adm=%f' % Adm)
print('Acm=%f' % Acm)
print('CMRR=%f (db)' % CMRR)
