import matplotlib.pyplot as plt
from numpy import pi
from sympy import *
from control import *
# from sympy import init_printing

init_printing()
plt.rc('figure', figsize=(8, 6))

s, B1, B2 = symbols('s B1 B2')

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10

IC = 0.2
VCB = 3
VCS = 4
Cje0 = 20
Cu0 = 10
Ccs0 = 20
b0 = 100
tF = 15
gamma = 1e-3
phi0 = 0.55
n = 0.5

gm = IC / VT * 1e-3
Cpi = tF * gm * 1e3 + 2 * Cje0
Cu = Cu0 / (1 + VCB / phi0) ** n
fT = 1e12 * gm / ((Cpi + Cu) * 2 * pi)
print('fT=%f (MHz)' % (fT * 1e-6))
B1 = b0 / (1 + b0 * s * 1e-12 * (Cpi + Cu / gm))

IC = 1
VCB = 1
VCS = 2
gm = IC / VT * 1e-3
Cpi = tF * gm * 1e3 + 2 * Cje0
Cu = Cu0 / (1 + VCB / phi0) ** n
fT = 1e12 * gm / ((Cpi + Cu) * 2 * pi)
print('fT=%f (MHz)' % (fT * 1e-6))
B2 = b0 / (1 + b0 * s * 1e-12 * (Cpi + Cu / gm))

D0 = denom(B1)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(B1)
N2 = float(N0)

B1b = tf(N2, D2)
bode(B1b, dB=True)

D0 = denom(B2)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(B2)
N2 = float(N0)

B2b = tf(N2, D2)
bode(B2b, dB=True)

plt.show()
