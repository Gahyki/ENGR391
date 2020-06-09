import numpy as np
upper = 5.8
lower = 1.7

def f(x):
    return (np.e**(-1.5*x**2))

def trapezoid():
    return (upper-lower)*(f(upper) + f(lower))/2

print(trapezoid())
