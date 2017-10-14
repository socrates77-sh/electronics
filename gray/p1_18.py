import matplotlib.pyplot as plt
from numpy import pi, arange, sqrt

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10
eox = 3.9 * 8.854e-12

k = 194e-6
Vt0 = 0.6
Ec = 1.5e6

plt.rc('figure', figsize=(8, 6))

W = 100e-6
L = 10e-6

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid()

VGS = 1
vds1_1 = arange(0, VGS - Vt0 + 0.01, 0.01)
ids1_1 = [(k / 2) * (W / L) * (2 * (VGS - Vt0) * vds1_1x - vds1_1x**2)
          for vds1_1x in vds1_1]
ids2_1 = (k / 2) * (W / L) * (VGS - Vt0)**2
vds_act = (Ec * L * (sqrt(1 + 2 * (VGS - Vt0) / (Ec * L)) - 1))
ids2 = (k / 2) * (W / L) * vds_act**2
vds1 = arange(0, vds_act, 0.01)
ids1 = [(k / 2) * (W / L) * (2 * (VGS - Vt0) * vds1x - vds1x**2) /
        (1 + vds1x / (Ec * L)) for vds1x in vds1]
ax.plot(vds1, ids1, 'r-')
ax.plot([vds_act, 3], [ids2, ids2], 'r-')


plt.show()
