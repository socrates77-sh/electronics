from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

ID = 100e-6
Vov = 0.3
lam = 0.03
a = 1000


gm1 = gm2 = 2*ID/Vov
ro1 = ro2 = 1/(lam*ID)

Rout_0 = gm2*ro1*ro2+ro1
Rout_short = a*gm2*resp(ro1, ro2)/(1+gm2*resp(ro1, ro2))
Rout_open = 0
Ro = Rout_0*(1+Rout_short)/(1+Rout_open)

Av = -gm1*Ro

print('Ro=%f (Gohm)' % (Ro*1e-9))
print('Av=%f' % Av)

# 276
