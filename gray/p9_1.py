# from sympy import symbols, solve, nsolve, diff, re, im, Abs, arg
# from sympy.plotting import plot
# from sympy.polys.partfrac import apart_full_decomposition
from resp import *
from math import *

import matplotlib.pyplot as plt
from sympy import init_printing
from numpy import arange
import sympy

A = 200
fb = 0.05
f1 = 1e6
f2 = 2e6
f3 = 4e6

# T_jf, f = symbols('T_jf f')

# T_jf = A*fb/((1+1j*f/f1)*(1+1j*f/f2)*(1+1j*f/f3))

# T1 = T_jf.evalf(subs={f: f1})
# T2 = T_jf.evalf(subs={f: f2})
# T3 = T_jf.evalf(subs={f: f3})

# print('T1=%f e ^ %f j' % (Abs(T1), arg(T1)*180/pi))
# print('T2=%f e ^ %f j' % (Abs(T2), arg(T2)*180/pi))
# print('T3=%f e ^ %f j' % (Abs(T3), arg(T3)*180/pi))

fx = [f1, f2, f3]
Tx = [A*fb/((1+1j*f/f1)*(1+1j*f/f2)*(1+1j*f/f3)) for f in fx]

for i in range(3):
    a = abs(Tx[i])
    p = atan(Tx[i].imag/Tx[i].real)*180/pi
    print('T%d=%f e ^ %f j' % (i, a, p))

fx = arange(-10e6, 10e6, 1e4)
Tx = [A*fb/((1+1j*f/f1)*(1+1j*f/f2)*(1+1j*f/f3)) for f in fx]
Tx_re = [T.real for T in Tx]
Tx_im = [T.imag for T in Tx]

# print(fx)
# print(Tx)
# print(Tx_re)
# print(Tx_im)

init_printing()
plt.rc('figure', figsize=(8, 6))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid()

ax.plot(Tx_re, Tx_im, 'b')

ax.set_xlim(-10, 10)
ax.set_xlabel('Re')
ax.set_ylabel('Im')

plt.show()

# 286
