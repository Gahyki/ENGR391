import numpy as np
from sympy import Matrix, S, linsolve, symbols
import math
#inputs
A = [[2,1,-1,1],[1,-2,1,-4],[3,-1,-2,-1],[-1,2,1,-2]]

anp = np.array(A)
cond = np.linalg.cond(anp, np.inf)
print(cond)
d = math.log10(cond)
#d + nb of req sig figs (round the number up)
sigfigs = 12
print(d + sigfigs)
