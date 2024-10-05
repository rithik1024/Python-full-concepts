num=int(input("enter the nu:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==j):
            print(i,end=" ")
        elif (j==num+1-i):
            print(i,end=" ")
        else:
            print('$',end=" ")
    print()
    