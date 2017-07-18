#Metodo Jacobi
#Erick Mora, Isaac Pilatuna

import random 
import numpy as np

n=200
A=np.random.random((n,n))
b=np.random.random(n)
D=np.zeros((n,n))
R=np.zeros((n,n))

for i in range (0,n):
	for j in range (0,n):
		D[i][i]=1.0/A[i][i]
		R[i][j]=A[i][j]
		R[i][i]=0.0

x0=np.random.random(n)
x1=np.random.random(n)

while (x1.all()!=x0.all()):
	for i in range (0,n):
		for j in range (0,n):
			x0[i]=x1[i]
			x1[i]=D[i][j]*(b[i]-R[i][j]*x0[i])


print(A)
print("\n")
print(b)
print("\n")
print(R)
print("\n")
print(D)
print("\n")
print(x0)
print("\n")
print(x1)
print("\n")
