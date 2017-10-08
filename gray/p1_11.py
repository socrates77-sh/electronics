import matplotlib.pyplot as plt
from sympy import *
from numpy import pi, arange

init_printing()
plt.rc('figure', figsize=(8, 6))

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10

tT1 = 1 / (2 * pi * 600e6)
tT2 = 1 / (2 * pi * 1e9)
Cu1 = 0.15e-12
gm1 = 1e-3 / VT
gm2 = 10e-3 / VT
gamma = 1 / (50e3 * gm1)

x, y = symbols('x y')
S = solve((x + y / gm1 - tT1,  x + y / gm2 - tT2), x, y)
tF = float(S[x])
Cje = float(S[y]) - Cu1

b0 = 100
phi0 = 0.55
Ccs1 = 1e-12
VCB = 2
VCS = 15

print('(a) when IC=0.1mA')
IC = 0.1e-3

gm = IC / VT
rpi = b0 / gm
ro = 1 / (gamma * gm)
ru = 5 * b0 * ro
Cpi = tF * gm + Cje
Cu = Cu1 * sqrt((1 + 10 / phi0) / (1 + VCB / phi0))
Ccs = Ccs1 * sqrt((1 + 10 / phi0) / (1 + VCS / phi0))
print('gm=%f (mA/V)' % (gm * 1e3))
print('rpi=%f (Kohm)' % (rpi * 1e-3))
print('ro=%f (Kohm)' % (ro * 1e-3))
print('ru=%f (Mohm)' % (ru * 1e-6))
print('Cpi=%f (pF)' % (Cpi * 1e12))
print('Cu=%f (pF)' % (Cu * 1e12))
print('Ccs=%f (pF)' % (Ccs * 1e12))

print('(a) when IC=1mA')
IC = 1e-3

gm = IC / VT
rpi = b0 / gm
ro = 1 / (gamma * gm)
ru = 5 * b0 * ro
Cpi = tF * gm + Cje
Cu = Cu1 * sqrt((1 + 10 / phi0) / (1 + VCB / phi0))
Ccs = Ccs1 * sqrt((1 + 10 / phi0) / (1 + VCS / phi0))
print('gm=%f (mA/V)' % (gm * 1e3))
print('rpi=%f (Kohm)' % (rpi * 1e-3))
print('ro=%f (Kohm)' % (ro * 1e-3))
print('ru=%f (Mohm)' % (ru * 1e-6))
print('Cpi=%f (pF)' % (Cpi * 1e12))
print('Cu=%f (pF)' % (Cu * 1e12))
print('Ccs=%f (pF)' % (Ccs * 1e12))

print('(a) when IC=5mA')
IC = 5e-3

gm = IC / VT
rpi = b0 / gm
ro = 1 / (gamma * gm)
ru = 5 * b0 * ro
Cpi = tF * gm + Cje
Cu = Cu1 * sqrt((1 + 10 / phi0) / (1 + VCB / phi0))
Ccs = Ccs1 * sqrt((1 + 10 / phi0) / (1 + VCS / phi0))
print('gm=%f (mA/V)' % (gm * 1e3))
print('rpi=%f (Kohm)' % (rpi * 1e-3))
print('ro=%f (Kohm)' % (ro * 1e-3))
print('ru=%f (Mohm)' % (ru * 1e-6))
print('Cpi=%f (pF)' % (Cpi * 1e12))
print('Cu=%f (pF)' % (Cu * 1e12))
print('Ccs=%f (pF)' % (Ccs * 1e12))


ICx = arange(1e-6,  10e-3, 1e-5)
fTx = [1 / (2 * pi * (tF + VT * (Cje + Cu) / k)) for k in ICx]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid()

ax.loglog(ICx, fTx, 'r')

ax.set_xlabel('I_C')
ax.set_ylabel('f_T')
plt.show()
