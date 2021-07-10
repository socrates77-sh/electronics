from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

Rs = 1e6
gm = 0.3e-3
Cgs = 100e-15

R1 = 1/gm
R2 = Rs
L = Rs*Cgs/gm

print(R1, R2, L)

s, B1 = symbols('s B1')
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
f = np.logspace(3, 11, num=100)
mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)
plt.show()

# 199
