import numpy as np

#value from function
xr = 23

#real value
r = 56

def abse():
    return abs(xr - r)

def rele():
    return abse()/abs(r)

print("absolute error: " + str(abse()))
print("relative error: " + str(rele()))
