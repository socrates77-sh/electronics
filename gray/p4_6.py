from sympy import symbols, solve, diff, log
from sympy.plotting import plot

un = 450e-4
eox = 3.9*8.86e-12
tox = 80e-10
dXd = 0.02e-6
Ld = 0.09e-6
q = 1.6e-19
e = 11.6*8.86e-12
Vt = 0.6
phi0 = 0.7
NA = 5e21

ID = 100e-6
Ldrw = 1e-6
W = 100e-6

Leff = Ldrw - 2*Ld

lamb = dXd/Leff
Cox = eox/tox

ro = 1/(lamb*ID)
gm = (2*ID*un*Cox*W/Leff) ** 0.5

phif = 0.5*phi0
gamma = (2*q*e*NA)**0.5/Cox
VGS1 = Vt+(2*ID/(un*Cox*W/Leff))**0.5
VSB = VGS1
gmb2 = gamma*gm/(2*(2*phif+VSB)**0.5)

Ro = ro*(1+(gm+gmb2)*ro)+ro

print('Ro=%f (Mohm)' % (Ro*1e-6))

# 60
