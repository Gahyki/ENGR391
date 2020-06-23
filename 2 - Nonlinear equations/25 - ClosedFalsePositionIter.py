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

#running the script
its = int(input("How many iterations are required? ")) + 1
a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))
for i in range(its):
    print("\n")
    #change the range
    middle = xc(a,b)
    iteration = inter(a, b, middle)
    print(iteration)
    if iteration == "This doesn't work":
        break
    a = iteration[0]
    b = iteration[1]
    print("Approximation of the root is: " + str(m(a, b)))
