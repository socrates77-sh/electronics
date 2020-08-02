from sympy import symbols, solve, diff, log
from sympy.plotting import plot

un = 450e-4
eox = 3.9 * 8.86e-12
tox = 80e-10
dXd = 0.02e-6
Ld = 0.09e-6

ID = 100e-6
Ldrw = 1e-6
W = 100e-6

Leff = Ldrw - 2*Ld

lamb = dXd/Leff
Cox = eox/tox

ro = 1/(lamb*ID)
gm = (2*ID*un*Cox*W/Leff) ** 0.5

Ro = gm*ro*ro

print('Ro=%f (Mohm)' % (Ro*1e-6))

print(8.86*11.6)
# 59
