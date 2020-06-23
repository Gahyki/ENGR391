import numpy as np

upper = 5
lower = 0
c = ((upper - lower)/6)
m = 6

def f(x):
    #the function
    return (5*np.cos(x**2))/(x**4+5)**(1/2)

def simpson():
    return c*(f(upper) + 4*f((upper+lower)/2) + f(lower))

print("point: " + '{0:.16f}'.format(simpson()))

def comp(x):
    total = 0
    tu = (upper-lower)/x + lower
    tl = lower
    while tu <= upper:
        tr = (tu - tl)/6*(f(tu) + 4*f((tu+tl)/2) + f(tl))
        total += tr
        tu += (upper-lower)/x
        tl += (upper-lower)/x
    return total

print("comp: " + '{0:.16f}'.format(comp(m)))
