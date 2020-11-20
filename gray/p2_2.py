from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

rho = 1e-2
T = 5e-6

R_sheet = rho/T

print('R_sheet=%f ohm/sq' % R_sheet)

# 18
