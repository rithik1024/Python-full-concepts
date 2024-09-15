num=int(input("enter the limit:"))
a=num
b=1
for i in range(1,num+1):
    print(a,end=" ")
    print(b,end=" ")
    a-=1
    b+=1