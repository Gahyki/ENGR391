from sympy import *
import numpy as np
x = Symbol("x")

#enter function here
y = log(x - 3) + x - 2
derived = y.diff(x)

root = float(input("What is the root: "))

def back(root):
    return abs(y.subs(x, root))
    
def forw(root):
    return back(root)/abs(derived.subs(x, root))
print(back(root))
print(derived)
print(forw(root))
