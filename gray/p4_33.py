from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

un = 450e-4
eox = 3.9*8.86e-12
tox = 80e-10

M = 2e-3
n = 1.5
I = 200e-6
T0 = 25+273

Cox = eox/tox

W_L = symbols('W_L')
eq = n*(2*I/(un*Cox*W_L))**0.5/(2*T0)-M
W_L_r = nsolve(eq, 1)


print('W/L=%f' % W_L_r)

# 101
