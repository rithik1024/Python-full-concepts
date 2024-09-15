names=["aadith","rithik"]
res=map(lambda i:i if i[0] in "aA" else 0,names)
print(list(res))
res1=filter(lambda i: i[0] in "aA",names)
print(list(res1))