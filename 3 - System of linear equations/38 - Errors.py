import numpy as np
from sympy import Matrix, S, linsolve, symbols
#inputs
A = [[3,2,7],[-2,4,-5],[1,0,4]]
XR = [[-8.3],[-14],[-3.5]]
B = [[-78],[0],[-26]]
R = [[-10], [-10], [-4]]

x, y, z = symbols("x, y, z")
asp = Matrix(A)
bsp = Matrix(B)
rsp = linsolve((asp, bsp), [x, y, z])
print(rsp)

anp = np.array(A)
xr = np.array(XR)
b = np.array(B)
r = np.array(R)

def forward(r, xr):
    result = r - xr
    return np.linalg.norm(result, np.inf)

def relforward(r, xr):
    return forward(r, xr)/np.linalg.norm(r, np.inf)

def backward(a, xr, b):
    result = a.dot(xr) - b
    return np.linalg.norm(result, np.inf)

def relbackward(a, xr, b):
    print(np.linalg.norm(b, np.inf))
    return backward(a, xr, b)/np.linalg.norm(b, np.inf)
