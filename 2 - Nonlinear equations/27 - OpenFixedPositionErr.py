import numpy as np
#Isolate for x --> x = f(x)
counter = 1

def f(x):
    #insert function here
    return np.cos(x)

def tolerance(a, b):
    #could be relative so be careful
    return abs(b - a)

err = float(input("What is the accepted error tolerance? "))
x = float(input("What is the initial guess? "))
print(counter)
print(x)
print(f(x))
print(tolerance(x, f(x)))

while tolerance(x, f(x)) >= err:
    print("\n")
    counter += 1
    print(counter)
    x1 = f(x)
    x = x1
    print("x: " + str(x))
    print("y: " + str(f(x1)))
    print("Error: " + str(tolerance(x, f(x))))


