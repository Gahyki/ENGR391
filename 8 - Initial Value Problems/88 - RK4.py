import numpy as np

#x0
t = 0
#y0
w = 1

#evaluated x value
r = 4

#steps
h = 0.5

#nb of loops
n = int(r/h)

def f(x, y):
    #function
    return x**3/y**2

def RK4(t, w):
    for i in range(n):
        k1 = f(t, w)
        k2 = f(t + h/2, w + h/2*k1)
        k3 = f(t + h/2, w + h/2*k2)
        k4 = f(t + h, w + h*k3)

        w += h/6*(k1 + 2*k2 + 2*k3 + k4)
        t += h
    return t, k1, k2, k3, k4, w

def e(h1, h2, w):
    return abs((w*h2 - w*h1)/((h1/h2)**4 - 1))

print(RK4(t, w))
