from sympy import symbols, solve, nsolve, diff, exp, integrate
from sympy.plotting import plot
from resp import *
from math import pi

q = 1.6e-19
Dp=10e-4
WB=8e-6
ND=1.2e22
A=120e-6*3e-6*pi/2

IC=q*A*ND*Dp/WB

print('IC=%f uA' % (IC*1e6))

# 20
