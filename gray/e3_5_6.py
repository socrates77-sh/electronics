VT = 26e-3

gm1 = 1.001e-3
gm2 = 0.999e-3
R1 = 101e3
R2 = 99e3
rtail = 1e6

gm = (gm1 + gm2) / 2
dgm = gm1 - gm2
R = (R1 + R2) / 2
dR = R1 - R2

Adm = -gm * R
Acm_dm = -(gm * dR + dgm * R) / (1 + 2 * gm * rtail)
Adm_cm = -1 / 4 * (gm * dR + dgm * R / (1 + 2 * gm * rtail))
Acm = -gm * R / (1 + 2 * gm * rtail)

print('Adm=%f' % Adm)
print('Acm_dm=%f' % Acm_dm)
print('Adm_cm=%f' % Adm_cm)
print('Acm=%f' % Acm)
