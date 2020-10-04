from sympy import symbols, solve, diff, log
from sympy.plotting import plot
from resp import *
from math import *

gm1 = 1.05e-3
gm2 = 0.95e-3
gm3 = 1.1e-3
gm4 = 0.9e-3

gm1_2 = 0.5*(gm1+gm2)
gm3_4 = 0.5*(gm3+gm4)
dgm1_2 = gm1-gm2
dgm3_4 = gm3-gm4

Gm_dm = gm1_2*((1-(dgm1_2/(2*gm1_2))**2)/(1+dgm3_4/(2*gm3_4)))

print('Gm[dm]=%f mA/V' % (Gm_dm*1e3))

# 86