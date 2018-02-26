from random import *

def fun(val):
    res = 0

    if (val > 6):
        res = 1.3333 - (val/6)
    elif (val > 2):
        res = -0.666 + (val/12)

    return val


def method():
    a = input("Limite inferior:\n")
    b = input("Limite superior:\n")

    n = input("Introduce n:\n")

    m = input("Introduce m:\n")

    print(m)

    numbers = []
    for i in range(n):
        r1 = random()
        r2 = random()

        x_star = a + (b - a) * r1
        f_star = fun(x_star)

        if (r2 <= (f_star/m)):
            numbers.append(x_star)

    print numbers

method()





