from sympy import symbols, solve, diff, log
from sympy.plotting import plot

IS = 5e-15
VA = 130
VBE = 0.65
bf = 200
VT = 26e-3

VCC = 5
R = 10e3

IC = (VCC-2*VBE)/R
ro = VA/IC
gm = IC/VT
Ro = 0.5*ro*(1+gm*ro/(1+gm*ro/bf))

print('Rout=%f (Mohm)' % (Ro*1e-6))

# 58
