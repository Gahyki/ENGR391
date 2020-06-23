from sympy import *
import numpy as np
x = Symbol('x')

#formula
y = x - cos(x)

def root(a):
    return a - y.subs(x, a)/y.diff(x).subs(x, a)

def abserror(a, b):
    return abs(b - a)


try:
    counter = 0
    ask = int(input("Enter 0 to input the iteration\nEnter 1 to input the accepted error\nEnter your choice here: "))
    if ask == 0:
        it = int(input("Enter the number of iterations to execute: "))
        r = float(input("What is the initial value? "))
        r1 = root(r)
        print(counter)
        print("x: " + str(r))
        print("x1: " + str(r1))
        for element in range(it):
            print("\n")
            counter += 1
            print(counter)
            r = r1
            r1 = root(r)
            print("x: " + str(r))
            print("x1: " + str(r1))
            print("Error: " + str(abserror(r, r1)))
            
    elif ask == 1:
        err = float(input("Enter the accepted error value: "))
        r = float(input("What is the initial value? "))
        r1 = root(r)
        print(counter)
        print("x: " + str(r))
        print("x1: " + str(r1))
        print("Error: " + str(abserror(r, r1)))
        while abserror(r, r1) >= err:
            print("\n")
            counter += 1
            print(counter)
            r = r1
            r1 = root(r)
            print("x: " + str(r))
            print("x1: " + str(r1))
            print("Error: " + str(abserror(r, r1)))
            
    else:
        print("That is not an option.")
except:
    print("Something went wrong.")
