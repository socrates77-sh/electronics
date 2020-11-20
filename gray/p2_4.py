from sympy import symbols, solve, nsolve, diff, exp, integrate
from sympy.plotting import plot
from resp import *
# from math import *

L = 200
W = 5

R_sheet_base = 100
R_sheet_emitter = 5
R_sheet_pinch = 5000

R_base = R_sheet_base*L/W
R_emitter = R_sheet_emitter*L/W
R_pinch = R_sheet_pinch*L/W

print('R_base=%f Kohm' % (R_base*1e-3))
print('R_emitter=%f ohm' % R_emitter)
print('R_pinch=%f Kohm' % (R_pinch*1e-3))

# 18
