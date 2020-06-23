import numpy as np
def f(x):
    #define your function here
    return x**3 - 7

def m(a, b):
    #middle
    return (a + b) / 2

def inter(a, b, middle):
    if f(a) * f(middle) < 0:
        return (a, middle)
    elif f(b) * f(middle) < 0:
        return (middle, b)
    else:
        return "This doesn't work"

def tolerance(a, b):
    return abs((b - a)/2)

#running the script
err = float(input("Acceptance error value: "))
a = float(input("What is the value of a? "))
b = float(input("What is the value of b? "))
it = 0
print(it)
print("("+ str(a) + ", " + str(b) + ")")
print(tolerance(a, b))

while tolerance(a, b) >= err:
    print("\n")
    middle = m(a, b)
    iteration = inter(a, b, middle)
    it += 1
    print(it)
    print(iteration)
    if iteration == "This doesn't work":
        break
    a = iteration[0]
    b = iteration[1]
    print(tolerance(a, b))
    print("Root is: " + str(m(a, b)))
