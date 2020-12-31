from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

R3 = 5e3
Vce_on = 0.2
Vbe_on = 0.7
VCC = 15

IQ = (VCC-Vbe_on)/R3

print('Part (b)')
print('=== for RL=2Kohm ===')

RL1 = 2e3

Vom = IQ*RL1
Iom = IQ
PL_max1 = 0.5*Vom*Iom
print('PL|max = %f (mW)' % (PL_max1*1e3))

print('=== for RL=10Kohm ===')

RL2 = 10e3

Vom = VCC-Vce_on
Iom = Vom/RL2
PL_max2 = 0.5*Vom*Iom
print('PL|max = %f (mW)' % (PL_max2*1e3))

print('Part (c)')
print('=== for RL=2Kohm ===')
Psup = 2*VCC*IQ

eta_c1 = PL_max1/Psup
print('eta_c = %f %%' % (eta_c1*100))

print('=== for RL=10Kohm ===')
eta_c2 = PL_max2/Psup
print('eta_c = %f %%' % (eta_c2*100))

print('Part (d')
RL = (VCC-Vce_on)/IQ
Vom = IQ*RL
Iom = IQ
PL_max3 = 0.5*Vom*Iom
print('RL = %f (Kohm)' % (RL*1e-3))
print('PL|max = %f (mW)' % (PL_max3*1e3))

# 110
