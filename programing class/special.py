#49
num=int(input("enter the number:"))
i=1
add=0
mul=1
l=num
while i<=len(str(l)):
    temp=num%10
    add+=temp
    mul*=temp
    num=num//10
    i+=1
print(add,mul)
if (add+mul)==l:
    print("strong number")
else:
    print("not a strong number")