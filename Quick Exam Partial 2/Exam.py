from random import randint

print("\n\tExamen rápido #3\n\tJuan Luis Suarez Ruiz\n\tShara Teresa González Mena\n\tEsteban Quintana Cueto")

def matA():
	n = int(input("Introduce el valor de n = "))
	porcentaje = float(input("Introduce el porcentaje = "))

	Matrix = [[0 for i in range(n)] for i in range(n)]

	for i in range(n):
		for j in range(n):
			print(Matrix[i][j], end = " ")
		print()

	p = (n*n)*(porcentaje/100)
	round(p,0)

	p = int(p)
	print("\nP = %i\n"% p)

	for i in range(p):
		r1 = r2 = 0
		while r1 == r2 :
			r1 = randint(0, n-1)
			r2 = randint(0, n-1)
		Matrix[r1][r2] = 1

	nummax = 0
	nummin = n
	cont = 0
	for i in range(n):
		for j in range(n):
			if Matrix[i][j] == 1:
				cont = cont + 1
			print(Matrix[i][j], end = " ")
		if cont > nummax:
			nummax = cont
		if cont < nummin:
			nummin = cont
		cont = 0
		print()


	print("Max = %i\tMin = %i"%(nummax,nummin))

def matB():
	n = int(input("Introduce el valor de n = "))
	porcentaje = float(input("Introduce el porcentaje = "))

	Matrix = [[0 for i in range(n)] for i in range(n)]

	for i in range(n):
		for j in range(n):
			print(Matrix[i][j], end = " ")
		print()

	p = (n*n)*(porcentaje/100)
	round(p,0)

	p = int(p)
	print("\nP = %i\n"% p)
	if (p % 2) != 0:
		p += 1
		print("\n Dado que es impar se toma P = %i\n"% p)
	print("P/2 = ", p/2)
	for i in range(int(p/2)):
		r1 = r2 = 0
		while r1 == r2 :
			r1 = randint(0, n-1)
			r2 = randint(0, n-1)
		Matrix[r1][r2] = 1
		Matrix[r2][r1] = 1

	nummax = 0
	nummin = n
	cont = 0
	for i in range(n):
		for j in range(n):
			if Matrix[i][j] == 1:
				cont = cont + 1
			print(Matrix[i][j], end = " ")
		if cont > nummax:
			nummax = cont
		if cont < nummin:
			nummin = cont
		cont = 0
		print()


	print("Max = %i\tMin = %i"%(nummax,nummin))

options = { 1 : matA,
            2 : matB
	   }

num = 0
while num != 3:
	num = int(input("\nElige la matriz que deseas probar:\n\t1. Matriz A\n\t2. Matriz B\n\t3. Salir\n>> "))
	options[num]()
