#15 14 13 12 11
 #  10 9 8 7 
    # 6 5 4 
      #32
       #1
num=15
for i in range(5,0,-1):
    print(" "*(5-i) ,end=" ")
    for j in range(i):
        print(num ,end=" ")
        num-=1
    print()
    
num=1
for i in range(1,6):
    print(" "*(5-i),end=" ")
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()