from sympy import symbols, evalf, solve, diff
from sympy import init_printing

init_printing()

VDD = 3
RD = 5e3
kn = 200e-6
W = 10e-6
L = 1e-6
Vt = 0.6

vi, vo = symbols('vi vo', positive=True)
ID = kn / 2 * W / L * (vi - Vt)**2
eq1 = VDD - ID * RD - vo
eq2 = vo + Vt - vi
sol = solve((eq1, eq2), vi, vo, dict=True)
vi1 = sol[0][vi]
vo1 = sol[0][vo]

print('Vi=%f (V)' % vi1)
print('Vo=%f (V)' % vo1)
