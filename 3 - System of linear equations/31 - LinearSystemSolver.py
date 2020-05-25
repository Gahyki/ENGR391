import numpy as np
from sympy import Matrix, S, linsolve, symbols
#inputs
A = [[5,-3,2],[10,4,-1],[-4,10,0]]
XR = [[2.2],[4.2],[-4.1]]
B = [[4],[-2],[5]]
R = []

x, y, z = symbols("x, y, z")
asp = Matrix(A)
bsp = Matrix(B)
rsp = linsolve((asp, bsp), [x, y, z])
print(R)
