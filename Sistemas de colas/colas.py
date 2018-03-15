"""
Métodos Cuantitativos y simulación

Alumnos:
    Shara Teresa González Mena
    Esteban Quintana Cueto
    Juan Luis Suárez Ruiz
"""
import math

print("Métodos Cuantitativos y simulación\nAlumnos:\n\tShara Teresa González Mena\n\tEsteban Quintana Cueto\n\tJuan Luis Suarez Ruiz\n\n")


def MMs():
    print("\n***** M/M/s=tiempos de llegada y tiempo de servicio exponencial y s es el número de servidores *****")

    lam = float(input("Introduce el valor de lambda(Tasa media de llegadas) = "))
    miu = float(input("Introduce el valor de Miu(Numero esperado de clientes en cola) = "))

    gv = float(input("Seleccione el valor que le dan: \n\t1)Wq\n\t2)Ws\n\t3)Ls\n\t4)Lq"))
    
    if gv == 1:
        wq = float(input("Introduce el valor de Wq(Tiempo esperado de espera en la cola)="))
        lq = lam*wq
        ws = wq+(1/miu)
        ls = lam*ws
    elif gv == 2:
        ws = float(input("Introduce el valor de Ws(Tiempo esperado de espera en el sistema)="))
        ls = lam*ws
        wq = ws-(1/miu)
        lq = lam*wq
    elif gv == 3:
        ls = float(input("Introduce el valor de Ls(Número esperado de clientes en el sistema)="))
        ws = ls/lam
        wq = ws-(1/miu)
        lq = lam*wq
    elif gv == 4:
        lq = float(input("Introduce el valor de Lq(Número esperado de clientes en la cola)="))
        wq = lq/lam
        ls = lq+(lam/miu)
        lq = lam*wq
    else: 
        print("Opción invalida")
    
    print("\n\tLs = %f\tLq = %f\tWs = %f\tWq = %f"%(ls,lq,ws,wq))
 

    return 0

def MGs():
    print("Hola ke ase")
    return 0

options = {1 : MMs,
           2 : MGs,
	   }

num = int(input("DISCRETAS:\n\t1. M/M/s\n\t2. M/G/s\n\nElige una opción: "))

options[num]()
