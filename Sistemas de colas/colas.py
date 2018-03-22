"""
Métodos Cuantitativos y simulación

Alumnos:
    Shara Teresa González Mena
    Esteban Quintana Cueto
    Juan Luis Suárez Ruiz
"""
import math

print("Métodos Cuantitativos y simulación\nAlumnos:\n\tShara Teresa González Mena\n\tEsteban Quintana Cueto\n\tJuan Luis Suarez Ruiz\n\n")

def little():
    print("\nLEY DE LITTLE\n")
    lam = float(input("Valor de lambda(Tasa media de llegadas) = "))
    miu = float(input("Valor de Miu(Numero esperado de clientes en cola) = "))

    op = int(input("Elige una opción: \n\t1. Calcular las medidas de desempeño\n\t2. Factor de utilización con uno o más servidores\n>> "))

    if(op == 1):
        gv = float(input("\nValor dado en el problema: \n\t1)Wq\n\t2)Ws\n\t3)Ls\n\t4)Lq\n>>"))

        if gv == 1:
            wq = float(input("Valor de Wq(Tiempo esperado de espera en la cola)="))
            lq = lam*wq
            ws = wq+(1/miu)
            ls = lam*ws
        elif gv == 2:
            ws = float(input("Valor de Ws(Tiempo esperado de espera en el sistema)="))
            ls = lam*ws
            wq = ws-(1/miu)
            lq = lam*wq
        elif gv == 3:
            ls = float(input("Valor de Ls(Número esperado de clientes en el sistema)="))
            ws = ls/lam
            wq = ws-(1/miu)
            lq = lam*wq
        elif gv == 4:
            lq = float(input("Valor de Lq(Número esperado de clientes en la cola)="))
            wq = lq/lam
            ls = lq+(lam/miu)
            lq = lam*wq
        else:
            print("Opción invalida")

        print("\n\tLs = %f\tLq = %f\tWs = %f\tWq = %f"%(ls,lq,ws,wq))

    else:
        serv = int(input("\nCantidad de servidores: "))
        ro = lam / serv * miu
        print("\nro con %d servidores = %f\n" % (serv, ro))


    return 0

def mm1():
    print("\n MODELO M/M/1\n")

    lam = float(input("Lambda (Tasa media de llegadas) = "))
    miu = float(input("Miu (Tasa media de servicio) = "))

    ls = lam / (miu - lam)
    lq = pow(lam,2) / (miu * (miu - lam))
    ws = 1 / (miu - lam)
    wq = lam / (miu * (miu - lam))

    print("\nMedidas de desempeño del sistema: \n\tLs = %f\tLq = %f\tWs = %f\tWq = %f"%(ls,lq,ws,wq))
    op = 0
    while(op != 5):
        print("\nProbabilidades\n\t1. Pn (Probabilidad de tener n clientes)\n\t2. P(Ls > n)\n\t3. P(Ws > t)\n\t4. P(Wq > t)\n\t5. Salir")
        op = int(input("\n¿Qué probabilidad deseas calcular? "))
        ro = lam/miu

        if op == 1:
            n = int(input("Valor de n = "))
            p = (1 - ro) * pow(ro, n)
            print("Probabilidad de %d = %f" % (n, p))
        elif op == 2:
            n = int(input("Valor de n = "))
            p = pow(ro, n + 1)
            print("Probabilidad de Ls > %d = %f" % (n, p))
        elif op == 3:
            t = float(input("Valor de t = "))
            p = math.exp(-miu * (1 - ro) * t)
            print("Probabilidad de Ws > %f = %f" % (t, p))
        elif op == 4:
            t = float(input("Valor de t = "))
            p = ro * math.exp(-miu * (1 - ro) * t)
            print("Probabilidad de Wq > %f = %f" % (t, p))
    return 0

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def p0sum(lam,miu,s,ro):
	sum = 0
	for n in range(0,s):
 		sum = sum + ((math.pow((lam/miu),n)/factorial(n)))

	return (1/(sum+((math.pow((lam/miu),s))/(factorial(s)*(1 - ro)))))

def mms():
    print("\n MODELO M/M/1")

    lam = float(input("Lambda (Tasa media de llegadas) = "))
    miu = float(input("Miu (Tasa media de servicio) = "))
    s = int(input("Numero de servidores: "))

    ro = lam/(s*miu)
    print("ro = ", ro)

    p0 = p0sum(lam,miu,s,ro)
    lq = ((math.pow(lam/miu,s))*p0*ro)/(factorial(s)*math.pow(1 - ro,2))
    wq = lq/lam
    ws = wq + (1/miu)
    ls = lam*ws

    print("\nMedidas de desempeño del sistema: \n\tLs = %f\tLq = %f\tWs = %f\tWq = %f"%(ls,lq,ws,wq))
    op = 1
    while op == 1:
        n = float(input("\nLa probabilidad que desea calcular: "))
        pn = (math.pow(lam/miu,n))*p0/(factorial(n))
        print("\nProbabilidad: W%i = %f"%(n,pn))
        op = int(input("\n¿Desea calcular otra probabilidad?\n\t1. Si\n\t2. No\n>>"))


    return 0
options = { 1 : little,
            2 : mm1,
            3 : mms
	   }

num = int(input("SISTEMAS DE COLAS:\n\t1. Little\n\t2. M/M/1\n\t3. M/M/S\n\nElige una opción: "))

options[num]()
