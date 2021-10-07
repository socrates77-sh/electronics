from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

R = 20e3
C = 50e-12
Cin = 0.2e-12
av = 1000
Ro = 5e3

Rc0 = Ro+R+av*R

T0 = C*Rc0+Cin*R
p1 = -1/T0

Rcins=resp(R,Ro/(1+av))
t1 = Cin*Rcins
t2 = C*Ro
p2 = -(1/t1+1/t2)

print('p1=%f (rad/s)' % p1)
print('p2=%f (rad/s)' % p2)

# 248
