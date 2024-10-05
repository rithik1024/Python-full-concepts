num=15
for i in range(5,0,-1):
    print(" "*(5-i),end=" ")
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()