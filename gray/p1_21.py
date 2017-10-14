import matplotlib.pyplot as plt
from numpy import pi, arange, sqrt

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10
eox = 3.9 * 8.854e-12

k = 54e-6
Vt0 = 0.7
Ec = 1.5e6
VDS = 5

W = 1e-6
L = 1e-6

plt.rc('figure', figsize=(8, 6))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid()

vgs = arange(Vt0, 5, 0.01)
vds_act = [(Ec * L * (sqrt(1 + 2 * (vgsx - Vt0) / (Ec * L)) - 1))
           for vgsx in vgs]
s_ids1 = [sqrt((k / 2) * (W / L) * vds_actx**2) for vds_actx in vds_act]
ax.plot(vgs, s_ids1, 'r')
ax.plot([0, Vt0], [0, 0],  'r')

ax.set_xlim(0, 5)
ax.set_ylim(0, 0.014)

plt.show()
