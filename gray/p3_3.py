from sympy import symbols, evalf, solve, diff
from sympy import init_printing

init_printing()
VT = 26e-3
beta = 200
VA = 120

Rs = 50e3
Rc = 50e3

Ic, Av = symbols('Ic Av')
Av = -beta * ((VA / Ic) * Rc / (VA / Ic + Rc)) / (beta * VT / Ic + Rs)
Ic_opt = solve(diff(Av, Ic))[1]
Av_opt = Av.evalf(subs={Ic: Ic_opt})
V_Rc = Ic_opt * Rc

print('Ic=%f (mA)' % (Ic_opt * 1e3))
print('Av=%f' % Av_opt)
print('V_Rc=%f (V)' % V_Rc)
