from sympy import *
import numpy as np
x = Symbol('x')

#formula
y = x**5 - 2*x**4 + 2*x**2 - x

def root(a):
    return a - y/y.diff(a)

def abserror(a, b):
    return abs(b - a)

ask = int(input("Enter 0 to input the iteration\nEnter 1 to input the accepted error\nEnter your choice here: "))

try:
    if ask == 0:
        it = int(input("Enter the number of iterations to execute: "))
        print(y)
        
        for element in range(it):
            
    elif ask == 1:
        err = float(input("Enter the accepted error value: "))
        print(1)
    else:
        print("That is not an option.")
except:
    print("That is not an option.")
