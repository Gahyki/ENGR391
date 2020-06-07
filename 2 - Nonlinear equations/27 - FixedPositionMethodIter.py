import numpy as np
#Isolate for x --> x = f(x)
counter = 0

def f(x):
    #insert function here
    return np.e**(x)+ 4*x**2

it = int(input("How many iterations would you like to have? "))
x = float(input("What is the initial guess? "))
print(counter)
print(f(x))

for element in range(it):
    print("\n")
    counter += 1
    x1 = f(x)
    x = x1
    print(counter)
    print(f(x1))

