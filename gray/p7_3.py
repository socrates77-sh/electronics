# from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

VT = 26e-3
Rs = 5e3
RL = 3e3
rb = 300
IC = 0.5e-3
beta = 200
fT = 500e6
Cu = 0.3e-12

gm = IC/VT
rpi = beta/gm
Cpi = gm/(2*3.1416*fT)-Cu
R = resp(Rs+rb, rpi)
Cx = gm*R*Cu
Rx = (1+Cpi/Cu)/gm
# print(Cx, Rx)


s, B1 = symbols('s B1')
# B1 = resp(1/(Cu*s), 1/gm*(1/(R*Cu*s)+Cpi/Cu+1))
Z1 = 1/(Cu*s)
Z2 = 1/(gm*R*Cu*s)+(1+Cpi/Cu)/gm
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

# print(D0)
# print(N0)
# print(D2)
# print(N2)
print(B1b)
f = np.logspace(0, 13, num=100)
mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)
print(np.logspace(0, 10, num=100))
# bode(B1b, omega=(1e5, 1e10), Hz=True,  dB=False)f
# print(mag)
# print(omega)

plt.show()


# 186
