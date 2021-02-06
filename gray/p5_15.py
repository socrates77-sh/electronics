from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VCC = 15
VBE_on=0.7
VCE_sat = 0.2
beta_pnp=50
beta_npn=200
IS=1e-14
IC13a=0.2e-3

print('part(a)')
print('when RL=1kohm')

RL1=1e3
Vo_minus=-VCC+VCE_sat+VBE_on+VBE_on

Vo_plus1=VCC-VCE_sat-VBE_on

print('Vo-=%f (V)' % Vo_minus)
print('Vo+=%f (V)' % Vo_plus1)

print('when RL=200ohm')
RL2=200
IC14=beta_npn*IC13a
Vo_plus2=IC14*RL2
print('Vo-=%f (V)' % Vo_minus)
print('Vo+=%f (V)' % Vo_plus2)

print('part(b)')
Vo=-Vo_minus
PL=0.5*Vo**2/RL1
Isup=Vo/(pi*RL1)
Psup=2*VCC*Isup
eta_c=PL/Psup
Ic = VCC/(2*RL1)
Vce = VCC-Ic*RL1
Pc = Vce*Ic

print('PL=%f (mW)' % (PL*1e3))
print('eta_c=%f%%' % (eta_c*100))
print('Pc=%f (mW)' % (Pc*1e3))

# 122