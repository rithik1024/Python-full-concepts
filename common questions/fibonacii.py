"""program to print fibonacci series    0 1 1 2 3 5 8"""

a=0
b=1
next_number=1
count=1
n=int(input("Enter the number: "))
print(a,end=" ")
while count<=n:
    print(next_number, end=" ")
    a=b
    b=next_number
    next_number=a+b
    count+=1
    
