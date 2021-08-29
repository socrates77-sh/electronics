from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
Rs = 10e3
RL = 5e3
beta = 200
IC2 = 0.5e-3
IC1 = 10e-6+IC2/beta
fT = 500e6
ICx=2e-3
Cu0 = 0.5e-12
Cje = 4e-12
Ccs0 = 1e-12
n = 0.5
phi0 = 0.55
Vsu = 6

gm1 = IC1/VT
gm2 = IC2/VT
rpi1 = beta/gm1
rpi2 = beta/gm2

VCB1 = Vsu
Cu1 = Cu0/(1+VCB1/phi0)**n
gmx = ICx/VT
Cpi1x = gmx/(2*3.1416*fT)-Cu1
Cb1x = Cpi1x-Cje
Cb1 = Cb1x*IC1/ICx
Cpi1 = Cb1+Cje

VC2=Vsu-RL*IC2
VB2=-0.6
VCB2=VC2-VB2
VCS2=VC2+Vsu
Cu2 = Cu0/(1+VCB2/phi0)**n
Ccs2 = Ccs0/(1+VCS2/phi0)**n
Cpi2x = gmx/(2*3.1416*fT)-Cu2
Cb2x = Cpi2x-Cje
Cb2 = Cb2x*IC2/ICx
Cpi2 = Cb2+Cje

v1, v2, vx = symbols('v1 v2 vx')
f1 = vx-v1-v2
f2 = -1+vx/Rs+v1/rpi1
f3 = v2/rpi2-v1/rpi1-gm1*v1
sol = solve((f1, f2, f3), v1, v2, vx)
Ru01 = sol[vx]

v1, v2 = symbols('v1 v2')
f1 = (v1+v2)/Rs-1+v1/rpi1
f2 = v2/rpi2-gm1*v1-v1/rpi1+1
sol = solve((f1, f2), v1, v2)
Rpi01 = sol[v1]

v1, v2 = symbols('v1 v2')
f1 = (v1+v2)/Rs+v1/rpi1
f2 = gm1*v1+v1/rpi1+1
sol = solve((f1, f2), v1, v2)
Rpi02 = resp(rpi2, sol[v2])

v1, v2, vx = symbols('v1 v2 vx')
f1 = (v1+v2)/Rs+v1/rpi1
f2 = v2/rpi2-gm1*v1-v1/rpi1-1
f3 = 1+gm2*v2+(v2-vx)/RL
sol = solve((f1, f2, f3), v1, v2, vx)
Ru02 = sol[vx]

Rcs02=RL


v1, v2 = symbols('v1 v2')
f1 = (v1+v2-1)/Rs+v1/rpi1
f2 = v2/rpi2-gm1*v1-v1/rpi1
sol = solve((f1, f2), v1, v2)
Av0 = -gm2*sol[v2]*RL

T0 = Rpi01*Cpi1+Rpi02*Cpi2+Ru01*Cu1+Ru02*Cu2+Rcs02*Ccs2
f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))

# 214
