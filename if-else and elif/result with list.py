l=[]
for i in range(1,5):
    l.append(int(input(f"Ener the Sub {i} : ")))
new=sum(l)/4
if new >=90 and new <=100:
    print("Distinciton")
elif new>=75 and new<=80:
    print("first class")
elif new>=0 and new<=50:
    print("Fail")
else:
    print("invalid option")