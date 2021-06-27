# from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
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
Cpi = gm/(2*pi*fT)-Cu
# CM = (1+gm*RL)*Cu
# f_3db = 1/(2*pi*resp(Rs+rb, rpi)*(CM+Cpi))

# R=resp(Rs+rb, rpi)
# p2=-(1/(RL*Cu)+1/(R*Cpi)+1/(RL*Cpi)+gm/Cpi)/(2*pi)

# print('f-3db=%f (MHz)' % (f_3db*1e-6))
# print('p2=%f (MHz)' % (p2*1e-6))
R = resp(Rs+rb, rpi)
Cx = gm*R*Cu
Rx = (1+Cpi/Cu)/gm
# print(Cx, Rx)


s, B1 = symbols('s B1')
# B1 = resp(1/(Cu*s), 1/gm*(1/(R*Cu*s)+Cpi/Cu+1))
Z1=1/(Cu*s)
Z2=1/(gm*R*Cu*s)+(1+Cpi/Cu)/gm
B1=Z1*Z2/(Z1+Z2)

# B1 = 25 * s / (2 * s**2 + 3 * s + 3)
# print(B1)
D0 = denom(B1)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(B1)
N1 = Poly(N0).all_coeffs()
N2 = [float(k) for k in N1]
B1b = tf(N2, D2)
bode(B1b, dB=True)
plt.show()


# 186
