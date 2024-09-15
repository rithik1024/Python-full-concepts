""" find the  second largest element """

a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if a<b and a>c:
    print(f"{a} is the  second largest number ")
elif a<c and a>b:
         print("a is greater")
if b<c and b>a:
    print(f"{b} is the  second largest number ")
elif b<a and b>c:
        print(f" {b}  is  second largest")
else:
    print("c is greter")
        
