from sympy import symbols, solve, nsolve, diff, log
from sympy.plotting import plot
from resp import *
# from math import *

VT = 26e-3
VA = 130
beta = 200
IS = 5e-15
Vbe_on = 0.7

VCC = 15
R1 = 13.7e3
R2 = 700

Iin = (VCC-2*Vbe_on)/R1

# Iout = symbols('Iout', positive=True)
Iout = symbols('Iout')
eq = 2*VT*log(Iin/IS)-VT*log(Iout/IS)-Iout*R2
sol = nsolve(eq, 1e-6)
Iout = sol

gm3=Iout/VT
ro3=VA/Iout

Rout=ro3*(1+gm3*R2/(1+gm3*R2/beta))

print('Iout=%f (mA)' % (Iout*1e3))
print('Rout=%f (Mohm)' % (Rout*1e-6))

# 93
