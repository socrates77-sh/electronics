VT = 26e-3

IC = 100e-6
b0 = 100
RL = 1e3
RS = 1e3

gm = IC / VT
rpi = b0 / gm

Ri = rpi + (b0 + 1) * RL
av = 1 / (1 + (RS + rpi) / ((b0 + 1) * RL))
Ro = (RS + rpi) / (b0 + 1)

print('Ri=%f (kohm)' % (Ri * 1e-3))
print('Ro=%f (ohm)' % Ro)
print('av=%f' % av)
