from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
Rs = 5e3
RL = 3e3
rb = 300
IC = 0.5e-3
beta = 200
fT = 500e6
Cu = 0.3e-12

gm = IC/VT
rpi = beta/gm
Cpi = gm/(2*pi*fT)-Cu
CM = (1+gm*RL)*Cu
f_3db = 1/(2*pi*resp(Rs+rb, rpi)*(CM+Cpi))

R=resp(Rs+rb, rpi)
p2=-(1/(RL*Cu)+1/(R*Cpi)+1/(RL*Cpi)+gm/Cpi)/(2*pi)

print('f-3db=%f (MHz)' % (f_3db*1e-6))
print('p2=%f (MHz)' % (p2*1e-6))



# 183
