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
VSB = 1
VDS = 2
VGS = 1
phi0 = 0.7
Csb0 = 20e-15
Cdb0 = 20e-15
Cgb = 5e-15
Cgs1 = 2e-15
Cgd = 2e-15

Cox = eox / tox
gamma = 1 / Cox * sqrt(2 * q * epi * NA)

Vt = Vt0 + gamma * (sqrt(2 * phi + VSB) - sqrt(2 * phi))
ID = (k / 2) * (W / L) * (VGS - Vt)**2 * (1 + lamb * VDS)
gm = sqrt(2 * k * ID * W / L)
gmb = gm * gamma / (2 * sqrt(2 * phi + VSB))
ro = 1 / (lamb * ID)
Csb = Csb0 / sqrt(1 + VSB / phi0)
VDB = VDS + VSB
Cdb = Cdb0 / sqrt(1 + VDB / phi0)
Cgs2 = (2 / 3) * W * L * Cox
Cgs = Cgs1 + Cgs2

print('gm=%f (mA/V)' % (gm * 1e3))
print('gmb=%f (mA/V)' % (gmb * 1e3))
print('ro=%f (Kohm)' % (ro * 1e-3))
print('Csb=%f (fF)' % (Csb * 1e15))
print('Cdb=%f (fF)' % (Cdb * 1e15))
print('Cgs=%f (fF)' % (Cgs * 1e15))
print('Cgd=%f (fF)' % (Cgd * 1e15))
print('Cgb=%f (fF)' % (Cgb * 1e15))
