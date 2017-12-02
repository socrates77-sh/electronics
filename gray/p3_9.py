from sympy import symbols, simplify, evalf, solve, diff
from sympy import init_printing
from numpy import log, sqrt

init_printing()

un = 650e-4
Cox = 1.38e-3
Vt = 0.7
ID = 200e-6

print('Part 1')
Vov = symbols('Vov', positive=True)
sol = solve(un * Cox / 2 * 10 * Vov**2 - ID)
VGS = sol[0] + Vt
Vo1 = 3 - VGS

print('Vo=%f (V)' % Vo1)
print('Av=%f' % 1)

print('Part 2')
gamma = 0.19
phi = 0.3
VSB = Vo1
Vt2 = Vt + gamma * ((2 * phi + VSB)**0.5 - (2 * phi)**0.5)
Vo2 = 3 - sol[0] - Vt2
chi = gamma / (2 * (2 * phi + VSB)**0.5)
Av = 1 / (1 + chi)

print('Vo=%f (V)' % Vo2)
print('Av=%f' % Av)
