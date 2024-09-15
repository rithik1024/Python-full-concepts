s="hello world"
rep=""
for i in s:
 if s.count(i)>1:
    rep+="*"
 else:
     rep+=i
print(rep)