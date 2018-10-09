from sympy import symbols, evalf, solve, diff, log

VT = 26e-3
R2 = 5e3
Iin = 1e-3

Iout = symbols('Iout', positive=True)
eq = VT * log(1e-3 / Iout) - R2 * Iout
sol = solve(eq)
print('Iout=%f (uA)' % (sol[0] * 1e6))
