from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VCC = 12
RL = 1e3
VCE_sat = 0.2

PL_max = (VCC-VCE_sat)**2/(2*RL)
eta = pi*(VCC-VCE_sat)/(4*VCC)

Ic = VCC/(2*RL)
Vce = VCC-Ic*RL
Pc = Vce*Ic

print('PL|max=%f (mW)' % (PL_max*1e3))
print('eta=%f%%' % (eta*100))
print('Pc=%f (mW)' % (Pc*1e3))

# 120
