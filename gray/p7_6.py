from sympy import symbols, solve, nsolve, diff
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
RT = 300e3
CT = 2e-12

gm = IC/VT
rpi = beta/gm
Cpi = gm/(2*3.1416*fT)-Cu
CM = (1+gm*RL)*Cu
p1 = 1/(resp(Rs+rb, rpi)*(CM+Cpi))
print(p1, gm, rpi)


s, B1 = symbols('s B1')
B1 = -RL*(1+s*RT*CT)/(2*RT)
B1_cm = B1

# D0 = denom(B1)
# D1 = Poly(D0).all_coeffs()
# D2 = [float(k) for k in D1]
N0 = numer(B1)
N1 = Poly(N0).all_coeffs()
N2 = [float(k) for k in N1]
B1b = tf(N2, 1)

print(B1b)

f = np.logspace(3, 10, num=100)
mag, phase, omega = bode(B1b, dB=True, Hz=True, omega=f)

plt.show()

Av0 = -gm*RL*rpi/(Rs+rb+rpi)
B1 = Av0/(1-s/p1)
B1_dm = B1

D0 = denom(B1)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(B1)
# N1 = Poly(N0).all_coeffs()
# N2 = [float(k) for k in N1]
N2 = [float(N0)]
B1b = tf(N2, D2)

print(B1b)

f = np.logspace(3, 10, num=100)
mag, phase, omega = bode(B1b, dB=True, Hz=True, omega=f)
plt.show()

B10=B1_dm/B1_cm
B1=simplify(B10)
print(B1)

D0 = denom(B1)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(B1)
# N1 = Poly(N0).all_coeffs()
# N2 = [float(k) for k in N1]
N2 = [float(N0)]
B1b = tf(N2, D2)
print(B1b)

f = np.logspace(3, 10, num=100)
mag, phase, omega = bode(B1b, dB=True, Hz=True, omega=f)
plt.show()

# 188
