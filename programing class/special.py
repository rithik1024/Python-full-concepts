#49
num=int(input("enter the number:"))
i=0
add=0
mul=1
hold=num
for i in range(0,len(str(hold))):
    temp=num%10
    add+=temp
    mul*=temp
    num=num//10
print(add,mul)
if (add+mul)==hold:
    print("special number")
else:
    print("not a special number")
