"""
Métodos Cuantitativos y simulación

Alumnos:
    Shara Teresa González Mena
    Esteban Quintana Cueto
    Juan Luis Suárez Ruiz
"""
import math
print("Métodos cuantitativos y simulación\nAlumnos:\n\tShara Teresa González Mena\n\tEsteban Quintana Cueto\n\tJuan Luis Suarez Ruiz\n\n")


def mid():
    r = input("Enter number: ")
    l = len(r)
    n = int(input("Enter the number of iterations: "))
    print("X0 = ", r)

    for i in range(0,n):
        x = str(int(r)*int(r))
        print("----- Iteración %d -----\n\tX%d * X%d = " % (i + 1, i, i), x)
        if l % 2 == 0:
            x = x.zfill(l*2)
        else:
            x = x.zfill(l)
        y1 = len(str(r))/2
        y2 = y1 + len(str(r))
        r = int(x [ int(y1) : int(y2)])
        print("\tX%d = " % (i+1), r)
        print("\tR = 0.%d" % (r))


    print(r)

    return 0

def conglin():

    print("\n***** Generador congruencial de numeros aleatorios *****")
    a = float(input("Valor de a = "))
    c = float(input("Valor de c = "))
    Z0 = float(input("Valor de Z0 = "))
    m = float(input("Valor de m = "))
    ite = float(input("Valores aleatorios que desea generar = "))
    Zi = Z0
    R = -1
    run = 1
    print("\n\tm = %f\tc = %f\tZ0 = %f\ta = %f"%(m,c,Z0,a))

    while run <= ite :
        Zi = ((a*Zi+c) % m)
        R = Zi/m
        print("\n\tZ%i = %f\tR = %f\tIter = %d "%(run,Zi,R,run))
        run = run +1

    return 0

options = { 1 : mid,
            2 : conglin }

num = int(input("GENERACIÓN DE NÚMEROS ALEATORIOS:\n\t1. Cuadrados medios\n\t2. Congruencia lineal\n\nElige una opción:  "))

options[num]()
