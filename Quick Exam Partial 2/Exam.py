from random import randint

print("\n\tExamen rápido #3")
n = int(input("Introduce el valor de n = "))
porcentaje = float(input("Introduce el porcentaje = "))

Matrix = [[0 for i in range(n)] for i in range(n)]
"""
for i in range(n):
	for j in range(n):
		Matrix[i][j] = 0
"""
for i in range(n):
	for j in range(n):
		print(Matrix[i][j], end = " ")
	print()


p = (n*n)*(porcentaje/100)	
round(p,0)

p = int(p)
print("\nP = %i\n"% i)

for i in range(p):
	r1 = r2 = 0
	while r1 == r2 :
		r1 = randint(0, n-1)
		r2 = randint(0, n-1)
	Matrix[r1][r2] = 1

for i in range(n):
	for j in range(n):
		print(Matrix[i][j], end = " ")
	print()
