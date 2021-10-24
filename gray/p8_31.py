from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from sympy.polys.partfrac import apart_full_decomposition
from resp import *
from math import *

VT = 26e-3
IC = 0.5e-3
beta = 100
VA = 50
Ri = 1e6
Ro = 10e3
av = 1000

gm = IC/VT
rpi = beta/gm
ro = VA/IC

print(gm, rpi, ro)


print('='*10)
print('Part (a)')
print('='*10)

a = av*gm*(rpi*resp(ro, Ro+rpi)/(Ro+rpi)) / \
    (1+gm*(rpi*resp(ro, Ro+rpi)/(Ro+rpi)))
f = 1
T = a*f
A = a/(1+T)
ria = Ri
roa = (Ro+rpi)/(beta+1)
Rin = ria*(1+T)
Rout = roa/(1+T)

print('T=%f' % T)
print('A=%f' % A)
print('Rin=%f (Mohm)' % (Rin*1e-6))
print('Rout=%f (ohm)' % Rout)

print('='*10)
print('Part (b)')
print('='*10)

R = av*gm*(rpi*resp(ro, Ro+rpi, Ri)/(Ro+rpi)) / \
    (1+gm*(rpi*resp(ro, Ro+rpi, Ri)/(Ro+rpi)))
A_inf = 1
d = (Ro+rpi)/((beta+1)*Ri)
A = A_inf*R/(1+R)+d/(1+R)

Ri_0 = Ri
Rin_short = R
Rin_open = 0
Ri = Ri_0*(1+Rin_short)/(1+Rin_open)

Ro_0 = roa
Rout_short = 0
Rout_open = R
Ro = Ro_0*(1+Rout_short)/(1+Rout_open)

print('A=%f' % A)
print('Rin=%f (Mohm)' % (Rin*1e-6))
print('Rout=%f (ohm)' % Rout)

# 281
