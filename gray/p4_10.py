from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *

un = 450e-4
eox = 3.9*8.86e-12
tox = 80e-10
dXd1 = 0.02e-6
dXd2 = 0.04e-6
Ld = 0.09e-6

Cox = eox/tox

Ldrw = 1e-6
W = 100e-6

Leff = Ldrw - 2*Ld

lamb1 = dXd1/Leff
lamb2 = dXd2/Leff

Av, ID = symbols('Av ID')

ro1 = 1/(lamb1*ID)
ro2 = 1/(lamb2*ID)

gm1 = (2*ID*un*Cox*W/Leff) ** 0.5

Av = -gm1*resp(ro1, ro2)

Av_1 = Av.evalf(subs={ID: 1e-3})
Av_2 = Av.evalf(subs={ID: 100e-6})
Av_3 = Av.evalf(subs={ID: 10e-6})
Av_4 = Av.evalf(subs={ID: 1e-6})

print('Part a')
print('Av=%f' % Av_1)
print('Av=%f' % Av_2)
print('Av=%f' % Av_3)
print('Av=%f' % Av_4)

n = 1.5
VT = 26e-3

gm1 = ID/(n*VT)
Av = -gm1*resp(ro1, ro2)

# Av_1 = Av.evalf(subs={ID: 1e-3})
# Av_2 = Av.evalf(subs={ID: 100e-6})
Av_3 = Av.evalf(subs={ID: 10e-6})
Av_4 = Av.evalf(subs={ID: 1e-6})

print('Part b')
# print('Av=%f' % Av_1)
# print('Av=%f' % Av_2)
print('Av=%f' % Av_3)
print('Av=%f' % Av_4)

# 72