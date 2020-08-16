from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
VA2 = 130
VA4 = 50
beta4 = 50
I_tail = 100e-6
Re = 2e3

IC = I_tail/2
gm = IC/VT

ro2 = VA2/IC
ro4 = VA4/IC

rpi4 = beta4/gm
Ro4 = ro4*(1+gm*resp(Re, rpi4+Re))

Rout = resp(ro2, Ro4)
Av = gm*Rout

print('Rout=%f (Kohm)' % (Rout*1e-3))
print('Av=%f' % Av)

#76