from sympy import symbols, simplify, evalf, solve, diff
from sympy import init_printing

init_printing()

# ix = symbols('ix')
vx = symbols('vx')
re = symbols('re')
ro = symbols('ro')
gm = symbols('gm')

ve = vx * re / (re + ro)
ix = vx / (ro + re) - gm * ve

Ro = vx/ix
print(simplify(Ro))
