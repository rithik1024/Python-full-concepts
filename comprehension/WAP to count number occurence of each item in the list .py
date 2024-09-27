name=['apple',"google","apple","yahoo","google","facebook","gamil","yahoo"]
count_pair={}
for item in name:
    if item not in count_pair:
        count_pair[item]=1
    else:
        count_pair[item]+=1
li=[]
print(count_pair)
li=list(count_pair.items())
print(li)
for i in li:
    for u in i:
      print(f"{u}",end=" ")
      if type(u)==str:
          print(":",end="")
      if type(u)==int:
          print("\n")

