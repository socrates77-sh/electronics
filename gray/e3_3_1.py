from resp import *

VT = 26e-3

b0 = 100
IC = 100e-6
RC = 5e3

gm = IC / VT
Ri = b0 / gm
Ro = RC
av = -gm * RC
ai = b0

print('(a)')
print('Ri=%f (kohm)' % (Ri * 1e-3))
print('Ro=%f (kohm)' % (Ro * 1e-3))
print('av=%f' % av)
print('ai=%f' % ai)

RL = 10e3
RS = 20e3
av = -gm * (Ri / (RS + Ri)) * resp(Ro, RL)

print('(b)')
print('av=%f' % av)
