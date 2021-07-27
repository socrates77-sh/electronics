from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
Rs = 10e3
RL = 5e3
IC = 1e-3
beta = 200
fT = 600e6
Cu = 0.2e-12
Cje = 2e-12
Ccs = 1e-12

gm = IC/VT
rpi = beta/gm

Av0 = -gm*RL*(rpi/(Rs+rpi))
Rpi0 = resp(rpi, Rs)
Ru0 = Rpi0+RL+gm*RL*Rpi0
Rcs0 = RL
Cpi = gm/(2*pi*fT)-Cu
T0 = Rpi0*Cpi+Ru0*Cu+Rcs0*Ccs

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (MHz)' % (f_3db*1e-6))

# 200
