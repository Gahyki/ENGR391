import numpy as np
def f(x):
    #define your function here
    return x**3 - 7

def m(a, b):
    #middle
    return (a+b)/2

def inter(a, b, middle):
    if f(a)*f(middle) < 0:
        return (a, middle)
    elif f(b)*f(middle) < 0:
        return (middle, b)
    else:
        return "This doesn't work"

#running the script
its = float(input("How many iterations are required? "))
a = float(input("What is the value of a? "))
b = float(input("What is the value of b? "))
for i in range(its):
    #change the range
    print("\n")
    print(str(i + 1))
    middle = m(a,b)
    iteration = inter(a, b, middle)
    print(iteration)
    if iteration == "This doesn't work":
        break
    a = iteration[0]
    b = iteration[1]
    print("Root is: " + str(m(a, b)))
