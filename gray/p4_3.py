from sympy import symbols, solve, diff, log
from sympy.plotting import plot

un = 450e-4
eox = 3.9 * 8.86e-12
tox = 80e-10
dXd = 0.02e-6

Vout = 0.2
Iout = 50e-6
lamb = 0.01

kn = un*eox/tox

L = dXd/lamb

W = symbols('W', positive=True)
eq = W/L*kn/2*Vout**2 - Iout
sol = solve(eq)
W = sol[0]

print('W=%f (um)' % (W*1e6))
print('L=%f (um)' % (L*1e6))

# 56