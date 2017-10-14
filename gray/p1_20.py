import matplotlib.pyplot as plt
from numpy import pi, arange, sqrt

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10
eox = 3.9 * 8.854e-12

Ec = 1.5e6
W = 10e-6
u = 450e-4

plt.rc('figure', figsize=(8, 6))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid()

lx = arange(0.4e-6, 10e-6, 0.01e-6)
Vov = 0.1
gm = [(50 * eox / x) * u * W / x * Vov for x in lx]
ax.plot(lx, gm, 'r')

gm1 = [W * (50 * eox / x) * u * Ec * (sqrt(1 + 2 * Vov / (Ec * x)
                                           ) - 1) / sqrt(1 + 2 * Vov / (Ec * x)) for x in lx]
ax.plot(lx, gm1, 'b')

ax.set_xlim(0, 1e-5)
ax.set_ylim(0, 6e-4)

plt.show()


for i in range(0, len(lx)):
    if (gm[i] - gm1[i]) / gm[i] < 0.1:
        print('l=%f (um)' % (lx[i] * 1e6))
        break
