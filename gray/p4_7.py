from sympy import symbols, solve, diff, log
from sympy.plotting import plot

un = 450e-4
eox = 3.9 * 8.86e-12
tox = 80e-10
dXd = 0.02e-6
Ld = 0.09e-6

Iout = 50e-6
Vout = 0.2

Cox = eox/tox

Ro = 1/((0.02/100)*Iout)
Vov = 0.5*Vout
gm = 2*Iout/Vov

ro = symbols('ro', positive=True)
eq = gm*ro*ro-Ro
sol = solve(eq)
ro = sol[0]

lamb = 1/(ro*Iout)
Leff = dXd/lamb

W_Leff = Iout*2/(un*Cox*Vov*Vov)

W = W_Leff*Leff

L = Leff+2*Ld

print('L=%f (um)' % (L*1e6))
print('W=%f (um)' % (W*1e6))

# 61
