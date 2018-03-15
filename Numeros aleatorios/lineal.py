
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
