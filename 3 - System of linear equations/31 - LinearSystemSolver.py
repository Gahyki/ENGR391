import numpy as np
from sympy import Matrix, S, linsolve, symbols
#inputs
A = [[1,1,1],[1,2,4],[1,3,9]]
B = [[7.7],[0.2],[-13.7]]

#sympy
x, y, z = symbols("x, y, z")
asp = Matrix(A)
bsp = Matrix(B)
rsp = linsolve((asp, bsp), [x, y, z])
print("Sympy: \n" + str(rsp) + "\n")

#numpy
anp = np.array(A)
bnp = np.array(B)
rnp = np.dot(np.linalg.inv(anp), bnp)
print("Numpy: \n" + str(rnp))

#TO GET D, MAKE MATRIX A AS THE LOWER OF LU
