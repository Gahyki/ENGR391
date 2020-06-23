import numpy as np

upper = 4
lower = 0

#check table 79 - 6
w0 = 5/9
w1 = 8/9
w2 = 5/9

def f(x):
    #define function here
    return x/(x**2 + 9)**(1/2)

def var(x):
    return (upper-lower)/2*x + (upper+lower)/2

def i(x, y, z):
    return (upper-lower)/2*(w0*f(x) + w1*f(y) + w2*f(z))
