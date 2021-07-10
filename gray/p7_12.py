from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

VT = 26e-3
rb = 200
IC = 0.5e-3
beta = 100
Cu = 0.3e-12
Cpi = 10e-12

gm = IC/VT
rpi = beta/gm
Ai0 = beta/(1+beta)
k1 = Cpi/gm
f_3db = 1/(2*3.1416*k1)

print('f-3db=%f (MHz)' % (f_3db*1e-6))

R2 = rb
R1 = 1/gm+R2/beta
L = Cpi*rpi*R2/beta
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
f = np.logspace(5, 11, num=100)
mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)
plt.show()

# 199
