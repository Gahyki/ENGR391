from sympy import sin, cos
import numpy as np

x = [-2,1,3]
y = [2,-1,1]

#linear square error

def xy():
    xy = []
    for i in range(len(x)):
        xy.append(x[i]*y[i])
    return xy
        
xy = xy()

def x2():
    x2 = []
    for i in range(len(x)):
        x2.append(x[i]**2)
    return x2

x2 = x2()

def a1():
    return (len(x)*sum(xy)-sum(x)*sum(y))/(len(x)*sum(x2)-sum(x)**2)

a1 = a1()

def a0():
    return 1/len(x)*sum(y)-a1*1/len(x)*sum(x)

a0 = a0()

def se(a0, a1):
    total = 0
    for i in range(len(x)):
        #function here
        total += float(y[i] - a0 - a1*x[i])**2
    return total

print(se(-4.8,1.3))
