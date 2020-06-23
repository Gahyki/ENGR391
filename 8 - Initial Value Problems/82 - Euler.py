import numpy as np

#initial value
t = 1
w = 1
h = 0.5
start = 1
end = 4

#counter
c = (end - start)/h

def f(x, y):
    #define function
    return 1 + y/x

for i in range(int(c) + 1):
    print("t: " + str('{0:.16f}'.format(t)))
    print("w: " + str('{0:.16f}'.format(w)) + "\n")
    w = w + h*f(t, w)
    t += h
    #c += 1
