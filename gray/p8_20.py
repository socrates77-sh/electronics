from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
beta = 100
VCC = 6
R1 = 2.4e3
R2 = 1.1e3
R3 = 640
R4 = 10e3
R5 = 300
R6 = 1.4e3
R7 = 300
R8 = R0 = 400
RF = 7e3
RL = 2e3
VBE_on = 0.6

IC8 = (2*VCC-VBE_on)/(R4+R6)
IC7 = IC8*R6/R5
IC1 = IC2 = 1/2*IC7
IC9 = IC7
IC3 = IC4 = 1/2*IC9
IC10 = IC11 = IC8*R6/R8
VC3 = VC4 = VCC-IC3*R2
VE5 = VC4-VBE_on

VC1x = symbols('VC1x')
f1 = (VCC-VC1x)/R1-(VC1x-VE5)/RF-IC1
sol = solve((f1), VC1x)
VC1 = sol[0]
IC5 = IC6 = IC10+(VE5-VC1)/RF

gm1 = IC1/VT
gm4 = IC4/VT
gm5 = IC5/VT
rpi1 = beta/gm1
rpi4 = beta/gm4
rpi5 = beta/gm5

Ri = 2*(rpi1 + (1+beta)*R3)

A1 = -gm1/(1+gm1*R3)

f = -1/RF
Ri5 = rpi5*(1+gm5*resp(RL/2, RF))
a = -resp(R1, RF, rpi1)*gm4*resp(Ri5, R2)

T = a*f
A = A1*a/(1+a*f)

roa=1/gm5+R2/(beta+1)
Ro=2*roa/(1+T)

print('T=%f' % T)
print('A=%f' % A)
print('Ri=%f (Kohm)' % (Ri*1e-3))
print('Ro=%f' % Ro)

# 267
