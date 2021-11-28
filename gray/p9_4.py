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


def search_mag(data, target):
    delta = 1e20
    idx = 0
    for i in range(len(data)):
        new_delta = abs(data[i]-target)
        if new_delta < delta:
            delta = new_delta
            idx = i
    return idx


G0 = 40000
f1 = 2e3
f2 = 200e3
f3 = 4e6

A0 = 100

s, B1 = symbols('s B1')
B1 = (G0/A0)/((1+s/(2*pi*f1))*(1+s/(2*pi*f2))*(1+s/(2*pi*f3)))

D0 = denom(B1)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(B1)
# N1 = Poly(N0).all_coeffs()
# N2 = [float(k) for k in N1]
N2 = [float(N0)]
B1b = tf(N2, D2)

print(B1b)
f = np.logspace(3, 10, num=1000)
# mag, phase, omega = bode(B1b, dB=False, Hz=True, omega=f)
mag, phase, omega = bode(B1b, dB=True, Hz=True, omega=f)
# plt.show()

idx = search_mag(mag, 1)
print(mag[idx])
print(omega[idx]/(2*pi))
print(phase[idx]*180/pi)


plt.show()

# 286
