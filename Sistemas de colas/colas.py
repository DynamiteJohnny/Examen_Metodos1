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
-    print("\n***** Ley de little *****")
-
-    lam = float(input("Introduce el valor de lambda(Tasa media de llegadas) = "))
-    miu = float(input("Introduce el valor de Miu(Numero esperado de clientes en cola) = "))
-
-    gv = float(input("Seleccione el valor que le dan: \n\t1)Wq\n\t2)Ws\n\t3)Ls\n\t4)Lq"))
-
-    if gv == 1:
-        wq = float(input("Introduce el valor de Wq(Tiempo esperado de espera en la cola)="))
-        lq = lam*wq
-        ws = wq+(1/miu)
-        ls = lam*ws
-    elif gv == 2:
-        ws = float(input("Introduce el valor de Ws(Tiempo esperado de espera en el sistema)="))
-        ls = lam*ws
-        wq = ws-(1/miu)
-        lq = lam*wq
-    elif gv == 3:
-        ls = float(input("Introduce el valor de Ls(Número esperado de clientes en el sistema)="))
-        ws = ls/lam
-        wq = ws-(1/miu)
-        lq = lam*wq
-    elif gv == 4:
-        lq = float(input("Introduce el valor de Lq(Número esperado de clientes en la cola)="))
-        wq = lq/lam
-        ls = lq+(lam/miu)
-        lq = lam*wq
-    else:
-        print("Opción invalida")
-
-    print("\n\tLs = %f\tLq = %f\tWs = %f\tWq = %f"%(ls,lq,ws,wq))

def mm1():
    print("\n Modelo M/M/1")

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

def mms():

    return 0
options = { 1 : little,
            2 : mm1,
            3 : mms
	   }

num = int(input("SISTEMAS DE COLAS:\n\t1. Little\n\t2. M/M/1\n\t3. M/M/S\n\nElige una opción: "))

options[num]()
