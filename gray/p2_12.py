from sympy import symbols, solve, nsolve, diff, exp, integrate, evalf
from sympy.plotting import plot
from resp import *
from math import pi

ID1 = 100
ID2 = 10
VGS1 = 1.5
VGS2 = 0.8

K, Vt = symbols('K, Vt')
eq1 = 0.5*K*(VGS1-Vt)**2-ID1
eq2 = 0.5*K*(VGS2-Vt)**2-ID2
sol = solve((eq1, eq2), K, Vt, dict=True)
K1 = sol[0][K]
Vt1 = sol[0][Vt]

print('un*Cox*W/L=%f uA/V' % K1)
print('Vt=%f V' % Vt1)


# 22
