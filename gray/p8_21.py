from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

Vo=10
VR=6.8
roa=93
a=3054

T=a*VR/Vo
Ro=roa/(1+T)

print('T=%f' % T)
print('Ro=%f' % Ro)

# 269
