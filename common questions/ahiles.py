a=[2,3,4,5,9,1,45,4,9]
b=[]
c=[]
n=0
for i in range(0,len(a)):
    b.append(a[i])
    if len(b)==3:
        c.append(b)
        b=[]
for i in range(0,len(c)):
    b.append(max(c[i]))
print(b)

""""
a=[2,3,4,5,9,1,45,4,9]
new=[]
res=[]
i=0
while i<len(a):
    new.append(a[i])
    i+=1
    if len(new)==3:
        res.append(max(new))
        new=[]        
print(res)
"""