import numpy as np
from sympy import Matrix, S, linsolve, symbols
#inputs
A = [[3,-2,4],[-24,15,-27],[21,-9,10]]
#XR = [[2.2],[4.2],[-4.1]]
B = [[38],[-258],[92]]

x, y, z = symbols("x, y, z")
asp = Matrix(A)
bsp = Matrix(B)
rsp = linsolve((asp, bsp), [x, y, z])
print(rsp)
