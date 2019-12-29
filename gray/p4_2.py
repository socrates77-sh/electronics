from sympy import symbols, solve, diff, log
from sympy.plotting import plot

IS = 5e-15
VA = 130
VBE = 0.7
bf = 200

VCC = 15
R = 10e3

Vout, Iout = symbols('Vout Iout')
VCE1 = VBE
VCE2 = Vout
I_IN = (VCC - VBE) / R
IS1 = 2 * IS
IS2 = 3 * IS


Iout = (IS2 / IS1) * I_IN * (1 + (VCE2 - VCE1) / VA) / \
    (1 + (1 + IS2 / IS1) / bf)

Iout_1 = Iout.evalf(subs={Vout: 1})
Iout_2 = Iout.evalf(subs={Vout: 5})
Iout_3 = Iout.evalf(subs={Vout: 30})

Rout_1 = VA/Iout_1
Rout_2 = VA/Iout_2
Rout_3 = VA/Iout_3

print('Iout=%f (mA)' % (Iout_1*1e3))
print('Iout=%f (mA)' % (Iout_2*1e3))
print('Iout=%f (mA)' % (Iout_3*1e3))
# plot(Iout, xlim=(-100, 50), ylim=(-10e-3, 10e-2))

print('Rout=%f (Kohm)' % (Rout_1*1e-3))
print('Rout=%f (Kohm)' % (Rout_2*1e-3))
print('Rout=%f (Kohm)' % (Rout_3*1e-3))
