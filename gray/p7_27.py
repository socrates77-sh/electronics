from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
VC = 5
RS = 20e3
RB1 = 10e3
RB2 = 20e3
Vsu = 10
Vo = 0
beta3 = 50
fT3 = 4e6
IC3x = 0.5e-3
Cu03 = 1e-12
Cje3 = 3e-12
Cbs03 = 2e-12
VA3 = 50
n = 0.5
phi0 = 0.55
beta1 = 200
fT1 = 500e6
IC1x = 1e-3
Cu01 = 0.7e-12
Cje1 = 3e-12
Ccs01 = 2e-12
VA1 = 120

IC6 = (Vsu-0.6)/RB2

# IC5x = symbols('IC5x', Real=True)
# eq1=log(IC6/IC5x)-IC5x*RB1/VT
# # eq1 = IC6/IC5x-exp(IC5x*RB1/VT)
# IC5 = nsolve(eq1, 1e-3)
IC5 = 10e-6
IC = IC5/2

ro1 = VA1/IC
gm1 = IC/VT
rpi1 = beta1/gm1
VCB1=VC
Cu1 = Cu01/(1+VCB1/phi0)**n
VCS1=VC+Vsu
Ccs1 = Ccs01/(1+VCS1/phi0)**n

gmx = IC1x/VT
Cpi1x = gmx/(2*3.1416*fT1)-Cu1
Cb1x = Cpi1x-Cje1
Cb1 = Cb1x*IC/IC1x
Cpi1 = Cb1+Cje1

ro3=VA3/IC
VCB3=VC-(Vsu-0.6)
Cu3 = Cu03/(1-VCB3/phi0)**n

ro=resp(ro1, ro3)

Av0=-gm1*ro*rpi1/(rpi1+RS)

Ru01=resp(RS,rpi1)+ro+gm1*resp(RS,rpi1)*ro
print(Ru01)

T0 = resp(RS,rpi1)*Cpi1+Ru01*Cu1+ro*(Ccs1+Cu3)

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))

# Cx=20e-12

# T0 = rpi1*(Cbs1+Cpi1)+Ru01*(Cx+Cu1)+ro*(Ccs2+2*Cu2)

# f_3db = 1/(2*pi*T0)

# print('f-3db=%f (KHz)' % (f_3db*1e-3))

# 208
