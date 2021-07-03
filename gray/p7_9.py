from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

VT = 26e-3
Rs = 250
RE = 4e3
rb = 200
IC = 0.3e-3
beta = 50
fT = 4e6

gm = IC/VT
rpi = beta/gm

Av0 = (gm*RE+RE/rpi)/(1+gm*RE+(Rs+rb+RE)/rpi)
wT = 2*3.1416*fT
z1 = -wT
Cpi = gm/wT

Ci = Cpi/(1+gm*RE)
Ri = (1+gm*RE)*rpi
print(Ci, Ri)

s, B1 = symbols('s B1')
B10 = rb+RE+resp(Ri, 1/(s*Ci))
B1 = simplify(B10)
print(B1)
D0 = denom(B1)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(B1)
N1 = Poly(N0).all_coeffs()
N2 = [float(k) for k in N1]
B1b = tf(N2, D2)

print(B1b)
f = np.logspace(3, 10, num=100)
mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)
plt.show()

R2 = Rs+rb
R1 = 1/gm+R2/beta
L = Cpi*rpi*R2/beta
print(R1, R2, L)

B10 = resp(R2, R1+s*L)
B1 = simplify(B10)
print(B1)
D0 = denom(B1)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(B1)
N1 = Poly(N0).all_coeffs()
N2 = [float(k) for k in N1]
B1b = tf(N2, D2)

print(B1b)
f = np.logspace(3, 10, num=100)
mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)
plt.show()

# 192
