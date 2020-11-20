from sympy import symbols, solve, nsolve, diff, exp, integrate
from sympy.plotting import plot
from resp import *
# from math import *

un = 800e-4
NA = 1e21
q = 1.6e-19
L = 0.5e-6
ND0 = 1e23

x = symbols('x')
ND = ND0*exp(-x/(L*1e6))
eq1 = ND-NA
xj = nsolve(eq1, 1, verify=False)*1e-6

ND = ND0*exp(-x/L)
R_sheet = 1/(q*un*integrate(ND-NA, (x, 0, xj)))
print(R_sheet)


print('R_sheet=%f ohm/sq' % R_sheet)

# 18
