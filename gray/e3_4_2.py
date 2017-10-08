VT = 26e-3

gm = 1e-3
ro = 20e3
X = 0.1

gmb = X * gm
Gm = gm * (1 - 1 / (1 + (gm + gmb) * ro + 1))
Ro = 2 * ro + (gm + gmb) * ro * ro

print('Gm=%f (mA/V)' % (Gm * 1e3))
print('Ro=%f (kohm)' % (Ro * 1e-3))
