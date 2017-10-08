import matplotlib.pyplot as plt
from sympy import symbols, evalf
# from sympy.plotting import plot
from numpy import arange
from sympy import init_printing

init_printing()
plt.rc('figure', figsize=(8, 6))

VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10

bF = 100
VA = 50

BV_CBO = 120
n = 4

aF = bF / (1 + bF)
BV_CEO = BV_CBO / bF**(1 / n)

# print('BV_CEO=%f (V)' % BV_CEO)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid()

VCE, IC = symbols('VCE IC')
M = 1 / (1 - (VCE / BV_CBO) ** n)

IB = 60e-6
IC = (1 + VCE / VA) * M * aF * IB / (1 - M * aF)
VCEx = arange(0, 32, 0.1)
ICx = [IC.evalf(subs={VCE: x}) for x in VCEx]
ax.plot(VCEx, ICx, 'b')

IB = 30e-6
IC = (1 + VCE / VA) * M * aF * IB / (1 - M * aF)
VCEx = arange(0, 32, 0.1)
ICx = [IC.evalf(subs={VCE: x}) for x in VCEx]
ax.plot(VCEx, ICx, 'g')

IB = 10e-6
IC = (1 + VCE / VA) * M * aF * IB / (1 - M * aF)
VCEx = arange(0, 32, 0.1)
ICx = [IC.evalf(subs={VCE: x}) for x in VCEx]
ax.plot(VCEx, ICx, 'r')

IB = 1e-6
IC = (1 + VCE / VA) * M * aF * IB / (1 - M * aF)
VCEx = arange(0, 32, 0.1)
ICx = [IC.evalf(subs={VCE: x}) for x in VCEx]
ax.plot(VCEx, ICx, 'c')

ax.set_xlim(0, 32)
ax.set_xlabel('VCE/V')
ax.set_ylabel('IC/A')
plt.show()
