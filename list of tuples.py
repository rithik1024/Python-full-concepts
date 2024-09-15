"""list of tuples with string and its length pair"""
names=['apple','orange','google','yahoo']
li=[(item,len(item))  for item in names]
print(li)