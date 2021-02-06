from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VCC = 15
VBE_on=0.7
VCE_sat = 0.2
beta=50
R1=20e3

print('part(a)')
print('when RL=10kohm')

RL1=10e3
Vo_minus=-VCC+VCE_sat+VBE_on

Vo_plus1=(VCC-VBE_on)/(1+R1/(beta*RL1))

print('Vo-=%f (V)' % Vo_minus)
print('Vo+=%f (V)' % Vo_plus1)

print('when RL=2Kohm')

RL2=2e3
Vo_minus=-VCC+VCE_sat+VBE_on

Vo_plus2=(VCC-VBE_on)/(1+R1/(beta*RL2))

print('Vo-=%f (V)' % Vo_minus)
print('Vo+=%f (V)' % Vo_plus2)

print('part(b)')
print('when RL=10kohm')
Vo=Vo_plus1
PL=0.5*Vo**2/RL1
Isup=Vo/(pi*RL1)
Psup=2*VCC*Isup
eta_c=PL/Psup
PQ_avg=(Psup-PL)/2

print('PL=%f (mW)' % (PL*1e3))
print('eta_c=%f%%' % (eta_c*100))
print('PQ_avg=%f (mW)' % (PQ_avg*1e3))

print('when RL=2kohm')
Vo=Vo_plus2
PL=0.5*Vo**2/RL2
Isup=Vo/(pi*RL2)
Psup=2*VCC*Isup
eta_c=PL/Psup
PQ_avg=(Psup-PL)/2

print('PL=%f (mW)' % (PL*1e3))
print('eta_c=%f%%' % (eta_c*100))
print('PQ_avg=%f (mW)' % (PQ_avg*1e3))

# 122