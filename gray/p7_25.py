from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
R1 = 30e3
Vsu = 10
Vo = 0
beta1 = 50
fT1 = 4e6
IC1x = 0.5e-3
Cu01 = 1e-12
Cje1 = 3e-12
Cbs01 = 2e-12
VA1 = 50
n = 0.5
phi0 = 0.55
beta2 = 100
fT2 = 500e6
Cu02 = 0.7e-12
Cje2 = 3e-12
Ccs02 = 2e-12
VA2 = 120


IC = (Vsu-0.6)/R1
VCB1 = Vo-(Vsu-0.6)
Cu1 = Cu01/(1-VCB1/phi0)**n
VBS1 = 2*Vsu-0.6
Cbs1 = Cbs01/(1+VBS1/phi0)**n
gmx = IC1x/VT
Cpi1x = gmx/(2*3.1416*fT1)-Cbs1-Cu1
Cb1x = Cpi1x-Cje1
Cb1 = Cb1x*IC/IC1x
Cpi1 = Cb1+Cje1
gm1 = IC/VT
rpi1 = beta1/gm1
ro1 = VA1/IC

VCB2 = Vo-(-Vsu+0.6)
Cu2 = Cu02/(1+VCB2/phi0)**n
VCS2 = Vo-(-Vsu)
Ccs2 = Ccs02/(1+VCS2/phi0)**n
ro2 = VA2/IC
ro=resp(ro1, ro2)

Avi0 = -beta1*ro

Ru01=rpi1+ro+gm1*rpi1*ro

T0 = rpi1*(Cbs1+Cpi1)+Ru01*Cu1+ro*(Ccs2+2*Cu2)

f_3db = 1/(2*pi*T0)

print('Avi0=%f (Mohm)' % (Avi0*1e-6))
print('f-3db=%f (KHz)' % (f_3db*1e-3))

Cx=20e-12

T0 = rpi1*(Cbs1+Cpi1)+Ru01*(Cx+Cu1)+ro*(Ccs2+2*Cu2)

f_3db = 1/(2*pi*T0)

print('f-3db=%f (KHz)' % (f_3db*1e-3))

# 208
