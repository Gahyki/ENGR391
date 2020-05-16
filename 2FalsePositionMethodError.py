import numpy as np
def f(x):
    #define your function here
    return x**2 - 3

def m(a, b):
    #middle
    return (a+b)/2

def xc(a, b):
    return (a*f(b) - b*f(a))/(f(b)-f(a))

def inter(a, b, xc):
    if f(a)*f(xc) < 0:
        return (a, xc)
    elif f(b)*f(xc) < 0:
        return (xc, b)
    else:
        return "This doesn't work"

def tolerance(a, b):
    return abs((b - a)/2)

#running the script
err = float(input("Acceptance error value: "))
a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))
it = 0
while tolerance(a, b) >= err:
    print("\n")
    middle = xc(a,b)
    iteration = inter(a, b, middle)
    it += 1
    print(it)
    print(iteration)
    if iteration == "This doesn't work":
        break
    before = tolerance(a, b)
    a = iteration[0]
    b = iteration[1]
    print(tolerance(a, b))
    if before == tolerance(a, b):
        break
