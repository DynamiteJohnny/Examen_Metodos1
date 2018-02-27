from random import *


def fun(val):
    return 2*val


def fun_two(val):
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
    print(len(ls))
    
    for i in range(len(ls)):
        acumulator += pow((ls[i] - media),2)

    return a*acumulator


def method():

    a = int(input("Limite inferior:\n"))
    b = int(input("Limite superior:\n"))
    n = int(input("Introduce n:\n"))
    m = int(input("Introduce m:\n"))

    numbers = []
    while True:
        if (len(numbers) == n):
            break
        else:
            r1 = random()
            r2 = random()

            x_star = a + (b - a) * r1
            f_star = fun(x_star)

            if (r2 <= (f_star/m)):
                numbers.append(x_star)

    print (numbers)
    print ("\nMedia: ")
    media = sum(numbers) / float(len(numbers))
    print (media)
    print ("\nVarianza")
    print (varianza(numbers,media))

method()
