import numpy as np
#inputs
a = np.array([[5,-3,2],[10,4,-1],[-4,10,0]])
xr = np.array([[2.2],[4.2],[-4.1]])
b = np.array([[4],[-2],[5]])
r = np.array([])

def forward(r, xr):
    result = r - xr
    return np.linalg.norm(result, np.inf)

def relforward(r, xr):
    return foward(r, xr)/np.linalg.norm(r, np.inf)

def backward(a, xr, b):
    result = a.dot(xr) - b
    return np.linalg.norm(result, np.inf)

def relbackward(a, xr, b):
    print(np.linalg.norm(b, np.inf))
    return backward(a, xr, b)/np.linalg.norm(b, np.inf)
