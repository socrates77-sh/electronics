from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

Rs = 10e3
RL = 1e3
ID = 0.5e-3
W = 100e-6
Ldrwn = 2e-6
Ld = 0.2e-6
kn = 60e-6
Cox = 0.7e-3
Cgd = 14e-15

L = Ldrwn-2*Ld
gm = (2*kn*W*ID/L)**0.5
Cgs = 2*W*L*Cox/3+W*Ld*Cox

Av0 = gm*RL/(1+gm*RL)
z1 = -gm/Cgs
R1 = (Rs+RL)/(1+gm*RL)
p1 = -1/(Cgs*R1)

print(Av0, z1, p1)

s, B1 = symbols('s B1')
B10 = Av0*(1-s/z1)/(1-s/p1)
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
f = np.logspace(3, 12, num=100)
mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)
plt.show()

# 194
