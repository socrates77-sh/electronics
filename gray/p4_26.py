from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

VT = 26e-3
VA = 130
beta = 200
IS = 5e-15
Vbe_on = 0.7

VCC = 15
R1 = 10e3
R2 = 1e3

Ic1 = (VCC-2*Vbe_on)/R1

Vbe1=VT*log(Ic1/IS)
Iout=Vbe1/R2

S_Iout_VCC=1/(1+Iout*R2/VT)

# print('Iout=%f (mA)' % (Iout*1e3))
# print('Rout=%f (Mohm)' % (Rout*1e-6))
print('S_Iout_VCC=%f' % S_Iout_VCC)

# 93
