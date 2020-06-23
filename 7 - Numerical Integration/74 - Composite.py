import numpy as np

upper = 2
lower = 1
m = 4

def f(x):
    return np.log(x)

def compt():
    h = (upper-lower)/m
    xi = np.linspace(lower, upper, m + 1)
    return h/2*(2*sum(f(xi)) - f(upper) - f(lower))

print("Trapezoid: " + str(compt()))

def comps():
    h = (upper-lower)/(2*m)
    x1 = np.linspace(lower+h, upper-h, m)
    x2 = np.linspace(lower+2*h, upper-2*h, m-1)
    return h/3*(f(upper) + f(lower) + 4*sum(f(x1)) + 2*sum(f(x2)))

print("Simpson: " + str(comps()))
