from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

RF = 100e3
RL = 10e3
Ri = 500e3
Ro = 200
av = 75000

print('='*10)
print('Part (a)')
print('='*10)

f = -1/RF
R1 = resp(RF, RL)
a = -R1*av*Ri*RF/((R1+Ro)*(Ri+RF))
zia = resp(RF, Ri)
zoa = resp(Ro, RF, RL)
T = a*f
Zi = zia/(1+T)
Zo = zoa/(1+T)
A = a/(1+a*f)

print('T=%f' % T)
print('A=%f (Kohm)' % (A*1e-3))
print('Zi=%f (ohm)' % Zi)
print('Zo=%f (ohm)' % Zo)

print('='*10)
print('Part (b)')
print('='*10)

R = resp(RL, RF+Ri)*Ri*av/((Ri+RF)*(Ro+resp(RL, RF+Ri)))
A_inf = -RF
d = Ri*resp(Ro, RL)/(Ri+RF+resp(Ro, RL))
A = A_inf*R/(1+R)+d/(1+R)

Zi_0 = resp(Ri, RF+resp(Ro, RL))
Rin_short = 0
Rin_open = R
Zi = Zi_0*(1+Rin_short)/(1+Rin_open)

Zo_0 = resp(RL, Ro, RF+Ri)
Rout_short = 0
Rout_open = R
Zo = Zo_0*(1+Rout_short)/(1+Rout_open)

print('A=%f (Kohm)' % (A*1e-3))
print('Zi=%f (ohm)' % Zi)
print('Zo=%f (ohm)' % Zo)

# 252
