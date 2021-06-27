from sympy import symbols, nsolve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

dVic=20
dVos=1e-3

CMRR=-20*log10(dVos/dVic)

print('CMRR=%f (db)' % CMRR)
