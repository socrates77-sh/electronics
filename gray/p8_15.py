from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
beta = 100
VBEon = 0.7
rb = 50
VCC = 3
R1 = 500
R2 = 200
R3 = 50
R4 = 78
R5 = 280
RF = 500
VB1 = 0

RE1 = R3+2*R4
RE2 = 2*R5

VE1 = VB1-VBEon

IC1x, IC3x, VC1x, VC3x, VE3x = symbols('IC1x, IC3x, VC1x, VC3x, VE3x')
f1 = IC1x+(VC3x-VE1)/RF-(VE1+VCC)/RE1
f2 = VC1x-VBEon-VE3x
f3 = (VE3x+VCC)/RE2-IC3x
f4 = VCC-R2*(IC3x+(VC3x-VE1)/RF)-VC3x
f5 = VCC-R1*IC1x-VC1x
sol = solve((f1, f2, f3, f4, f5), IC1x, IC3x, VC1x, VC3x, VE3x)
IC1 = sol[IC1x]
IC3 = sol[IC3x]

print('IC1=%f (mA)' % (IC1*1e3))
print('IC3=%f (mA)' % (IC3*1e3))

gm1 = IC1/VT
gm3 = IC3/VT
rpi1 = beta/gm1
rpi3 = beta/gm3

Rx1 = resp(RF, R3)
Rx2 = RF+R3
f = R3/(RF+R3)

a = gm1*gm3*resp(R1, (rpi3+rb))*rpi3*resp(R2, Rx2)/((1+gm1*Rx1)*(rpi3+rb))

T = a*f
A = a/(1+a*f)
ria = rpi1*(1+gm1*Rx1)
roa = resp(R2, Rx2)
Ri = 2*ria*(1+T)
Ro = 2*roa/(1+T)

print('T=%f' % T)
print('A=%f' % A)
print('Ri=%f (Kohm)' % (Ri*1e-3))
print('Ro=%f (ohm)' % Ro)

# 262
