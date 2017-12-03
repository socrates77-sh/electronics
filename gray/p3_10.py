from numpy import log, sqrt
from resp import *

VT = 26e-3
VBE = 0.7
R1 = 1e3
R2 = 50
VIN = 5
VCC = 10
beta = 200

Vo = VIN - VBE - VBE
Io = Vo / R2
Ix = VBE / R1
IE2 = Io - Ix
IB2 = IE2 / (1 + beta)
IE1 = IB2 + Ix
IC2 = IE2 * beta / (beta + 1)
IC1 = IE1 * beta / (beta + 1)

rpi2 = beta * VT / IC2
rpi2p = resp(rpi2, R1)
gm2 = IC2 / VT
Ri2 = rpi2p + (1 + gm2 * rpi2p) * R2

gm1 = IC1 / VT
rpi1 = beta / gm1
Ri = rpi1 + (1 + gm1 * rpi1) * Ri2
print('Ri=%f (Kohm)' % (Ri * 1e-3))

Av1 = 1 / (1 + rpi1 / ((1 + beta) * Ri2))
Av2 = 1 / (1 + rpi2p / ((1 + gm2 * rpi2p) * R2))
Av = Av1 * Av2
print('Av=%f' % Av)
