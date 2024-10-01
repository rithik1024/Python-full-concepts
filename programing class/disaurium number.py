num=int(input("enter the number:"))
temp=0
sum=0
while num>0:
     l=len(str(num))
     temp=num%10
     sum+=temp**int(l)
     num=num//10
print(sum)