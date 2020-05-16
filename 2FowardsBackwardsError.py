from sympy import *
import numpy as np
x = Symbol("x")

#enter function here
y = np.e**x + sin(x) - 4
derived = y.diff(x)

root = float(input("What is the root: "))

def back(root):
    return abs(y.subs(x, root))
    
def fow(root):
    return back(root)/abs(derived.subs(x, root))
print(back(root))
print(derived)
print(fow(root))
