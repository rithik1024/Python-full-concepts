a=[2,3,4,5,9,1,45,4,9]
new=[]
res=[]
i=0
c=1
while i<len(a):
    new.append(a[i])
    i+=1
    if len(new)==3:
        res.append(max(new))
        new=[]  
        i=c
        c+=1   
print(res)