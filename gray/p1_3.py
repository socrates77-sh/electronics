VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10

NA = 8e21
ND = 1e23
Ecrit = 4e7

BV = epi * (NA + ND) / (2 * q * NA * ND) * Ecrit**2
print('BV=%f (V)' % BV)
