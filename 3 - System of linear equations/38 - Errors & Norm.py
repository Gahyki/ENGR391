import numpy as np
from sympy import Matrix, S, linsolve, symbols
#inputs
A = [[3,2,7],[-2,4,-5],[1,0,4]]
XR = [[-8.3],[-14],[-3.5]]
B = [[-78],[0],[-26]]
R = []

x, y, z = symbols("x, y, z")
asp = Matrix(A)
bsp = Matrix(B)
rsp = linsolve((asp, bsp), [x, y, z])
print(rsp)

anp = np.array(A)
xr = np.array(XR)
b = np.array(B)
r = np.array(R)

def fe(r, xr):
    result = r - xr
    return np.linalg.norm(result, np.inf)

def rfe(r, xr):
    return fe(r, xr)/np.linalg.norm(r, np.inf)

def be(a, xr, b):
    result = a.dot(xr) - b
    return np.linalg.norm(result, np.inf)

def rbe(a, xr, b):
    print(np.linalg.norm(b, np.inf))
    return be(a, xr, b)/np.linalg.norm(b, np.inf)

def m(r, xr, a, b):
    return fe(r, xr)/be(a, xr, b)

#y is the order or the subscript of the norm
def norm(x, y):
    return np.linalg.norm(x, y)
