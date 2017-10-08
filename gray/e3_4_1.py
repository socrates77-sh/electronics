VT = 26e-3

b0 = 100
IC2 = 100e-6
I_BIAS = 10e-6

IB2 = IC2 / b0
IE1 = IB2 + I_BIAS

gm1 = IE1 / VT
rpi1 = b0 / gm1
gm2 = IC2 / VT
rpi2 = b0 / gm2
rpic = rpi1 + (b0 + 1) * rpi2
bc = b0 * (b0 + 1)
gmc = gm2 / (1 + (rpi1 / ((b0 + 1) * rpi2)))

print('rpic=%f (kohm)' % (rpic * 1e-3))
print('bc=%f' % bc)
print('gmc=%f (A/V)' % gmc)
