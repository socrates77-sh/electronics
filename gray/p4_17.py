from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

un = 550e-4
up = 250e-4
eox = 3.9*8.86e-12
tox = 150e-10
dXd_n = 0.08e-6
dXd_p = 0.04e-6
Ld_n = 0.12e-6
Ld_p = 0.18e-6

Ldrw = 1e-6
Wn = 50e-6
Wp = 100e-6

Itail = 100e-6

Leff_n = Ldrw - 2*Ld_n
Leff_p = Ldrw - 2*Ld_p
Cox = eox/tox

lamb_n = dXd_n/Leff_n
lamb_p = dXd_p/Leff_p

ID = 0.5*Itail

ro4 = 1/(lamb_n*ID)
ro2 = ro4
ro6 = 1/(lamb_p*ID)
ro8 = ro6

gm4 = sqrt(2*ID*un*Cox*Wn/Leff_n)
gm6 = sqrt(2*ID*up*Cox*Wp/Leff_p)
gm1 = gm4

Rout = resp(gm6*ro6*ro8, gm4*ro4*ro2)

Av = gm1*Rout

print('Av=%f' % Av)

# 83
