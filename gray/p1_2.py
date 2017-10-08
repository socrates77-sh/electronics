from numpy import log, sqrt

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10

NA = 8e21
ND = 1e23
VD = 0
A = 2e-9

phi0 = VT * log(NA * ND / ni ** 2)

Cj = A * sqrt(q * epi * NA * ND / (2 * (NA + ND))) / sqrt(phi0 - VD)
print('Cj=%f (pF)' % (Cj * 1e12))

VD = -5
Cj = A * sqrt(q * epi * NA * ND / (2 * (NA + ND))) / sqrt(phi0 - VD)
print('Cj=%f (pF)' % (Cj * 1e12))

VD = 0.3
Cj = A * sqrt(q * epi * NA * ND / (2 * (NA + ND))) / sqrt(phi0 - VD)
print('Cj=%f (pF)' % (Cj * 1e12))
