from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
beta_n = 200
beta_p = 100
VBEon = 0.7
VCC = 6
R1 = 1.25e3
R2 = 10e3
R3 = 1e3
RE = 5e3
RL = 6e3

IC1 = VBEon/R1
IC2 = (VCC-VBEon)/RE-IC1
IC3 = VCC/RL

gm1 = gm2 = IC1/VT
# gm2 = IC2/VT
gm3 = IC3/VT
rpi1 = beta_n/gm1
# rpi2 = beta_n/gm2
rpi3 = beta_p/gm3

Rx1 = resp(R2, R3)
Rx2 = R2+R3
RE1 = Rx1/beta_n+1/gm2

a = gm1*gm3*resp(R1,rpi3)*resp(RL,Rx2)/(1+gm1*RE1)
f = R3/(R2+R3)

T = a*f
A = a/(1+a*f)
ria = rpi1*(1+gm1*RE1)
roa =resp(RL,Rx2)
Ri = ria*(1+T)
Ro = roa/(1+T)

print('T=%f' % T)
print('A=%f' % A)
print('Ri=%f (Mohm)' % (Ri*1e-6))
print('Ro=%f (ohm)' % Ro)


# 258
