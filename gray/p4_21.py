from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
# from math import *

VT = 26e-3
VA = 130
beta0 = 200
Vbe_on = 0.7

VCC = 30
Iout = 5e-6

IC2 = Iout

R1, R2 = symbols('R1 R2', positive=True)
Iin = (VCC-Vbe_on)/R1
R2 = (VT/Iout)*log(Iin/Iout)
f = R1+R2
df = diff(f, R1)
sol = solve(df)
R1_r = sol[0]
R2_r = R2.evalf(subs={R1: R1_r})

print('R1=%f (Kohm)' % (R1_r*1e-3))
print('R2=%f (Kohm)' % (R2_r*1e-3))


# 91
