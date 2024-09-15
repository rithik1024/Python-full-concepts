limit=int(input("enter the limit:"))
c=0
 
for num in range(1,limit+1):
    for j in range(1,num+1):
        if num%j==0:
            c+=1
    if c==2:
        print(num)
    c=0
# i=int(input('enter the number:'))10

# if 0<i<4:
#     print('prime')
# elif i%2!=0 and i%3!=0:
#     print("prime")
# else:
#     print("Not a prime")