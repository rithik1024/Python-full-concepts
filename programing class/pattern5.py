num=int(input('enter the number:' ))
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==j):
            print('$',end=" ")
        elif (j==(num+1-i)):#i+j==n   
            print('$',end=' ')
        else:
            print(j,end=" ")
    print()