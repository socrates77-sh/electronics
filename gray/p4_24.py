from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
# from math import *

VT = 26e-3
It = 0.1e-6
n = 1.5
Iout = 0.1e-6

print('Part (a)')
Iin = 1e-6

R = symbols('R')
f = log(Iin/Iout)-Iin*R/(n*VT)
sol = solve(f)
R_r = sol[0]
W_L = Iin/It

print('R=%f (Kohm)' % (R_r*1e-3))
print('W/L>%f' % W_L)


print('Part (b)')
R = 10e3

Iin = symbols('Iin')
f = log(Iin/Iout)-Iin*R/(n*VT)
sol = solve(f)
Iin_r = sol[1]
W_L = Iin_r/It

print('Iin=%f (uA)' % (Iin_r*1e6))
print('W/L>%f' % W_L)

# 93
