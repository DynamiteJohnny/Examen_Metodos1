import numpy

# Policy will return the number of policy of each posibility. Ex: s = [001]
def policy(n, actions):
    convert_string = "01"
    if n < actions:
        return convert_string[n]
    else:
        # // operator return floor division
        return policy(n//actions, actions) + convert_string[n % actions]

# Función de eliminación gausseana encontrado en internet
def gauss(A, b):
    """
    Gaussian elimination with partial pivoting.
    % input: A is an n x n nonsingular matrix
    %        b is an n x 1 vector
    % output: x is the solution of Ax=b.
    % post-condition: A and b have been modified.
    """
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for k in range(n-1):
        maxindex = abs(A[k:, k]).argmax() + k
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        # Swap rows
        if maxindex != k:
            A[[k, maxindex]] = A[[maxindex, k]]
            b[[k, maxindex]] = b[[maxindex, k]]
        for row in range(k+1, n):
            multiplier = A[row][k]/A[k][k]
            # the only one in this column since the rest are zero
            A[row][k] = multiplier
            for col in range(k + 1, n):
                A[row][col] = A[row][col] - multiplier*A[k][col]
            # Equation solution column
            b[row] = b[row] - multiplier*b[k]
    x = numpy.zeros(n)
    k = n-1
    x[k] = b[k]/A[k, k]
    while k >= 0:
        x[k] = (b[k] - numpy.dot(A[k, k+1:], x[k+1:]))/A[k, k]
        k = k-1
    return x


def main():
    print("\nMétodos Cuantitativos y simulación\nAlumnos:\n\tShara Teresa González Mena\n\tEsteban Quintana Cueto\n\tJuan Luis Suarez Ruiz\n")
    print("\n Iteración de políticas:\n")
    # Load files
    P = []
    R = []
    maxV = []
    policies = []
    with open("matrix_p.txt", "r") as f:
        for line in f:
            P.append(numpy.matrix(line))

    with open("matrix_r.txt", "r") as f:
        for line in f:
            R.append(numpy.matrix(line))

    alpha = float(input("Ingrese el valor de alpha: "))
    states = int(input("Ingrese el número de estados: "))
    actions = len(P)

    print(" ------------ Valores iniciales ----------\n")
    print("alpha = ", alpha, "Estados = ", states, "Actions = ", actions)
    for i in range(actions):
        print("P", i, " = \n", P[i], "\n")
        print("R", i, " = \n", R[i], "\n")

    # Policies' posibilities
    policyPosib = pow(actions, states)
    print("Posibilidades de políticas", policyPosib)

    CS = []
    for i in range(actions):
        for j in range(states):
            # Will get line per line of P and R
            auxP = numpy.squeeze(numpy.array(P[i][j]))
            auxR = numpy.squeeze(numpy.array(R[i][j]))
            auxCS = 0
            for k in range(states):
                # Multiply element k of the line auxP * element k of line auxR
                auxCS += auxP[k] * auxR[k]
            CS.append(auxCS)
    CS = numpy.reshape(CS, (actions, states))

    for i in range(actions):
        print("\nC (s =", i, ") = ", CS[i])


    S = []
    for i in range(policyPosib):
        #print("---- i = ", i)
        pos = policy(i, actions)
        pos = ((states - len(pos)) * "0") + pos
        print("\n--------  Política = ", pos , "------------\n")
        policies.append(pos)
        aux = 0
        C = []
        newP = []
        newR = []
        for s in range(states):
            #print("--- s = ", s)
            indexC = int(pos[s])
            auxP = numpy.squeeze(numpy.array(P[indexC][s]))
            auxR = numpy.squeeze(numpy.array(R[indexC][s]))
            auxC = 0

            # C values for the evaluated policy
            for j in range(states):
                auxC += auxP[j] * auxR[j]
            C.append(round(auxC, 4))
            newP.append(auxP)
            newR.append(auxR)


        # Create new P and R according to the evaluated policy
        newP = numpy.reshape(newP, (states, states))
        newR = numpy.reshape(newR, (states, states))

        g = newP.copy()

        for i in range(states):
            auxVs = 0
            for j in range(states):
                if i == j:
                    aux = 1 - (alpha * g[i][j])
                else:
                    aux = -alpha * g[i][j]
                g[i][j] = aux

        V = gauss(numpy.copy(g), numpy.copy(C))
        Vk = []
        for k in range(actions):
            for i in range(states):
                auxVs = 0
                auxP = numpy.squeeze(numpy.array(P[k]))
                for j in range(states):
                    auxVs += alpha * auxP[i][j] * V[j]
                    # print(alpha, "(", auxP[i][j], "*", V[j], ")")
                auxVs += CS[k][i]
                # print(auxVs)
                Vk.append(auxVs)

        Vk = numpy.reshape(Vk, (actions, states))
        print("P = ")
        print(newP, "\n")
        print("R = ")
        print(newR, "\n")
        for i in range(states):
            print("C%d = %f" % (i, C[i]))
        print("\n")
        for i in range(states):
            print("V(%d) = %f" % (i, V[i]))

        print("\nMEJORAMIENTO DE POLÍTICA:")
        for i in range(actions):
            print("V(s = %d)"%(i))
            print(Vk[i])

        print("\nV máxima: ", Vk.max())
        maxV.append(Vk.max())

        #Las soluciones quedan guardadas en el arreglo maxV

main()
