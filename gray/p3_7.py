from resp import *
from numpy import log, sqrt

ID = 100e-6
RD = 10e3
k = 200e-6
lam = 0.01
W = 100e-6
L = 1e-6

print('Part1')
gm = sqrt(2 * ID * k * W / L)
ro = 1 / (lam * ID)
Ri = (ro + RD) / (1 + gm * ro)
print('Ri=%f (ohm)' % Ri)

print('Part2')
RD = 1e6
Ri = (ro + RD) / (1 + gm * ro)
print('Ri=%f (ohm)' % Ri)
