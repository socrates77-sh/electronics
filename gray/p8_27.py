from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

Ri = 1e6
Ro = 10e3
av = 200
Rs = 10e3
RF = 100e3


R = av*resp(Ri, Rs)/(Ro+RF+resp(Ri, Rs))
A_inf = -RF/Rs
d = resp(Ri, RF+Ro)*Ro/((Rs+resp(Ri, RF+Ro))*(RF+Ro))
A = A_inf*R/(1+R)+d/(1+R)

Ri_0 = Rs+resp(Ri, RF+Ro)
Rin_short = R
Rin_open = av*Ri/(Ro+RF+Ri)
Ri = Ri_0*(1+Rin_short)/(1+Rin_open)

Ro_0 = resp(Ro, RF+resp(Ri, Rs))
Rout_short = 0
Rout_open = R
Ro = Ro_0*(1+Rout_short)/(1+Rout_open)

print('R=%f' % R)
print('A=%f' % A)
print('Ri=%f (ohm)' % Ri)
print('Ro=%f (ohm)' % Ro)

# 277
