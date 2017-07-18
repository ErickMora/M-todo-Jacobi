#Metodo Jacobi
#Erick Mora, Isaac Pilatuna

import random 
import numpy as np
import sys

n=int(sys.argv[1])
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
x1=np.zeros(n)

def jacobi(x0,x1):
	while (round(np.linalg.norm(np.dot(A,x1)-b),10)!=round(.0,10)):
		x0=x1
		x1=np.dot(D,(b-np.dot(R,x0)))

		if(round(np.linalg.norm(np.dot(A,x1)-b),10)==round(.0,10)):
			print("Solucion: ")
			print(x1)
			break
			jacobi(x0,x1)
		
print("Matriz A: ")
print(A)
print("Array b: ")
print(b)
		
jacobi(x0,x1)
