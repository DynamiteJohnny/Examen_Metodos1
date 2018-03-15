from random import *


def fun1(val):
    return 2*val


def fun2(val):
    res = 0
    if (val <= 6 and val >= 2):
        #print("Entro")
        res = -0.666 + (val/12)
        #print("res = %f" % (res))
    else:
        if (val > 6 and val <= 8):
            res = 1.3333 - (val/6)
            #print("res = %f" % (res))
        else:
            res = 0
            #print("res = %f" % (res))
    return res


def varianza(ls,media):
    a = len(ls)
    b = 1 / a
    acumulator = 0

    for i in range(0,a):
        acumulator += pow((ls[i] - media),2)

    return b*acumulator



def method():

    a = int(input("Limite inferior:\n"))
    b = int(input("Limite superior:\n"))
    n = int(input("Introduce n:\n"))
    m = float(input("Introduce m:\n"))


    numbers = []

    num = int(input("\t1. Función 1 (2x)\n\t2. Función 2 (-1/6 + x/12 | 4/3 - x/6)\nElige una opción: "))


    while True:
        if (len(numbers) == n):
            break
        else:
            r1 = random()
            r2 = random()
            #print("R1= %f\n R2 = %f" % (r1,r2))
            #r1 = float(input("Introduce r1:\n"))
            #r2 = float(input("Introduce r2:\n"))

            x_star = a + (b - a) * r1
            if num == 1:
                f_star = fun1(x_star)
            else:
                f_star = fun2(x_star)

            if (r2 <= (f_star/m)):
                numbers.append(x_star - 3)


    media = sum(numbers) / len(numbers)
    print("Numeros:")
    print (numbers)
    print ("\nMedia: %f" % (media))
    print ("Varianza: %f " % (varianza(numbers,media)))
    print ("X mínima : %f" % (min(numbers)))
    print ("X máxima : %f" % (max(numbers)))


method()
