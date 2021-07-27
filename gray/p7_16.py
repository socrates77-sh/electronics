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
RF = 30e3

gm = IC/VT
rpi = beta/gm

k = (1/RF-gm)/(1/RF+1/RL)
R1 = RF/(1-k)

Av0 = k*resp(rpi, R1)/(resp(rpi, R1)+Rs)

Rpi0 = resp(Rs, rpi, R1)

Rpi0_1 = resp(rpi, Rs)
Ru0_1 = Rpi0_1+RL+gm*RL*Rpi0_1
Ru0 = resp(Ru0_1, RF)

RA = resp(Rs, rpi)
Rcs0 = (RA+RF)/(RA*(1/RA+gm))

Cpi = gm/(2*pi*fT)-Cu
T0 = Rpi0*Cpi+Ru0*Cu+Rcs0*Ccs

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (MHz)' % (f_3db*1e-6))

# 201
