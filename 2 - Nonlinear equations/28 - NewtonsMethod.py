from sympy import *
import numpy as np
x = Symbol('x')

#formula
y = x**5 - 2*x**4 + 2*x**2 - x

def root(a):
    return a - y.subs(x, a)/y.diff(x).subs(x, a)

def abserror(a, b):
    return abs(b - a)


try:
    counter = 0
    ask = int(input("Enter 0 to input the iteration\nEnter 1 to input the accepted error\nEnter your choice here: "))
    if ask == 0:
        it = int(input("Enter the number of iterations to execute: "))
        print(y)
        
        #for element in range(it):
            
    elif ask == 1:
        err = float(input("Enter the accepted error value: "))
        r = float(input("What is the initial value? "))
        r1 = root(r)
        print(r)
        print(r1)
        print(counter)
        print(y)
        while abserror(r, r1) >= err:
            counter += 1
            print(counter)
            
    else:
        print("That is not an option.")
except:
    print("Something went wrong.")
