from resp import *

VT = 26e-3
beta = 200
eta = 2e-4

IC = 250e-6
Rc = 20e3

gm = IC / VT
Ri = beta / gm
ro = 1 / (eta * gm)
Ro = resp(Rc, ro)

print('Gm=%f (mA/V)' % (gm * 1e3))
print('Ri=%f (Kohm)' % (Ri * 1e-3))
print('Ro=%f (Kohm)' % (Ro * 1e-3))
