from numpy import log, sqrt

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10

NA = 8e21
ND = 1e23
VR = 5

print('(a)')
phi0 = VT * log(NA * ND / ni ** 2)
print('phi0=%f (mV)' % (phi0 * 1e3))

W1 = sqrt(2 * epi * (phi0 + VR) / (q * NA * (1 + NA / ND)))
print('W1=%f (um)' % (W1 * 1e6))

W2 = sqrt(2 * epi * (phi0 + VR) / (q * ND * (1 + ND / NA)))
print('W2=%f (um)' % (W2 * 1e6))

Emax = -q * NA * W1 / epi
print('Emax=%f (V/cm)' % (Emax / 100))

print('(b1)')
VR = 0
phi0 = VT * log(NA * ND / ni ** 2)
print('phi0=%f (mV)' % (phi0 * 1e3))

W1 = sqrt(2 * epi * (phi0 + VR) / (q * NA * (1 + NA / ND)))
print('W1=%f (um)' % (W1 * 1e6))

W2 = sqrt(2 * epi * (phi0 + VR) / (q * ND * (1 + ND / NA)))
print('W2=%f (um)' % (W2 * 1e6))

Emax = -q * NA * W1 / epi
print('Emax=%f (V/cm)' % (Emax / 100))

print('(b2)')
VR = -0.3
phi0 = VT * log(NA * ND / ni ** 2)
print('phi0=%f (mV)' % (phi0 * 1e3))
W1 = sqrt(2 * epi * (phi0 + VR) / (q * NA * (1 + NA / ND)))
print('W1=%f (um)' % (W1 * 1e6))
W2 = sqrt(2 * epi * (phi0 + VR) / (q * ND * (1 + ND / NA)))
print('W2=%f (um)' % (W2 * 1e6))

Emax = -q * NA * W1 / epi
print('Emax=%f (V/cm)' % (Emax / 100))
