from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
VA = 130
beta0 = 200
Vbe_on = 0.7

VCC = 30
R1 = 30e3
Iout = 5e-6

IC2 = Iout

Iin = (VCC-Vbe_on)/R1
R2 = (VT/Iout)*log(Iin/Iout)

ro2 = VA/IC2
gm2 = IC2/VT
rpi2 = beta0/gm2
Ro = ro2*(1+gm2*resp(rpi2, R2))

print('R2=%f (Kohm)' % (R2*1e-3))
print('Ro=%f (Mohm)' % (Ro*1e-6))

# 91
