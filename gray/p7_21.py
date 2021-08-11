from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
Rs = 100e3
RL = 3e3
IC1 = 10e-6
IC2 = 1e-3
beta = 100
fT = 500e6
Cu = 0.4e-12
Cje = 2e-12
Ccs = 1e-12

gm1 = IC1/VT
gm2 = IC2/VT
rpi1 = beta/gm1
rpi2 = beta/gm2
Cpi1 = gm2/(2*pi*fT)-Cu-9.7e-12
Cpi2 = gm2/(2*pi*fT)-Cu

v1, v2, vo = symbols('v1 v2 vo')
f1 = vo/RL+gm2*v2+gm1*v1
f2 = v2/rpi2-gm1*v1-v1/rpi1
f3 = (v1+v2-1)/Rs+v1/rpi1
sol = solve((f1, f2, f3), v1, v2, vo)
Av0 = sol[vo]

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

Rcs01 = Rcs02 = RL

v1, v2, vx = symbols('v1 v2 vx')
f1 = (v1+v2)/Rs+v1/rpi1-1
f2 = v2/rpi2-gm1*v1-v1/rpi1
f3 = 1+gm1*v1+gm2*v2+(v1+v2-vx)/RL
sol = solve((f1, f2, f3), v1, v2, vx)
Ru01 = sol[vx]

v1, v2, vx = symbols('v1 v2 vx')
f1 = (v1+v2)/Rs+v1/rpi1
f2 = v2/rpi2-gm1*v1-v1/rpi1-1
f3 = 1+gm1*v1+gm2*v2+(v2-vx)/RL
sol = solve((f1, f2, f3), v1, v2, vx)
Ru02 = sol[vx]

T0 = Rpi01*Cpi1+Rpi02*Cpi2+Ru01*Cu+Ru02*Cu+Rcs01*Ccs+Rcs02*Ccs

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))

v1, v2 = symbols('v1 v2')
f1 = (v1+v2-1)/Rs+v1/rpi1
f2 = v2/rpi2-gm1*v1-v1/rpi1
sol = solve((f1, f2), v1, v2)
Av0 = -gm2*sol[v2]*RL

Rcs01 = 0

v1, v2, vx = symbols('v1 v2 vx')
f1 = vx-v1-v2
f2 = -1+vx/Rs+v1/rpi1
f3 = v2/rpi2-v1/rpi1-gm1*v1
sol = solve((f1, f2, f3), v1, v2, vx)
Ru01 = sol[vx]

v1, v2, vx = symbols('v1 v2 vx')
f1 = (v1+v2)/Rs+v1/rpi1
f2 = v2/rpi2-gm1*v1-v1/rpi1-1
f3 = 1+gm2*v2+(v2-vx)/RL
sol = solve((f1, f2, f3), v1, v2, vx)
Ru02 = sol[vx]

T0 = Rpi01*Cpi1+Rpi02*Cpi2+Ru01*Cu+Ru02*Cu+Rcs01*Ccs+Rcs02*Ccs

f_3db = 1/(2*pi*T0)

print('Av0=%f' % Av0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))

# 204
