from random import *


def fun1(val):
    return 2*val


def fun2(val):
    res = 0
    if (val > 6):
        res = 1.3333 - (val/6)
    elif (val > 2):
        res = -0.666 + (val/12)
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
    m = int(input("Introduce m:\n"))

    numbers = []

    """num = int(input("\t1. Función 1 (2x)\n\t2. Función 2 (-1/6 + x/12 | 4/3 - x/6)\nElige una opción: "))"""


    while True:
        if (len(numbers) == n):
            break
        else:
            r1 = random()
            r2 = random()

            x_star = a + (b - a) * r1
            f_star = fun1(x_star)

            if (r2 <= (f_star/m)):
                numbers.append(x_star)


    media = sum(numbers) / float(len(numbers))
    print("Numeros:")
    print (numbers)
    print ("\nMedia: %f" % (media))
    print ("Varianza: %f " % (varianza(numbers,media)))
    print ("X máxima : %f" % (max(numbers)))


method()
