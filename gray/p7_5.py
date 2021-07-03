# from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

Rs = 10e3
RL = 5e3
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

Cx = gm*Rs*Cgd
Rx = (1+Cgs/Cgd)/gm
# print(Cx, Rx)
print(Cx, Rx, Cgd)


s, B1 = symbols('s B1')
# B1 = resp(1/(Cu*s), 1/gm*(1/(R*Cu*s)+Cpi/Cu+1))
Z1 = 1/(Cgd*s)
Z2 = 1/(Cx*s)+Rx
B10 = Z1*Z2/(Z1+Z2)
# B1=(1+s*Rx*Cx)/(s*(Cx+Cu)+s*s*Rx*Cx*Cu)
B1 = simplify(B10)
# print(B1)
# B1 = 25 * s / (2 * s**2 + 3 * s + 3)
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


# 186
