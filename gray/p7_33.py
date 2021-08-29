from sympy import symbols, solve, nsolve, diff
from sympy.plotting import plot
from resp import *
from math import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from control import *

ID1 = 1e-3
ID2 = 4e-3
Cgd1 = 0.05e-12
Cgs1 = 0.2e-12
Csb1 = Cdb1 = 0.09e-12
Vov1 = 0.3
Cgd2 = 0.2e-12
Cgs2 = 0.8e-12
Csb2 = Cdb2 = 0.36e-12
Vov2 = 0.3

Ai0 = 4

gm1 = 2*ID1/Vov1

T0 = (Cgs1+Cdb1+Cgs2+Cgd2)/gm1
f_3db = 1/(2*pi*T0)
tr = 0.35/f_3db

print('Ai0=%f' % Ai0)
print('f-3db=%f (KHz)' % (f_3db*1e-3))
print('tr=%f (ns)' % (tr*1e9))

# 219
