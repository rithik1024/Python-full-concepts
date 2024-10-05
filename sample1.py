lis=[]
listlen=5
numof=5
k=15
while numof >= 1:
    for i in range(k,0,-1):
        lis.append(i)
        if len(lis) == listlen:
            for j in lis:
               print(j,end=" ")
            print()
            lis.clear()
            listlen=listlen-1
    numof-=1
print(numof)
listlend=1
if numof==0:
    numofd=5
    while numofd >= 1:
        for y in range(1,k+1):
            lis.append(y)
            if len(lis) == listlend:
                for m in lis:
                     print(m,end=" ")
                print()
                lis.clear()
                listlend=listlend+1
        numofd-=1