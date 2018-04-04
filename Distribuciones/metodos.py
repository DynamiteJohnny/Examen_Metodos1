"""
Métodos Cuantitativos y simulación

Alumnos:
    Shara Teresa González Mena
    Esteban Quintana Cueto
    Juan Luis Suárez Ruiz
"""
import math

print("Métodos Cuantitativos y simulación\nAlumnos:\n\tShara Teresa González Mena\n\tEsteban Quintana Cueto\n\tJuan Luis Suarez Ruiz\n\n")

def formulas_generales():
    print("\n ***** Formulas Generales (Valor esperado, varianza, desviación estándar) *****\n")
    noX = int(input("Ingresa el número de x's: "))
    x = [0] * noX
    p = [0] * noX
    f = [0] * noX
    valor_esperado = 0
    varianza = 0

    for i in range(0, noX):
        x[i] = float(input("\nx = "))
        p[i] = float(input("p(%d) = " % (x[i])))
        valor_esperado += x[i]*p[i]
    f[0] = p[0]

    print("\n---- Resultados -----")
    for i in range(0, noX):
        if i > 0:
            f[i] = f[i-1] + p[i]
        print("F(%d) = %f" % (x[i],f[i]), end= " | ")
        varianza += math.pow((x[i]-valor_esperado),2)*p[i]
    desvest = math.sqrt(varianza)

    print("\n\n\tValor esperado = %f" % (valor_esperado))
    print("\tVarianza = %f" % (varianza))
    print("\tDesviación estándar = %f" % (desvest))

    return 0;

def uniforme_discreta():
    print("\n***** Distribución Uniforme Discreta *****\n")
    noX = int(input("Ingresa el número de x's: "))
    x = [0] * noX
    p = [0] * noX
    f = [0] * noX
    valor_esperado = 0
    varianza = 0

    for i in range(0, noX):
        x[i] = float(input("\nx = "))
        p[i] = float(input("p(%d) = " % (x[i])))
        valor_esperado += x[i]*p[i]
    f[0] = p[0]

    print("\n---- Resultados -----")
    for i in range(0, noX):
        if i > 0:
            f[i] = f[i-1] + p[i]
        print("F(%d) = %f" % (x[i],f[i]), end= " | ")
        varianza += math.pow((x[i]-valor_esperado),2)*p[i]

    print("\n\n\tValor esperado = %f" % (valor_esperado))
    print("\tVarianza = %f" % (varianza))
    print("\tDesviación estándar = %f" % (math.sqrt(varianza)))

    return 0;

def binomial():
    print("\n***** Distribución Binomial *****\n")
    p = float(input("Probabilidad de éxito p = "))
    q = float(input("Probabilidad de fracaso q = "))
    n = int(input("Número de pruebas n = "))
    acum = int(input("\n¿Qué deseas calcular?:\n\t1. Normal\n\t2. Acumulativa\n"))
    prob = 0

    if acum == 1:
        k = int(input("Introduce k = "))
        print("\n---- Resultados ----")
        prob = (math.factorial(n)/(math.factorial(k)*math.factorial(n-k))) * math.pow(p,k) * math.pow(q,(n-k))
        print("\n\tp(k = %i) = %f" % (k, prob))
    else:
        x1 = int(input("Introduce el límite inferior = "))
        x2 = int(input("Introduce el límite superior = "))
        print("\n---- Resultados ----")
        for i in range(x1,x2+1):
            prob += (math.factorial(n)/(math.factorial(i)*math.factorial(n-i))) * math.pow(p,i) * math.pow(q,(n-i))
        print("\n\tp(%i <= X <= %i) = %f" % (x1, x2, prob))

    print("\n\tValor esperado = %f" % (n*p))
    print("\tVarianza = %f" % (n*p*q))
    print("\tDesviación estándar = %f" % (math.sqrt(varianza)))

    return 0

def poisson():
    print("\n ***** Distribución Poisson *****")
    l = float(input("Introduce el valor de lambda = "))
    acum = int(input("¿Qué deseas calcular?\n\t1. Normal\n\t2. Acumulativa\n"))
    prob = 0

    if acum == 1:
        x = int(input("Introduce el valor de x = "))
        prob = (math.exp(l * -1) * math.pow(l ,x) ) / math.factorial(x)
        print("\n---- Resultados -----")
        print("\n\tp(X = %i) = %f" % (x, prob))
    else:
        x1 = int(input("Introduce el límite inferior = "))
        x2 = int(input("Introduce el límite superior = "))
        print("\n---- Resultados ----")
        for i in range(x1,x2+1):
            prob += (math.exp(l * -1) * math.pow(l ,i) ) / math.factorial(i)
        print("\n\tp(%i <= X <= %i) = %f" % (x1, x2, prob))

    print("\n\tValor esperado = %f" % (l))
    print("\tVarianza = %f" % (l))
    print("\tDesviación estándar = %f" % (math.sqrt(l)))

def procesos_poisson():
    print("\n***** Procesos de Poisson *****")
    alpha = float(input("Introduce el valor de alpha = "))
    t = float(input("Introduce el valor de t = "))
    acum = int(input("¿Qué deseas calcular?\n\t1. Normal\n\t2. Acumulativa\n"))
    prob = 0

    if acum == 1:
        x = int(input("Introduce el valor de x = "))
        prob = (math.exp(alpha * t * -1) * math.pow(alpha * t ,x) ) / math.factorial(x)
        print("\n---- Resultados -----")
        print("\n\tp(X = %i) = %f" % (x, prob))
    else:
        x1 = int(input("Introduce el límite inferior = "))
        x2 = int(input("Introduce el límite superior = "))
        print("\n---- Resultados ----")
        for i in range(x1,x2+1):
            prob += (math.exp(alpha * t * -1) * math.pow(alpha * t ,i) ) / math.factorial(i)
        print("\n\tp(%i <= X <= %i) = %f" % (x1, x2, prob))

    print("\n\tValor esperado = %f" % (alpha * t))
    print("\tVarianza = %f" % (alpha * t))
    print("\tDesviación estándar = %f" % (math.sqrt(alpha * t)))

    return 0

def generador_congruencial_li():
    print("\n***** Generador congruencial de numeros aleatorios *****")
    a = float(input("Introduce el valor de a = "))
    c = float(input("Introduce el valor de c = "))
    Z0 = float(input("Introduce el valor de Z0 = "))
    m = float(input("Introduce el valor de m = "))
    ite = float(input("Introduce el numero de valores aleatorios que desea generar = "))
    Zi = Z0
    R = -1
    run = 1
    print("\n\tm = %f\tc = %f\tZ0 = %f\ta = %f"%(m,c,Z0,a))
 
    while run <= ite :
        Zi = ((a*Zi+c) % m)
        R = Zi/m
        print("\tZ%i = %f\tR = %f\tIter = %f\n "%(run,Zi,R,run))
        run = run +1

    return 0

def exponencial():
    print("\n***** Distribución Exponencial *****")
    l = float(input("Introduce el valor de lambda = "))
    acum = int(input("¿Qué deseas calcular?\n\t1. Normal\n\t2. Acumulativa\n"))
    prob = 0

    if acum == 1:
        x = int(input("Introduce el valor de x = "))
        prob = (1 - math.exp(l * x * -1)) - (1 - math.exp(l * (x-1) * -1))
        print("\n---- Resultados -----")
        print("\n\tp(X = %i) = %f" % (x, prob))
    else:
        x1 = int(input("Introduce el límite inferior = "))
        x2 = int(input("Introduce el límite superior = "))
        print("\n---- Resultados ----")
        prob = (1 - math.exp(l * x2 * -1)) - (1 - math.exp(l * x1 * -1))
        print("\n\tp(%i <= X <= %i) = %f" % (x1, x2, prob))

    print("\n\tValor esperado = %f" % (1/l))
    print("\tVarianza = %f" % (1 / math.pow(l,2)))
    print("\tDesviación estándar = %f" % (math.sqrt(1 / math.pow(l,2))))

    return 0

options = {1 : formulas_generales,
           2 : uniforme_discreta,
           3 : binomial,
           4 : poisson,
           5 : procesos_poisson,
           6 : exponencial,
	   7 : generador_congruencial_li,
	   }

num = int(input("DISCRETAS:\n\t1. Fórmulas generales\n\t2. Distribución uniforme discreta\n\t3. Distribución binomial\n\t4. Distribución Poisson\n\t5. Procesos de Poisson\nCONTINUAS:\n\t6. Distribución exponencial\nGeneradores:\n\t7. Generador congruencial lineal\n\nElige una opción: "))

options[num]()
