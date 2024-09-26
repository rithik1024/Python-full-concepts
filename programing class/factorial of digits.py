#1! 4!  5!
num=int(input("enterthe number:"))   
fac=1
res=0
temp=0
for i in range(0,4):
    temp=num%10
    temp=int(temp)
    for j in range(1,temp+1):
       fac+=fac*1
    res=res+fac
    num=num/10
print(res)

#1+24+120