import numpy as np
import math

upper = math.pi/2
lower = 0
m = 8

def f(x):
    #the function
    return (1-np.cos(x))/x**2

def point():
    return (upper-lower)*f((upper+lower)/2)

print("point: " + '{0:.16f}'.format(point()))

def comp(x):
    total = 0
    tu = (upper-lower)/x + lower
    tl = lower
    while tu <= upper:
        tr = (tu - tl) * f((tu + tl)/2)
        total += tr
        tu += (upper-lower)/x
        tl += (upper-lower)/x
        print(tu)
    return total

print("comp: " + '{0:.16f}'.format(comp(m)))
