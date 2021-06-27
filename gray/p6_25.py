from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
# from math import *

VT = 26e-3
Vbe_on = 0.7
VCC = 10
VEE = 10

IREF = (VCC+VEE-2*Vbe_on)/39e3

I1 = symbols('I1')
eq = VT*log(IREF/I1)-5e3*I1
# eq = log(5/I1) - I1
I1_r = nsolve(eq, 1e-6, verfiy=False)

IC1 = IC2 = 0.5*I1_r

print('IC1=IC2=%f (uA)' % (IC1*1e6))

# 172
