n=65
line=int(input ("enetr the number of lines:"))
for i in range(1,line):
  print(" "*(line-1),end="")
  line-=1
  for j in range(i):
    print(chr(n),end=" ")
    n+=1
  print()