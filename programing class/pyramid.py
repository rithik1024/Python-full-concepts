n=3
for i in range(1,5):
    print(" "*(n),end=" ")
    n-=1
    for j in range(i):
        print('*',end=' ')
    print()
