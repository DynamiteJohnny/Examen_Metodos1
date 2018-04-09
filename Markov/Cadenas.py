def readMatrix(filename):
    f = open ( filename , 'r')
    l = [ map(int,line.split(',')) for line in f ]
    return l

matrix1 = readMatrix('./matrix1.txt')
matrix2 = readMatrix('./matrix2.txt')

for line in matrix1:
    print(list(line))
