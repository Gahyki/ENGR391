import numpy as np
#Isolate for x --> x = f(x)
counter = 0

def f(x):
    #insert function here
    return np.cos(x)

it = int(input("How many iterations would you like to have? "))
x = float(input("What is the initial guess? "))
print(counter)
print("x: " + str(x))
print("y: " + str(f(x)))

for element in range(it):
    print("\n")
    counter += 1
    x1 = f(x)
    x = x1
    print(counter)
    print("x: " + str(x))
    print("y: " + str(f(x1)))

