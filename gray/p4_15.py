from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

un = 550e-4
up = 250e-4
eox = 3.9*8.86e-12
esi = 11.6*8.86e-12
tox = 150e-10
dXd_n = 0.08e-6
dXd_p = 0.04e-6
Ld_n = 0.12e-6
Ld_p = 0.18e-6
NA = 5e21
ni = 1.45e16
q = 1.6e-19
VT = 26e-3

Ldrw = 1e-6
W2 = 50e-6
W4 = 100e-6
Itail = 100e-6
Rs = 2e3

Leff2 = Ldrw - 2*Ld_n
Leff4 = Ldrw - 2*Ld_p

Cox = eox/tox
lamb_n = dXd_n/Leff2
lamb_p = dXd_p/Leff4

ID = 0.5*Itail

ro2 = 1/(lamb_n*ID)
ro4 = 1/(lamb_p*ID)

gm2 = sqrt(2*ID*un*Cox*W2/Leff2)
gm4 = sqrt(2*ID*up*Cox*W4/Leff4)

Ro4 = ro4*(1+gm4*Rs)

Rout = resp(ro2, Ro4)
Av = gm2*Rout

print('Rout=%fohm' % (Rout*1e-3))
print('Av=%f' % Av)

# 81
