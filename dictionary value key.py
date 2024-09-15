s="abcdABCD"
print(list(s))
di={}
for i in s:
    di[i]=ord(i)
print(di.items())
for i in di:
    print(list(di.items()))
for i in list(di.items()):
    for j in i:
     print(j,end=" ")
