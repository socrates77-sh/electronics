from sympy import symbols, simplify, evalf, solve, diff
from sympy import init_printing
from numpy import log, sqrt

init_printing()

un = 650e-4
Cox = 1.38e-3
Vt = 0.7
ID = 200e-6

print('Part 1')
# Vov = symbols('Vov', positive=True)
# sol = solve(un * Cox / 2 * 10 * Vov**2 - ID)
Vov = sqrt(ID / (0.5 * un * Cox * 10))
VGS = Vov + Vt
Vo1 = 3 - VGS

print('Vo=%f (V)' % Vo1)
print('Av=%f' % 1)

print('Part 2')
gamma = 0.19
phi = 0.3
VSB = Vo1
Vt2 = Vt + gamma * ((2 * phi + VSB)**0.5 - (2 * phi)**0.5)
Vo2 = 3 - Vov - Vt2
chi = gamma / (2 * (2 * phi + Vo2)**0.5)
Av2 = 1 / (1 + chi)

print('Vo=%f (V)' % Vo2)
print('Av=%f' % Av2)

print('Part 3')
RL = 100e3
ID3 = ID + Vo2 / RL
Vov3 = sqrt(ID3 / (0.5 * un * Cox * 10))
VGS3 = Vov3 + Vt2
Vo3 = 3 - VGS3
gm3 = sqrt(2 * ID3 * un * Cox * 10)
Rout = 1 / (gm3 * (1 + phi))
Av3 = Av2 * RL / (RL + Rout)

print('Vo=%f (V)' % Vo3)
print('Av=%f' % Av3)

print('Part 4')
RL = 10e3
ID4x = ID + Vo3 / RL
Vov4x = sqrt(ID4x / (0.5 * un * Cox * 10))
VGS4x = Vov4x + Vt2
Vo4x = 3 - VGS4x
VSB = Vo4x
Vt4 = Vt + gamma * ((2 * phi + VSB)**0.5 - (2 * phi)**0.5)
ID4 = ID + Vo4x / RL
Vov4 = sqrt(ID4 / (0.5 * un * Cox * 10))
VGS4 = Vov4 + Vt4
Vo4 = 3 - VGS4
gm4 = sqrt(2 * ID4 * un * Cox * 10)
Rout = 1 / (gm4 * (1 + phi))
Av4 = Av2 * RL / (RL + Rout)

print('Vo=%f (V)' % Vo4)
print('Av=%f' % Av4)