from sympy import *
import numpy as np
x = Symbol("x")

#enter function here
y = x**5 - 2*x**4 + 2*x**2 - x
derived = y.diff(x)

root = float(input("What is the root: "))

def be(root):
    return abs(y.subs(x, root))
    
def fe(root):
    return be(root)/abs(derived.subs(x, root))
print("Backward error: " + str(be(root)))
print(derived)
print("Forward error: " + str(fe(root)))
