from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
VA4 = 130
VA6 = 50
beta4 = 200
beta6 = 50

IC = symbols('IC')

ro4 = VA4/IC
ro6 = VA6/IC

Ro1 = 0.5*beta6*ro6
Ro2 = beta4*ro4

Rout = resp(Ro1, Ro2)

gm = IC/VT

Av= gm*Rout

print('Av=%f' % Av)

# 83
