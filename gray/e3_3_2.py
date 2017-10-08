VT = 26e-3

k = 100e-6
RD = 5e3
W = 50e-6
L = 1e-6
VDD = 5
Vt = 0.8
Vi = 1

ID = (k / 2) * (W / L) * (Vi - Vt) ** 2
Vo = VDD - ID * RD

gm = k * (W / L) * (Vi - Vt)

av = -gm * RD

print('av=%f' % av)
