"""
Métodos Cuantitativos y simulación

Alumnos:
    Shara Teresa González Mena
    Esteban Quintana Cueto
    Juan Luis Suárez Ruiz
"""
import math

print("Métodos Cuantitativos y simulación\nAlumnos:\n\tShara Teresa González Mena\n\tEsteban Quintana Cueto\n\tJuan Luis Suarez Ruiz\n\n")


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
options = { 1 : mm1,
            2 : mms
	   }

num = int(input("SISTEMAS DE COLAS:\n\t1. M/M/1\n\t2. M/M/S\n\nElige una opción: "))

options[num]()
