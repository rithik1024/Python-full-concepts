#49
num=int(input("enter the number:"))
add=0
mul=1
temp=num
while num>0:
    add+=num%10
    mul*=num%10
    num=num//10
print(add,mul)
if (add+mul)==temp:
    print("special number")
else:
    print("not a special number")
