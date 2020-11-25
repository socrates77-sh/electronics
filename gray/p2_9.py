from sympy import symbols, solve, nsolve, diff, exp, integrate, evalf
from sympy.plotting import plot
from resp import *
from math import pi

RB = 10e3
R_sheet = 100
Lch = 26e-6
d = 3e-6
Cj = 1e-1

W = symbols('W')

L = W*RB/R_sheet
A_bottom = W*L+2*Lch**2
P = 2*L+6*Lch+2*(Lch-W)
A_sidewall = 0.5*pi*d*P
C_total = Cj*(A_bottom+A_sidewall)

W1 = 6e-6
C1 = C_total.evalf(subs={W: W1})
print('C1=%f pF' % (C1*1e9))

W2 = 12e-6
C2 = C_total.evalf(subs={W: W2})
print('C2=%f pF' % (C2*1e9))

# 21
