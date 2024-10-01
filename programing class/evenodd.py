num=int(input("enetr the number:"))
if num%2==0:
 for i in range (0,num+2,2):
    print(i)
else:
    for i in range(1,num+2,2):
        print(i)