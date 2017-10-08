import matplotlib.pyplot as plt
from sympy import *
from control import *

init_printing()
plt.rc('figure', figsize=(8, 6))

s, B1 = symbols('s B1')

B1 = 25 * s / (2 * s**2 + 3 * s + 3)

D0 = denom(B1)
D1 = Poly(D0).all_coeffs()
D2 = [float(k) for k in D1]
N0 = numer(B1)
N1 = Poly(N0).all_coeffs()
N2 = [float(k) for k in N1]

B1b = tf(N2, D2)
bode(B1b, dB=True)

plt.show()
