from numpy import linalg as LA

import numpy


def read_matrix(filename):
    array = []
    f = open(filename, 'r')
    lines = [map(int, line.split(',')) for line in f]

    for l in lines:
        array.append(list(l))

    matrix = numpy.asmatrix(array)

    return matrix


def elevate_matrix(matrix, n):
    return LA.matrix_power(matrix,n)


print("\nMétodos Cuantitativos y simulación\nAlumnos:\n\tShara Teresa González Mena\n\tEsteban Quintana Cueto\n\tJuan Luis Suarez Ruiz\n")
print("\n Elevación de matrices\n")


path = input("Ingrese un archivo de matriz (utilize paths relativos) Archivo de ejemplo: './matrix.txt' >  ")
A = read_matrix(path)
print(A)
print("\n")

power = int(input("Ingrese la potencia a la que elevará la matriz. Ej. 2 >  "))
result = elevate_matrix(A, power)

print(result)