s="bunch of code"
l=s.split()
d={}
for i in l:
    d[i]=len(i)
print(list(d.items()))
for i in list(d.items()):
    print(i)