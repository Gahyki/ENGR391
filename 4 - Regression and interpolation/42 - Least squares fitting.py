from sympy import sin, cos
import numpy as np

x = [0,1,2,3]
y = [-1.9,1,4.1,4.3]
total = 0


#Type 2
A = []
for i in range(len(x)):
    app = [1, np.sin(x[i]), np.cos(x[i])]
    A.append(app)
print(A)
B = [[-1.9],[1],[4.1],[4.3]]
T = np.transpose(A)
F = T.dot(A)
G= T.dot(B)
print(F)
print(G)
print("asdfasd")

thea = np.linalg.inv(F).dot(G)


#Type 1
a0 = thea[0][0]
a1 = thea[1][0]
a2 = thea[2][0]

for i in range(len(x)):
    s = (y[i] - a0 - a1*np.sin(x[i]) - a2*np.cos(x[i]))**2
    total += s
print(total)
