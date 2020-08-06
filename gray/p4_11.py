from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

un = 450e-4
eox = 3.9*8.86e-12
esi = 11.6*8.86e-12
tox = 80e-10
dXd = 0.02e-6
Ld = 0.09e-6
NA = 5e21
ni = 1.45e16
q = 1.6e-19
VT = 26e-3
Vt2_0 = -1

Ldrw = 1e-6
W1 = 100e-6
W2 = 10e-6

Vout = 1

Leff = Ldrw - 2*Ld

VSB2 = Vout
phi_f = VT*log(NA/ni)
Cox = eox/tox
gamma2 = 1/Cox*sqrt(2*q*esi*NA)
Vt2 = Vt2_0+gamma2*(sqrt(2*phi_f+VSB2)-sqrt(2*phi_f))

gm2 = un*Cox*W2*(-Vt2)/Leff
gmb2 = gm2*gamma2/(2*sqrt(2*phi_f+VSB2))

ID1 = 0.5*un*Cox*W2*(-Vt2)/Leff
gm1 = sqrt(2*ID1*un*Cox*W1/Leff)

lamb = dXd/Leff

ro1 = 1/(lamb*ID1)
ro2 = ro1

Av = -gm1*resp(ro1, ro2, 1/gmb2)

print('Av=%f' % Av)

# 72