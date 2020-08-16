from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
VA2 = 130
VA4 = 50
I_tail = 100e-6

IC = I_tail/2
gm = IC/VT

ro2 = VA2/IC
ro4 = VA4/IC

Rout = resp(ro2, ro4)
Av = gm*Rout

print('Rout=%f (Kohm)' % (Rout*1e-3))
print('Av=%f' % Av)
