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


def search_phase(data, target):
    delta = 1e6
    idx = 0
    for i in range(len(data)):
        new_delta = abs(data[i]-target)
        if new_delta < delta:
            delta = new_delta
            idx = i
    return idx


A = 200
fb = 0.05
f1 = 1e6
f2 = 2e6
f3 = 4e6

s, B1 = symbols('s B1')
B1 = 200/((1+s/(2*pi*f1))*(1+s/(2*pi*f2))*(1+s/(2*pi*f3)))

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
# mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)
mag, phase, omega = bode(B1b, dB=True, Hz=True, omega=f)
# plt.show()

G_0 = 20*log10(mag[0])
idx_180 = search_phase(phase, -pi)
f_180 = omega[idx_180]/(2*pi)
G_180 = 20*log10(mag[idx_180])

print('G(w=0)=%f (db)' % G_0)
print('G(w=-180)=%f (db)' % G_180)
print('f(w=-180)=%f (MHz)' % (f_180*1e-6))

idx_120 = search_phase(phase, -120/180*pi)
f_120 = omega[idx_120]/(2*pi)
G_120 = 20*log10(mag[idx_120])

print('G(w=-120)=%f (db)' % G_120)
print('f(w=-120)=%f (MHz)' % (f_120*1e-6))

x = 10**(-G_120/20)
print(x)

print(len(omega))

plt.show()

# 286
