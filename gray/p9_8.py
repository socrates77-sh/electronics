# from sympy import symbols, solve, nsolve, diff, re, im, Abs, arg
# from sympy.plotting import plot
# from sympy.polys.partfrac import apart_full_decomposition
from scipy.sparse.extract import find
from resp import *


import matplotlib.pyplot as plt
from sympy import init_printing
import numpy as np
from sympy import *
from control import *
from math import *


a0 = 1e5
f1 = 5
f = 0.01
R0 = 100

w1 = 2*pi*f1

R1, R2, L = symbols('R1 R2 L')
f1 = R1*R2/(R1+R2)-R0/(1+a0*f)
f2 = L/R1-1/w1
f3 = L/(R1+R2)-1/((1+a0*f)*w1)
# sol = solve((f1, f2, f3), R1, R2, L)
sol = solve((f1, f2, f3))

R1_r = sol[0][R1]
R2_r = sol[0][R2]
L_r = sol[0][L]

print('R1=%f (ohm)' % R1_r)
print('R2=%f (ohm)' % R2_r)
print('L=%f (mH)' % (L_r*1e3))

s=symbols('s')
Zo=R0/(1+a0*f)*(1+s/w1)/(1+s/((1+a0*f)*w1))
D0 = denom(Zo)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(Zo)
N1 = Poly(N0).all_coeffs()
N2 = [float(k) for k in N1]
# N2 = [float(N0)]
B1b = tf(N2, D2)

f = np.logspace(3, 10, num=1000)
# mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)
mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)

print(B1b)

plt.show()

# 288
