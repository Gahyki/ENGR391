import numpy as np

#x0
t = 0
#y0
w = 1

#steps
h = 0.2

#evaluated value of x
r = 1

#nb of looping
n = int(abs((r-t)/h))

def f(x, y):
    #function
    return x*y + x**3

def RKt(t, w):
    for i in range(n):
        k1 = f(t, w)
        k2 = f(t + h, w + k1*h)
        print(str(t) + " " + str(w))
        w += h/2*(k1 + k2)
        t += h
    return w


def RKm(t, w):
    for i in range(n):
        k1 = f(t, w)
        k2 = f(t + h/2, w + k1*h/2)
        w += h*k2
        t += h
    return w

def e(h1, h2, w):
    return abs((w*h2 - w*h1)/((h1/h2)**2 - 1))
'''
a = RKt(t, w)
print('{0:.16f}'.format(a))'''
b = RKm(t, w)
print('{0:.16f}'.format(b))
#print(e(1, h, a))
