# from sympy import symbols, solve, nsolve, diff, exp, integrate, evalf
from sympy.plotting import plot
from resp import *
from math import pi, log, sqrt

Ydf = 0.9
Yft = 0.8
Cw = 100
Cp = 0.6

NYws1 = 47
C1 = Cw/(NYws1*Ydf*Yft)+Cp/Yft

NYws2 = 200
C2 = 2*Cw/(NYws2*Ydf*Yft)+Cp/Yft

print('C1=$ %f' % C1)
print('C2=$ %f' % C2)


# 28
