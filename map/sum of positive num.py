nums=[1,-8,-3,4,]
res=list(map(lambda i:i if i >0 else 0 ,nums))
print(res)
a=filter(lambda i:i!=0,res)
for i in a:
    print(i,end=" ")
#print(list(a))