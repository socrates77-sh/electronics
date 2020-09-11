from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
# from math import *

VT = 26e-3
Vbe_on = 0.7

VCC = 15
R1 = 20e3
R2 = 10e3

Iin = (VCC-Vbe_on)/R1

Iout = symbols('Iout', positive=True)

f = VT*log(Iin/Iout) - Iout*R2
sol = solve(f)

print(sol)
Iout_r = sol[0]

print('Iout=%f (uA)' % (Iout_r*1e6))

# 91
