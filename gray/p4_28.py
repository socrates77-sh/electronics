from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
IS = 5e-15
I1 = 200e-6
Vout = 1.262

R1, R2, R3 = symbols('R1 R2 R3')

Vbe1 = VT*log(I1/IS)
eq1 = Vbe1+I1*R1-Vout
R1_r = nsolve(eq1, 1)

Vbe2 = Vbe1-0.1
I2 = IS*exp(Vbe2/VT)
eq2 = Vbe1+I2*R2-Vout
R2_r = nsolve(eq2, 1)

eq3 = Vbe1+R2_r*(Vbe1-Vbe2)/R3-Vout
R3_r = nsolve(eq3, 1, verify=False)

print('R1=%f (Kohm)' % (R1_r*1e-3))
print('R2=%f (Kohm)' % (R2_r*1e-3))
print('R3=%f (Kohm)' % (R3_r*1e-3))

# 95
