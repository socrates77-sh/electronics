from numpy import pi, arange, sqrt

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10
eox = 3.9 * 8.854e-12

W = 10e-6
L = 1e-6
k = 194e-6
lamb = 0.024
tox = 80e-10
phi = 0.3
Vt0 = 0.6
NA = 5e21
phi0 = 0.7
Csb0 = 20e-15
Cdb0 = 20e-15
Cgb = 5e-15
Cgs1 = 2e-15
Cgd = 2e-15

Cox = eox / tox
gamma = 1 / Cox * sqrt(2 * q * epi * NA)

VSB = 0
VDS = 3
VGS = 1

Vt = Vt0 + gamma * (sqrt(2 * phi + VSB) - sqrt(2 * phi))
ID = (k / 2) * (W / L) * (VGS - Vt)**2 * (1 + lamb * VDS)
gm = sqrt(2 * k * ID * W / L)
Cgs2 = (2 / 3) * W * L * Cox
Cgs = Cgs1 + Cgs2

fT = gm / (2 * pi * (Cgs + Cgb + Cgd))
print('fT=%f (GHz)' % (fT * 1e-9))

VGS = 1.5
Vt = Vt0 + gamma * (sqrt(2 * phi + VSB) - sqrt(2 * phi))
ID = (k / 2) * (W / L) * (VGS - Vt)**2 * (1 + lamb * VDS)
gm = sqrt(2 * k * ID * W / L)
Cgs2 = (2 / 3) * W * L * Cox
Cgs = Cgs1 + Cgs2

fT = gm / (2 * pi * (Cgs + Cgb + Cgd))
print('fT=%f (GHz)' % (fT * 1e-9))

VGS = 2
Vt = Vt0 + gamma * (sqrt(2 * phi + VSB) - sqrt(2 * phi))
ID = (k / 2) * (W / L) * (VGS - Vt)**2 * (1 + lamb * VDS)
gm = sqrt(2 * k * ID * W / L)
Cgs2 = (2 / 3) * W * L * Cox
Cgs = Cgs1 + Cgs2

fT = gm / (2 * pi * (Cgs + Cgb + Cgd))
print('fT=%f (GHz)' % (fT * 1e-9))

