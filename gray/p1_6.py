VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10

Ecrit = 3e7
ND = 1e21
bF = 400
n = 4

BV_CBO = epi * Ecrit**2 / (2 * q * ND)
BV_CEO = BV_CBO / bF**(1 / n)
print('BV_CEO=%f (V)' % BV_CEO)
