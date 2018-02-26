r=input("Enter number:\n")
l=len(str(r))
n=input("Enter the number of iterations:\n")
list = []

for i in range(n):
    x=str(r*r)
    if l % 2 == 0:
        x = x.zfill(l*2)
    else:
        x = x.zfill(l)
    y=(len(x)-l)/2
    r=int(x[y:y+l])
    list.append(r)
    print r