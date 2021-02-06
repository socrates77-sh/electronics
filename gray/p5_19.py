from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VCC = 15
VBE_on=0.7
VCE_sat = 0.2
beta_pnp=30
beta_npn=150
IS_pnp=1e-15
IS_npn=1e-14
IC7=0.15e-3

print('part(a)')
Vo_plus=VCC-VCE_sat-VBE_on
Vo_minus=-VCC+VCE_sat+VBE_on

print('Vo-=%f (V)' % Vo_minus)
print('Vo+=%f (V)' % Vo_plus)

# print('part(b)')
# PQ=2*VCC*IC3
# print('PQ=%f (mW)' % (PQ*1e3))

# print('part(c)')
# RL=8
# Vo=-Vo_minus
# PL=0.5*Vo**2/RL
# Isup=Vo/(pi*RL)
# Psup=2*VCC*Isup
# eta_c=PL/Psup
# Ic = VCC/(2*RL)
# Vce = VCC-Ic*RL
# Pc = Vce*Ic

# print('PL=%f (W)' % PL)
# print('eta_c=%f%%' % (eta_c*100))
# print('Pc=%f (W)' % Pc)

# 124