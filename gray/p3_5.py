from resp import *

VT = 26e-3

IC = 250e-6
Rc = 10e3

gm = IC / VT
Ri = 1/gm
Ro = Rc

print('Gm=%f (mA/V)' % (gm * 1e3))
print('Ri=%f (Kohm)' % (Ri * 1e-3))
print('Ro=%f (Kohm)' % (Ro * 1e-3))
