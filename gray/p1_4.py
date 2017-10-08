VT = 26e-3
ni = 1.5e16
q = 1.6e-19
epi = 1.04e-10

Ecrit = 3e7
VR = 150

ND = Ecrit ** 2 * epi / (2 * q * VR) / 1.5**2
print('ND=%e (atoms/cm3)' % (ND * 1e-6))
