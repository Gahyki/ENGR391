import numpy as np
from sympy import *

x = Symbol('x')

#formula
y = x**5 - 2*x**4 + 2*x**2 - x
r = -1

#order 1
bi = 1/2
fp = abs(y.diff(x))

#order 2
nt = abs(y.diff(x).diff(x).subs(x, r)/(2*y.diff(x).subs(x, r)))

def e(l, e, a):
    #x = previous iteration error value
    #a = order
    return l*e**a

print(e(nt, 0.02, 2))
