import numpy as np
from sympy import Matrix, S, linsolve, symbols
import math
#inputs
A = [[9,-2,6,1],[-10.5,-10,100,-4],[-9,-2,3,3],[-3,2,250,-2]]

anp = np.array(A)

#maximal magnification factor
cond = np.linalg.cond(anp, np.inf)
print("Cond: " + str(cond))

d = math.log10(cond)
print("d: " + str(d))

#d + nb of req sig figs (round the number up)
sigfigs = 12
print("Total nb of req sig figs: " + str(d + sigfigs))
