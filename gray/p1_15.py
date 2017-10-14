import matplotlib.pyplot as plt
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

plt.rc('figure', figsize=(14, 6))
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.grid()
ax2.grid()

VGS = 1.5
v_tri = arange(0, VGS - Vt0 + 0.05, 0.05)
i_tri = [(k / 2) * (W / L) * (2 * (VGS - Vt0) * v - v**2) for v in v_tri]
i_sat = (k / 2) * (W / L) * (VGS - Vt0)**2
ax1.plot(v_tri, i_tri, 'r')
ax1.plot([VGS - Vt0, 3], [i_sat, i_sat], 'r')

VGS = 3
v_tri = arange(0, VGS - Vt0 + 0.05, 0.05)
i_tri = [(k / 2) * (W / L) * (2 * (VGS - Vt0) * v - v**2) for v in v_tri]
i_sat = (k / 2) * (W / L) * (VGS - Vt0)**2
ax1.plot(v_tri, i_tri, 'b')
ax1.plot([VGS - Vt0, 3], [i_sat, i_sat], 'b')

ax1.set_xlim(0, 3)
ax1.set_ylim(0, 0.006)

Cox = eox / tox
gamma = 1 / Cox * sqrt(2 * q * epi * NA)

VSB = 0
Vt = Vt0 + gamma * (sqrt(2 * phi + VSB) - sqrt(2 * phi))
vx = arange(Vt, 2, 0.01)
ix = [(k / 2) * (W / L) * (v - Vt)**2 for v in vx]
ax2.plot(vx, ix, 'r')
ax2.plot([0, Vt], [0, 0],  'r')

VSB = 0.5
Vt = Vt0 + gamma * (sqrt(2 * phi + VSB) - sqrt(2 * phi))
vx = arange(Vt, 2, 0.01)
ix = [(k / 2) * (W / L) * (v - Vt)**2 for v in vx]
ax2.plot(vx, ix, 'b')
ax2.plot([0, Vt], [0, 0],  'r')

VSB = 1
Vt = Vt0 + gamma * (sqrt(2 * phi + VSB) - sqrt(2 * phi))
vx = arange(Vt, 2, 0.01)
ix = [(k / 2) * (W / L) * (v - Vt)**2 for v in vx]
ax2.plot(vx, ix, 'g')
ax2.plot([0, Vt], [0, 0],  'r')

ax2.set_xlim(0, 2)
ax2.set_ylim(0, 0.002)

plt.show()
