from resp import *

VT = 26e-3
beta = 200
eta = 2e-4
IC1 = 250e-6
IC2 = 250e-6

gm1 = IC1 / VT
rpi1 = beta / gm1
Ri = rpi1
print('Ri=%f (Kohm)' % (Ri * 1e-3))

gm2 = IC2 / VT
ro2 = 1 / (eta * gm2)
Ro = beta * ro2
print('Ro=%f (Mohm)' % (Ro * 1e-6))

Gm = gm1
print('Gm=%f (mA/V)' % (Gm * 1e3))

Av = -Gm * Ro
print('Av=%f' % Av)
