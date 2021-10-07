from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *


VDD = 6
R1 = 4.35e3
R2 = 10e3
R3 = 1e3
RS = 5e3
RL = 6e3
W_L = 100
Vt = 1
kn = 60e-6
kp = 20e-6

ID1x, VS1x = symbols('ID1x,VS1x')
f1 = ID1x-kn/2*W_L*(-VS1x-Vt)**2
f2 = VS1x+VDD-RS*2*ID1x
sol = solve((f1, f2), ID1x, VS1x)
ID1, VS1 = sol[0]
ID2 = ID1
ID3 = VDD/RL

gm1=gm2=(2*kn*W_L*ID1)**0.5
gm3=(2*kp*W_L*ID3)**0.5

print(gm1,gm3)

Rx1 = resp(R2, R3)
Rx2 = R2+R3
RS1 = resp(RS,1/gm2)

a = gm1*gm3*R1*resp(RL,Rx2)/(1+gm1*RS1)
f = R3/(R2+R3)

T = a*f
A = a/(1+a*f)
# ria = rpi1*(1+gm1*RE1)
roa =resp(RL,Rx2)
# Ri = ria*(1+T)
Ro = roa/(1+T)

print('T=%f' % T)
print('A=%f' % A)
# print('Ri=%f (Mohm)' % (Ri*1e-6))
print('Ro=%f (ohm)' % Ro)

# 260
