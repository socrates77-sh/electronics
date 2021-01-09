from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

VDD = 2.5
IQ = 1e-3
W_L = 1000
k = 200e-6
Vt0 = 0.7
phi_f = 0.3
gamma = 0.5
vi = 0.5

VI = symbols('VI')
Vov1 = (2*IQ/(k*W_L))**0.5
Vo = -VDD-2*phi_f+(-gamma/2+((gamma/2)**2+VI-Vov1-Vt0 +
                             gamma*(2*phi_f)**0.5+VDD+2*phi_f)**0.5)**2
Vsb = Vo+VDD
X = gamma/(2*(2*phi_f+Vsb)**0.5)
Av = 1/(1+X)

Av_1 = Av.evalf(subs={VI: vi})
Av_2 = Av.evalf(subs={VI: 0})
Av_3 = Av.evalf(subs={VI: -vi})

print('Av_plus=%f' % Av_1)
print('Av_Q=%f' % Av_2)
print('Av_minus=%f' % Av_3)

# 112
