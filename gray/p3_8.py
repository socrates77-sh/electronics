from resp import *
from numpy import log, sqrt

VT = 26e-3
RS = 5e3
RL = 500
IC = 1e-3
beta = 200

rpi = beta * VT / IC
Ri = rpi + (beta + 1) * RL
Ro = resp((RS + rpi) / (beta + 1), RL)
Av = 1 / (1 + (RS + rpi) / ((beta + 1) * RL))

print('Ri=%f (Kohm)' % (Ri * 1e-3))
print('Ro=%f (ohm)' % Ro)
print('vo/vs=%f' % Av)
