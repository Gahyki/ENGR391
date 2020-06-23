import numpy as np

#x
x = [1,2,4]
#y
B = np.array([-0.4, -3.5, 2.9])

#Getting A
A = []
for i in range(len(x)):
    C = []
    for j in range(len(x)):
        C.append(x[i]**j)
    A.append(C)
A = np.array(A)

#Solving equation
V = np.linalg.inv(A).dot(B)

#Van Der Mond
def van(x):
    a = []
    for i in range(len(V)):
        a.append(x**i)
    return a
#nb to find
x = 3
F = np.array(van(x))
print(F)
print(V)
R = F.dot(V)
print(R)
