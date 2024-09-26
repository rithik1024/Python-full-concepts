limit=int(input("enter the limit:"))
c=0
 
for num in range(1,limit+1):
    for j in range(1,num+1):
        if num%j==0:
            c+=1
    if c==2:
        print(num)
    c=0
#----------------------------------------------

# num=int(input("enter the number:"))
# c=0
# for i in range(1,num+1):
#     if num%i==0:
#         c+=1
# if c==2:
#         print("prime number")
# else:
#         print("not a prime ")
# c=0