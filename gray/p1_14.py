from numpy import pi

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10

fT = 9 * 50e6
tF = 0.25e-9
Cu = 0.6e-12
IC = 1e-3
b0 = 100
VA = 40
Ccs = 2e-12

gm = IC / VT
tT = 1 / (2 * pi * fT)
Cje = (tT - tF) * gm - Cu

IC = 2e-3
gm = IC / VT
rpi = b0 / gm
ro = VA / IC
ru = 5 * b0 * ro
Cpi = tF * gm + Cje

print('gm=%f (mA/V)' % (gm * 1e3))
print('rpi=%f (Kohm)' % (rpi * 1e-3))
print('ro=%f (Kohm)' % (ro * 1e-3))
print('ru=%f (Mohm)' % (ru * 1e-6))
print('Cpi=%f (pF)' % (Cpi * 1e12))
print('Cu=%f (pF)' % (Cu * 1e12))
print('Ccs=%f (pF)' % (Ccs * 1e12))
