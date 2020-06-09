import numpy as np

upper = 4.6
lower = 0.9
c = ((upper - lower)/6)

def f(x):
    #the function
    return (np.cos(1.3*x)*np.e**(-3.6*x))

def simpson():
    return c*(f(upper) + 4*f((upper+lower)/2) + f(lower))

print(simpson())
