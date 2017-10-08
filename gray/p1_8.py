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
rpi = b0 / gm
ro = 1 / (gamma * gm)
ru = 5 * b0 * ro
Cpi = tF * gm * 1e3 + 2 * Cje0
Cu = Cu0 / (1 + VCB / phi0)**n
Ccs = Ccs0 / (1 + VCS / phi0)**n

print('gm=%f (mA/V)' % (gm * 1e3))
print('rpi=%f (Kohm)' % (rpi * 1e-3))
print('ro=%f (Kohm)' % (ro * 1e-3))
print('ru=%f (Mohm)' % (ru * 1e-6))
print('Cpi=%f (fF)' % (Cpi))
print('Cu=%f (fF)' % Cu)
print('Ccs=%f (fF)' % Ccs)
